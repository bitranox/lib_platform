#!/bin/bash

# Setup Wine 32 Bit
mkdir ~/wine
WINEARCH=win32 WINEPREFIX=~/wine/wine32 winecfg
