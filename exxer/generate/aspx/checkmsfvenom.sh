#!/bin/bash
[ $(command -v msfvenom) ] || { echo "please install the package: 'msfvenom'" ; exit 1 ; }