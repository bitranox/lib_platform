#!/bin/bash
save_path="`dirname \"$0\"`"

wine_drive_c_dir=${WINEPREFIX}/drive_c

echo "Download Git Portable Binaries"
cd ${HOME}
wget -nc --no-check-certificate -O binaries_portable_git-master.zip https://github.com/bitranox/binaries_portable_git/archive/master.zip

echo "Unzip Git Portable Binaries Master to ${HOME}"
unzip -nqq ./binaries_portable_git-master.zip -d ${HOME}

if [[ "${WINEARCH}" == "win32" ]]
    then
        echo "Unzip Git Portable Binaries 32 Bit to ${wine_drive_c_dir}"
        unzip -qq ./binaries_portable_git-master/bin/PortableGit32_v2.21.0.zip -d ${wine_drive_c_dir}
    else
        echo "Unzip Git Portable Binaries 64 Bit to ${wine_drive_c_dir}"
        unzip -qq ./binaries_python_wine-master/bin/PortableGit64_v2.21.0.zip -d ${wine_drive_c_dir}
    fi

cd ${save_path}
