#!/bin/bash
# NAME="teleportHome.sh"
# BLURB="Sync $HOME to DESTINATION"
# SOURCE="https://github.com/vonbrownie/homebin/blob/master/teleportHome.sh"
set -eu

LIB="https://github.com/vonbrownie/homebin/blob/master/Library.sh"
HOMEBIN="$HOME/bin"
# A library of functions for shell scripts
HOMEBIN_LIB="$HOMEBIN/Library.sh"
SYNC_OPT="--archive --verbose --delete --sparse"
EXCLUDE_OPT="--exclude=*[Cc]ache*/ --exclude=*[Tt]rash*/ \
--exclude=*[Tt]humbnail*/"
DESTINATION="${*: -1}"
DEST_EXIST=1    # DESTINATION exists ... 0=True, 1=False
INCLUDE_OPT=1   # Include (and exclude) items from a config file
INCLUDE_CONFIG="$HOME/.teleportHomeInclude"

if [ -x "$HOMEBIN_LIB" ]; then
    # shellcheck source=/dev/null
    . $HOMEBIN_LIB
else
    echo -e "\n(O<"
    echo "(/)_ .: ERROR: I require '$HOMEBIN_LIB' to do my magic."
    echo "Download script from $LIB and place in $HOMEBIN."
    exit 1
fi

while getopts ":in" OPT
do
    case $OPT in
        i)
            if [ -e "$INCLUDE_CONFIG" ]; then
                INCLUDE_OPT=0
            else
                L_echo_red "$(L_penguin) .: ERROR: '$INCLUDE_CONFIG' not found."
                exit 1
            fi
            ;;
        n)
            SYNC_OPT="$SYNC_OPT --dry-run"
            ;;
        *)
            L_echo_red "$(L_penguin) .: ERROR: Invalid option '-$OPTARG'."
            exit 1
            ;;
    esac
done

# Use the ``keychain`` utility to manage SSH keys for password-less logins
# to servers.
# See http://www.circuidipity.com/secure-remote-access-using-ssh-keys.html
# shellcheck source=/dev/null
. ${HOME}/.keychain/${HOSTNAME}-sh

# Test that specified DESTINATION exists.
if [[ -z "$DESTINATION" ]]; then
    L_echo_red "$(L_penguin) .: ERROR: No DESTINATION specified."
    exit 1
elif [[ "$DESTINATION" =~ .*:.* ]]; then
    SERVER="$(echo "$DESTINATION" | cut -f1 -d':')"
    SERVER_DIR="$(echo "$DESTINATION" | cut -f2 -d':')"
    if ssh $SERVER [ -d $SERVER_DIR ]; then
        DEST_EXIST=0
    fi
else
    if [ -d $DESTINATION ]; then
        DEST_EXIST=0
    fi
fi
if [[ $DEST_EXIST -ne 0 ]]; then
    L_echo_red "$(L_penguin) .: ERROR: '$DESTINATION' not found."
    exit 1
fi

# Sync $HOME to DESTINATION
if [[ $INCLUDE_OPT -eq 0 ]]; then
    rsync $SYNC_OPT --include-from=$INCLUDE_CONFIG ${HOME}/ ${DESTINATION}/
else
    rsync $SYNC_OPT $EXCLUDE_OPT ${HOME}/ ${DESTINATION}/
fi
L_echo_green "$(L_penguin)"
