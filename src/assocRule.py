import pandas as pd
from common import *

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules

from multiprocessing.pool import ThreadPool

INPUT_DIR = getAbsPath("temp/reorganized")
OUT_DIR = getAbsPath("output/association")

def associationMine(country_file):
    country_data = pd.read_csv(INPUT_DIR + "/" + country_file)

    start = 1960
    end = 2020
    for x in range(start, end+1):
        x_str = str(x)
        country_data[x_str] = country_data["Indicator Code"] + "@" + country_data[x_str]

    transaction_list = []
    for x in range(start, end+1):
        transaction_list.append(country_data[x_str].tolist())
    
    te = TransactionEncoder()
    te_array = te.fit(transaction_list).transform(transaction_list)

    df = pd.DataFrame(te_array, columns=te.columns_)

    frequent_itemsets_fp = fpgrowth(df, min_support=0.01, use_colnames=True)

    rules_fp = association_rules(frequent_itemsets_fp, metric="confidence", min_threshold=0.8)

    rules_fp.to_csv(OUT_DIR + "/" + country_file, index=False)
    return "Association generated for %s file" % country_file


def run():
    file_names = os.listdir(INPUT_DIR)
    results = ThreadPool(5).imap_unordered(associationMine, file_names)
    for r in results:
        if r is not None:
            print(r)

if __name__ == '__main__':
    run()