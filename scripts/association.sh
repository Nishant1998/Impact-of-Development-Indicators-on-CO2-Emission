#!/bin/bash

mkdir -p temp/reorganized
mkdir -p output/association

python3 src/assocPreprocess.py
python3 src/assocRule.py