#!/bin/bash
username=`id -nu`
if [ "$username" = "pangercic" ]
then
./bin/buildout -vc debugUbuntu904.cfg
elif [ "$username" = "infnine" ]
then    
./bin/buildout -vc debug.cfg
else
    echo "I do not know YOU."
fi

