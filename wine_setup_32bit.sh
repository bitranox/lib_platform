#!/bin/bash

save_path="`dirname \"$0\"`"

echo "Setup Wine 32 Bit"
mkdir -p ~/wine
DISPLAY=:0 WINEARCH=win32 WINEPREFIX=~/wine/wine32 winecfg


echo "Download Python 3.7.3 32 Bit"
cd ~
wget --no-check-certificate https://github.com/bitranox/python_wine_binaries/blob/master/bin/python3.7.3_wine_32.zip

echo "Unzip Python 3.7.3 32 Bit"
unzip ./python3.7.3_wine_32.zip -d ~/wine/wine32/drive_c

cd ~/wine/wine32/drive_c
ls -l

cd ${save_path}
