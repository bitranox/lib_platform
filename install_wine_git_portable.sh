#!/bin/bash
save_path="`dirname \"$0\"`"

wine_drive_c_dir=${WINEPREFIX}/drive_c
decompress_dir=${HOME}/decompress

echo "Download Git Portable Binaries"
wget -nc --no-check-certificate -O ${decompress_dir}/binaries_portable_git-master.zip https://github.com/bitranox/binaries_portable_git/archive/master.zip

echo "Unzip Git Portable Binaries Master to ${HOME}"
unzip -nqq ${decompress_dir}/binaries_portable_git-master.zip -d ${decompress_dir}

if [[ "${WINEARCH}" == "win32" ]]
    then
        echo "Unzip Git Portable Binaries 32 Bit to ${decompress_dir}"
        unzip -qq ${decompress_dir}/binaries_portable_git-master/bin/PortableGit32*.zip -d ${wine_drive_c_dir}
    else
        echo "Unzip Git Portable Binaries 64 Bit to ${decompress_dir}"
        unzip -qq ${decompress_dir}/binaries_portable_git-master/bin/PortableGit64*.zip -d ${wine_drive_c_dir}
    fi

cd ${save_path}
