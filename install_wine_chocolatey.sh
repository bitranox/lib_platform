#!/bin/bash
save_path="`dirname \"$0\"`"

wine_drive_c_dir=${WINEPREFIX}/drive_c
powershell_install_dir=${wine_drive_c_dir}/windows/system32/powershell

wine ${powershell_install_dir}/pwsh -ExecutionPolicy unrestricted get-executionpolicy

wine ${powershell_install_dir}/pwsh.exe -NoProfile -InputFormat None -ExecutionPolicy unrestricted -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

cd ${save_path}
