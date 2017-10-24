#!/bin/bash

unlink /opt/logs/supervisord/supervisor.sock
supervisord -c /opt/work/zoro/src/supervisord/supervisord.conf

