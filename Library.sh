#!/bin/bash
# NAME="Library.sh"
# BLURB="A library of functions for bash shell scripts"
# SOURCE="https://github.com/vonbrownie/homebin"
set -eu

# Place script in $HOME/bin and call its functions by adding to a script ...
# . $HOME/bin/Library.sh

# ANSI escape codes
RED="\033[1;31m"
GREEN="\033[1;32m"
YELLOW="\033[1;33m"
NC="\033[0m" # no colour


L_echo_red() {
echo -e "${RED}$1${NC}"
}


L_echo_green() {
echo -e "${GREEN}$1${NC}"
}


L_echo_yellow() {
echo -e "${YELLOW}$1${NC}"
}


L_penguin() {
cat << _EOF_
(O<
(/)_
_EOF_
}


L_invalid_reply() {
L_echo_red "\n'${REPLY}' is invalid input..."
}


L_invalid_reply_yn() {
L_echo_red "\n'${REPLY}' is invalid input. Please select 'Y(es)' or 'N(o)'..."
}


L_run_script() {
while :
do
    read -n 1 -p "Run script now? [yN] > "
    if [[ $REPLY == [yY] ]]; then
        echo -e "\nLet's roll then ..."
        sleep 2
        if [[ -x "/usr/games/sl" ]]; then
            /usr/games/sl
        fi
        break
    elif [[ $REPLY == [nN] || $REPLY == "" ]]; then
        echo -e "\n$( L_penguin )"
        exit
    else
        L_invalid_reply_yn
    fi
done
}


L_banner_begin() {
L_echo_yellow "\n\t\t*** $1 BEGIN ***\n"
}


L_banner_end() {
L_echo_green "\n\t\t*** $1 END ***\n"
}


L_sig_ok() {
L_echo_green "--> [ OK ]"
}


L_sig_fail() {
L_echo_red "--> [ FAIL ]"
}


L_mktemp_dir_pwd() {
# Create a workspace directory within DIR
local DIR
    DIR="$(pwd)"
local WORK_DIR
    WORK_DIR=$( mktemp -d -p "$DIR" )
if [[ ! "$WORK_DIR" || ! -d "$WORK_DIR" ]]; then
    exit 1
fi
echo "$WORK_DIR"
}


L_mnt_mount_vfat() {
# $1 is sd[a-z][0-9] and $2 is MOUNTPOINT
local _UID
    _UID="1000"
local _GID
    _GID="1000"
# Helpful! https://help.ubuntu.com/community/Mount/USB#Mount_the_Drive
# Extra MNT_OPTS allow read and write on drive with regular username
local MNT_OPTS
    MNT_OPTS="uid=$_UID,gid=$_GID,utf8,dmask=027,fmask=137"
sudo mount -t vfat /dev/"$1" "$2" -o $MNT_OPTS
if [[ ! $( L_mnt_detect "$1" ) ]]; then
    exit 1
fi
}


L_mnt_mount() {
# $1 is sd[a-z][0-9] and $2 is MOUNTPOINT
local M_DEVICE
    M_DEVICE="$( mount | grep "$1" | cut -d' ' -f1 )"
sudo mount "/dev/$1" "$2"
# confirm
if [[ ! $( L_mnt_detect "$1" ) ]]; then
    L_sig_fail
    exit 1
fi
}


L_mnt_umount() {
# $1 is sd[a-z][0-9]
local M_DEVICE
    M_DEVICE="$( mount | grep "$1" | cut -d' ' -f1 )"
sudo umount "$M_DEVICE"
# confirm
if [[ $( L_mnt_detect "$1" ) ]]; then
    L_sig_fail
    exit 1
fi
}


L_bak_file() {
for f in "$@"; do cp "$f" "$f.$(date +%FT%H%M%S).bak"; done
}


L_all_done() {
local AU_REVOIR
    AU_REVOIR="All done!"
if [[ -x "/usr/games/cowsay" ]]; then
    /usr/games/cowsay "$AU_REVOIR"
else
    echo -e "$( L_penguin ) .: $AU_REVOIR"
fi
}


