#!/bin/sh

# PATH=$1
ls
# BASE="https://raw.githubusercontent.com/yt-dlp-archives/plugins/main/pluggables";

# for name in "$@"; do
#     printf "Downloading %s ...\n" "${name}";
#     EXTR=$(curl "${BASE}/${name}/yt_dlp_plugins/extractor/${name}.py" || printf "404: Not Found");
#     PPRO=$(curl "${BASE}/${name}/yt_dlp_plugins/postprocessor/${name}.py" || printf "404: Not Found");
#     if [ "${EXTR}" = "404: Not Found" ]&&[ "${PPRO}" = "404: Not Found" ] ; then
#         printf "%s" "${EXTR}";
#     fi
# done