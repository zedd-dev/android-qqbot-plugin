#!/bin/bash
ssh $USER@$SERVER sh -c "
    qq unplug androidbot
    qq plug androidbot
"