#!/bin/bash
save_path="`dirname \"$0\"`"

echo "Setup Wine Machine at ${WINEPREFIX}, WINEARCH=${WINEARCH} "
mkdir -p ${WINEPREFIX}
wine_drive_c_dir=${WINEPREFIX}/drive_c

Xvfb :99 -screen 0 1024x768x24 > /dev/null 2>&1 &
winecfg

echo "Disable GUI Crash Dialogs"
winetricks nocrashdialog

echo "Install common Packets"
# winetricks -q msxml3  # win32 ok
winetricks -q msxml6
winetricks -q dotnet462
winetricks -q allfonts
winetricks -q windowscodecs

cd ${save_path}
