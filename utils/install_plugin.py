import sys

if sys.version_info <= (3, 4):
    print("your python version is too old")
    exit(1)

import urllib.request
import json

print("YTDLP ARCHIEVES PLUGINS SEARCH+INSTALLATION TOOL\n")
plg_nm = input("plugin name: ")
plugin_list_json = json.loads(urllib.request.urlopen("https://raw.githubusercontent.com/yt-dlp-archives/plugins/main/pluggin_list.json").read())

print("\n")
worked_flag = 0
for plgin in plugin_list_json["list"]:
    if plgin["plugin"] == plg_nm:
        # install
        print(f"install candidate found of type [{plgin["type"]}]")
        worked_flag = 1

if worked_flag == 0:
    print(f"no installation candidate for plugin of name: \"{plg_nm}\"")
    exit(1)
else:
    print("done")