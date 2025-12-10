/*
┌──────────────────────────────────────────────────────────────────┐
│  Author: Ivan Murzak (https://github.com/IvanMurzak)             │
│  Repository: GitHub (https://github.com/IvanMurzak/Unity-MCP)    │
│  Copyright (c) 2025 Ivan Murzak                                  │
│  Licensed under the Apache License, Version 2.0.                 │
│  See the LICENSE file in the project root for more information.  │
└──────────────────────────────────────────────────────────────────┘
*/

#nullable enable
using System.ComponentModel;
using System.Text;
using com.IvanMurzak.McpPlugin;
using com.IvanMurzak.ReflectorNet.Utils;
using UnityEditor;

namespace com.IvanMurzak.Unity.MCP.Editor.API
{
    using Consts = McpPlugin.Common.Consts;
    public partial class Tool_Assets
    {
        [McpPluginTool
        (
            "Assets_Find",
            Title = "Find assets in the project"
        )]
        [Description(@"Search assets by name, type (t:), label (l:), bundle (b:), area (a:), or glob pattern. Common types: t:Prefab t:Scene t:Script t:Material t:Texture t:AudioClip t:Sprite t:Mesh t:AnimationClip")]
        public string Search
        (
            // <ref>https://docs.unity3d.com/ScriptReference/AssetDatabase.FindAssets.html</ref>
            [Description("Search filter. Supports: name, t:Type, l:label, b:bundle, a:area, glob:pattern. Case insensitive. Empty searches all.")]
            string? filter = null,
            [Description("Folders to search in. If null, searches all folders.")]
            string[]? searchInFolders = null
        )
        => MainThread.Instance.Run(() =>
        {
            var assetGuids = (searchInFolders?.Length ?? 0) == 0
                ? AssetDatabase.FindAssets(filter ?? string.Empty)
                : AssetDatabase.FindAssets(filter ?? string.Empty, searchInFolders);

            var stringBuilder = new StringBuilder();
            stringBuilder.AppendLine("instanceID | assetGuid                            | assetPath");
            stringBuilder.AppendLine("-----------+--------------------------------------+---------------------------------");
            //                       " -12345    | 8e09c738-7b14-4d83-9740-2b396bd4cfc9 | Assets/Editor/Image.png");

            for (var i = 0; i < assetGuids.Length; i++)
            {
                if (i >= Consts.MCP.Plugin.LinesLimit)
                {
                    stringBuilder.AppendLine($"... and {assetGuids.Length - i} more assets. Use {nameof(searchInFolders)} parameter to specify request.");
                    break;
                }
                var assetPath = AssetDatabase.GUIDToAssetPath(assetGuids[i]);
                var assetObject = AssetDatabase.LoadAssetAtPath<UnityEngine.Object>(assetPath);
                if (assetObject == null) continue;
                var instanceID = assetObject.GetInstanceID();
                stringBuilder.AppendLine($"{instanceID,-10} | {assetGuids[i],-36} | {assetPath}");
            }

            return $"[Success] Assets found: {assetGuids.Length}.\n{stringBuilder}";
        });
    }
}