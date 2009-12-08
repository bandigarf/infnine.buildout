#!/bin/bash
#run the script from bibliography folder
hostn=`hostname`
if [ "$hostn" = "lapradig94" ]
then
/home/pangercic/programming/infnine.buildout/bin/repozo -B -f /home/pangercic/programming/infnine.buildout/var/filestorage/Data.fs -z -v -r /home/pangercic/programming/infnine.buildout/var/filestorage/backup/

elif [ "$hostn" = "lapradig39" ]
then
/home/pangercic/programming/infnine.buildout/bin/repozo -B -f /home/pangercic/programming/infnine.buildout/var/filestorage/Data.fs -z -v -r /home/pangercic/programming/infnine.buildout/var/filestorage/backup/

elif [ "$hostn" = "www9" ]
then	
/usr/local/share/infnine/infnine.buildout/bin/repozo -B -f /usr/local/share/infnine/infnine.buildout/var/filestorage/Data.fs -z -v -r /usr/local/share/infnine/infnine.buildout/var/filestorage/backup/

elif [ "$hostn" = "ias" ]
then	
/usr/local/share/iasweb/infnine.buildout/bin/repozo -B -f /usr/local/share/iasweb/infnine.buildout/var/filestorage/Data.fs -z -v -r /usr/local/share/iasweb/infnine.buildout/var/filestorage/backup/

else
    echo "I do not know YOU."
fi

