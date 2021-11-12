from common import *
import pandas as pd

import requests
import zipfile
import io

from multiprocessing.pool import ThreadPool

import shutil

WORLD_BANK_URL = "https://api.worldbank.org/v2/country/all/indicator/%s?source=2&downloadformat=csv"
def fetchFile(args):
    ind_name, sub_dir_name = args
    url = WORLD_BANK_URL % ind_name
    unzip_dir = getAbsPath("temp/download/%s" % ind_name)
    outputDirectory = getAbsPath("data/worldbank/%s/" % (sub_dir_name))
    outfile = getAbsPath(outputDirectory + "/" + ind_name + ".csv")

    #skip if file already exists
    if isFile(outfile):
        return "Skipping %s, data already available" % (ind_name)

    #download and unzip
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(unzip_dir)

    #create type directory if not present
    if not os.path.exists(outputDirectory):
        os.makedirs(outputDirectory)

    #copy only the csv data file in to the data directory
    for file in os.listdir(unzip_dir):
        if file.startswith("API_"):
            sourceFile = unzip_dir +"/"+ file
            shutil.copyfile(sourceFile, outfile)

    return "%s, downloaded successfully!" % (ind_name)

def run():
    config = pd.read_csv(getAbsPath("config/indicators.csv"))
    config = config.loc[config["Primary"] == True]

    indicators = []
    for index, row in config.iterrows():
        indicators.append((row["Indicator Code"], row["Type"]))
 
    # Run 5 multiple threads. Each call will take the next element in urls list
    results = ThreadPool(5).imap_unordered(fetchFile, indicators)
    for r in results:
        if r is not None:
            print(r)

if __name__ == '__main__':
    run()