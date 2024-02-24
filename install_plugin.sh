#!/bin/sh

CONFIG_PATH=$1;
shift;

BASE="https://raw.githubusercontent.com/yt-dlp-archives/plugins/main/pluggables";
NOT_FOUND=$(curl -s "${BASE}/_this_path_does_not_exist");

for name in "$@"; do
    if [ -e "${CONFIG_PATH}/${name}" ]; then
        printf "%s already exists at %s\n" "$name" "${CONFIG_PATH}/${name}";
        exit 1;
    fi

    STATUS="a";
    printf "Downloading extractor for %s ... " "${name}";
    EXTR=$(curl -s "${BASE}/${name}/yt_dlp_plugins/extractor/${name}.py");
    if [ "${EXTR}" = "$NOT_FOUND" ] ; then
        printf "Not Found. Ignoring.\n";
    else
        STATUS="b";
        printf "Done.\n";

        printf "Installing extractor for %s ... " "${name}";
        mkdir -p "${CONFIG_PATH}/${name}/yt_dlp_plugins/extractor/";
        printf "%s" "$EXTR" > "${CONFIG_PATH}/${name}/yt_dlp_plugins/extractor/${name}.py";
        printf "Done.\n";
    fi

    printf "Downloading postprocessor for %s ... " "${name}";
    PPRO=$(curl -s "${BASE}/${name}/yt_dlp_plugins/postprocessor/${name}.py");
    if [ "${PPRO}" = "$NOT_FOUND" ] ; then
        printf "Not Found. Ignoring.\n";
    else
        STATUS="b";
        printf "Done.\n";

        printf "Installing postprocessor for %s ... " "${name}";
        mkdir -p "${CONFIG_PATH}/${name}/yt_dlp_plugins/postprocessor/";
        printf "%s" "$EXTR" > "${CONFIG_PATH}/${name}/yt_dlp_plugins/postprocessor/${name}.py";
        printf "Done.\n";
    fi

    if [ "${STATUS}" = "a" ] ; then
        printf "%s\n" "$name does not exists in pluggables registry.";
    fi
done