#! /bin/sh


DN=$(basename $PWD)
#docker run --env-file ./.env -p 1024:80 -t ${DN} sh &
docker run -p 1024:80 -t ${DN} &

#rm -f .env

