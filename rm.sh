#! /bin/sh
#
DN=$(basename $PWD)

for dn in ${DN} alpine '<none>'; do
    docker images | grep ${dn}
    if [ $? -eq 0 ]; then
        docker image rm -f $(docker images | grep ${dn} | awk '{print $3}')
    fi
done

