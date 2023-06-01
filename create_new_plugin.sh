#!/bin/sh
NAME=$1;

if [ -z "$NAME" ]; then
	printf "give a plugin name\n";
    exit 1;
fi

mkdir -p "$NAME/yt_dlp_plugins/extractor";
mkdir -p "$NAME/yt_dlp_plugins/postprocessor";

touch "$NAME/yt_dlp_plugins/extractor/$NAME.py";
touch "$NAME/yt_dlp_plugins/postprocessor/$NAME.py";

printf "done\n";
exit 0;
