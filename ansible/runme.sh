#!/bin/bash 
HOST="$1"
RECIPE="$2"
PORT=22

function hostup() { 
  local SRV="$1"
  if ( ! ssh -p $PORT -o 'BatchMode yes' -qq pi@$SRV "exit 0" ); then
    echo "No SSH access to host \"$SRV\"!"
    return 1
  fi
  return 0
}

# check for script_path
if [ "$0" != "./runme.sh" ] ; then 
	echo "Please run this script as \"./$( basename $0 $@)\"."
	exit 1
fi

# Check for arguments
if [ -z $HOST ] || [ -z $RECIPE ] ; then 
	echo "Usage: $0 <host> <recipe_file>"
	exit 0;
fi

if ( ! hostup "$HOST" ); then
	echo "Host $HOST appears to be non-reachable by ssh!"
	exit 1;
fi

if [ ! -f "$RECIPE" ]; then 
	echo "Playbook $RECIPE directory not found!"
	exit 1;
fi

echo "Running playbook $RECIPE on $HOST"
ansible-playbook -u pi -i "$HOST", "$RECIPE" -vv -c ssh -s
