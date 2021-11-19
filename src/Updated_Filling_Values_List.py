#!/usr/bin/env python
# coding: utf-8

# In[13]:


#******** The input to this file will be the original unprocessed file
#******** It will fill the missing values
#******** List of files should be given as input
#******** Just add the names of files to 'csv_name' variable as a list
#******** The output will be in the form of new csv files generated for all the input files 
#******** With '_NotBinned' appended to the original file name
    
import pandas as pd
from common import *
a = 1990
lst = []
for m in range(31):
    z = a + m
    lst.append(str(z))
b = 1960
lst_drop = []
for m in range(30):
    z = b + m
    lst_drop.append(str(z))

INPUT_DIR = getAbsPath("data/worldbank")
OUTPUT_DIR = getAbsPath("Output/Not Binned")
CONFIG_FILE = getAbsPath("config/indicators.csv")

def run():

    config = pd.read_csv(CONFIG_FILE)
    selected = config[config["Primary"] == True]

    for index, row in selected.iterrows():
        ind_code = row["Indicator Code"]
        ind_type = row["Type"]

        fillValues(ind_type, ind_code)

def fillValues(ind_type, ind_code):

    input_path = INPUT_DIR + "/" + ind_type + "/" + ind_code + ".csv"
    df11 = pd.read_csv(input_path, index_col=0, skiprows=[0,1,2,3])
    if 'Unnamed: 65' in df11.columns:
        df_drop = df11.drop(columns = ['Unnamed: 65'])
    else:
        df_drop = df11
    df_temp2 = df_drop.drop(columns = lst_drop)
    df_temp = df_temp2.fillna('Unknown')
    count = 0
    for m in lst: 
        for w in df_temp[m]:
            if w!= 'Unknown':
                if int(m) >= 1991:
                    year_index = str(int(m) - 1)
                    if df_temp[year_index][count] == 'Unknown':
                        z = int(year_index)
                        lst2 = lst[:(z - 1989)]
                        for num in lst2:
                            df_temp[num][count] = w
            elif w == 'Unknown':
                if int(m) >= 1991:
                    year_index = str(int(m) - 1)
                    if df_temp[year_index][count] != 'Unknown':
                        z = int(year_index)
                        val = df_temp[year_index][count]
                        df_temp[m][count] = val
            count = count + 1  
        count = 0

    if not os.path.exists(OUTPUT_DIR + "/" + ind_type):
        os.makedirs(OUTPUT_DIR + "/" + ind_type)

    out_file =  OUTPUT_DIR + "/" + ind_type + "/" + ind_code + '_NotBinned.csv'
    df_temp.to_csv(out_file)

if __name__ == '__main__':
    run()


# In[ ]:




