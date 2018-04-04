#!/bin/bash

SCRIPT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
DATA_DIR="$SCRIPT_DIR/../data"
TOOLS_DIR="$SCRIPT_DIR/../tools"

# based on https://github.com/NCBI-Hackathons/VirusFriends
mkdir -p "$TOOLS_DIR"
cd "$TOOLS_DIR"
if [[ -z $(ls | grep magicblast) ]]; then
  echo "installing magicblast..."
  url=ftp://ftp.ncbi.nlm.nih.gov/blast/executables/magicblast/LATEST/ncbi-magicblast-1.3.0-x64-linux.tar.gz
  wget "$url" -O magicblast.tar.gz
  tar -xvf magicblast.tar.gz
  rm -f magicblast.tar.gz
  # P=$(find . -name magicblast | sed -e 's/magicblast$//; s/^\.\///')
  # echo "magicblast installed in $NEWPATH:$PWD/$P"
fi

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
makeblastdb -in genomes.fasta -input_type fasta -dbtype nucl -parse_seqids -out viralg -title "An integrated database for viral genomics"

popd
