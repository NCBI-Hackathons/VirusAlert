#!/bin/bash

SCRIPT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
DATA_DIR="$SCRIPT_DIR/../data"
TOOLS_DIR="$SCRIPT_DIR/../tools"

# based on https://github.com/NCBI-Hackathons/VirusFriends
echo "installing magicblast..."
mkdir -p "$TOOLS_DIR"
cd "$TOOLS_DIR"
wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/magicblast/LATEST/ncbi-magicblast-1.3.0-x64-linux.tar.gz -O magicblast.tar.gz
tar -xvf magicblast.tar.gz
rm -f magicblast.tar.gz
P=$(find . -name magicblast | sed -e 's/magicblast$//; s/^\.\///')
echo "magicblast installed in $NEWPATH:$PWD/$P"
