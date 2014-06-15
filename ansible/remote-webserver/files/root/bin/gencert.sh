#!/bin/bash
set -e

NAME=$1
if [ -z $NAME ] ; then echo "Usage: $0 <CERT>"; exit 0; fi
if [ -f "$NAME" ] ; then echo "Key $NAME allready present! Please remove first!"; exit 0; fi

openssl req -new -x509 -keyout "$NAME" -out "$NAME" -days 99999 -nodes -subj /C="NL"/ST="Noord-Holland"/L="Amsterdam"/O="FlipHess"/OU="fliphess.com"/CN="$( hostname -f )"
chmod 400 $NAME
