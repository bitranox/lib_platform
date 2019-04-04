#!/bin/bash
save_path="`dirname \"$0\"`"

wine_drive_c_dir=${WINEPREFIX}/drive_c
install_dir=${wine_drive_c_dir}/install/powershell
mkdir -p ${install_dir}

cd ${install_dir}

if [[ "${WINEARCH}" == "win32" ]]
    then
        echo "Download Powershell 32 Bit"
        wget --no-check-certificate -O powershell.zip https://github.com/PowerShell/PowerShell/releases/download/v6.2.0/PowerShell-6.2.0-win-x86.zip
    else
        echo "Download Powershell 64 Bit"
        wget --no-check-certificate -O powershell.zip https://github.com/PowerShell/PowerShell/releases/download/v6.2.0/PowerShell-6.2.0-win-x64.zip
    fi

unzip -qq ./powershell.zip -d ${install_dir}
mv *.exe powershell-setup.exe

echo "contents of installdir ${install_dir}: "
ls ${install_dir} -l
cd ${save_path}

wine c:/install/powershell/powershell-setup.exe /quiet /passive /norestart
wine powershell -h
