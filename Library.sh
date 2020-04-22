#!/bin/bash
#
# NAME="Library.sh"
# DESCRIPTION="A library of functions for bash shell scripts."

# ANSI escape codes
RED="\\033[1;31m"
GREEN="\\033[1;32m"
YELLOW="\\033[1;33m"
PURPLE="\\033[1;35m"
NC="\\033[0m" # no colour

L_echo_red() {
echo -e "${RED}$1${NC}"
}

L_echo_green() {
echo -e "${GREEN}$1${NC}"
}

L_echo_yellow() {
echo -e "${YELLOW}$1${NC}"
}

L_echo_purple() {
echo -e "${PURPLE}$1${NC}"
}

L_banner_begin() {
L_echo_yellow "\\n--------[  $1  ]--------\\n"
}

L_banner_end() {
L_echo_green "\\n--------[  $1 END  ]--------\\n"
}

L_sig_ok() {
L_echo_green "\\n--> [ OK ]"
}

L_sig_fail() {
L_echo_red "\\n--> [ FAIL ]"
}

L_invalid_reply() {
L_echo_red "\\n$1 is invalid input..."
}

L_invalid_reply_yn() {
L_echo_red "\\n$1 is invalid input. Please select 'Y(es)' or 'N(o)'..."
}

L_penguin() {
cat << _EOF_
(O<
(/)_
_EOF_
}

L_run_script() {
while :
do
    read -r -n 1 -p "Run script now? [yN] > "
    if [[ "$REPLY" == [yY] ]]; then
        echo -e "\\nLet's roll then ..."
        sleep 4
        break
    elif [[ "$REPLY" == [nN] || "$REPLY" == "" ]]; then
        L_echo_purple "\\n$( L_penguin )"
        exit
    else
        L_invalid_reply_yn
    fi
done
}

L_test_announce() {
    L_echo_yellow "\\n$( L_penguin ) .: Let's first run a few tests ..."
}

L_test_root() {
local ERR="ERROR: script must be run with root privileges."
if (( EUID != 0 )); then
    L_echo_red "\\n$( L_penguin ) .: $ERR"
    exit 1
fi
}

L_test_internet() {
local ERR="ERROR: script requires internet access to do its job."
local UP
export UP
UP=$( nc -z 8.8.8.8 53; echo $? ) # Google DNS is listening?
if [[ "$UP" -ne 0 ]]; then
    L_echo_red "\\n$( L_penguin ) .: $ERR"
    exit 1
fi
}

L_test_required_file() {
local FILE=$1
local ERR="ERROR: file '$FILE' not found."
if [[ ! -f "$FILE" ]]; then
    L_echo_red "\\n$( L_penguin ) .: $ERR"
    exit 1
fi
}

L_test_homedir() {
# $1 is $USER
local ERR="ERROR: no USERNAME provided."
if [[ "$#" -eq 0 ]]; then
    L_echo_red "\\n$( L_penguin ) .: $ERR"
    exit 1
elif [[ ! -d "/home/$1" ]]; then
    local ERR1="ERROR: a home directory for '$1' not found."
    L_echo_red "\\n$( L_penguin ) .: $ERR1"
    exit 1
fi
}

L_bak_file() {
for f in "$@"; do cp "$f" "$f.$(date +%FT%H%M%S).bak"; done
}

L_apt_update_upgrade() {
L_echo_yellow "\\nUpdate packages and upgrade $HOSTNAME ..."
apt update && apt -y full-upgrade
L_sig_ok
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

L_debian_codename() {
lsb_release -c | awk -F: '{print $NF}' | sed 's/[[:blank:]]//g'
}

L_all_done() {
local MSG="All done!"
if [[ -x "/usr/games/cowsay" ]]; then
    L_echo_green "$( /usr/games/cowsay "$MSG" )"
else
    echo -e "$( L_penguin ) .: $MSG"
fi
}
