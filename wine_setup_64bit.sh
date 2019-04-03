#!/bin/bash

# Setup Wine 64 Bit
mkdir -p ~/wine
DISPLAY=:0 WINEPREFIX=~/wine/wine64 winecfg
