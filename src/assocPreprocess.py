import pandas as pd
from common import *

from multiprocessing.pool import ThreadPool

PREPROCESSED_PATH = getAbsPath("Output/Binned")
REORGANIZED_PATH = getAbsPath("temp/reorganized")

def reorganize(args):
    indCode2DataMap, country_code, out_columns = args
    result = pd.DataFrame(columns=out_columns)
    for indicator_name in indCode2DataMap:
        indicator_data = indCode2DataMap[indicator_name]
        result = result.append(indicator_data.loc[country_code], ignore_index=True)

    result.drop("Country Name", axis="columns", inplace=True)
    result.to_csv(REORGANIZED_PATH + "/" + country_code + ".csv", index=False)

    return "preprocessed file for %s generated" % (country_code)


def run():

    indCode2DataMap = {}
    indTypes = os.listdir(PREPROCESSED_PATH)
    for indType in indTypes:
        for ind in os.listdir(PREPROCESSED_PATH + "/" + indType):
            indCode2DataMap[ind] = pd.read_csv(PREPROCESSED_PATH + "/" + indType + "/" + ind, index_col="Country Code")
            
    first_file_data = indCode2DataMap[ind]

    inputs = []
    for country_code, row in first_file_data.iterrows():
        inputs.append((indCode2DataMap, country_code, first_file_data.columns))

    results = ThreadPool(5).imap_unordered(reorganize, inputs)
    for r in results:
        if r is not None:
            print(r)

if __name__ == '__main__':
    run()
