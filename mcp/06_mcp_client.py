"""
=============================================================
 FILE 06 — MCP CLIENT (Connecting to a Server)
=============================================================

So far we've only built SERVERS.
Now let's learn how to write a CLIENT that connects to a server.

A CLIENT is the "consumer" side:
  - It connects to an MCP server
  - Discovers tools, resources, and prompts
  - Calls tools and reads resources

In real use, the AI model (Claude, GPT) acts as the client.
But you can also write a Python client directly — useful for:
  - Testing your server
  - Building custom AI apps
  - Automating workflows

NOTE: This file shows you how to connect to the server built
in 02_simple_mcp_server.py. You need to run that server first
(or another MCP server) for this to work.

Requirements:
  pip install mcp

=============================================================
"""

import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


# ---- Step 1: Define the server we want to connect to ----
# StdioServerParameters tells the client HOW to launch the server.
# Here we launch 02_simple_mcp_server.py as a subprocess.
server_params = StdioServerParameters(
    command="python",                       # The executable to run
    args=["02_simple_mcp_server.py"],       # Arguments to the executable
    # env={"MY_ENV_VAR": "value"},          # Optional environment variables
)


async def main():
    """Connect to the server, discover tools, and call one."""

    print("Connecting to MCP server...")

    # ---- Step 2: Open a connection using stdio_client ----
    # stdio_client launches the server process and sets up pipes to talk to it
    async with stdio_client(server_params) as (read, write):

        # ---- Step 3: Create a session ----
        # ClientSession manages the MCP handshake (initialize / list / call)
        async with ClientSession(read, write) as session:

            # ---- Step 4: Initialize the session ----
            # This performs the MCP "initialize" handshake
            await session.initialize()
            print("Connected! Session initialized.\n")

            # ---- Step 5: Discover available TOOLS ----
            print("=== Available Tools ===")
            tools_result = await session.list_tools()

            for tool in tools_result.tools:
                print(f"  Tool: {tool.name}")
                print(f"    Description: {tool.description}")
            print()

            # ---- Step 6: Call a TOOL ----
            print("=== Calling 'add_numbers' tool ===")
            result = await session.call_tool(
                "add_numbers",          # Name of the tool to call
                {"a": 15, "b": 27}      # Arguments to pass
            )

            # result.content is a list of content objects
            # Each has a .text attribute if it's a TextContent
            for content_item in result.content:
                print(f"  Result: {content_item.text}")
            print()

            # ---- Step 7: Discover available RESOURCES ----
            # (This only works if the server exposes resources)
            print("=== Available Resources ===")
            try:
                resources_result = await session.list_resources()
                if resources_result.resources:
                    for resource in resources_result.resources:
                        print(f"  Resource: {resource.uri} — {resource.name}")
                else:
                    print("  (No resources exposed by this server)")
            except Exception as e:
                print(f"  (Could not list resources: {e})")
            print()

            # ---- Step 8: Discover available PROMPTS ----
            print("=== Available Prompts ===")
            try:
                prompts_result = await session.list_prompts()
                if prompts_result.prompts:
                    for prompt in prompts_result.prompts:
                        print(f"  Prompt: {prompt.name} — {prompt.description}")
                else:
                    print("  (No prompts exposed by this server)")
            except Exception as e:
                print(f"  (Could not list prompts: {e})")

            print("\nDone! Session closed.")


# Run the client
if __name__ == "__main__":
    asyncio.run(main())
