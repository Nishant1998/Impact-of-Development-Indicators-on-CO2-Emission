#!/bin/bash

rm -rf "Output/Binned"
rm -rf "Output/Not Binned"

python3 src/Updated_Binning_List.py
python3 src/Updated_Filling_Values_List.py