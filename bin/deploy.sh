#!/bin/bash 

BINDIR=$(dirname $0)

cd $BINDIR
cd ".."

git pull 

#delete *.pyc just in case
find . -name "*.pyc" -exec rm -rf {} \;

pip install --allow-external --allow-unverified -r requirements.txt

python manage.py migrate
#mkdir -p static static_local cache
python manage.py collectstatic
