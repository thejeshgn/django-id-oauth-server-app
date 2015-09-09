#!/bin/bash 

export DJ_AUTH_APP_BINDIR=$(dirname $0)

cd ".."

export DJ_AUTH_APP_PROTOCOL="--http"
export DJ_AUTH_APP_PORT="8080"
export DJ_AUTH_APP_IP="127.0.0.1"
export DJ_AUTH_APP_LOGFILE="/home/tgn/django_id_oauth-server/django_id_oauth-server.log"
export DJ_AUTH_APP_PIDFILE="/home/tgn/django_id_oauth-server/django_id_oauth-server.pid"
export DJ_AUTH_APP_NO_PROCESS="5"