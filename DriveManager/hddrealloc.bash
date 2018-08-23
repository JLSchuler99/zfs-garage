#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

my_drives="$(python driveNameManager.py dump | awk '{ print $1 }')"

print_hdd_realloc(){
    printf "Hard disc reallocated sectors:\n"
    for drive in $my_drives; do
	if [ -L /dev/disk/by-id/$(python driveNameManager.py get ${drive}) ];
	then
            realloc=$(${sudo} smartctl -a /dev/disk/by-id/$(python driveNameManager.py get ${drive}) | grep Reallocated_S | awk '{ print $10 }')
    
	    printf "${drive} ${realloc}\n"
    	else
	    printf "No such device ${drive}\n"
    	fi
    done
    echo
    echo
}
print_hdd_realloc
