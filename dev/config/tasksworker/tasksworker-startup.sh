#!/bin/bash
/etc/init.d/cron start
gearmand -d
python /usr/local/bin/tasksworker.py
