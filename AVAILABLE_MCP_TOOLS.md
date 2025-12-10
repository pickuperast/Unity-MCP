# Available MCP Tools in Unity-MCP-Server

This document lists all available MCP tools provided by the Unity-MCP-Plugin.

## Server Information
- **Server Name**: unity-mcp-server
- **Version**: 0.22.1
- **Running on Port**: 2248 (mapped from internal port 8080)
- **Transport**: HTTP with Server-Sent Events (SSE)
- **Protocol Version**: 2024-11-05

## How Tools Are Exposed

Tools are defined in the Unity-MCP-Plugin using the `[McpPluginTool]` attribute:

```csharp
[McpPluginTool("tool_name", Title = "Tool Title")]
public string MethodName(params...) { ... }
```

## Asset Management Tools

### Assets_Find
**Description**: Search the asset database using the search filter string

**Method**: `Assets_Find`

**Parameters**:
- `filter` (string, optional): Search filter string. Can be empty.
  - Name search: `"test asset"` or `"test"`
  - Type search: `"t:Texture"`, `"t:Prefab"`, etc.
  - Label search: `"l:important"`
  - AssetBundle search: `"b:bundlename"`
  - Area search: `"a:assets"`, `"a:packages"`, `"a:all"`
  - Glob search: `"glob:Editor/*"`

- `searchInFolders` (string[], optional): Folders where search will start. If null, searches all folders.

**Available Asset Types**:
- t:AnimationClip
- t:AudioClip
- t:AudioMixer
- t:ComputeShader
- t:Font
- t:GUISkin
- t:Material
- t:Mesh
- t:Model
- t:PhysicMaterial
- t:Prefab
- t:Scene
- t:Script
- t:Shader
- t:Sprite
- t:Texture
- t:VideoClip
- t:VisualEffectAsset
- t:VisualEffectSubgraph

**Example**:
```json
{
  "method": "tools/call",
  "params": {
    "name": "Assets_Find",
    "arguments": {
      "filter": "t:Material l:important",
      "searchInFolders": ["Assets/Materials"]
    }
  }
}
```

### Assets_Load
**Description**: Load an asset from the project

**Related Files**:
- Assets.Load.cs

### Assets_Read
**Description**: Read asset file contents

**Related Files**:
- Assets.Read.cs

### Assets_Modify
**Description**: Modify asset properties

**Related Files**:
- Assets.Modify.cs

### Assets_Move
**Description**: Move assets to a new location

**Related Files**:
- Assets.Move.cs

### Assets_Copy
**Description**: Copy assets in the project

**Related Files**:
- Assets.Copy.cs

### Assets_Delete
**Description**: Delete assets from the project

**Related Files**:
- Assets.Delete.cs

### Assets_CreateFolders
**Description**: Create folder structure in the project

**Related Files**:
- Assets.CreateFolders.cs

### Assets_Refresh
**Description**: Refresh the asset database

**Related Files**:
- Assets.Refresh.cs

## Material Tools

### Assets_Material_Create
**Description**: Create a new material asset

**Related Files**:
- Assets.Material.Create.cs

### Assets_Material
**Description**: Manage material assets

**Related Files**:
- Assets.Material.cs

### Assets_Shader_ListAll
**Description**: List all available shaders in the project

**Related Files**:
- Assets.Shader.ListAll.cs

### Assets_Shader
**Description**: Manage shader assets

**Related Files**:
- Assets.Shader.cs

## Prefab Tools

### Assets_Prefab
**Description**: Manage prefab assets

**Related Files**:
- Assets.Prefab.cs

### Assets_Prefab_Create
**Description**: Create a new prefab from a GameObject

**Related Files**:
- Assets.Prefab.Create.cs

### Assets_Prefab_Open
**Description**: Open a prefab for editing

**Related Files**:
- Assets.Prefab.Open.cs

### Assets_Prefab_Close
**Description**: Close the prefab editing mode

**Related Files**:
- Assets.Prefab.Close.cs

### Assets_Prefab_Save
**Description**: Save changes to a prefab

**Related Files**:
- Assets.Prefab.Save.cs

### Assets_Prefab_Instantiate
**Description**: Instantiate a prefab in the scene

**Related Files**:
- Assets.Prefab.Instantiate.cs

## GameObject Tools

### GameObject_Find
**Description**: Find GameObjects in the scene hierarchy

**Related Files**:
- GameObject.Find.cs

### GameObject_Create
**Description**: Create a new GameObject

**Related Files**:
- GameObject.Create.cs

### GameObject_Destroy
**Description**: Destroy a GameObject

**Related Files**:
- GameObject.Destroy.cs

### GameObject_Duplicate
**Description**: Duplicate a GameObject

**Related Files**:
- GameObject.Duplicate.cs

### GameObject_Modify
**Description**: Modify GameObject properties (name, position, rotation, etc.)

**Related Files**:
- GameObject.Modify.cs

### GameObject_SetParent
**Description**: Change the parent of a GameObject

**Related Files**:
- GameObject.SetParent.cs

### GameObject_AddComponent
**Description**: Add a component to a GameObject

**Related Files**:
- GameObject.AddComponent.cs

### GameObject_DestroyComponents
**Description**: Remove components from a GameObject

**Related Files**:
- GameObject.DestroyComponents.cs

## Component Tools

### Component_GetAll
**Description**: Get all components on a GameObject

**Related Files**:
- Component.GetAll.cs

### Component
**Description**: Manage components on GameObjects

**Related Files**:
- Component.cs

## Scene Management Tools

### Scene_Create
**Description**: Create a new scene

**Related Files**:
- Scene.Create.cs

### Scene_Load
**Description**: Load a scene from the project

**Related Files**:
- Scene.Load.cs

### Scene_Save
**Description**: Save the current scene

**Related Files**:
- Scene.Save.cs

### Scene_Unload
**Description**: Unload a scene

**Related Files**:
- Scene.Unload.cs

### Scene_GetLoaded
**Description**: Get list of currently loaded scenes

**Related Files**:
- Scene.GetLoaded.cs

### Scene_GetHierarchy
**Description**: Get the GameObject hierarchy of a scene

**Related Files**:
- Scene.GetHierarchy.cs

## Editor Control Tools

### Editor_Selection_Get
**Description**: Get the current selected GameObjects in the editor

**Related Files**:
- Editor.Selection.Get.cs

### Editor_Selection_Set
**Description**: Set the selected GameObjects in the editor

**Related Files**:
- Editor.Selection.Set.cs

### Editor_Selection
**Description**: Manage editor selection

**Related Files**:
- Editor.Selection.cs

### Editor_SetApplicationState
**Description**: Control editor application state (play/pause/stop)

**Related Files**:
- Editor.SetApplicationState.cs

### Editor_GetApplicationInformation
**Description**: Get information about the editor (version, paths, etc.)

**Related Files**:
- Editor.GetApplicationInformation.cs

### Editor
**Description**: General editor information and stats

**Related Files**:
- Editor.cs

## Script Management Tools

### Script_Read
**Description**: Read script file contents

**Related Files**:
- Script.Read.cs

### Script_UpdateOrCreate
**Description**: Update or create a script file

**Related Files**:
- Script.UpdateOrCreate.cs

### Script_Delete
**Description**: Delete a script file

**Related Files**:
- Script.Delete.cs

### Script_Execute
**Description**: Execute/compile a script

**Related Files**:
- Script.Execute.cs

### Script
**Description**: Manage script files

**Related Files**:
- Script.cs

## Scripting Tools

### Reflection_MethodFind
**Description**: Find methods in loaded assemblies

**Related Files**:
- Reflection.MethodFind.cs

### Reflection_MethodCall
**Description**: Call methods in loaded assemblies

**Related Files**:
- Reflection.MethodCall.cs

### Reflection
**Description**: Reflection utilities

**Related Files**:
- Reflection.cs

## Console Tools

### Console_GetLogs
**Description**: Get console logs from the editor

**Related Files**:
- Console.GetLogs.cs

### Console
**Description**: Console management

**Related Files**:
- Console.cs

## Test Tools

### TestRunner_Run
**Description**: Run unit tests in the project

**Related Files**:
- TestRunner.Run.cs
- TestRunner/ (supporting classes)

### TestRunner
**Description**: Test runner management

**Related Files**:
- TestRunner.cs

## Resources

### GameObject Hierarchy Resource
**Description**: Read the GameObject hierarchy structure of a scene

**Related Files**:
- GameObject.Hierarchy.cs

## Prompts

### Asset Management Prompt
**Description**: Structured prompt for asset management operations

**Related Files**:
- AssetManagement.cs

### Animation Timeline Prompt
**Description**: Structured prompt for animation timeline operations

**Related Files**:
- AnimationTimeline.cs

### Scene Management Prompt
**Description**: Structured prompt for scene management operations

**Related Files**:
- SceneManagement.cs

### GameObject & Component Prompt
**Description**: Structured prompt for GameObject and component operations

**Related Files**:
- GameObjectComponent.cs

### Scripting & Code Prompt
**Description**: Structured prompt for scripting and code operations

**Related Files**:
- ScriptingCode.cs

### Debugging & Testing Prompt
**Description**: Structured prompt for debugging and testing operations

**Related Files**:
- DebuggingTesting.cs

## Tool Categories Summary

```
Total Tools Available: 50+

Categories:
├── Asset Management (7)
│   ├── Assets_Find
│   ├── Assets_Load
│   ├── Assets_Read
│   ├── Assets_Modify
│   ├── Assets_Move
│   ├── Assets_Copy
│   ├── Assets_Delete
│   └── Assets_CreateFolders
│
├── Material & Shader (4)
│   ├── Assets_Material_Create
│   ├── Assets_Material
│   ├── Assets_Shader
│   └── Assets_Shader_ListAll
│
├── Prefab Management (6)
│   ├── Assets_Prefab
│   ├── Assets_Prefab_Create
│   ├── Assets_Prefab_Open
│   ├── Assets_Prefab_Close
│   ├── Assets_Prefab_Save
│   └── Assets_Prefab_Instantiate
│
├── GameObject Operations (8)
│   ├── GameObject_Find
│   ├── GameObject_Create
│   ├── GameObject_Destroy
│   ├── GameObject_Duplicate
│   ├── GameObject_Modify
│   ├── GameObject_SetParent
│   ├── GameObject_AddComponent
│   └── GameObject_DestroyComponents
│
├── Components (2)
│   ├── Component_GetAll
│   └── Component
│
├── Scene Management (6)
│   ├── Scene_Create
│   ├── Scene_Load
│   ├── Scene_Save
│   ├── Scene_Unload
│   ├── Scene_GetLoaded
│   └── Scene_GetHierarchy
│
├── Editor Control (6)
│   ├── Editor_Selection_Get
│   ├── Editor_Selection_Set
│   ├── Editor_Selection
│   ├── Editor_SetApplicationState
│   ├── Editor_GetApplicationInformation
│   └── Editor
│
├── Script Management (5)
│   ├── Script_Read
│   ├── Script_UpdateOrCreate
│   ├── Script_Delete
│   ├── Script_Execute
│   └── Script
│
├── Scripting (3)
│   ├── Reflection_MethodFind
│   ├── Reflection_MethodCall
│   └── Reflection
│
├── Console (2)
│   ├── Console_GetLogs
│   └── Console
│
└── Testing (2)
    ├── TestRunner_Run
    └── TestRunner
```

## Architecture Overview

### Tool Registration
Tools are registered using the `[McpPluginToolType]` attribute on classes that contain tool methods. Each tool method is decorated with `[McpPluginTool]` attribute that specifies:
- Tool ID/Name
- Tool Title
- Description
- Parameter schemas

### Tool Execution Flow
```
MCP Client
    ↓
HTTP POST to /
    ↓
MCP Server (unity-mcp-server)
    ↓
Tool Router (via McpPlugin.Server)
    ↓
Unity Plugin (via SignalR on port 8080)
    ↓
Tool Implementation (Reflection-based execution)
    ↓
Response back through chain
```

### Parameter Passing
Tools support structured parameters through JSON schemas. Parameters are validated and type-converted before being passed to the tool methods. Complex types like Vector3, Quaternion, Color, etc. are supported through custom JSON converters.

## Using the Server

### 1. Start the Docker Container
```bash
docker run -p 2248:8080 unity-mcp-server
```

### 2. Initialize MCP Session
```bash
curl -X POST http://localhost:2248/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
      "protocolVersion": "2024-11-05",
      "capabilities": {},
      "clientInfo": {"name": "my-client", "version": "1.0"}
    }
  }'
```

### 3. Call a Tool
```bash
curl -X POST http://localhost:2248/ \
  -H "Content-Type: application/json" \
  -H "Mcp-Session-Id: <session-id>" \
  -d '{
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {
      "name": "Assets_Find",
      "arguments": {
        "filter": "t:Material"
      }
    }
  }'
```

### 4. List Available Tools
```bash
curl -X POST http://localhost:2248/ \
  -H "Content-Type: application/json" \
  -H "Mcp-Session-Id: <session-id>" \
  -d '{
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/list",
    "params": {}
  }'
```

## Notes

- The server requires an active Unity Editor instance with the Unity-MCP-Plugin running
- The plugin communicates with the server via SignalR on port 8080 (configurable)
- Tool execution timeout is 10000ms by default (configurable)
- All tools run on the main Unity Editor thread
- Complex operations (like script compilation) may take time

## Configuration

Key environment variables (set when starting the container):
- `UNITY_MCP_PORT` (default: 8080): Plugin connection port
- `UNITY_MCP_PLUGIN_TIMEOUT` (default: 10000): Plugin timeout in milliseconds
- `UNITY_MCP_CLIENT_TRANSPORT` (default: http): Transport method (stdio or http)
