#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr


def readData(fileName):
    # This funtion read data in dataframe. 
    data = pd.read_csv(fileName)
    data = data.rename(columns={"Country Name": "Country_Name", "Country Code": "Country_Code"})
    
    # handel unknown value
    data = data.replace('Unknown',np.nan)
    data = data.dropna()
    
    return data


def getCountriesName(df1,df2):
    ''' This funtion give list of countries. 
    It does not consider which have unknown value for all years.
    CountriesList.csv have info which are 195 countres and which are other groups'''
    
    contriesListDf = pd.read_csv("../Output/CountriesList.csv")
    
    commonCountry = np.intersect1d(np.array(df1.Country_Name.to_list()), np.array(df2.Country_Name.to_list()))
    contriesList = np.intersect1d(commonCountry, np.array(contriesListDf[contriesListDf['Type'] == 'country'].Name.to_list()))
    return contriesList
    

def getCountriesCode(df,names):
    # this funtion get country codes from its names
    df = df[df.Country_Name.isin(names)].sort_values('Country_Name')
    codes = df.Country_Code.to_list()
    return codes

def pearson_rvalue(path1,path2,name1,name2,plot=False):
    # this funtion calculate correlation coefficient
    R = [] # pearson R
    p_value = []
    
    # read indicators file from given paths
    data1 = readData(path1)
    data2 = readData(path2)
    
    # get list of countries
    # only selected 195 country And country with are common in both feature.
    contriesList = getCountriesName(data1,data2)
    contriesList = np.insert(contriesList,len(contriesList),"World")
    contriesList.sort()
    
    
    
    data2 = data2[data2["Country_Name"].isin(contriesList)].sort_values('Country_Name')
    data1 = data1[data1["Country_Name"].isin(contriesList)].sort_values('Country_Name')
    
    data2 = data2.iloc[:, 4:].values.astype(float)
    data2 = pd.DataFrame(np.concatenate((np.array(data1.iloc[:, :4].values) , data2), axis=1), columns=data1.columns.to_list())
    
    # for every country 
    for i in range(len(contriesList)):
        x = data1.iloc[:, 4:].values[i].astype(float)
        y = data2.iloc[:, 4:].values[i].astype(float)
        # calculate r and p value for each country
        r,p =  pearsonr(x,y)
        
        # add r and pvalue in list
        R.append(r)
        p_value.append(p)
        
        if(plot == True):
            plt.scatter(x,y)
            plt.xlabel(name1)
            plt.ylabel(name2)
            plt.title("{} -> R = {}, P_Value = {}".format(contriesList[i],r,p))
            plt.show()
    
    # add data of r and pvalue in dataframe        
    correlation_and_pvalue = pd.DataFrame()
    correlation_and_pvalue["Country_Name"] = contriesList
    correlation_and_pvalue["Country_Code"] = getCountriesCode(data1,contriesList)
    correlation_and_pvalue["R"] = R
    correlation_and_pvalue["P_Value"] = p_value
    
    return correlation_and_pvalue

