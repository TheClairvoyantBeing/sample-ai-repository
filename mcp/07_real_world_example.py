"""
=============================================================
 FILE 07 — REAL-WORLD EXAMPLE (File System MCP Server)
=============================================================

This is a complete, practical MCP server that lets the AI:
  1. LIST files in a directory       (Tool)
  2. READ the content of a file      (Tool + Resource)
  3. WRITE content to a file         (Tool)
  4. GET a "file summary" prompt     (Prompt)

This is close to what a real production MCP server looks like.
It also shows proper ERROR HANDLING and SECURITY checks.

Requirements:
  pip install mcp

HOW TO RUN:
  python 07_real_world_example.py

SECURITY NOTE:
  This server restricts access to a SAFE directory only.
  It will refuse to read/write files outside of it.
  Always restrict file access in real servers!

=============================================================
"""

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, Resource, Prompt, PromptMessage, PromptArgument, TextContent
import asyncio
import os
import pathlib


# ---- Configuration ----
# The server will only allow access to files within this directory.
# Change this to any folder you want to expose. Using a temp dir for safety.
SAFE_BASE_DIR = pathlib.Path(os.path.expanduser("~")) / "mcp_workspace"

# Create the workspace directory if it doesn't exist
SAFE_BASE_DIR.mkdir(parents=True, exist_ok=True)

# Create some sample files in the workspace for testing
(SAFE_BASE_DIR / "hello.txt").write_text("Hello from MCP! This is a sample file.")
(SAFE_BASE_DIR / "notes.txt").write_text("Meeting notes:\n- Discussed MCP\n- Action: build a server\n- Owner: You!")
(SAFE_BASE_DIR / "data.csv").write_text("name,age,city\nAlice,30,London\nBob,25,Paris\nCarol,35,Tokyo")

print(f"[Server] Workspace is at: {SAFE_BASE_DIR}")

app = Server("filesystem-server")


# ---- SECURITY HELPER ----
def safe_path(filename: str) -> pathlib.Path | None:
    """
    Resolve a filename to an absolute path and check it's inside SAFE_BASE_DIR.
    Returns the path if safe, or None if it's a path traversal attempt.

    This prevents attacks like: filename = "../../etc/passwd"
    """
    resolved = (SAFE_BASE_DIR / filename).resolve()
    # Check that the resolved path starts with the base dir
    if SAFE_BASE_DIR.resolve() in resolved.parents or resolved == SAFE_BASE_DIR.resolve():
        return resolved
    return None  # Suspicious path — block it


# ==============================================================
# TOOLS
# ==============================================================

@app.list_tools()
async def list_tools() -> list[Tool]:
    return [

        # ---- Tool 1: List files ----
        Tool(
            name="list_files",
            description="Lists all files in the MCP workspace directory.",
            inputSchema={
                "type": "object",
                "properties": {}  # No arguments needed
            }
        ),

        # ---- Tool 2: Read a file ----
        Tool(
            name="read_file",
            description="Reads and returns the text content of a file in the MCP workspace.",
            inputSchema={
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "Name of the file to read (e.g., 'notes.txt')"
                    }
                },
                "required": ["filename"]
            }
        ),

        # ---- Tool 3: Write a file ----
        Tool(
            name="write_file",
            description="Writes (or overwrites) a file in the MCP workspace with given content.",
            inputSchema={
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "Name of the file to create or overwrite"
                    },
                    "content": {
                        "type": "string",
                        "description": "The text content to write into the file"
                    }
                },
                "required": ["filename", "content"]
            }
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict):

    # ---- list_files ----
    if name == "list_files":
        files = list(SAFE_BASE_DIR.iterdir())

        if not files:
            return [TextContent(type="text", text="The workspace is empty.")]

        file_list = []
        for f in files:
            size = f.stat().st_size
            kind = "DIR" if f.is_dir() else "FILE"
            file_list.append(f"  [{kind}] {f.name}  ({size} bytes)")

        output = f"Files in workspace ({SAFE_BASE_DIR}):\n" + "\n".join(file_list)
        return [TextContent(type="text", text=output)]

    # ---- read_file ----
    elif name == "read_file":
        filename = arguments["filename"]
        path = safe_path(filename)

        if path is None:
            return [TextContent(type="text", text=f"Security error: '{filename}' is outside the workspace.")]

        if not path.exists():
            return [TextContent(type="text", text=f"Error: File '{filename}' does not exist.")]

        if not path.is_file():
            return [TextContent(type="text", text=f"Error: '{filename}' is not a file.")]

        # Read and return the file content
        content = path.read_text(encoding="utf-8", errors="replace")
        return [TextContent(type="text", text=f"Content of '{filename}':\n---\n{content}")]

    # ---- write_file ----
    elif name == "write_file":
        filename = arguments["filename"]
        content  = arguments["content"]
        path = safe_path(filename)

        if path is None:
            return [TextContent(type="text", text=f"Security error: '{filename}' is outside the workspace.")]

        # Write the content to the file
        path.write_text(content, encoding="utf-8")
        return [TextContent(type="text", text=f"Successfully wrote {len(content)} characters to '{filename}'.")]

    else:
        raise ValueError(f"Unknown tool: {name}")


# ==============================================================
# RESOURCES
# ==============================================================

@app.list_resources()
async def list_resources() -> list[Resource]:
    """Expose all files in the workspace as readable resources."""
    resources = []
    for f in SAFE_BASE_DIR.iterdir():
        if f.is_file():
            # Determine MIME type from extension
            mime = "text/plain"
            if f.suffix == ".csv":
                mime = "text/csv"
            elif f.suffix == ".json":
                mime = "application/json"

            resources.append(Resource(
                uri=f"file://{f.name}",
                name=f.name,
                description=f"File in workspace: {f.name} ({f.stat().st_size} bytes)",
                mimeType=mime
            ))
    return resources


@app.read_resource()
async def read_resource(uri: str):
    """Read a file resource by URI."""
    # Extract filename from URI: "file://notes.txt" -> "notes.txt"
    filename = uri.replace("file://", "")
    path = safe_path(filename)

    if path is None or not path.exists():
        return [TextContent(type="text", text=f"Resource not found: {uri}")]

    content = path.read_text(encoding="utf-8", errors="replace")
    return [TextContent(type="text", text=content)]


# ==============================================================
# PROMPTS
# ==============================================================

@app.list_prompts()
async def list_prompts() -> list[Prompt]:
    return [
        Prompt(
            name="summarize_file",
            description="Generate a summary of a file from the workspace.",
            arguments=[
                PromptArgument(name="filename", description="The file to summarize", required=True),
                PromptArgument(name="style",    description="Summary style: 'brief' or 'detailed'", required=False)
            ]
        )
    ]


@app.get_prompt()
async def get_prompt(name: str, arguments: dict | None) -> list[PromptMessage]:
    if name == "summarize_file":
        args = arguments or {}
        filename = args.get("filename", "(unknown file)")
        style    = args.get("style", "brief")

        path = safe_path(filename)
        if path and path.exists():
            file_content = path.read_text(encoding="utf-8", errors="replace")
        else:
            file_content = "(File not found or inaccessible)"

        prompt_text = (
            f"Please provide a {style} summary of the following file named '{filename}':\n\n"
            f"```\n{file_content}\n```"
        )
        return [PromptMessage(role="user", content=TextContent(type="text", text=prompt_text))]

    else:
        raise ValueError(f"Unknown prompt: {name}")


# ==============================================================
# ENTRY POINT
# ==============================================================

async def main():
    print(f"[Server] Starting filesystem MCP server...")
    print(f"[Server] Workspace: {SAFE_BASE_DIR}")
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
