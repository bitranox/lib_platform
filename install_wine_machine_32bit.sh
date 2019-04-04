#!/bin/bash
save_path="`dirname \"$0\"`"

##########################################
echo "Setup Wine 32 Bit"
mkdir -p ${HOME}/wine
wine_dir="${HOME}/wine/wine32"   ## expand the home dir with ${HOME} - wine does not like "~"
wine_drive_c_dir=${wine_dir}/drive_c

# export WINEARCH=win32
# export WINEPREFIX=${wine_dir}
# export DISPLAY=:99.0

# /etc/init.d/xvfb start  ## does not work
# sleep 3
# sudo service xvfb start ## does not work


# WINEARCH=win32 WINEPREFIX=${wine_dir} winecfg
winecfg

echo "Disable GUI Crash Dialogs"
winetricks nocrashdialog

echo "Download Python Binaries"
cd ~
wget --no-check-certificate -O pywine-master.zip https://github.com/bitranox/python_wine_binaries/archive/master.zip
# NOT WORKING :
# wget --no-check-certificate -O pywine32.zip https://github.com/bitranox/python_wine_binaries/blob/master/bin/python3.7.3_wine_32.zip # not working !


echo "Unzip Python 3.7.3 32 Bit to ${wine_drive_c_dir}"
unzip ./pywine-master.zip -d ${HOME}
unzip ./python_wine_binaries-master/bin/python3.7.3_wine_32.zip -d ${wine_drive_c_dir}
wine c:/Python37-32/python -m pip install --upgrade pip

cd ${save_path}
