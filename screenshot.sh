#!/usr/bin/env bash
#
# Capture and display screenshots in GNOME using gnome-screenshot and
# eog (image viewer).
# In `Settings->Devices->Keyboard` I unset default screenshot shortcuts
# and make custom shortcuts to capture:
# * desktop - Print
# * window - Alt+Print
# * area - Shift+Print
#
FILENAME="${HOME}/tmp/screenshot-$(date +%FT%H%M%S).png"
if [ $# -eq 0 ]; then
    gnome-screenshot -f "$FILENAME"
elif [ $# -eq 1 ]; then
    # $1 = '-w' (window) or '-a' (select area)
    gnome-screenshot "$1" -f "$FILENAME"
fi
eog "$FILENAME"
