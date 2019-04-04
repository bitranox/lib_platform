#!/bin/bash
save_path="`dirname \"$0\"`"

echo "Setup Wine Machine at ${WINEPREFIX}, WINEARCH=${WINEARCH} "
mkdir -p ${WINEPREFIX}
wine_drive_c_dir=${WINEPREFIX}/drive_c
winecfg

echo "Disable GUI Crash Dialogs"
winetricks nocrashdialog

echo "Install common Packets"
winetricks -q dotnet20
winetricks -q msxml3 dotnet35sp1
winetricks lucida
winetricks windowscodecs

cd ${save_path}
