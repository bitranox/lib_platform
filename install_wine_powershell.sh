#!/bin/bash
save_path="`dirname \"$0\"`"

wine_drive_c_dir=${WINEPREFIX}/drive_c
powershell_install_dir=${wine_drive_c_dir}/opt/powershell
mkdir -p ${powershell_install_dir}

cd ${powershell_install_dir}

if [[ "${WINEARCH}" == "win32" ]]
    then
        echo "Download Powershell 32 Bit"
        # wget --no-check-certificate -O powershell.zip https://github.com/PowerShell/PowerShell/releases/download/v6.2.0/PowerShell-6.2.0-win-x86.zip
        wget --no-check-certificate -O powershell.msi https://github.com/PowerShell/PowerShell/releases/download/v6.2.0/PowerShell-6.2.0-win-x86.msi
    else
        echo "Download Powershell 64 Bit"
        # wget --no-check-certificate -O powershell.zip https://github.com/PowerShell/PowerShell/releases/download/v6.2.0/PowerShell-6.2.0-win-x64.zip
        wget --no-check-certificate -O powershell.msi https://github.com/PowerShell/PowerShell/releases/download/v6.2.0/PowerShell-6.2.0-win-x64.msi
    fi

# unzip -qq ./powershell.zip -d ${powershell_dir}
# wine ${powershell_dir}/pwsh -h

wine msiexec /i ${powershell_install_dir}/powershell.msi /quiet

cd ${save_path}
