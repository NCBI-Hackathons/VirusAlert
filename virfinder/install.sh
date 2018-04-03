#!/bin/bash

# comment out when done working on it:
export SCRIPT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
export DATA_DIR="$SCRIPT_DIR/../data"
export TOOLS_DIR="$SCRIPT_DIR/../tools"

# fetch R package source
echo "downloading virfinder..."
pushd "$TOOLS_DIR"
if [[ ! -d VirFinder ]]; then
  wget https://codeload.github.com/jessieren/VirFinder/zip/master
  unzip master
  mv VirFinder-master/linux/VirFinder ./
  rm -r *master*
fi
popd

# install R package + dependencies
echo "installing virfinder..."
sudo apt-get -y install r-base
mkdir -p "${TOOLS_DIR}/R"
Rscript "${SCRIPT_DIR}/install.R"

# install analysis repdencies
sudo apt-get install -y python3-biopython sra-toolkit
