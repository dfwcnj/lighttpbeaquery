#! /bin/sh

DN=$(basename $PWD)
#docker run --env-file ./.env -p 1024:80 -u root -it ${DN} sh
docker run -p 1024:80 -u root -it ${DN} sh

#rm -f .env

