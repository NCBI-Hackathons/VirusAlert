#!/bin/bash

SCRIPT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
DATA_DIR="$SCRIPT_DIR/../data"
TOOLS_DIR="$SCRIPT_DIR/../tools"
R_USER_LIBS="$TOOLS_DIR/R"
VF_DIR="$TOOLS_DIR/VirFinder"
export PATH=$TOOLS_DIR:$PATH

echo "installing debian dependencies..."
sudo apt-get install python3-biopython sra-toolkit r-base

echo "installing R dependencies to ${TOOLS_DIR}/R..."
mkdir -p "$R_USER_LIBS"
echo """
# see https://www.r-bloggers.com/permanently-setting-the-cran-repository/
local({
  r <- getOption('repos')
  r['CRAN'] <- 'http://cran.cnr.berkeley.edu/'
  options(repos = r)
})

install.packages('glmnet', dependencies=TRUE, lib='$R_USER_LIBS')
install.packages('Rcpp', dependencies=TRUE, lib='$R_USER_LIBS')

source('https://bioconductor.org/biocLite.R')
biocLite('qvalue')
""" | R --slave

echo "downloading VirFinder to ${TOOLS_DIR}/VirFinder..."
pushd "$TOOLS_DIR"
if [[ ! -d VirFinder ]]; then
  wget https://codeload.github.com/jessieren/VirFinder/zip/master
  unzip master
  mv VirFinder-master/linux/VirFinder ./
  rm -r *master*
fi
popd

echo "installing VirFinder R package..."
echo """
install.packages('$VF_DIR', repos=NULL, type='source', lib='$R_USER_LIBS')
""" | R --slave
