#!/bin/bash 

BINDIR=$(dirname $0)

cd $BINDIR
cd ".."

#git pull 

#delete *.pyc just in case
#find . -name "*.pyc" -exec rm -rf {} \;

pip install -r requirements.txt

# Install app 
#python manage.py makemigrations
python manage.py migrate
#mkdir -p static static_local cache
#python manage.py collectstatic --noinput -c
