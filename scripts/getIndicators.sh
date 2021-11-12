#!/bin/bash
rm -r ./temp/download
mkdir ./temp/download
mkdir ./temp/download/unzipped
mkdir ./temp/download/zipped

rm -r ./data/worldbank
mkdir ./data/worldbank

while IFS=",", read -r ind_name ind_code ind_selected ind_type
do
    if [ ${ind_selected^^} = "TRUE" ]
    then
        echo "fetching" $ind_name
        wget -O ./temp/download/zipped/$ind_code.zip "https://api.worldbank.org/v2/country/all/indicator/${ind_code}?source=2&downloadformat=csv"
        unzip ./temp/download/zipped/$ind_code.zip -d ./temp/download/unzipped/$ind_code
        mkdir -p ./data/worldbank/$ind_type
        cp ./temp/download/unzipped/$ind_code/API_$ind_code* ./data/worldbank/$ind_type/$ind_code.csv
        echo $ind_code
        echo $ind_type
    fi  
done < <(tail -n +2 "config/indicators.csv")