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
csv_name = ['SL.EMP.VULN.ZS','SL.EMP.WORK.ZS','SL.FAM.WORK.ZS','SL.IND.EMPL.ZS','SL.SRV.EMPL.ZS','SL.UEM.ADVN.ZS','SL.UEM.BASC.ZS','SL.UEM.INTM.ZS','SL.UEM.TOTL.ZS','SN.ITK.DEFC.ZS','SN.ITK.SVFI.ZS','SP.DYN.CDRT.IN','SP.POP.TOTL.FE.ZS','SP.POP.TOTL.MA.ZS','SP.RUR.TOTL.ZS','SP.URB.TOTL.IN.ZS']
up_folder = 'Social/'
file_name = []
for name in range(len(csv_name)):
    file_name.append('C:/Users/param/Downloads/DM-Project-master (1)/DM-Project-master/data/worldbank/' + up_folder + csv_name[name] + '.csv')
    df11 = pd.read_csv(file_name[name], index_col=0, skiprows=[0,1,2,3])
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
    out_file = csv_name[name] + '_NotBinned.csv'
    df_temp.to_csv(out_file)


# In[ ]:




