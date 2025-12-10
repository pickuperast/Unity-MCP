# Unity-MCP-Server Docker Setup Summary

## Status: ✅ Running Successfully

Your Docker container is **up and running** on port **2248**.

## Quick Start

```bash
# Server is running at:
http://localhost:2248

# Help endpoint:
curl http://localhost:2248/help
```

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    MCP Clients                              │
│         (Claude Desktop, VS Code, etc.)                     │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      │ MCP Protocol (JSON-RPC 2.0)
                      │ HTTP + Server-Sent Events
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│              Docker Container (port 2248)                   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐  │
│  │    ASP.NET Core Web Host (Kestrel)                 │  │
│  │                                                      │  │
│  │  ┌─────────────────────────────────────────────┐   │  │
│  │  │  MCP Server (unity-mcp-server v0.22.1)     │   │  │
│  │  │  - Protocol: 2024-11-05                     │   │  │
│  │  │  - Transport: HTTP                          │   │  │
│  │  │  - Port: 8080 (internal)                    │   │  │
│  │  └─────────────────────────────────────────────┘   │  │
│  │                    │                                 │  │
│  │                    │ SignalR                         │  │
│  │                    │ port 8080                       │  │
│  │                    ▼                                 │  │
│  │  ┌─────────────────────────────────────────────┐   │  │
│  │  │  McpServerHub (SignalR)                     │   │  │
│  │  │  - Real-time bidirectional communication    │   │  │
│  │  │  - Supports: WebSockets, Server-Sent Events│   │  │
│  │  └─────────────────────────────────────────────┘   │  │
│  └─────────────────────────────────────────────────────┘  │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      │ SignalR Connection
                      │ port 8080
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│         Unity-MCP-Plugin (in Unity Editor)                  │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐  │
│  │  Tool Definitions (Reflection-based)               │  │
│  │  - 50+ Available Tools                             │  │
│  │  - Asset Management                                │  │
│  │  - GameObject Operations                           │  │
│  │  - Scene Management                                │  │
│  │  - Script Management                               │  │
│  │  - Editor Control                                  │  │
│  │  - And many more...                                │  │
│  └─────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Server Information

| Property | Value |
|----------|-------|
| **Server Name** | unity-mcp-server |
| **Version** | 0.22.1.0 |
| **Protocol Version** | 2024-11-05 |
| **Transport** | HTTP with Server-Sent Events |
| **Internal Port** | 8080 |
| **Host Port** | 2248 |
| **Status** | ✅ Running |

## Available Tools

The server exposes **50+ MCP tools** across multiple categories:

### Core Categories:

1. **Asset Management** (8 tools)
   - Find, Load, Read, Modify, Move, Copy, Delete, Create Folders

2. **Prefab Management** (6 tools)
   - Create, Open, Close, Save, Instantiate, General Management

3. **GameObject Operations** (8 tools)
   - Find, Create, Destroy, Duplicate, Modify, Set Parent, Add/Destroy Components

4. **Scene Management** (6 tools)
   - Create, Load, Save, Unload, Get Loaded, Get Hierarchy

5. **Editor Control** (6 tools)
   - Selection Get/Set, Application State, Application Information

6. **Script Management** (5 tools)
   - Read, Create/Update, Delete, Execute

7. **Scripting & Reflection** (3 tools)
   - Method Find, Method Call, General Reflection

8. **Materials & Shaders** (4 tools)
   - Create Materials, Manage Materials, List/Manage Shaders

9. **Component Tools** (2 tools)
   - Get All Components, Component Management

10. **Console & Testing** (4 tools)
    - Get Logs, Test Runner

## How to Use

### 1. View All Available Tools

Run this to get a detailed list of all tools:
```bash
cat AVAILABLE_MCP_TOOLS.md
```

### 2. Test the Server

The server is already running. You can verify connectivity:
```bash
curl http://localhost:2248/help
```

### 3. Connect with MCP Client

For Claude Desktop, VS Code MCP extension, or any other MCP client, configure it to connect to:
```
http://localhost:2248
```

The server uses the standard MCP protocol (JSON-RPC 2.0 over HTTP with Server-Sent Events).

### 4. Example Tool Call (from a client)

After initializing the MCP session, you can call a tool like:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "Assets_Find",
    "arguments": {
      "filter": "t:Prefab",
      "searchInFolders": ["Assets/Prefabs"]
    }
  }
}
```

## Configuration

### Start with Custom Settings

```bash
# Custom port
docker run -p 3000:8080 unity-mcp-server --port 8080

# STDIO transport (for command-line clients)
docker run -p 2248:8080 unity-mcp-server --client-transport stdio

# Custom plugin timeout
docker run -p 2248:8080 unity-mcp-server --plugin-timeout 15000
```

## Important Notes

⚠️ **Requirements**:
- Unity Editor must be running with the Unity-MCP-Plugin installed
- Plugin must be connected to the server via SignalR on port 8080
- Tools execute on the Unity main thread (some operations are blocking)

## Logs

View server logs:
```bash
docker logs $(docker ps -q -f ancestor=unity-mcp-server)
```

Follow logs in real-time:
```bash
docker logs -f $(docker ps -q -f ancestor=unity-mcp-server)
```

## Container Management

### Stop the server
```bash
docker stop $(docker ps -q -f ancestor=unity-mcp-server)
```

### Remove the container
```bash
docker rm $(docker ps -aq -f ancestor=unity-mcp-server)
```

### View container info
```bash
docker ps -f ancestor=unity-mcp-server
```

## Files Created

- `AVAILABLE_MCP_TOOLS.md` - Complete tool reference
- `DOCKER_SETUP_SUMMARY.md` - This file
- `test-mcp-tools.py` - Python test client
- `test-mcp-tools.sh` - Bash test script

## Protocol Specification

The server implements the **Model Context Protocol (MCP)** specification:

- **Version**: 2024-11-05
- **Protocol**: JSON-RPC 2.0
- **Transport**: HTTP with Server-Sent Events (SSE)
- **Capabilities**:
  - Tools: ✅ Supported
  - Resources: ✅ Supported
  - Prompts: ✅ Supported
  - Logging: ✅ Supported

## Resources

- **GitHub**: https://github.com/IvanMurzak/Unity-MCP
- **MCP Spec**: https://modelcontextprotocol.io/
- **ASP.NET Core**: https://learn.microsoft.com/en-us/aspnet/core/

## Next Steps

1. ✅ Docker image built and running
2. ✅ Server listening on port 2248
3. ⏭️ Connect a Unity Editor with the plugin
4. ⏭️ Connect an MCP client (Claude Desktop, etc.)
5. ⏭️ Start using the available tools!

---

**Happy coding!** 🚀
