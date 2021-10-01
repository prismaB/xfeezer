#!/bin/bash

[ $UID = 0 ] || { echo "please run it as root privalages this script." ; exit 1 ; }

echo "installing the python packages"
pip3 install -r requiremets.txt

sleep 2

echo "starting the checkfiles.py"

sleep 2

python3 checkpyversion.py