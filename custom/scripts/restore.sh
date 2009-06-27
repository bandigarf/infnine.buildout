#!/bin/bash
if [ -z "$1" ]
then
        echo "WARNING: Pass restore date as following: YYYY-MM-DD"
        exit
fi
username=`id -nu`
if [ "$username" = "pangercic" ]
then
/home/pangercic/programing/inf9_webpage/infnine.buildout/bin/repozo -Rv -r  /home/pangercic/programing/inf9_webpage/infnine.buildout/var/filestorage/backup/ -D $1 -o /home/pangercic/programing/inf9_webpage/infnine.buildout/var/filestorage/Copy.fs
elif [ "$username" = "infnine" ]
then	
/usr/proj/infnine/infnine.buildout/bin/repozo -Rv -r /usr/proj/infnine/infnine.buildout/var/filestorage/backup -D $1 -o /usr/proj/infnine/infnine.buildout/var/filestorage/Copy.fs
else
    echo "I do not know YOU."
fi

