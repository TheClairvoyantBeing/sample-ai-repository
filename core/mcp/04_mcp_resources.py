"""
=============================================================
 FILE 04 — MCP RESOURCES (Serving Data to the AI)
=============================================================

RESOURCES are how you give the AI access to DATA.
While TOOLS are "functions the AI can call",
RESOURCES are "files or data the AI can READ".

Examples of resources:
  - A text file: file:///home/user/notes.txt
  - A database row: db://users/42
  - A web page snapshot: https://example.com/page
  - An in-memory config: config://app/settings

Resources are identified by a URI (Uniform Resource Identifier).
The AI can list available resources and then read the ones it needs.

=============================================================
"""

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Resource, TextContent
import asyncio

app = Server("resources-demo-server")

# ---- In-memory "database" of fake users ----
# In a real app this would come from a real DB or files
FAKE_DATABASE = {
    "user:1": {"name": "Alice", "role": "admin",    "email": "alice@example.com"},
    "user:2": {"name": "Bob",   "role": "developer","email": "bob@example.com"},
    "user:3": {"name": "Carol", "role": "analyst",  "email": "carol@example.com"},
}

# ---- Static text "documents" ----
FAKE_DOCS = {
    "doc:welcome":   "Welcome to the MCP demo system! Use resources to access data.",
    "doc:faq":       "Q: What is MCP? A: Model Context Protocol — a standard for AI-tool integration.",
    "doc:changelog": "v1.0 — Initial release\nv1.1 — Added resources support\nv1.2 — Added prompts",
}


# ---- Step 1: List all available resources ----
# When the AI (or client) asks "what data can I access?", this runs
@app.list_resources()
async def list_resources() -> list[Resource]:
    """Return all resources this server makes available."""

    resources = []

    # Expose each user as a resource with a unique URI
    for user_id, user_data in FAKE_DATABASE.items():
        resources.append(Resource(
            uri=f"users://{user_id}",               # Unique identifier
            name=f"User: {user_data['name']}",       # Human-friendly name
            description=f"Profile data for {user_data['name']} ({user_data['role']})",
            mimeType="application/json"              # Type hint for the client
        ))

    # Expose each document as a resource
    for doc_id, _ in FAKE_DOCS.items():
        resources.append(Resource(
            uri=f"docs://{doc_id}",
            name=f"Document: {doc_id.split(':')[1].capitalize()}",
            description=f"Static documentation: {doc_id}",
            mimeType="text/plain"
        ))

    return resources


# ---- Step 2: Read a specific resource by URI ----
# When the AI says "give me the content of users://user:1", this runs
@app.read_resource()
async def read_resource(uri: str):
    """Return the content of the requested resource URI."""

    # ---- Serve user data ----
    if uri.startswith("users://"):
        # Extract the user ID from the URI
        # e.g., "users://user:1" -> "user:1"
        user_id = uri.replace("users://", "")

        if user_id in FAKE_DATABASE:
            user = FAKE_DATABASE[user_id]
            # Format the user data as readable text
            content = (
                f"Name:  {user['name']}\n"
                f"Role:  {user['role']}\n"
                f"Email: {user['email']}"
            )
            return [TextContent(type="text", text=content)]
        else:
            return [TextContent(type="text", text=f"Error: No user found with ID '{user_id}'")]

    # ---- Serve document data ----
    elif uri.startswith("docs://"):
        doc_id = uri.replace("docs://", "")

        if doc_id in FAKE_DOCS:
            return [TextContent(type="text", text=FAKE_DOCS[doc_id])]
        else:
            return [TextContent(type="text", text=f"Error: Document '{doc_id}' not found")]

    # ---- Unknown URI scheme ----
    else:
        return [TextContent(type="text", text=f"Error: Unknown URI scheme in '{uri}'")]


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
