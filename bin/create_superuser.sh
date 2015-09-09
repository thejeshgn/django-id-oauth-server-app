#!/bin/bash 

BINDIR=$(dirname $0)

echo $BINDIR
cd $BINDIR
cd ".."

python manage.py createsuperuser