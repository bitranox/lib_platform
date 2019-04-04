#!/bin/bash
echo "Install xvfb virtual framebuffer"
# sudo apt-get install -y x11-xkb-utils # can not be installed
sudo apt-get install -y x11-utils
sudo apt-get install -y xserver-common
sudo apt-get install -y xvfb

# either use xvfb-run to start programs, or :
# Xvfb :99 & export DISPLAY=:99 & <> command>

