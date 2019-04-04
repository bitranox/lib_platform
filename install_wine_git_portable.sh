#!/bin/bash
save_path="`dirname \"$0\"`"

wine_drive_c_dir=${WINEPREFIX}/drive_c

cd ${HOME}

wget -nc --no-check-certificate -O pywine-master.zip https://github.com/bitranox/python_wine_binaries/archive/master.zip

echo "Unzip Python 3.7.3 Master to ${HOME}"
unzip -nqq ./pywine-master.zip -d ${HOME}

if [[ "${WINEARCH}" == "win32" ]]
    then
        echo "Unzip Git Portable 32 Bit"
        unzip -qq ./python_wine_binaries-master/bin/PortableGit32_2.21.0.zip -d ${wine_drive_c_dir}
    else
        echo "Unzip Git Portable 64 Bit"
        unzip -qq ./python_wine_binaries-master/bin/PortableGit64_2.21.0.zip -d ${wine_drive_c_dir}
    fi

cd ${save_path}
