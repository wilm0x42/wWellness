#!/bin/sh

excludes="--exclude=wwellness-cron --exclude=upgrade-log.txt"


if [ -z "$1" ]; then
	echo "Usage: deploy.sh user@remotehost"
	exit 0
fi

echo "Uploading files via rsync"
rsync $excludes --delete -a . $1:/opt/wWellness/
echo "Done!"

echo "Running install.sh on remote host"
ssh -t $1 -C "cd /opt/wWellness/; sudo ./install.sh"
echo "Done!"
