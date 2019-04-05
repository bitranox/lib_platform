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
        echo "Joining Multipart Zip in ${decompress_dir}/binaries_portable_git-master/bin"
        cat ${decompress_dir}/binaries_python_wine-master/bin/python3.7.3_wine_32* > ${decompress_dir}/binaries_portable_git-master/bin/joined_python37.zip
    else
        echo "Joining Multipart Zip in ${decompress_dir}/binaries_portable_git-master/bin"
        cat ${decompress_dir}/binaries_python_wine-master/bin/python3.7.3_wine_64* > ${decompress_dir}/binaries_portable_git-master/bin/joined_python37.zip
    fi

echo "Unzip Python 3.7.3 to ${wine_drive_c_dir}"
unzip -qq ${decompress_dir}/binaries_python_wine-master/bin/joined_python37.zip -d ${wine_drive_c_dir}

cd ${save_path}
