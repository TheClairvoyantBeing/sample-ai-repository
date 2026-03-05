"""
=============================================================
 FILE 05 — MCP PROMPTS (Reusable Prompt Templates)
=============================================================

PROMPTS in MCP are reusable templates that a server provides.
They are like "saved workflows" or "canned instructions" that
users or AI systems can use to kick off a task in a structured way.

Use cases:
  - A "code review" prompt that fills in the language and code
  - A "summarize document" prompt that takes a doc and a length
  - A "translate text" prompt that takes source/target language

The server defines the prompts.
The client (user or AI) picks one and fills in the arguments.

=============================================================
"""

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Prompt, PromptMessage, PromptArgument, TextContent
import asyncio

app = Server("prompts-demo-server")


# ---- Step 1: Declare available prompts ----
@app.list_prompts()
async def list_prompts() -> list[Prompt]:
    """Tell clients what prompt templates this server offers."""
    return [

        # ---- PROMPT 1: Code Review ----
        Prompt(
            name="code_review",
            description="Generate a thorough code review for a given snippet.",
            arguments=[
                PromptArgument(
                    name="language",
                    description="The programming language (e.g., Python, JavaScript)",
                    required=True
                ),
                PromptArgument(
                    name="code",
                    description="The code snippet to review",
                    required=True
                ),
                PromptArgument(
                    name="focus",
                    description="What to focus on: 'security', 'performance', or 'readability'",
                    required=False  # Optional — defaults to general review
                ),
            ]
        ),

        # ---- PROMPT 2: Summarize Text ----
        Prompt(
            name="summarize",
            description="Summarize a piece of text at a given detail level.",
            arguments=[
                PromptArgument(
                    name="text",
                    description="The text to summarize",
                    required=True
                ),
                PromptArgument(
                    name="length",
                    description="Desired length: 'short' (1 sentence), 'medium' (1 paragraph), 'long' (full summary)",
                    required=False  # Defaults to 'medium'
                ),
            ]
        ),

        # ---- PROMPT 3: Translate ----
        Prompt(
            name="translate",
            description="Translate text from one language to another.",
            arguments=[
                PromptArgument(name="text",            description="Text to translate",   required=True),
                PromptArgument(name="target_language", description="Target language name", required=True),
            ]
        ),
    ]


# ---- Step 2: Return the filled-in prompt messages ----
# When the client "gets" a prompt by name, this function runs.
# It receives the arguments and returns actual message content.
@app.get_prompt()
async def get_prompt(name: str, arguments: dict | None) -> list[PromptMessage]:
    """Build and return the prompt messages for the requested prompt."""

    args = arguments or {}  # Default to empty dict if no args passed

    # ---- Fill in code_review prompt ----
    if name == "code_review":
        language = args.get("language", "unknown language")
        code     = args.get("code", "(no code provided)")
        focus    = args.get("focus", "general quality")  # default value

        # Build the actual prompt text
        prompt_text = (
            f"Please perform a {focus} code review of the following {language} code.\n"
            f"Focus on: {focus}\n\n"
            f"```{language.lower()}\n{code}\n```\n\n"
            f"Provide specific, actionable feedback."
        )

        # Return as a list of PromptMessage objects
        return [PromptMessage(
            role="user",                                    # 'user' or 'assistant'
            content=TextContent(type="text", text=prompt_text)
        )]

    # ---- Fill in summarize prompt ----
    elif name == "summarize":
        text   = args.get("text", "(no text provided)")
        length = args.get("length", "medium")

        # Map length to an instruction
        length_instructions = {
            "short":  "in exactly one sentence",
            "medium": "in one concise paragraph",
            "long":   "in detail, covering all key points"
        }
        instruction = length_instructions.get(length, "in one concise paragraph")

        prompt_text = (
            f"Please summarize the following text {instruction}:\n\n"
            f"---\n{text}\n---"
        )
        return [PromptMessage(role="user", content=TextContent(type="text", text=prompt_text))]

    # ---- Fill in translate prompt ----
    elif name == "translate":
        text            = args.get("text", "(no text provided)")
        target_language = args.get("target_language", "English")

        prompt_text = (
            f"Translate the following text into {target_language}. "
            f"Only return the translated text, nothing else.\n\n"
            f"Text to translate:\n{text}"
        )
        return [PromptMessage(role="user", content=TextContent(type="text", text=prompt_text))]

    else:
        raise ValueError(f"Unknown prompt: '{name}'")


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
