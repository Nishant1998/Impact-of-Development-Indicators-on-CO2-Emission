import pandas as pd
from common import *

INPUT_DIR = getAbsPath("Output/association")
INDICATOR_PATH = getAbsPath("config/indicators.csv")
OUT_PATH = getAbsPath("Output/topAssoc.csv")
def run():

    indicators = pd.read_csv(INDICATOR_PATH, index_col=1)
    result = pd.DataFrame()

    for filename in os.listdir(INPUT_DIR):
        data = pd.read_csv(getAbsPath(INPUT_DIR + "/" + filename))
        result = pd.concat([result, data["antecedents"] +"->"+ data["consequents"]])

    result.columns = ["rules"]
    result = result.rules.value_counts(normalize=True)
    result = result.reset_index()

    result[['Rule1', 'Rule2']] = result["index"].str.split('->', expand=True)

    result["Rule1"] = result["Rule1"].apply(lambda x: x.replace("frozenset({'", "").replace("'})", ""))
    result["Rule2"] = result["Rule2"].apply(lambda x: x.replace("frozenset({'", "").replace("'})", ""))

    result["tag1"] = result["Rule1"].apply(lambda x: x.split("@")[1])
    result["tag2"] = result["Rule2"].apply(lambda x: x.split("@")[1])

    result["Rule1"] = result["Rule1"].apply(lambda x: x.split("@")[0])
    result["Rule2"] = result["Rule2"].apply(lambda x: x.split("@")[0])

    result["Rule1Name"] = result["Rule1"].apply(lambda x: indicators.loc[x]["Indicator Name"])
    result["Rule2Name"] = result["Rule2"].apply(lambda x: indicators.loc[x]["Indicator Name"])

    columns = ["Rule1Name", "tag1", "Rule2Name", "tag2", "rules"]
    result = result[columns]
    result.to_csv(OUT_PATH, index=False)

if __name__ == '__main__':
    run()