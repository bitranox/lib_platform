#!/bin/bash

# Setup Wine 64 Bit
echo $PIP_PREFIX
mkdir -p ~/wine
DISPLAY=:0 WINEPREFIX=~/wine/wine64 winecfg
