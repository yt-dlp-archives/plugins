import sys

if sys.version_info <= (3, 4):
    print("your python version is too old")
    exit(1)

from pathlib import Path
import os
import json

project_dir = Path(__file__).parents[1]
plgin_path = os.path.join(project_dir, "pluggables")

plgin_list = []
for pname in os.listdir(plgin_path):
    ptypes = os.path.join(os.path.join(plgin_path, pname), "yt_dlp_plugins")
    for ptype in os.listdir(ptypes):
        if os.path.isfile(os.path.join(os.path.join(ptypes, ptype), f"{pname}.py")):
            print(f"adding pluggin [{pname}] of type [{ptype}]")
            plgin_list.append({"plugin": pname, "type": ptype})

with open(os.path.join(project_dir, "pluggin_list.json"), "w") as json_file:
    json.dump({"list": plgin_list}, json_file, indent=4)
    json_file.close()