import sys

if sys.version_info <= (3, 4):
    print("FATAL: your python version is too old")
    exit(1)

import urllib.request
import json
import os
import re

BASE_PATH = "https://raw.githubusercontent.com/yt-dlp-archives/plugins/main"

print("YTDLP ARCHIEVES PLUGINS SEARCH+INSTALLATION TOOL")

plgn_input = input("\nplugins to install (saparate by spaces): ")
if (len(plgn_input) == 0):
    print("\nSILLY: no plugins specified to install")
    exit(1)
plg_nms = re.split(" +", plgn_input)

plugins_path = input("plugin install path (empty for auto-search):")
if (len(plugins_path) == 0):
    plugin_path_lookups = [
        f"{os.getenv("XDG_CONFIG_HOME")}/yt-dlp/plugins",
        f"{os.getenv("XDG_CONFIG_HOME")}/yt-dlp-plugins",
        f"{os.getenv("APPDATA")}/yt-dlp/plugins",
        f"{os.getenv("APPDATA")}/yt-dlp-plugins",
        f"{os.getenv("HOME")}/.yt-dlp/plugins",
        f"{os.getenv("HOME")}/yt-dlp-plugins",
        f"{os.getenv("HOME")}/.config/yt-dlp/plugins",
        "/etc/yt-dlp/plugins",
        "/etc/yt-dlp-plugins"
    ]
    for pth in plugin_path_lookups:
        pthhh = os.path.normpath(pth)
        if os.path.isdir(pthhh):
            plugins_path = pthhh
            break
    if (len(plugins_path) == 0):
        print("\nWARNING: could not find plugin installation path automatically")
        plugins_path = input("manually provide plugin path: ")
        if not plugins_path.endswith("plugins"):
            print("FATAL: plugins path must end with \"plugins\"")
            exit(1)
    else:
        print(f"\nautomatically selected installation path [{plugins_path}]")

print()
plugin_list_json = json.loads(urllib.request.urlopen(f"{BASE_PATH}/pluggin_list.json").read())

for plg_nm in plg_nms:
    installed = 0
    for plgin in plugin_list_json["list"]:
        pname = plgin["plugin"]
        ptype = plgin["type"]
        if pname == plg_nm:
            print(f"[    FOUND]: install candidate [{pname}] of type [{ptype}] found")
            worked_flag = 1
            plugin_rel_path = f"{pname}/yt_dlp_plugins/{ptype}/{pname}.py"
            plugin_file_path = os.path.normpath(os.path.join(plugins_path, plugin_rel_path))
            plugin_file_data = urllib.request.urlopen(f"{BASE_PATH}/pluggables/{plugin_rel_path}").read()
            os.makedirs(os.path.dirname(plugin_file_path), exist_ok=True)
            with open(plugin_file_path, f"wb") as new_plugin:
                new_plugin.write(plugin_file_data)
                installed = 1
                new_plugin.close()
            print(f"[INSTALLED]: install candidate [{pname}] of type [{ptype}] installed")
    if installed == 0:
        print(f"[NOT_FOUND]: install candidate [{plg_nm}] not found at registry")

print("\ndone. bye o/")