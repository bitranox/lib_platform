#!/bin/bash
save_path="`dirname \"$0\"`"

wine ${powershell_install_dir}/pwsh -ExecutionPolicy unrestricted get-executionpolicy

wine c:/windows/system32/powershell/pwsh.exe -NoProfile -InputFormat None -ExecutionPolicy unrestricted -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

cd ${save_path}
