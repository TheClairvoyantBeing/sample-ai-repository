"""
=============================================================
 FILE 02 — YOUR FIRST MCP SERVER (Minimal Example)
=============================================================

In this file we create the simplest possible MCP server.
It has ONE tool: a calculator that adds two numbers.

Requirements:
  pip install mcp

HOW TO RUN THIS SERVER:
  python 02_simple_mcp_server.py

The server will start and wait for a client to connect.
By default it uses STDIO transport (reads from stdin, writes to stdout).

=============================================================
"""

# ---- Import the MCP library ----
# `mcp` is the official Python SDK for the Model Context Protocol
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import asyncio  # MCP uses async/await (asynchronous Python)


# ---- Step 1: Create the server instance ----
# Give it a name — this is what the client will see when it connects
app = Server("my-first-mcp-server")


# ---- Step 2: Define what tools the server exposes ----
# @app.list_tools() is a decorator — it tells MCP:
# "When a client asks 'what tools do you have?', run this function"
@app.list_tools()
async def list_tools() -> list[Tool]:
    """Return the list of tools this server provides."""
    return [
        Tool(
            name="add_numbers",          # The tool's unique name
            description="Adds two numbers together and returns the sum.",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "The first number"
                    },
                    "b": {
                        "type": "number",
                        "description": "The second number"
                    }
                },
                "required": ["a", "b"]  # Both fields must be provided
            }
        )
    ]


# ---- Step 3: Define what happens when a tool is CALLED ----
# @app.call_tool() is triggered when the AI (or client) actually calls a tool
@app.call_tool()
async def call_tool(name: str, arguments: dict):
    """Execute the tool when the client calls it."""

    # Check which tool was called by name
    if name == "add_numbers":
        # Extract the arguments the AI passed in
        a = arguments["a"]
        b = arguments["b"]

        # Do the actual work
        result = a + b

        # Return the result as a list of TextContent objects
        # (MCP requires results to be in this format)
        return [TextContent(type="text", text=f"The sum of {a} and {b} is {result}")]

    else:
        # Handle unknown tool names gracefully
        raise ValueError(f"Unknown tool: {name}")


# ---- Step 4: Start the server ----
async def main():
    """Entry point — starts the server using stdio transport."""
    # stdio_server() handles reading input from stdin and writing to stdout
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())
