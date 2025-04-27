#! /bin/sh

DN=$(basename $PWD)
#docker run --env-file ./.env -it -p 1024:80 ${DN} sh
docker run -it -p 1024:80 ${DN} sh

#rm -f .env
