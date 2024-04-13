import sys

if sys.version_info <= (3, 4):
    print("FATAL: your python version is too old")
    exit(1)

from pathlib import Path
import os

project_dir = Path(__file__).parents[1]
plgins_path = os.path.join(project_dir, "pluggables")

pname = input("name of new plugin: ")
if len(pname) == 0:
    print("SILLY: name of plugin cannot be empty")
    exit(0)

ptype = "postprocessor"

plugin_path = os.path.normpath(os.path.join(plgins_path, f"{pname}/yt_dlp_plugins/{ptype}/{pname}.py"))

if os.path.isfile(plugin_path):
    print(f"FATAL: {ptype} of name [{pname}] already exists")
    exit(1)

os.makedirs(os.path.dirname(plugin_path), exist_ok=True)
with open(plugin_path, f"w") as new_plugin:
    new_plugin.write(f"# created by YTDLP ARCHIVE {ptype.upper()} SCRIPT")
    new_plugin.close()

print(f"add {ptype} plugin code to file:\n\t {plugin_path}")

print("done")