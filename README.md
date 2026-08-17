# Thunar Symlink Translator

A lightweight Python utility designed to convert absolute symbolic links to relative ones. This is particularly useful for making links portable across different environments, mounts, or machines.

## Features
* Scans selected directories or single files.
* Resolves absolute targets and rewrites them to relative links relative to their parent directories.
* Avoids altering already relative links.

## Installation & Setup
1. Clone this repository or copy the `cli.py` script.
2. In Thunar, go to **Edit** -> **Configure custom actions...**
3. Add a new action:
   * **Name:** `Translate Symlinks to Relative`
   * **Command:** `python3 /home/v/Projects/Thunar-Action/Thunar-Symlink-Translator/cli.py %F`
   * **Icon:** `emblem-symbolic-link`
4. In the **Appearance Conditions** tab, check **Directories** and all file types, setting the pattern to `*`.

## License
MIT License
