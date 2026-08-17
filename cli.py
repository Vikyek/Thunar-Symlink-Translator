#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

def notify(title, msg, icon="dialog-information"):
    subprocess.run(["notify-send", title, msg, "-i", icon])

def make_relative(link_path):
    """Converts an absolute symlink to a relative one."""
    if not os.path.islink(link_path):
        return False, "Not a symbolic link"
    
    try:
        target = os.readlink(link_path)
        if not os.path.isabs(target):
            return False, "Already relative"
        
        parent = os.path.dirname(os.path.abspath(link_path))
        relative_target = os.path.relpath(target, parent)
        
        # Recreate symlink as relative
        os.unlink(link_path)
        os.symlink(relative_target, link_path)
        return True, relative_target
    except Exception as e:
        return False, str(e)

def process_path(p, results):
    if os.path.islink(p):
        success, res = make_relative(p)
        if success:
            results["converted"].append((p, res))
        else:
            results["skipped"].append((p, res))
    elif os.path.isdir(p):
        for root, dirs, files in os.walk(p):
            for d in dirs:
                full_path = os.path.join(root, d)
                if os.path.islink(full_path):
                    success, res = make_relative(full_path)
                    if success:
                        results["converted"].append((full_path, res))
            for f in files:
                full_path = os.path.join(root, f)
                if os.path.islink(full_path):
                    success, res = make_relative(full_path)
                    if success:
                        results["converted"].append((full_path, res))

def main():
    if len(sys.argv) < 2:
        notify("Symlink Portable Translator", "No files or directories specified.")
        return

    # Use arguments, handling any that might start with dashes by skipping them
    targets = [t for t in sys.argv[1:] if os.path.exists(t) or os.path.islink(t)]

    if not targets:
        notify("Symlink Portable Translator", "No valid targets found.")
        return

    results = {
        "converted": [],
        "skipped": []
    }

    for target in targets:
        process_path(target, results)

    converted_count = len(results["converted"])
    
    if converted_count > 0:
        msg = f"Successfully converted {converted_count} symlinks to relative paths."
        notify("Symlink Translator Complete", msg, "dialog-ok")
    else:
        notify("Symlink Translator Complete", "No absolute symlinks needed translation.", "dialog-information")

if __name__ == "__main__":
    main()
