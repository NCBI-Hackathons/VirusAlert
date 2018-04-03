#!/bin/bash

# comment out when done working on it:
SCRIPT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
DATA_DIR="$SCRIPT_DIR/../data"
TOOLS_DIR="$SCRIPT_DIR/../tools"

# fetch R package source
echo "downloading virfinder..."
pushd "$TOOLS_DIR"
wget https://codeload.github.com/jessieren/VirFinder/zip/master 
unzip Virfinder-master.zip
mv Virfiner-master/linux/VirFinder ./
rm -r Virfinder-master*
popd

# install R package + dependencies
echo "installing virfinder..."
sudo apt-get -y install r-base
Rscript "install.R"
