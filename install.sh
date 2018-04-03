!/bin/bash
#Commentut when done working on it:
SCRIPT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
DATA_DIR="$SCRIPT_DIR/../data"
TOOLS_DIR="$SCRIPT_DIR/../tools"
export PATH=$TOOLS_DIR:$PATH
pushd "$TOOLS_DIR"
wget "http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/current/sratoolkit.current-centos_linux64.tar.gz"
tar -xzf sratoolkit.current-centos_linux64.tar.gz
popd 
pushd "$DATA_DIR"
echo "input the SRRs of the data you would like to work with (now will just be our data)"
touch HBV01wVirus.fasta
touch HBV02control.fasta
touch MecqueEbola.fasta
/home/ubuntu/LongReadViruses/tools/sratoolkit.2.9.0-centos_linux64/bin/fastq-dump -X 5 -Z SRR5383888 > HBV01wVirus
/home/ubuntu/LongReadViruses/tools/sratoolkit.2.9.0-centos_linux64/bin/fastq-dump -X 5 -Z SRR5383891 > HBV02control
/home/ubuntu/LongReadViruses/tools/sratoolkit.2.9.0-centos_linux64/bin/fastq-dump -X 5 -Z SRR5150787 > MecqueEbola
 
 
popd
 
echo "installing virusfriends..."

