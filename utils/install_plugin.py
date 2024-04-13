import sys

if sys.version_info <= (3, 4):
    print("your python version is too old")
    exit(1)

import urllib.request
import json
import os
import re

BASE_PATH = "https://raw.githubusercontent.com/yt-dlp-archives/plugins/main"

print("YTDLP ARCHIEVES PLUGINS SEARCH+INSTALLATION TOOL")
plg_nms = re.split(" +", input("plugins to install (saparate by spaces): "))
plugin_list_json = json.loads(urllib.request.urlopen(f"{BASE_PATH}/pluggin_list.json").read())

plugins_path = os.path.join(os.getcwd(), "_ignored")

print("\n")
for plg_nm in plg_nms:
    installed = 0
    for plgin in plugin_list_json["list"]:
        pname = plgin["plugin"]
        ptype = plgin["type"]
        if pname == plg_nm:
            print(f"[    FOUND] install candidate [{pname}] of type [{ptype}] found")
            worked_flag = 1
            plugin_rel_path = f"{pname}/yt_dlp_plugins/{ptype}/{pname}.py"
            plugin_file_path = os.path.join(plugins_path, plugin_rel_path)
            plugin_file_data = urllib.request.urlopen(f"{BASE_PATH}/pluggables/{plugin_rel_path}").read()
            os.makedirs(os.path.dirname(plugin_file_path), exist_ok=True)
            with open(plugin_file_path, f"wb") as new_plugin:
                new_plugin.write(plugin_file_data)
                installed = 1
                new_plugin.close()
            print(f"[INSTALLED] install candidate [{pname}] of type [{ptype}] installed")
    if installed == 0:
        print(f"[NOT_FOUND] install candidate [{plg_nm}] not found at registry")

print("\ndone. bye o/")