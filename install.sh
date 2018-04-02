#!/bin/bash

for step in virfinder blast rpsblast xgboost; do
  ./${step}/install.sh 2>&1 | tee ${step}/install.log
done
