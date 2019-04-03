#!/bin/bash

save_path="`dirname \"$0\"`"

echo "Setup Wine 32 Bit"
mkdir -p ~/wine
DISPLAY=:0 WINEARCH=win32 WINEPREFIX=~/wine/wine32 winecfg


echo "Download Python 3.7.3 32 Bit"
cd ~
wget --no-check-certificate -O pywine32.zip https://github.com/bitranox/python_wine_binaries/blob/master/bin/python3.7.3_wine_32.zip
# wget --no-check-certificate -O pywine32.zip https://github.com/bitranox/python_wine_binaries/archive/master.zip       # working !

windows_drive_c_path=~/wine/wine32/drive_c
echo "Unzip Python 3.7.3 32 Bit to $windows_drive_c_path"
unzip ./pywine32.zip -d $windows_drive_c_path

cd $(windows_drive_c_path)
echo "this is now the content of $windows_drive_c_path"
ls -l

cd ${save_path}
