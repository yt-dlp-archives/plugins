#!/bin/sh
NAME=$1;
TYPE="postprocessor";

if [ -z "$NAME" ]; then
	printf "No plugin name provided.\nUsage: %s <plugin name>\nExample: %s hanime\n" "$0" "$0";
    exit 1;
fi

if [ -e "./pluggables/$NAME/yt_dlp_plugins/$TYPE/$NAME.py" ]; then
	printf "%s for %s already exists at %s\n" "$TYPE" "$NAME" "./pluggables/$NAME/yt_dlp_plugins/";
    exit 1;
fi

mkdir -p "./pluggables/$NAME/yt_dlp_plugins/$TYPE";
touch "./pluggables/$NAME/yt_dlp_plugins/$TYPE/$NAME.py";
printf "Put your %s code in './pluggables/%s/yt_dlp_plugins/%s/%s.py'\n"  "$TYPE" "$NAME" "$TYPE" "$NAME";
printf "Done.\n";
exit 0;
