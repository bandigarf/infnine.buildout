#!/bin/bash
hostn=`hostname`
echo "Did you set a semester identifier (src/infnine.data/infnine/data/teaching2zope.py)? ([y|n])"
read refresh_cache
if [ "$refresh_cache" = "y" ] 
then
    if [ "$hostn" = "lapradig39" ]
    then
        cd /home/pangercic/programming/infnine.buildout/ && ./bin/zope-secondary run src/infnine.data/infnine/data/teaching2zope.py

    elif [ "$hostn" = "lapradig94" ]
    then
        cd /home/pangercic/programming/infnine.buildout/ && ./bin/zope-secondary run src/infnine.data/infnine/data/teaching2zope.py
   
    elif [ "$hostn" = "ias" ]
    then	
        cd /usr/local/share/iasweb/infnine.buildout && ./bin/zope-secondary run src/infnine.data/infnine/data/teaching2zope.py

    elif [ "$hostn" = "www9" ]
    then	
        cd /usr/local/share/infnine/infnine.buildout && ./bin/zope-secondary run src/infnine.data/infnine/data/teaching2zope.py
    
else
        echo "I do not know YOU."
    fi
else
    echo "Exiting script!!!"
fi
