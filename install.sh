#!/bin/bash

SCRIPT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
DATA_DIR="$SCRIPT_DIR/../data"
TOOLS_DIR="$SCRIPT_DIR/../tools"
VF_DIR="$TOOLS_DIR/VirFinder"
echo "TOOLS_DIR: $TOOLS_DIR"
echo "DATA_DIR: $DATA_DIR"
export R_USER_LIBS="${TOOLS_DIR}/R"
export PATH=$TOOLS_DIR:$PATH

echo "installing debian dependencies..."
sudo apt-get install python3-biopython sra-toolkit r-base python3-docopt libxml2 libxml2-dev libcurl4-openssl-dev libssl-dev

echo "installing R dependencies to ${TOOLS_DIR}/R..."
mkdir -p "$R_USER_LIBS"
echo """
# see https://www.r-bloggers.com/permanently-setting-the-cran-repository/
local({
  r <- getOption('repos')
  r['CRAN'] <- 'http://cran.cnr.berkeley.edu/'
  options(repos = r)
})

install.packages('tidyverse', dependencies=TRUE, lib='$R_USER_LIBS')
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

# get viral refseq blast database
mkdir -p "$DATA_DIR"
pushd "$DATA_DIR"
for url in \
  'http://mirrors.vbi.vt.edu/mirrors/ftp.ncbi.nih.gov/blast/db/ref_viruses_rep_genomes.tar.gz'; do
    name="$(basename "$url")"
    [[ -f "$name" ]] || wget "$url"
    tar xvzf "$name"
done

wget http://www.virusite.org/archive/2018.1/genomes.fasta.zip
unzip genomes.fasta.zip

perl -ne 'if(!/^[\s\t]/){print $_}' genomes.fasta |awk -v RS=">" -v FS="\n" -v ORS="" ' { if ($2) print ">"$0 } ' >  genomes_clean.fasta

makeblastdb -in genomes_clean.fasta -input_type fasta -dbtype nucl -parse_seqids -out viralg -title "An integrated database for viral genomics"

popd
