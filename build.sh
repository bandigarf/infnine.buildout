#!/bin/bash
hostn=`hostname`
if [ "$hostn" = "lapradig94" ]
then
echo $hostn
./bin/buildout -vc debugUbuntu904.cfg

elif [ "$hostn" = "lapradig39" ]
then    
echo $hostn
./bin/buildout -vc debug.cfg

elif [ "$hostn" = "ias" ]
then    
echo $hostn
./bin/buildout -Novc debug.cfg

elif [ "$hostn" = "www9" ]
then    
echo $hostn
./bin/buildout -Novc debug.cfg

else
    echo "I do not know YOU."
fi

