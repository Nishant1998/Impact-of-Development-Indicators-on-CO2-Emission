#!/bin/bash

rm -rf temp/reorganized
mkdir -p temp/reorganized
python3 src/assocPreprocess.py

rm -rf Output/association
mkdir -p Output/association
python3 src/assocRule.py

python3 src/assocAnalysis.py