#!/bin/bash
save_path="`dirname \"$0\"`"

wine_drive_c_dir=${WINEPREFIX}/drive_c
decompress_dir=${HOME}/decompress
mkdir -p ${decompress_dir}

echo "Download Python Binaries"
https://github.com/bitranox/binaries_python_wine/archive/master.zip
wget -nc --no-check-certificate -O ${decompress_dir}/binaries_python_wine-master.zip https://github.com/bitranox/binaries_python_wine/archive/master.zip

echo "Unzip Python 3.7.3 Master to ${HOME}"
unzip -nqq ${decompress_dir}/binaries_python_wine-master.zip -d ${decompress_dir}

if [[ "${WINEARCH}" == "win32" ]]
    then
        echo "Unzip Python 3.7.3 32 Bit to ${wine_drive_c_dir}"
        unzip -qq ${decompress_dir}/binaries_python_wine-master/bin/python3.7.3_wine_32.zip -d ${wine_drive_c_dir}
    else
        echo "Unzip Python 3.7.3 64 Bit to ${wine_drive_c_dir}"
        unzip -qq ${decompress_dir}/binaries_python_wine-master/bin/python3.7.3_wine_64.zip -d ${wine_drive_c_dir}
    fi

cd ${save_path}
