#!/bin/bash
git pull --rebase
if [ $? -eq 0 ];then
    cp -f ./helper.py ~/.qqbot-tmp/plugins/
    qq unplug helper
    qq plug helper
fi
