#!/bin/bash

# Test script to query available MCP tools from the Unity-MCP-Server
# Uses MCP protocol with HTTP transport and Server-Sent Events (SSE)

SERVER_URL="http://localhost:2248"
SESSION_ID="test-session-$(date +%s)"

echo "Unity-MCP-Server Test Client"
echo "Server URL: $SERVER_URL"
echo "Session ID: $SESSION_ID"
echo ""

# Step 1: Initialize session
echo "=========================================="
echo "Step 1: Initializing MCP session..."
echo "=========================================="
echo ""

INIT_RESPONSE=$(curl -s -X POST "$SERVER_URL/" \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
      "protocolVersion": "2024-11-05",
      "capabilities": {},
      "clientInfo": {"name": "test-client", "version": "1.0"}
    }
  }')

echo "Init Response:"
echo "$INIT_RESPONSE" | grep -o 'data:.*' || echo "$INIT_RESPONSE"
echo ""

# Step 2: List tools
echo "=========================================="
echo "Step 2: Listing available tools..."
echo "=========================================="
echo ""

TOOLS_RESPONSE=$(curl -s -X POST "$SERVER_URL/" \
  -H "Content-Type: application/json" \
  -H "Mcp-Session-Id: $SESSION_ID" \
  -d '{
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/list",
    "params": {}
  }')

echo "Tools Response:"
echo "$TOOLS_RESPONSE"
echo ""

# Step 3: List resources
echo "=========================================="
echo "Step 3: Listing available resources..."
echo "=========================================="
echo ""

RESOURCES_RESPONSE=$(curl -s -X POST "$SERVER_URL/" \
  -H "Content-Type: application/json" \
  -H "Mcp-Session-Id: $SESSION_ID" \
  -d '{
    "jsonrpc": "2.0",
    "id": 3,
    "method": "resources/list",
    "params": {}
  }')

echo "Resources Response:"
echo "$RESOURCES_RESPONSE"
