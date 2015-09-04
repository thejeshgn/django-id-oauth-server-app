#!/bin/bash 
#IMPORT VARIABLES
. ./variables.sh


uwsgi --stop $DJ_AUTH_APP_PIDFILE