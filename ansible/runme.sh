#!/bin/bash 
HOST="$1"
MOD="$2"
PORT=22

function hostup() { 
  local SRV="$1"
  if ( ! ssh -p $PORT -o 'BatchMode yes' -qq pi@$SRV "exit 0" ); then
    echo "No SSH access to host \"$SRV\"!"
    return 1
  fi
  return 0
}

# Check for arguments
if [ -z $HOST ] || [ -z $MOD ] ; then 
	echo "Usage: $0 <host> <module>"
	exit 0;
fi

if ( ! hostup "$HOST" ); then
	echo "Host $HOST appears to be non-reachable by ssh!"
	exit 1;
fi

if [ ! -f "$MOD/main.yaml" ]; then 
	echo "Playbook $MOD/main.yaml not found!"
	exit 1;
fi

echo "Running playbook $MOD/main.yaml on $HOST"
ansible-playbook -u pi -i "$HOST", "$MOD/main.yaml" -vv -c ssh -s

