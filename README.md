# YT-DLP Archieve Plugins
An archieve of all rejected and/or contriversial yt-dlp Plugin code for educational and example purposes.

# Rules
1. All Plugins must be working.
2. No Plugin should contain unnecessary/malicious code.
3. No code here should be used for nothing other than educational purposes AND ESPECIALLY NOT FOR PIRACY.
4. Have fun. 🗿

# Project Structure
```html
-- <this repo>
    \
    |-- README.md
    .
    .
    .
    |-- pluggables/
        \
        |-- <plugin_name_1>/
        |   \
        |   |-- yt_dlp_plugins/
        |       \
        |       |-- extractor/  (if plugin has extractor)
        |       |   \
        |       |   |-- <plugin_name_1>.py
        |       |
        |       |-- postprocessor/  (if plugin has postprocessor)
        |           \
        |           |-- <plugin_name_1>.py
        |
        |-- <plugin_name_2>/
        .   \
        .   |-- ...
        .
```
This project structure is to abide by the yt-dlp Plugin specifications as of date. But you don't have to care about that.
`create_new_extractor.sh` and `create_new_postprocessor.sh` scripts will build the required directory structure for you.
