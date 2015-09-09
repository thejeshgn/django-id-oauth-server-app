#!/bin/bash 
echo "USING LOCAL - TEST VARIABLES"
export DJ_AUTH_APP_BINDIR=$(dirname $0)
export DJ_AUTH_APP_PROTOCOL="--http" 
export DJ_AUTH_APP_PORT="8080"
export DJ_AUTH_APP_IP="127.0.0.1"
export DJ_AUTH_APP_LOGFILE="/media/thej/data2/django-id-oauth-server-app/django_id_oauth-server.log"
export DJ_AUTH_APP_PIDFILE="/media/thej/data2/django-id-oauth-server-app/django_id_oauth-server.pid"
export DJ_AUTH_APP_NO_PROCESS="5"