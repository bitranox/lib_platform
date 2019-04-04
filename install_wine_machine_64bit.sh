#!/bin/bash
save_path="`dirname \"$0\"`"

##########################################
echo "Setup Wine 64 Bit"
mkdir -p ${HOME}/wine
wine_dir="${HOME}/wine/wine64"   ## expand the home dir with ${HOME} - wine does not like "~"
wine_drive_c_dir=${wine_dir}/drive_c

export WINEPREFIX=${wine_dir}
export DISPLAY=:99.0

sudo service xvfb start

WINEPREFIX=${wine_dir} winecfg

echo "Disable GUI Crash Dialogs"
xvfb-run winetricks nocrashdialog

echo "Download Python Binaries"
cd ~
wget --no-check-certificate -O pywine-master.zip https://github.com/bitranox/python_wine_binaries/archive/master.zip
# NOT WORKING :
# wget --no-check-certificate -O pywine32.zip https://github.com/bitranox/python_wine_binaries/blob/master/bin/python3.7.3_wine_32.zip # not working !


echo "Unzip Python 3.7.3 64 Bit to ${wine_drive_c_dir}"
unzip ./pywine-master.zip -d ${HOME}
unzip ./python_wine_binaries-master/bin/python3.7.3_wine_64.zip -d ${wine_drive_c_dir}

cd ${save_path}
