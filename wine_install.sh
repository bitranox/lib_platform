#!/bin/bash
echo "Build Start"
sudo dpkg --add-architecture i386
REM git clone git://source.winehq.org/git/wine.git
REM cd wine
REM sudo apt-get update
REM sudo apt-get install build-essential
REM ./configure
REM ./make
REM cd ..

wget -nc https://dl.winehq.org/wine-builds/winehq.key
sudo apt-key add winehq.key
sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ xenial main'
sudo apt-get update
sudo apt-get install --install-recommends winehq-devel
