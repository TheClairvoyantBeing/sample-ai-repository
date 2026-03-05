"""
=============================================================
 FILE 03 — MCP TOOLS (Multiple Tools with Validation)
=============================================================

In this file we build a server with MULTIPLE tools.
We also show how to:
  - Validate user input properly
  - Return errors cleanly
  - Use optional parameters in tools

Think of TOOLS as "functions the AI can call on demand".
The AI reads your tool descriptions and autonomously decides
which tool to invoke based on the user's request.

Requirements:
  pip install mcp

=============================================================
"""

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import asyncio
import math  # We'll use this for the math tools

app = Server("math-tools-server")


@app.list_tools()
async def list_tools() -> list[Tool]:
    """
    Expose three separate tools to the AI:
    1. add         — addition
    2. multiply    — multiplication
    3. square_root — returns the square root (with optional rounding)

    The AI reads 'description' and 'inputSchema' to understand each tool.
    Write descriptions as if you're explaining to a smart person who
    doesn't know anything about your code.
    """
    return [
        # ---- TOOL 1: Addition ----
        Tool(
            name="add",
            description="Adds two numbers. Use this when the user wants to add or sum values.",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "First number"},
                    "b": {"type": "number", "description": "Second number"}
                },
                "required": ["a", "b"]
            }
        ),

        # ---- TOOL 2: Multiplication ----
        Tool(
            name="multiply",
            description="Multiplies two numbers together. Use when the user asks to multiply or find a product.",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "First factor"},
                    "b": {"type": "number", "description": "Second factor"}
                },
                "required": ["a", "b"]
            }
        ),

        # ---- TOOL 3: Square Root (with OPTIONAL parameter) ----
        Tool(
            name="square_root",
            description=(
                "Returns the square root of a number. "
                "Optionally rounds the result to a given number of decimal places."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "number": {
                        "type": "number",
                        "description": "The number to find the square root of (must be >= 0)"
                    },
                    # 'decimal_places' is OPTIONAL — notice it's not in "required"
                    "decimal_places": {
                        "type": "integer",
                        "description": "How many decimal places to round to (optional, default: no rounding)"
                    }
                },
                "required": ["number"]  # Only 'number' is required
            }
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict):
    """
    Route the incoming tool call to the correct logic.

    Best practice: Use if/elif/else to dispatch by tool name.
    Always handle the 'else' case for unknown tool names.
    """

    # ---- Handle 'add' ----
    if name == "add":
        a = arguments["a"]
        b = arguments["b"]
        result = a + b
        return [TextContent(type="text", text=f"{a} + {b} = {result}")]

    # ---- Handle 'multiply' ----
    elif name == "multiply":
        a = arguments["a"]
        b = arguments["b"]
        result = a * b
        return [TextContent(type="text", text=f"{a} × {b} = {result}")]

    # ---- Handle 'square_root' with INPUT VALIDATION ----
    elif name == "square_root":
        number = arguments["number"]

        # Validate: square root of a negative number doesn't exist in real numbers
        if number < 0:
            # Return an error message as text content
            return [TextContent(
                type="text",
                text=f"Error: Cannot compute square root of a negative number ({number}). "
                     f"Please provide a number >= 0."
            )]

        result = math.sqrt(number)

        # Handle the OPTIONAL 'decimal_places' parameter
        # .get() returns None if the key doesn't exist (safe way to access optional args)
        decimal_places = arguments.get("decimal_places")
        if decimal_places is not None:
            result = round(result, decimal_places)

        return [TextContent(type="text", text=f"√{number} = {result}")]

    # ---- Unknown tool ----
    else:
        raise ValueError(f"Unknown tool name: '{name}'. Available: add, multiply, square_root")


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
