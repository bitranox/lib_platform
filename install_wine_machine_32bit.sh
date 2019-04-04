#!/bin/bash
save_path="`dirname \"$0\"`"

##########################################
echo "Setup Wine 32 Bit"
mkdir -p ~/wine
wine_dir="~/wine/wine32"
wine_dir = eval ${wine_dir}

export WINEARCH=win32
export WINEPREFIX=${wine_dir}
xvfb-run wine winecfg

##########################################
echo "Disable GUI Crash Dialogs"
xvfb-run winetricks nocrashdialog

##########################################
echo "Download Python 3.7.3 32 Bit"
cd ~
wget --no-check-certificate -O pywine32.zip https://github.com/bitranox/python_wine_binaries/archive/master.zip
# NOT WORKING :
# wget --no-check-certificate -O pywine32.zip https://github.com/bitranox/python_wine_binaries/blob/master/bin/python3.7.3_wine_32.zip # not working !

##########################################
wine_drive_c_dir=${wine_dir}/drive_c
echo "Unzip Python 3.7.3 32 Bit to ${wine_drive_c_dir}"
unzip ./pywine32.zip -d ${wine_drive_c_dir}
cd ${wine_drive_c_dir}
echo "this is now the content of ${wine_drive_c_dir}"
ls -l

cd ${save_path}
