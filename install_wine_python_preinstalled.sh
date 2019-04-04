#!/bin/bash
save_path="`dirname \"$0\"`"

wine_drive_c_dir=${WINEPREFIX}/drive_c

echo "Download Python Binaries"
cd ${HOME}
wget -nc --no-check-certificate -O pywine-master.zip https://github.com/bitranox/python_wine_binaries/archive/master.zip
# NOT WORKING :
# wget --no-check-certificate -O pywine32.zip https://github.com/bitranox/python_wine_binaries/blob/master/bin/python3.7.3_wine_32.zip # not working !

echo "Unzip Python 3.7.3 Master to ${HOME}"
unzip -qq ./pywine-master.zip -d ${HOME}

if [[ "${WINEARCH}" == "win32" ]]
    then
        echo "Unzip Python 3.7.3 32 Bit to ${wine_drive_c_dir}"
        unzip -qq ${HOME}/python_wine_binaries-master/bin/python3.7.3_wine_32.zip -d ${wine_drive_c_dir}
    else
        echo "Unzip Python 3.7.3 32 Bit to ${wine_drive_c_dir}"
        unzip -qq ${HOME}/python_wine_binaries-master/bin/python3.7.3_wine_64.zip -d ${wine_drive_c_dir}
    fi

cd ${save_path}
