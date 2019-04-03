#!/bin/bash

# Setup Wine 32 Bit
mkdir -p ~/wine
WINEARCH=win32 WINEPREFIX=~/wine/wine32 winecfg
