#!/bin/bash

# comment out when done working on it:
SCRIPT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
DATA_DIR="$SCRIPT_DIR/../data"
TOOLS_DIR="$SCRIPT_DIR/../tools"

pushd "TOOLS_DIR"
mkdir $DATA_DIR/fastq-dump
wget "http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-centos_linux64.tar.gz"
tar -xzf sratoolkit.current-centos_linux64.tar.gz
echo "input the SRRs of the data you would like to work with (now will just be our data)"
$DATA_DIR/fastq-dump -X 5 -Z SRR5383888
$DATA_DIR/fastq-dump -X 5 -Z SRR5383891
$DATA_DIR/fastq-dump -X 5 -Z SRR5150787
popd

echo "installing virusfriends..."
