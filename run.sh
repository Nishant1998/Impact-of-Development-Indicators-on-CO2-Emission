#!/bin/bash

sh scripts/getIndicators.sh
echo "Data Fetch completed"
sh scripts/preprocessing.sh
echo "Initial preprocessing completed"
sh scripts/associationOverall.sh
echo "Association Rules completed"
sh scripts/corelation.sh


