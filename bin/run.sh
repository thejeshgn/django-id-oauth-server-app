#!/bin/bash 

BINDIR=$(dirname $0)

if [ -z $1 ]; then
    BIND="0.0.0.0:8000"
else
    BIND=$1
fi
echo $BINDIR

cd $BINDIR
cd ".."

python manage.py runserver $BIND