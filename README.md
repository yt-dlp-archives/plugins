![demo_img](./demo.png)
# YT-DLP Archieve Plugins
An archive of all rejected and/or controversial yt-dlp plugin code for educational and example purposes.

# Rules
1. All plugins must be working.
2. No plugin should contain unnecessary/malicious code.
3. No code here should be used for anything other than educational purposes AND ESPECIALLY NOT FOR PIRACY.
4. Have fun. 🗿

# List of Plugins
Look inside https://github.com/yt-dlp-archives/plugins/blob/main/pluggin_list.md

# How do I install a plugin from here?
## Automated install
```bash
python -c "import urllib.request as r;exec(r.urlopen('https://a.hman.io/l/yi').read())"
```
It will interactively ask you for needed info. (like in the demo image)  
> NOTE: You might need to type "python.exe" instead of just "python" on windows.  
> NOTE: You should read https://a.hman.io/l/yi (install script) to make sure I aren't doing anything sus.  
https://a.hman.io/l is my link shortner.

## Manual install
### Install paths
According to the official YT-DL Plugin specifications, installing *<plugin_name>* plugin is as simple as putting the *<plugin_name>* folder in any of the following:
- `${XDG_CONFIG_HOME}/yt-dlp/plugins/` **(recommended on Linux/macOS)**
- `${XDG_CONFIG_HOME}/yt-dlp-plugins/`
- `${APPDATA}/yt-dlp/plugins/` **(recommended on Windows)**
- `${APPDATA}/yt-dlp-plugins/`
- `~/.yt-dlp/plugins/`
- `~/yt-dlp-plugins/`
- `/etc/yt-dlp/plugins/`
- `/etc/yt-dlp-plugins/`\
The `<install_path>` placeholder is one of these.
1. Clone this repo:
```bash
git clone https://github.com/yt-dlp-archives/plugins.git yt-dl_archive_plugins
```
2. Open the `yt-dl_archive_plugins` cloned above.
3. Open the `pluggables` folder in `yt-dl_archive_plugins`.
4. Copy the *<plugin_name>* folder into *<install_path>*.

# How do I add a new plugin?
1. Clone this repo and get into the directory:
```bash
git clone https://github.com/yt-dlp-archives/plugins.git yt-dl_archive_plugins
cd yt-dl_archive_plugins
```
2.
    1. If your plugin has an extractor:
    ```bash
    python utils/create_new_extractor.py
    ```
    > NOTE: You might need to type "python.exe" instead of just "python" on windows.  
    2. If your plugin has a postprocessor:
    ```bash
    python utils/create_new_postprocessor.py
    ```
    > NOTE: You might need to type "python.exe" instead of just "python" on windows.  
3. Follow the instructions provided by the scripts.
4. Update the registry
    ```bash
    python utils/update_plugin_list.py
    ```
    > NOTE: You might need to type "python.exe" instead of just "python" on windows.  
5. Make a pull request to this repository.


# Some sites are disabled by default by yt-dlp
Install the plugin named `ununsupported` to remove the restrictions.  
Follow: [How do I install a plugin](#how-do-i-install-a-plugin-from-here)

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
This project structure is to abide by the yt-dlp plugin specifications as of date. \
But you don't have to care about that. \
`utils/create_new_extractor.py` and `utils/create_new_postprocessor.py` scripts will build the required directory structure for you.
