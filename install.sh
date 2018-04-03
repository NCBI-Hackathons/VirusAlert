!/bin/bash

SCRIPT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
DATA_DIR="$SCRIPT_DIR/../data"
TOOLS_DIR="$SCRIPT_DIR/../tools"
export PATH=$TOOLS_DIR:$PATH
 
for tool in virfinder virusfriends; do
  ./${tool}/install.sh 2>&1 | tee ${tool}/install.log
done

echo "installing longreadviruses dependencies..."
sudo apt-get install python-docopt
# TODO install the script itself?
