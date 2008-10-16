#!/bin/bash
#run the script from bibliography folder
username=`id -nu`
if [ "$username" = "pangercic" ]
then
/home/pangercic/programing/inf9_webpage/infnine.buildout/bin/repozo -B -f /home/pangercic/programing/inf9_webpage/infnine.buildout/var/filestorage/Data.fs -z -v -r /home/pangercic/programing/inf9_webpage/infnine.buildout/var/filestorage/backup/
elif [ "$username" = "infnine" ]
then	
/usr/proj/infnine/infnine.buildout/bin/repozo -B -f /usr/proj/infnine/infnine.buildout/var/filestorage/Data.fs -z -v -r /usr/proj/infnine/infnine.buildout/var/filestorage/backup/
else
    echo "I do not know YOU."
fi

