#!/bin/bash

NAME="backend"
REPO_DIR=/home/ubuntu/britecore_test_project
DJANGO_DIR="$REPO_DIR/backend"
SOCKET_FILE=/home/ubuntu/run/gunicorn.sock
USER="ubuntu"
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=config.settings
DJANGO_WSGI_MODULE=config.wsgi

echo "Starting $NAME as `whoami`"

cd $DJANGO_DIR
source venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGO_DIR:$PYTHONPATH
export BRITECORE_ENV=PROD

RUN_DIR=$(dirname $SOCKET_FILE)
test -d $RUN_DIR || mkdir -p $RUN_DIR

gunicorn ${DJANGO_WSGI_MODULE}\
	--name $NAME\
	--workers $NUM_WORKERS\
	--user=$USER\
	--bind=unix:$SOCKET_FILE\
	--log-level=debug\
	--log-file=gunicorn.log

