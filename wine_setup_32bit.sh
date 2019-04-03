#!/bin/bash

save_path="`dirname \"$0\"`"

echo "Setup Wine 32 Bit"
mkdir -p ~/wine
DISPLAY=:0 WINEARCH=win32 WINEPREFIX=~/wine/wine32 winecfg

cd ${save_path}

