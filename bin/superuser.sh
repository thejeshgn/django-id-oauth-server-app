#!/bin/bash 

BINDIR=$(dirname $0)

cd $BINDIR
cd ".."

python manage.py createsuperuser