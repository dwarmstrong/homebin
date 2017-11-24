#!/bin/bash
# NAME="startup.sh"
# BLURB="personal startup script"
# SOURCE="https://github.com/vonbrownie/homebin/blob/master/startup.sh"

# Inspired by "Better Control for Startup Applications"
# https://ubuntu-mate.community/t/better-control-for-startup-applications/11484

# Play the Ubuntu login sound
paplay --volume=50000 /usr/share/sounds/ubuntu/stereo/desktop-login.ogg &

sleep 2

# Bind commands to certain keys and load key mappings
/home/dwa/bin/keyboardconf &

# Clipboard manager
parcellite &

# Janitor                 
[ -d ~/.local/share/Trash ] && rm -rf ~/.local/share/Trash/*
