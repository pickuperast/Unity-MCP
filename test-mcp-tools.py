#!/usr/bin/env python3
"""
Test script to query available MCP tools from the Unity-MCP-Server
"""

import json
import requests
import sys

# Server configuration
SERVER_URL = "http://localhost:2248"
SESSION_ID = "test-session-001"

def make_mcp_request(method, params=None):
    """Make an MCP JSON-RPC request to the server"""
    headers = {
        "Content-Type": "application/json",
        "Mcp-Session-Id": SESSION_ID
    }

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params or {}
    }

    try:
        response = requests.post(SERVER_URL, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def initialize_session():
    """Initialize MCP session"""
    print("Initializing MCP session...")
    response = requests.post(
        SERVER_URL,
        json={
            "jsonrpc": "2.0",
            "id": 0,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {
                    "name": "test-client",
                    "version": "1.0"
                }
            }
        },
        headers={"Content-Type": "application/json"}
    )

    if response.status_code == 200:
        data = response.text
        print(f"Response: {data}")
        return True
    else:
        print(f"Error: {response.status_code}")
        return False

def list_tools():
    """List all available MCP tools"""
    print("\n" + "="*80)
    print("LISTING AVAILABLE MCP TOOLS")
    print("="*80 + "\n")

    response = make_mcp_request("tools/list")

    if "error" in response:
        print(f"Error: {response['error']}")
        return

    if "result" in response:
        tools = response["result"].get("tools", [])

        if not tools:
            print("No tools available")
            return

        print(f"Total tools available: {len(tools)}\n")

        for i, tool in enumerate(tools, 1):
            print(f"{i}. {tool.get('name', 'Unknown')}")
            if "description" in tool:
                print(f"   Description: {tool['description']}")
            if "inputSchema" in tool:
                schema = tool["inputSchema"]
                if "properties" in schema:
                    print(f"   Parameters:")
                    for param_name, param_info in schema["properties"].items():
                        param_type = param_info.get("type", "unknown")
                        param_desc = param_info.get("description", "")
                        print(f"     - {param_name} ({param_type}): {param_desc}")
            print()
    else:
        print(json.dumps(response, indent=2))

def list_resources():
    """List all available MCP resources"""
    print("\n" + "="*80)
    print("LISTING AVAILABLE MCP RESOURCES")
    print("="*80 + "\n")

    response = make_mcp_request("resources/list")

    if "error" in response:
        print(f"Error: {response['error']}")
        return

    if "result" in response:
        resources = response["result"].get("resources", [])

        if not resources:
            print("No resources available")
            return

        print(f"Total resources available: {len(resources)}\n")

        for i, resource in enumerate(resources, 1):
            print(f"{i}. {resource.get('uri', 'Unknown')}")
            if "description" in resource:
                print(f"   Description: {resource['description']}")
            print()
    else:
        print(json.dumps(response, indent=2))

def main():
    print("Unity-MCP-Server Test Client")
    print("Server URL: " + SERVER_URL)
    print()

    # Initialize session
    initialize_session()

    # List tools
    list_tools()

    # List resources
    list_resources()

if __name__ == "__main__":
    main()
