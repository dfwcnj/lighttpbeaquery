#! /bin/sh

DN=$(basename $PWD)
CID=$(docker ps | grep ${DN} | awk '{print $1}')
if ! test -z ${CID}; then
    docker stop ${CID}
fi
CID=$(docker ps | grep sl.sh | awk '{print $1}')
if ! test -z ${CID}; then
    docker stop ${CID}
fi

