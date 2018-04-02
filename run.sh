#!/bin/bash

for step in virfinder blast rpsblast xgboost; do
  ./${step}/run.sh 2>&1 | tee ${step}/run.log
done
