#!/bin/bash 
BINDIR=$(dirname $0)
cd $BINDIR
echo $BINDIR


echo "USING TEST VARIABLES"
. ./local_variables.sh
echo "OVERRIDING WITH PRODUCTION VARIABLES"
. ./production_variables.sh

echo $DJ_AUTH_APP_PIDFILE


uwsgi --stop $DJ_AUTH_APP_PIDFILE