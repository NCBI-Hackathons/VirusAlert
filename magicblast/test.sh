#!/bin/bash

export SCRIPT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
export DATA_DIR="$SCRIPT_DIR/../data"
export TOOLS_DIR="$SCRIPT_DIR/../tools"

echo "running magicblast..."
pushd "$DATA_DIR"
magicblast -db ref_viruses_rep_genomes -query SRR6172653.fastq -infmt fastq -outfmt tabular -score 40 > out.tsv
popd
