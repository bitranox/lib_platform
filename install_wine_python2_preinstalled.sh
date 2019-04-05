#!/bin/bash
save_path="`dirname \"$0\"`"

# if used outside github/travis You need to set :
# WINEARCH=win32    for 32 Bit Wine
# WINEARCH=""       for 64 Bit Wine
# WINEPREFIX={HOME}/.wine   or the wine prefix You are using

wine_drive_c_dir=${WINEPREFIX}/drive_c
decompress_dir=${HOME}/decompress
mkdir -p ${decompress_dir}

python_version_short=python27
python_version_full=python2.7.16
python_version_doc="Python 2.7.16"

echo "Download ${python_version_doc} Binaries"
https://github.com/bitranox/binaries_${python_version_short}_wine/archive/master.zip
wget -nc --no-check-certificate -O ${decompress_dir}/binaries_${python_version_short}_wine-master.zip https://github.com/bitranox/binaries_${python_version_short}_wine/archive/master.zip

echo "Unzip ${python_version_doc} Master to ${HOME}"
unzip -nqq ${decompress_dir}/binaries_${python_version_short}_wine-master.zip -d ${decompress_dir}

if [[ "${WINEARCH}" == "win32" ]]
    then
        echo "Joining Multipart Zip in ${decompress_dir}/binaries_${python_version_short}_wine-master/bin"
        cat ${decompress_dir}/binaries_${python_version_short}_wine-master/bin/${python_version_full}_wine_32* > ${decompress_dir}/binaries_${python_version_short}_wine-master/bin/joined_${python_version_short}.zip
    else
        echo "Joining Multipart Zip in ${decompress_dir}/binaries_${python_version_short}_wine-master/bin"
        cat ${decompress_dir}/binaries_${python_version_short}_wine-master/bin/${python_version_full}_wine_64* > ${decompress_dir}/binaries_${python_version_short}_wine-master/bin/joined_${python_version_short}.zip
    fi

echo "Unzip ${python_version_doc} to ${wine_drive_c_dir}"
unzip -qq ${decompress_dir}/binaries_${python_version_short}_wine-master/bin/joined_${python_version_short}.zip -d ${wine_drive_c_dir}

rm -r ${decompress_dir}

cd ${save_path}
