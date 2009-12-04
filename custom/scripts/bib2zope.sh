#!/bin/bash
hostn=`hostname`
if [ "$hostn" = "lapradig39" ]
then
/home/pangercic/programming/infnine.buildout/bin/zope-secondary run /home/pangercic/programming/infnine.buildout/src/infnine.data/infnine/data/bib2zope.py

elif [ "$hostn" = "lapradig94" ]
then
/home/pangercic/programming/infnine.buildout/bin/zope-secondary run /home/pangercic/programming/infnine.buildout/src/infnine.data/infnine/data/bib2zope.py

elif [ "$hostn" = "ias" ]
then	
/usr/local/share/iasweb/infnine.buildout/bin/zope-secondary run /usr/local/share/iasweb/infnine.buildout/src/infnine.data/infnine/data/bib2zope.py
/usr/local/share/iasweb/infnine.buildout/custom/scripts/bibsplitter.py

elif [ "$hostn" = "www9" ]
then	
/usr/local/share/infnine/infnine.buildout/bin/zope-secondary run /usr/local/share/infnine/infnine.buildout/src/infnine.data/infnine/data/bib2zope.py
/usr/local/share/infnine/infnine.buildout/custom/scripts/bibsplitter.py

else
    echo "I do not know YOU."
fi

