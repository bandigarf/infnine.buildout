#!/bin/bash
direct=`pwd | rev | awk -F \/ '{print $1}' | rev`
username=`id -nu`
#if [ "$direct" = "bibliography" ]
#then
echo "Did you set a semester identifier (src/infnine.data/infnine/data/teaching2zope.py)? ([y|n])"
read refresh_cache
if [ "$refresh_cache" = "y" ] 
then
    if [ "$username" = "pangercic" ]
    then
        cd /home/pangercic/programming/infnine.buildout/ && ./bin/zope-secondary run src/infnine.data/infnine/data/teaching2zope.py
    elif [ "$username" = "infnine" ]
    then	
        cd /usr/proj/infnine/infnine.buildout && ./bin/zope-secondary run src/infnine.data/infnine/data/teaching2zope.py
    else
        echo "I do not know YOU."
    fi
else
    echo "Exiting script!!!"
fi
