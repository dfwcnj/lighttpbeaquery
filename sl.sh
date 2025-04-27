#! /bin/sh
#
# set -x

if ! test -f .env; then
    echo no .env file
    exit 1
fi
. /.env
export BEA_API_KEY

# docker run -t
sudo chmod a+w /dev/pts/0

. pyenv/bin/activate

#/usr/sbin/lighttpd -t -f /etc/lighttpd/lighttpd.conf
/usr/sbin/lighttpd -D -f /etc/lighttpd/lighttpd.conf

# rm -f .env
