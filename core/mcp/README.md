# 🧠 MCP — Model Context Protocol

## What is MCP?

**MCP (Model Context Protocol)** is an open protocol developed by Anthropic that lets you connect AI models (like Claude, GPT, etc.) to external tools, data sources, and services in a standardized way.

Think of it like **USB for AI** — instead of every AI needing custom code to access every tool, MCP provides one universal plug.

---

## 📁 Folder Structure

```
mcp/
├── README.md                    ← You are here
├── 01_what_is_mcp.py            ← Core concepts explained in code
├── 02_simple_mcp_server.py      ← Build your first MCP server
├── 03_mcp_tools.py              ← How to expose tools to the AI
├── 04_mcp_resources.py          ← How to expose data/resources
├── 05_mcp_prompts.py            ← How to expose prompt templates
├── 06_mcp_client.py             ← Connect to an MCP server as a client
└── 07_real_world_example.py     ← A real-world file system example
```

---

## 🔧 Installation

Before running any file, install the MCP Python SDK:

```bash
pip install mcp
```

For the client examples you may also need:
```bash
pip install anthropic   # if using Claude as the LLM
```

---

## 🧭 Learning Path

Work through the files **in order** (01 → 07). Each file builds on the previous.

| File | Topic | Difficulty |
|------|-------|------------|
| `01_what_is_mcp.py` | Core concepts & terminology | ⭐ Beginner |
| `02_simple_mcp_server.py` | Minimal MCP server | ⭐ Beginner |
| `03_mcp_tools.py` | Defining tools (functions the AI can call) | ⭐⭐ Intermediate |
| `04_mcp_resources.py` | Serving data/content to the AI | ⭐⭐ Intermediate |
| `05_mcp_prompts.py` | Offering prompt templates | ⭐⭐ Intermediate |
| `06_mcp_client.py` | Connecting to a server as a client | ⭐⭐⭐ Advanced |
| `07_real_world_example.py` | Full file system MCP server | ⭐⭐⭐ Advanced |

---

## 🌐 Key Concepts at a Glance

| Concept | Description |
|---------|-------------|
| **Server** | Your Python app that exposes tools/data |
| **Client** | The AI (or app) that connects to the server |
| **Tool** | A function the AI can call (e.g., search, calculate) |
| **Resource** | Data the AI can read (e.g., file contents, DB rows) |
| **Prompt** | Reusable prompt templates the server provides |
| **Transport** | How server & client communicate (stdio or SSE) |

---

## 📚 References

- Official Docs: https://modelcontextprotocol.io
- GitHub SDK: https://github.com/modelcontextprotocol/python-sdk
- Anthropic Blog: https://www.anthropic.com/news/model-context-protocol
