APPNAME=django_rest_demo
APPDIR=/home/ubuntu/$APPNAME/

LOGFILE=$APPDIR'log/gunicorn.log'
ERRORFILE=$APPFIR'log/gunicorn-error.log'

NUM_WORKERS=3

ADDRESS=127.0.0.1:8000

cd $APPDIR

#source ~/.bashrc
. /home/ubuntu/$APPNAME/venv/bin/activate

exec gunicorn $APPNAME.wsgi:application \
-w $NUM_WORKERS --bind=$ADDRESS \
--log-level=debug \
--log-file=$LOGFILE 2>>$LOGFILE  1>>$ERRORFILE &
