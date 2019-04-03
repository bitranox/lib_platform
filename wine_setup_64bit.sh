#!/bin/bash

save_path="`dirname \"$0\"`"

echo "Setup Wine 64 Bit"
mkdir -p ~/wine
DISPLAY=:0 WINEPREFIX=~/wine/wine64 winecfg

cd ${save_path}
