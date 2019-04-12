#!/bin/bash
save_path="`dirname \"$0\"`"

## set wine prefix to ${HOME}/.wine if not given by environment variable
if [[ -z ${WINEPREFIX} ]]
    then
        echo "WARNING - no WINEPREFIX in environment - set now to ${HOME}/.wine"
        WINEPREFIX=${HOME}/.wine
    fi

wine_drive_c_dir=${WINEPREFIX}/drive_c
decompress_dir=${HOME}/bitranox_decompress
mkdir -p ${decompress_dir}

echo "Download Git Portable Binaries"
wget -nc --no-check-certificate -O ${decompress_dir}/binaries_portable_git-master.zip https://github.com/bitranox/binaries_portable_git/archive/master.zip

echo "Unzip Git Portable Binaries Master to ${decompress_dir}"
unzip -nqq ${decompress_dir}/binaries_portable_git-master.zip -d ${decompress_dir}

if [[ "${WINEARCH}" == "win32" ]]
    then
        echo "Joining Multipart Zip in ${decompress_dir}/binaries_portable_git-master/bin"
        cat ${decompress_dir}/binaries_portable_git-master/bin/PortableGit32* > ${decompress_dir}/binaries_portable_git-master/bin/joined_PortableGit.zip
        add_git_path="c:/PortableGit32/cmd"
    else
        echo "Joining Multipart Zip in ${decompress_dir}/binaries_portable_git-master/bin"
        cat ${decompress_dir}/binaries_portable_git-master/bin/PortableGit64* > ${decompress_dir}/binaries_portable_git-master/bin/joined_PortableGit.zip
        add_git_path="c:/PortableGit64/cmd"
    fi

echo "Unzip Git Portable Binaries to ${wine_drive_c_dir}"
unzip -qq ${decompress_dir}/binaries_portable_git-master/bin/joined_PortableGit.zip -d ${wine_drive_c_dir}

echo "add Path Settings to Registry"
wine_current_reg_path="`wine reg QUERY \"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment\" /v PATH | grep REG_SZ | sed 's/^.*REG_SZ\s*//'`"
wine_new_reg_path="${add_git_path};${wine_current_reg_path}"
wine reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /t REG_SZ /v PATH /d "${wine_new_reg_path}" /f
wine_actual_reg_path="`wine reg QUERY \"HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment\" /v PATH | grep REG_SZ | sed 's/^.*REG_SZ\s*//'`"
echo "Wine PATH=${wine_actual_reg_path}"

rm -r ${decompress_dir}

cd ${save_path}
