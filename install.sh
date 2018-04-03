#!/bin/bash

export ROOT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"
export DATA_DIR="$ROOT_DIR/data"
export TOOLS_DIR="$ROOT_DIR/tools"

for step in virusfriends virfinder blast rpsblast xgboost; do
  ./${step}/install.sh 2>&1 | tee ${step}/install.log
done
