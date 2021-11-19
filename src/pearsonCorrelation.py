#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr


# In[2]:


def readData(fileName):
    data = pd.read_csv(fileName)
    data = data.rename(columns={"Country Name": "Country_Name", "Country Code": "Country_Code"})
    
    # handel unknown value
    data = data.replace('Unknown',np.nan)
    data = data.dropna()
    
    return data


# In[3]:


def getCountriesName(df1,df2):
    ''' This funtion give list of countries. 
    It does not consider which have unknown value for all years.
    CountriesList.csv have info which are 195 countres and which are other groups'''
    
    contriesListDf = pd.read_csv("../Output/CountriesList.csv")
    
    commonCountry = np.intersect1d(np.array(df1.Country_Name.to_list()), np.array(df2.Country_Name.to_list()))
    contriesList = np.intersect1d(commonCountry, np.array(contriesListDf[contriesListDf['Type'] == 'country'].Name.to_list()))
    return contriesList
    


# In[4]:


def getCountriesCode(df,names):
    df = df[df.Country_Name.isin(names)].sort_values('Country_Name')
    codes = df.Country_Code.to_list()
    return codes


# In[5]:


def pearson_rvalue(path1,path2,name1,name2,plot=False):
    R = []
    p_value = []
    
    data1 = readData(path1)
    data2 = readData(path2)
    # "DM-Project/Output/Not Binned/Emission/EN.ATM.CO2E.KT_NotBinned.csv"
    # "DM-Project/Output/Not Binned/Land/AG.LND.FRST.ZS_NotBinned.csv"
    
    #get list of countries
    contriesList = getCountriesName(data1,data2)
    contriesList = np.insert(contriesList,len(contriesList),"World")
    contriesList.sort()
    
    
    
    data2 = data2[data2["Country_Name"].isin(contriesList)].sort_values('Country_Name')
    data1 = data1[data1["Country_Name"].isin(contriesList)].sort_values('Country_Name')
    
    data2 = data2.iloc[:, 4:].values.astype(float)
    data2 = pd.DataFrame(np.concatenate((np.array(data1.iloc[:, :4].values) , data2), axis=1), columns=data1.columns.to_list())
    
    for i in range(len(contriesList)):
        x = data1.iloc[:, 4:].values[i].astype(float)
        y = data2.iloc[:, 4:].values[i].astype(float)
        r,p =  pearsonr(x,y)
        
        R.append(r)
        p_value.append(p)
        
        if(plot == True):
            plt.scatter(x,y)
            plt.xlabel(name1)
            plt.ylabel(name2)
            plt.title("{} -> R = {}, P_Value = {}".format(contriesList[i],r,p))
            plt.show()
            
    correlation_and_pvalue = pd.DataFrame()
    correlation_and_pvalue["Country_Name"] = contriesList
    correlation_and_pvalue["Country_Code"] = getCountriesCode(data1,contriesList)
    correlation_and_pvalue["R"] = R
    correlation_and_pvalue["P_Value"] = p_value
    
    return correlation_and_pvalue


# In[ ]:




