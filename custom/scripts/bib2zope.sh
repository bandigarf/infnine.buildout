#!/bin/bash
direct=`pwd | rev | awk -F \/ '{print $1}' | rev`
username=`id -nu`
if [ "$direct" = "bibliography" ]
then
if [ "$username" = "pangercic" ]
then
/home/pangercic/programing/inf9_webpage/infnine.buildout/bin/zope-secondary run /home/pangercic/programing/inf9_webpage/infnine.buildout/src/infnine.data/infnine/data/bib2zope.py
elif [ "$username" = "infnine" ]
then	
/usr/proj/infnine/infnine.buildout/bin/zope-secondary run /usr/proj/infnine/infnine.buildout/src/infnine.data/infnine/data/bib2zope.py
else
    echo "I do not know YOU."
fi
else
echo "run script from bibliography directory"
fi

