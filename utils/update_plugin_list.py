import sys

if sys.version_info <= (3, 4):
    print("FATAL: your python version is too old")
    exit(1)

from pathlib import Path
import os
import json

project_dir = Path(__file__).parents[1]
plgin_path = os.path.join(project_dir, "pluggables")

plgin_list = []
plgin_list_simple = "# PLUGINS LIST\n"
for pname in os.listdir(plgin_path):
    ptypes = os.path.join(os.path.join(plgin_path, pname), "yt_dlp_plugins")
    for ptype in os.listdir(ptypes):
        if os.path.isfile(os.path.normpath(os.path.join(os.path.join(ptypes, ptype), f"{pname}.py"))):
            print(f"adding pluggin [{pname}] of type [{ptype}]")
            plgin_list.append({"plugin": pname, "type": ptype})
            plgin_list_simple += f"- **{pname}** (*{ptype}*)\n"

with open(os.path.join(project_dir, "pluggin_list.json"), "w") as json_file:
    json.dump({"list": plgin_list}, json_file, indent=4)
    json_file.close()

with open(os.path.join(project_dir, "pluggin_list.md"), "w") as md_file:
    md_file.write(plgin_list_simple)
    md_file.close()