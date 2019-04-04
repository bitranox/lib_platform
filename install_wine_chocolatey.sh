#!/bin/bash
save_path="`dirname \"$0\"`"

wine "c:/opt/powershell/pwsh.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

cd ${save_path}
