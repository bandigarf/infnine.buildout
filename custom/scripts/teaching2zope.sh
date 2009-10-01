#!/bin/bash
direct=`pwd | rev | awk -F \/ '{print $1}' | rev`
username=`id -nu`
#if [ "$direct" = "bibliography" ]
#then
if [ "$username" = "pangercic" ]
then
cd /home/pangercic/programing/inf9_webpage/infnine.buildout/ && ./bin/zope-secondary run src/infnine.data/infnine/data/teaching2zope.py
elif [ "$username" = "infnine" ]
then	
cd /usr/proj/infnine/infnine.buildout && ./bin/zope-secondary run src/infnine.data/infnine/data/teaching2zope.py
else
    echo "I do not know YOU."
fi

