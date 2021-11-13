#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df11 = pd.read_csv('C:/Users/param/Downloads/DM-Project-master (1)/DM-Project-master/data/worldbank/Agriculture/AG.LND.AGRI.ZS.csv', index_col=0, skiprows=[0,1,2,3])
df_drop = df11.drop(columns = ['Unnamed: 65'])
df_temp = df_drop.fillna('Unknown')


# In[2]:


a = 1960
lst = []
for m in range(61):
    z = a + m
    lst.append(str(z))
count = 0
for m in lst: 
    for w in df_temp[m]:
        if w!= 'Unknown':
            if int(m) >= 1961:
                year_index = str(int(m) - 1)
                if df_temp[year_index][count] == 'Unknown':
                    z = int(year_index)
                    lst2 = lst[:(z - 1959)]
                    for num in lst2:
                        df_temp[num][count] = w
        elif w == 'Unknown':
            if int(m) >= 1961:
                year_index = str(int(m) - 1)
                if df_temp[year_index][count] != 'Unknown':
                    z = int(year_index)
                    val = df_temp[year_index][count]
                    lst3 = lst[(z - 1959):]
                    for num in lst3:
                        df_temp[num][count] = val
        count = count + 1  
    count = 0
df_temp


# In[3]:


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


# In[4]:


df_temp.to_csv('EG.FEC.RNEW.ZS_filled.csv')


# In[ ]:




