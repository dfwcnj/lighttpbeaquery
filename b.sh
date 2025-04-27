#! /bin/sh

if ! test -f .env; then
    echo no .env file
    exit 1
fi
. ./.env
export BEA_API_KEY

./ec.sh

DN=$(basename $PWD)
docker build -f ./Dockerfile -t ${DN} .

rm -f .env

