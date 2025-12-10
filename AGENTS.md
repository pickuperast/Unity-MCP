# AGENTS.md

## Build Commands
- Server: `cd Unity-MCP-Server &amp;&amp; dotnet restore &amp;&amp; dotnet build -c Release`
- Multi-platform: `cd Unity-MCP-Server &amp;&amp; ./build-all.ps1 Release` (or .sh; ~2-5min, timeout 10min)
- Unity Plugin: Open Unity-MCP-Plugin in Unity Editor (no CLI build)

## Lint/Test Commands
- Format: EditorConfig (.editorconfig); `dotnet format` if setup
- Server tests: `cd Unity-MCP-Server &amp;&amp; dotnet test`
- Single server test: `dotnet test --filter &quot;TestName=YourTest&quot;`
- Unity tests: `commands/run-unity-tests.ps1 -UnityPath &quot;C:\\Path\\To\\Unity.exe&quot; -TestMode editmode` (or playmode/standalone; needs Unity Editor, ~15-30min)
- Single Unity test: Use Unity Test Runner in Editor (EditMode/PlayMode)

## Code Style (C#)
- Indent: 4 spaces; EOL: CRLF; UTF-8
- Imports: System.* first; no groups
- Naming: PascalCase public; camelCase private; readonly fields
- Braces: new line before `{`; space around operators
- Qualify: no for fields/properties/methods; use predefined types (int/string)
- From Copilot: .NET 9; no spaces in paths; manual Unity validation

## Key Notes
- .NET 9 SDK required (NETSDK1045 if &lt;9)
- Unity paths no spaces
- Tests: EditMode/Runtime in Assets/root/Tests/
- Copilot: Reference this first; Unity needs Editor (no headless CI)
