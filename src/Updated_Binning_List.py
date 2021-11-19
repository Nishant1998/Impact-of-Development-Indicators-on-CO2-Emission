import pandas as pd
from common import *
import json

INPUT_DIR = getAbsPath("data/worldbank")
OUTPUT_DIR = getAbsPath("Output/Binned")
CONFIG_FILE = getAbsPath("config/indicators.csv")

def fillMissingData(data, columns):
    data.drop(getColumns(1960, 1979), inplace=True, axis=1)
    if 'Unnamed: 65' in data:
        data.drop('Unnamed: 65', inplace=True, axis=1)

    for i in range(len(columns)-2, -1, -1):
        data[columns[i]] = data[columns[i]].fillna(data[columns[i+1]])

    for i in range(0, len(columns)-1):
        data[columns[i+1]] = data[columns[i+1]].fillna(data[columns[i]])

def preProcess(ind_code, ind_type, ind_bins, ind_labels, normalize):
    file_path = INPUT_DIR + "/" + ind_type + "/" + ind_code + ".csv"
    data = pd.read_csv(file_path, index_col=1, skiprows=[0,1,2,3])
    
    columns = getColumns(1980, 2020)
    fillMissingData(data, columns)

    for i in range(0,len(columns)):

        if not pd.isna(normalize):
            data[columns[i]] = data[columns[i]] / normalize

        data[columns[i]] = pd.cut(data[columns[i]], bins=ind_bins, labels=ind_labels)
        data[columns[i]] = data[columns[i]].values.add_categories('Unknown')
        data[columns[i]] = data[columns[i]].fillna('Unknown')

    data = data.reset_index()
    columns = ["Country Name", "Country Code", "Indicator Name", "Indicator Code"] + columns
    data = data[columns]

    if not os.path.exists(OUTPUT_DIR + "/" + ind_type):
        os.makedirs(OUTPUT_DIR + "/" + ind_type)

    OUTPUT_FILE = OUTPUT_DIR + "/" + ind_type + "/" + ind_code + ".csv"

    data.to_csv(OUTPUT_FILE, index=False)

def run():

    config = pd.read_csv(CONFIG_FILE)
    selected = config[config["Primary"] == True]

    for index, row in selected.iterrows():
        ind_code = row["Indicator Code"]
        ind_type = row["Type"]
        bins = json.loads(row["Bins"])
        labels = json.loads(row["Labels"])
        normalize = row["Normalize"]

        preProcess(ind_code, ind_type, bins, labels, normalize)

if __name__ == '__main__':
    run()

