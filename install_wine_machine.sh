#!/bin/bash
save_path="`dirname \"$0\"`"

if [[ -z ${wine_windows_version} ]]
    then
        echo "WARNING - no wine_windows_version in environment - set now to win10"
        echo "available Versions: win10, win2k, win2k3, win2k8, win31, win7, win8, win81, win95, win98, winxp"
        wine_windows_version="win10"
    fi

echo "Setup Wine Machine at ${WINEPREFIX}, WINEARCH=${WINEARCH}, wine_windows_version=${wine_windows_version}"
mkdir -p ${WINEPREFIX}
wine_drive_c_dir=${WINEPREFIX}/drive_c
# xvfb-run --auto-servernum winecfg # fails marshal_object couldnt get IPSFactory buffer for interface ...
winecfg

echo "Disable GUI Crash Dialogs"
winetricks nocrashdialog

echo "Set Windows Version to ${wine_windows_version}"
winetricks -q ${wine_windows_version}

sudo apt-get install -y libxml32

echo "Install common Packets"
# check if we run headless with xvfb service
xvfb_framebuffer_service_active="False"
systemctl is-active --quiet xvfb && xvfb_framebuffer_service_active="True"
# run winetricks with xvfb if needed
if [[ ${xvfb_framebuffer_service_active} == "True" ]]
	then
		xvfb-run winetricks -q windowscodecs
	else
		winetricks -q windowscodecs
	fi

cd ${save_path}
