#!/bin/bash
git pull --rebase
if [ $? -eq 0 ];then
    cp -f ./*.py ~/.qqbot-tmp/plugins/
    qq unplug androidbot
    qq plug androidbot
fi
