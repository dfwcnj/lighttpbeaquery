#! /bin/sh

if ! test -f .env; then
    echo no .env file
    exit 1
fi
. ./.env
export BEA_API_KEY

if ! grep BEA_API_KEY etc/lighttpd.conf | grep -v grep; then
    echo 'setenv.add-environment = (\n    "BEA_API_KEY" => "'$BEA_API_KEY'"\n)' >> etc/lighttpd.conf
fi

