#! /bin/sh

if test -z $BEA_API_KEY; then
    echo environment not available
    exit 1
fi
if test -f .env; then
    chmod 0600 .env
fi
env | grep -E BEA_API_KEY >.env
chmod 0400 .env

