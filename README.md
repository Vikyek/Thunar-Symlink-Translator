# Thunar Symlink Translator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight Python utility designed to convert absolute symbolic links to relative ones. This is particularly useful for making links portable across different environments, mounts, or machines.

---

## 📋 Requirements & Dependencies

- **Python:** Python 3.7+
- **Desktop Alerts:** `libnotify` (`notify-send` for desktop notification dialogs)

Install on Arch Linux:
```bash
sudo pacman -S python libnotify
```

---

## 🌟 Features
* Scans selected directories or single files recursively.
* Resolves absolute targets and rewrites them to relative links relative to their parent directories.
* Avoids altering already relative links.
* Desktop notification feedback on completion.

---

## 🚀 Installation & Setup

### Automated Installation
```bash
git clone https://github.com/Vikyek/Thunar-Symlink-Translator.git
cd Thunar-Symlink-Translator
chmod +x install.sh
./install.sh
```

### Manual Installation
1. Copy `cli.py` to `~/.local/bin/thunar-symlink-translator`:
   ```bash
   mkdir -p ~/.local/bin
   cp cli.py ~/.local/bin/thunar-symlink-translator
   chmod +x ~/.local/bin/thunar-symlink-translator
   ```
2. In Thunar, go to **Edit** -> **Configure custom actions...**
3. Add a new action:
   * **Name:** `Translate Symlinks to Relative`
   * **Command:** `thunar-symlink-translator %F`
   * **Icon:** `emblem-symbolic-link`
4. In the **Appearance Conditions** tab, check **Directories** and all file types, setting the pattern to `*`.

---

## 💻 Usage & CLI Examples

### Via Command Line
```bash
# Convert symlinks in a specific folder recursively
thunar-symlink-translator /path/to/directory

# Convert multiple specific files or symlinks
thunar-symlink-translator /path/to/link1 /path/to/link2 /path/to/folder
```

### Via Thunar File Manager
1. Select one or more folders or symlinked files in Thunar.
2. Right-click and choose **Translate Symlinks to Relative**.
3. A notification will display the number of converted symlinks.

---

## 🔗 Part of a Larger Collection
This project is part of the **[Thunar-Action-Collection](https://github.com/Vikyek/Thunar-Action-Collection)**—a curated collection of custom Thunar action scripts and utilities designed to enhance the Thunar File Manager on Linux. Visit the collection repository for other useful actions and full setup guides.

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
