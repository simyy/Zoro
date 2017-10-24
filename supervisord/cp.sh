#!/bin/bash


if [ -f "/etc/supervisord.conf" ]; then
    rm /etc/supervisord.conf
fi
cp /opt/work/zoro/src/supervisord/supervisord.conf /etc/supervisord.conf
