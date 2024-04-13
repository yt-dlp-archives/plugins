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

for plgin in plugin_list_json["list"]:
    pname = plgin["plugin"]
    ptype = plgin["type"]
    for plg_nm in plg_nms:
        if pname == plg_nm:
            print(f"install candidate [{pname}] found of type [{ptype}]")
            worked_flag = 1
            plugin_file_path = os.path.join(plugins_path, f"{pname}/yt_dlp_plugins/{ptype}/{pname}.py")
            plugin_file = urllib.request.urlopen(f"{BASE_PATH}/pluggables/{pname}/yt_dlp_plugins/{ptype}/{pname}.py").read()
            os.makedirs(os.path.dirname(plugin_file_path), exist_ok=True)
            with open(plugin_file_path, f"wb") as new_plugin:
                new_plugin.write(plugin_file)
                new_plugin.close()

if worked_flag == 0:
    print(f"no installation candidate for plugin of name: \"{plg_nm}\"")
    exit(1)
else:
    print("done")