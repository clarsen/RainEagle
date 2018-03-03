#!/bin/bash
PATH=/usr/local/bin:$PATH
export PATH

cd $HOME/git
lock=/tmp/raineagle.running
if [ -f $lock ]; then
    echo $0 still running
    exit 1
fi
touch $lock

pipenv run python RainEagle/bin/eagle_to_influx.deploy.py >> /tmp/eagle-to-influx-cron.out 2>&1
rm $lock
