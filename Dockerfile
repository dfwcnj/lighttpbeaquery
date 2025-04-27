# https://github.com/m4rcu5nl/docker-lighttpd-alpine
# https://github.com/spujadas/lighttpd-docker
# https://github.com/johnelse/docker-lighttpd
# https://github.com/rtsp/docker-lighttpd
# Dockerfile for lighttpd

FROM alpine:latest

RUN apk update && \
	apk add lighttpd && \
	apk add lighttpd-mod_auth && \
	apk add python3 && \
	apk add python3-doc && \
	apk add py3-pip && \
        apk add iproute2 && \
        apk add iptables && \
        apk add daemontools-encore && \
	apk add sudo

# install adds user and group lighttpd

RUN mkdir -p /etc/lighttpd
RUN mkdir -p /usr/local/bin
RUN mkdir -p  /var/www/localhost/htdocs
RUN mkdir -p  /var/www/localhost/cgi-bin
RUN mkdir -p  /var/www/localhost/wlib
RUN mkdir -p  /etc/sudoers.d
# RUN mkdir /run

COPY etc/* /etc/lighttpd/
COPY wlib/* /var/www/localhost/wlib
RUN chmod 0664 /etc/lighttpd/*
RUN chgrp lighttpd etc/lighttpd/*
RUN chgrp lighttpd /var/www/localhost/htdocs /var/www/localhost/wlib
RUN chmod 0775 /var/www/localhost/htdocs /var/www/localhost/wlib

COPY *.py /var/www/localhost/cgi-bin/
COPY *.html /var/www/localhost/htdocs/

COPY .env /.env
RUN chown lighttpd .env
COPY sl.sh /sl.sh
COPY v.sh /v.sh
RUN /v.sh
RUN find /pyenv -name \*.pyc -delete
RUN echo 'lighttpd ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/lighttpd
# RUN passwd -d lighttpd
RUN chgrp lighttpd /run && chmod 0774 /run

EXPOSE 80

USER lighttpd

# CMD ["/usr/sbin/lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]
CMD ["/sl.sh"]
