#!/bin/bash
echo "Build Start"
sudo dpkg --add-architecture i386
git clone git://source.winehq.org/git/wine.git
cd wine
sudo apt-get update
sudo apt-get install build-essential
./configure
./make
cd ..
