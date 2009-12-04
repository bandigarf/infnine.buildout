#!/bin/bash
if [ -z "$1" ]
then
        echo "WARNING: Pass restore date as following: YYYY-MM-DD"
        exit
fi
hostn=`hostname`
if [ "$hostn" = "lapradig94" ]
then
/home/pangercic/programming/infnine.buildout/bin/repozo -Rv -r  /home/pangercic/programming/infnine.buildout/var/filestorage/backup/ -D $1 -o /home/pangercic/programming/infnine.buildout/var/filestorage/Copy.fs

elif [ "$hostn" = "lapradig39" ]
then
/home/pangercic/programming/infnine.buildout/bin/repozo -Rv -r  /home/pangercic/programming/infnine.buildout/var/filestorage/backup/ -D $1 -o /home/pangercic/programming/infnine.buildout/var/filestorage/Copy.fs

elif [ "$hostn" = "www9" ]
then	
/usr/local/share/infnine/infnine.buildout/bin/repozo -Rv -r /usr/local/share/infnine/infnine.buildout/var/filestorage/backup -D $1 -o /usr/local/share/infnine/infnine.buildout/var/filestorage/Copy.fs

elif [ "$hostn" = "ias" ]
then	
/usr/local/share/iasweb/infnine.buildout/bin/repozo -Rv -r /usr/local/share/iasweb/infnine.buildout/var/filestorage/backup -D $1 -o /usr/local/share/iasweb/infnine.buildout/var/filestorage/Copy.fs

else
    echo "I do not know YOU."
fi

