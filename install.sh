#!/bin/bash

SCRIPT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
DATA_DIR="$SCRIPT_DIR/../data"
TOOLS_DIR="$SCRIPT_DIR/../tools"
export PATH=$TOOLS_DIR:$PATH

echo "installing debian dependencies..."
sudo apt-get install python3-biopython sra-toolkit r-base

echo "installing R dependencies..."
R -e """
# see https://www.r-bloggers.com/permanently-setting-the-cran-repository/
local({
  r <- getOption("repos")
  r["CRAN"] <- "http://cran.cnr.berkeley.edu/"
  options(repos = r)
})

toolsdir=Sys.getenv('TOOLS_DIR')
libdir=file.path(toolsdir, 'R')
srcdir=file.path(toolsdir, 'VirFinder')

install.packages("glmnet", dependencies=TRUE, lib=libdir)
install.packages("Rcpp", dependencies=TRUE, lib=libdir)

source("https://bioconductor.org/biocLite.R")
biocLite("qvalue")
"""

echo "downloading virfinder..."
pushd "$TOOLS_DIR"
if [[ ! -d VirFinder ]]; then
  wget https://codeload.github.com/jessieren/VirFinder/zip/master
  unzip master
  mv VirFinder-master/linux/VirFinder ./
  rm -r *master*
fi
popd

echo "installing virfinder..."
sudo apt-get -y install r-base
mkdir -p "${TOOLS_DIR}/R"
R -e "install.packages(srcdir, repos=NULL, type='source', lib=libdir)"
