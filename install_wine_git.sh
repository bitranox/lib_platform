#!/bin/bash
save_path="`dirname \"$0\"`"

echo "Install Git"
wine choco install git -params '"/GitAndUnixToolsOnPath"'

cd ${save_path}
