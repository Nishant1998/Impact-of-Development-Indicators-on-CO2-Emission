#!/usr/bin/env python
# coding: utf-8

# In[11]:


#******** The input to this file will be the output file of 'Updated_Filling_Values_List'
#******** Input File should have '_NotBinned' appended to the original file name
#******** Here also, List of files should be given as input
#******** Just add the names of files to 'csv_name' variable as a list
#******** The output will be in the form of new csv files generated for all the input files 
#******** With ' _binned' appended to the original file name in place of '_NotBinned'

import pandas as pd
a = 1990
lst = []
for m in range(31):
    z = a + m
    lst.append(str(z))
#up_folder = ['Resources/', 'Resources/']
csv_name = ['SL.EMP.VULN.ZS','SL.EMP.WORK.ZS','SL.FAM.WORK.ZS','SL.IND.EMPL.ZS','SL.SRV.EMPL.ZS','SL.UEM.ADVN.ZS','SL.UEM.BASC.ZS','SL.UEM.INTM.ZS','SL.UEM.TOTL.ZS','SN.ITK.DEFC.ZS','SN.ITK.SVFI.ZS','SP.DYN.CDRT.IN','SP.POP.TOTL.FE.ZS','SP.POP.TOTL.MA.ZS','SP.RUR.TOTL.ZS','SP.URB.TOTL.IN.ZS']
file_name = []
for name in range(len(csv_name)):
    file_name.append('C:/Users/param/Downloads/DM-Project-master (1)/DM-Project-master/data/Ipynb Files/'+ csv_name[name] + '_NotBinned.csv')
    df11 = pd.read_csv(file_name[name], index_col = 0) #skiprows=[0,1,2,3])
    if 'Unnamed: 65' in df11.columns:
        df_drop = df11.drop(columns = ['Unnamed: 65'])
    else:
        df_drop = df11
    df_temp = df_drop.fillna('Unknown')
    count = 0
    for m in lst: 
        for w in df_temp[m]:
            if w!= 'Unknown':
                if float(w) <= 5:
                    df_temp[m][count] = '0_5'
                if float(w) > 5 and float(w) <= 10:
                    df_temp[m][count] = '5_10'
                if float(w) > 10 and float(w) <= 15:
                    df_temp[m][count] = '10_15'
                if float(w) > 15 and float(w) <= 20:
                    df_temp[m][count] = '15_20'
                if float(w) > 20 and float(w) <= 25:
                    df_temp[m][count] = '20_25'
                if float(w) > 25 and float(w) <= 30:
                    df_temp[m][count] = '25_30'
                if float(w) > 30 and float(w) <= 35:
                    df_temp[m][count] = '30_35'
                if float(w) > 35 and float(w) <= 40:
                    df_temp[m][count] = '35_40'
                if float(w) > 40 and float(w) <= 45:
                    df_temp[m][count] = '40_45'
                if float(w) > 45 and float(w) <= 50:
                    df_temp[m][count] = '45_50'
                if float(w) > 50 and float(w) <= 55:
                    df_temp[m][count] = '50_55'
                if float(w) > 55 and float(w) <= 60:
                    df_temp[m][count] = '55_60'
                if float(w) > 60 and float(w) <= 65:
                    df_temp[m][count] = '60_65'
                if float(w) > 65 and float(w) <= 70:
                    df_temp[m][count] = '65_70'
                if float(w) > 70 and float(w) <= 75:
                    df_temp[m][count] = '70_75'
                if float(w) > 75 and float(w) <= 80:
                    df_temp[m][count] = '75_80'
                if float(w) > 80 and float(w) <= 85:
                    df_temp[m][count] = '80_85'
                if float(w) > 85 and float(w) <= 90:
                    df_temp[m][count] = '85_90'
                if float(w) > 90 and float(w) <= 95:
                    df_temp[m][count] = '90_95'
                if float(w) > 95:
                    df_temp[m][count] = '95_100'
            count = count + 1  
        count = 0
    out_file = csv_name[name] + '_binned.csv'
    df_temp.to_csv(out_file)
    print(name)


# In[ ]:




