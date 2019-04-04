#!/bin/bash
save_path="`dirname \"$0\"`"

##########################################
echo "Setup Wine"
mkdir -p ${WINEPREFIX}
wine_drive_c_dir=${WINEPREFIX}/drive_c
winecfg

echo "Disable GUI Crash Dialogs"
winetricks nocrashdialog

echo "Download Python Binaries"
cd ~
wget --no-check-certificate -O pywine-master.zip https://github.com/bitranox/python_wine_binaries/archive/master.zip
# NOT WORKING :
# wget --no-check-certificate -O pywine32.zip https://github.com/bitranox/python_wine_binaries/blob/master/bin/python3.7.3_wine_32.zip # not working !


echo "Unzip Python 3.7.3 32 & 64 Bit to ${wine_drive_c_dir}"
unzip -qq ./pywine-master.zip -d ${HOME}
unzip -qq ./python_wine_binaries-master/bin/python3.7.3_wine_32.zip -d ${wine_drive_c_dir}
unzip -qq ./python_wine_binaries-master/bin/python3.7.3_wine_64.zip -d ${wine_drive_c_dir}

echo "Install Chocolatey"
wine "%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

echo "Install Git"
wine choco install git -params '"/GitAndUnixToolsOnPath"'

cd ${save_path}
