#!/bin/bash

cd /opt/Wellness/

cp ./wwellness-cron /etc/cron.d/

#rm -rf __pycache__/

date >> upgrade-log.txt
git rev-parse HEAD >> upgrade-log.txt
