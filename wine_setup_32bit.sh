#!/bin/bash

# Setup Wine 32 Bit
mkdir -p ~/wine
DISPLAY=:0 WINEARCH=win32 WINEPREFIX=~/wine/wine32 winecfg
