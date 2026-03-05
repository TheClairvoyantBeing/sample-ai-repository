"""
=============================================================
 FILE 01 — WHAT IS MCP? (Model Context Protocol)
=============================================================

MCP is a standard protocol that allows AI models to connect
to external tools and data sources in a uniform way.

ANALOGY:
  Think of it like a plug socket standard.
  - The AI model = a device that needs power (context)
  - MCP Server  = the power socket (provides context)
  - Tools       = power outlets (functions the AI can use)
  - Resources   = the electricity (data)

WHY MCP?
  Before MCP, every AI integration was custom-built.
  - If you wanted Claude to read your DB, you coded it yourself.
  - If another team wanted GPT to do the same, they coded it again.
  MCP standardizes this — build once, connect to any AI.

=============================================================
 THE THREE THINGS A SERVER CAN EXPOSE
=============================================================

1. TOOLS
   - Functions the AI can *call*
   - Example: search_web(query), run_sql(query), send_email(to, body)
   - The AI decides WHEN and HOW to call them based on the user request

2. RESOURCES
   - Data the AI can *read*
   - Example: file contents, database rows, API responses
   - Identified by a URI, like file:///home/user/notes.txt

3. PROMPTS
   - Reusable *prompt templates* the server provides
   - Example: a "code review" prompt, a "summarize doc" prompt
   - The AI (or user) can pick and fill these templates

=============================================================
 HOW COMMUNICATION WORKS
=============================================================

MCP uses JSON-RPC 2.0 over a "transport" layer.
Two built-in transports:

  a) STDIO  — Server talks via stdin/stdout (good for local tools)
  b) SSE    — Server uses HTTP Server-Sent Events (good for remote)

Message flow:
  Client (AI/app)  --->  sends a request  --->  Server
  Server           --->  sends a response --->  Client

=============================================================
 SIMPLE MENTAL MODEL IN PSEUDOCODE
=============================================================
"""

# ---- PSEUDOCODE (not real runnable code, just for understanding) ----

# Step 1: AI gets a user message
user_message = "What files are in my project folder?"

# Step 2: AI looks at available TOOLS from MCP server
available_tools = [
    {"name": "list_files", "description": "Lists files in a directory"},
    {"name": "read_file",  "description": "Reads a file's content"},
]

# Step 3: AI decides to call a tool
tool_call = {
    "tool": "list_files",
    "arguments": {"path": "/home/user/project"}
}

# Step 4: MCP Server executes the tool and returns the result
tool_result = ["main.py", "utils.py", "README.md"]  # example result

# Step 5: AI uses the result to form its final answer
final_answer = f"Your project folder contains: {tool_result}"

print("Concept File — No code to run here.")
print("Read the comments above to understand MCP concepts.")
print("Move on to 02_simple_mcp_server.py when ready!")
