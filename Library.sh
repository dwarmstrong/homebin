#!/bin/bash
# (O< 
# (/)_ .: Library.sh -- a library of functions for bash shell scripts :.
# SOURCE
#     https://github.com/vonbrownie/homebin/blob/master/Library.sh
#
# To use these functions in shell scripts ... place this script in $HOME/bin
# and call its functions by adding:
#
# . Library.sh
#
# "A library for shell scripts"
#    http://www.circuidipity.com/shell-script-library.html

echoRed() {
echo -e "\E[1;31m$1"
echo -e '\e[0m'
}

echoGreen() {
echo -e "\E[1;32m$1"
echo -e '\e[0m'
}

echoYellow() {
echo -e "\E[1;33m$1"
echo -e '\e[0m'
}

echoBlue() {
echo -e "\E[1;34m$1"
echo -e '\e[0m'
}

echoMagenta() {
echo -e "\E[1;35m$1"
echo -e '\e[0m'
}

echoCyan() {
echo -e "\E[1;36m$1"
echo -e '\e[0m'
}

penguinista() {
cat << _EOF_

(O<
(/)_
_EOF_
}

header() {
echoCyan "$( penguinista ) .: $top ..."                                            
}                                                                                  
                                                                                   
footer() {
echoGreen "\n\nOK ... $bottom ..."
sleep 4                                                                            
}                                                                                  
                                                                                   
exitOK() {
echoGreen "\n$( penguinista ) .: Exiting ... Have a good day!"
exit                                                                               
}                                                                                  
                                                                                   
badRep() {
echoRed "\n'$REPLY' is invalid input ...\n"                                        
}                                                                                  
                                                                                   
badRepYN() {
echoRed "\n'$REPLY' is invalid input. Please select 'Y(es)' or 'N(o)' ...\n"       
}

confirmStart() {
while :
do
    read -n 1 -p "Run script now? [yN] > "
    if [[ $REPLY == [yY] ]]
    then
        echoGreen "\nLet's roll then...\n"
        sleep 2
        break
    elif [[ $REPLY == [nN] || $REPLY == "" ]]
    then
        penguinista
        exit
    else
        badRepYN
    fi
done
}

testRoot() {
local message="$scriptName requires ROOT privileges to do its job."
if [[ $UID -ne 0 ]]
then
    echoRed "\n$( penguinista ) .: $message\n"
    exit 1
fi
}

testConnect() {
local message="$NAME requires an active network interface."
if ! $(ip addr show | grep "state UP" &>/dev/null); then
    echoRed "$( penguinista ) .: $message"
    echo "INTERFACES FOUND"
    ip link
    exit 1
fi
}
