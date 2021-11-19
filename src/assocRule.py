import pandas as pd
from common import *

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules

from multiprocessing.pool import ThreadPool

INPUT_DIR = getAbsPath("temp/reorganized")
OUT_DIR = getAbsPath("Output/association")

def associationMine(country_file):
    country_data = pd.read_csv(INPUT_DIR + "/" + country_file)

    start = 1990
    end = 2020
    for x in range(start, end+1):
        x_str = str(x)
        country_data[x_str] =  country_data["Indicator Code"] + "@" + country_data[x_str]

    transaction_list = []
    for x in range(start, end+1):
        transaction_list.append(country_data[x_str].tolist())
    
    te = TransactionEncoder()
    te_array = te.fit(transaction_list).transform(transaction_list)

    df = pd.DataFrame(te_array, columns=te.columns_)

    frequent_itemsets_fp = fpgrowth(df, min_support=1, use_colnames=True)
    frequent_itemsets_fp = frequent_itemsets_fp[frequent_itemsets_fp["itemsets"].apply(lambda x: not any("Unknown" in item for item in x))]
    frequent_itemsets_fp = frequent_itemsets_fp[frequent_itemsets_fp["itemsets"].apply(lambda x: len(x)) < 5]

    if not frequent_itemsets_fp.empty:
        rules_fp = association_rules(frequent_itemsets_fp, metric="confidence", min_threshold=1)

        rules_fp["antecedents_len"] = rules_fp["antecedents"].apply(lambda x: len(x))
        rules_fp = rules_fp[rules_fp["antecedents_len"] == 1]
        rules_fp["consequents_len"] = rules_fp["consequents"].apply(lambda x: len(x))
        rules_fp = rules_fp[rules_fp["consequents_len"] == 1]
        rules_fp["interesting"] = rules_fp["consequents"].apply(lambda x: any("EN.ATM.CO2E.KT" in item for item in x))

        rules_fp = rules_fp[rules_fp["interesting"]]

        rules_fp.to_csv(OUT_DIR + "/" + country_file, index=False)
        return "Association generated for %s file" % country_file
    else:
        return "Association could not be generated for %s file" % country_file


def run():
    file_names = os.listdir(INPUT_DIR)
    results = ThreadPool(5).imap_unordered(associationMine, file_names)
    for r in results:
        if r is not None:
            print(r)

if __name__ == '__main__':
    run()