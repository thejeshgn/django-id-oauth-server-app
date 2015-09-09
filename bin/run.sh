#!/bin/bash 

BINDIR=$(dirname $0)
cd $BINDIR
echo $BINDIR

echo "USING TEST VARIABLES"
. ./local_variables.sh
echo "OVERRIDING WITH PRODUCTION VARIABLES"
. ./production_variables.sh

echo $DJ_AUTH_APP_PIDFILE

touch $DJ_AUTH_APP_PIDFILE
#TODO for end user
#1. Do not run uWSGI instances as root. You can start your uWSGIs as root, 
#   but be sure to drop privileges with the uid and gid options.



cd ".."
uwsgi --module=app.wsgi:application --env DJANGO_SETTINGS_MODULE=app.settings --master --pidfile=$DJ_AUTH_APP_PIDFILE $DJ_AUTH_APP_PROTOCOL=$DJ_AUTH_APP_IP:$DJ_AUTH_APP_PORT --processes=$DJ_AUTH_APP_NO_PROCESS --harakiri=20 --max-requests=5000 --vacuum --buffer-size=30000 --daemonize=$DJ_AUTH_APP_LOGFILE     