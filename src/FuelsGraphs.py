#!/usr/bin/env python
# coding: utf-8

# In[33]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from pearsonCorrelation import readData


# In[34]:


#read data

data1 = readData("../Output/Not Binned/Resources/EG.ELC.RNEW.ZS_NotBinned.csv")
data2 = readData("../Output/Not Binned/Resources/EG.ELC.PETR.ZS_NotBinned.csv")
data3 = readData("../Output/Not Binned/Resources/EG.ELC.NUCL.ZS_NotBinned.csv")
data4 = readData("../Output/Not Binned/Resources/EG.ELC.NGAS.ZS_NotBinned.csv")
data5 = readData("../Output/Not Binned/Resources/EG.ELC.HYRO.ZS_NotBinned.csv")
data6 = readData("../Output/Not Binned/Resources/EG.ELC.COAL.ZS_NotBinned.csv")


# In[ ]:





# In[35]:


contriesListDf = pd.read_csv("../Output/CountriesList.csv")
c1 = contriesListDf[contriesListDf["Economy_Type"] == "developed"].Name.to_list()
c2 = contriesListDf[contriesListDf["Economy_Type"] == "developing "].Name.to_list()
c3 = contriesListDf[contriesListDf["Economy_Type"] == "under_developed "].Name.to_list()


# In[36]:


d1a = data1[data1["Country_Name"].isin(c1)].iloc[:,4:].values.astype(float)
d1b = data1[data1["Country_Name"].isin(c2)].iloc[:,4:].values.astype(float)
d1c = data1[data1["Country_Name"].isin(c3)].iloc[:,4:].values.astype(float)

d2a = data2[data2["Country_Name"].isin(c1)].iloc[:,4:].values.astype(float)
d2b = data2[data2["Country_Name"].isin(c2)].iloc[:,4:].values.astype(float)
d2c = data2[data2["Country_Name"].isin(c3)].iloc[:,4:].values.astype(float)

d3a = data3[data3["Country_Name"].isin(c1)].iloc[:,4:].values.astype(float)
d3b = data3[data3["Country_Name"].isin(c2)].iloc[:,4:].values.astype(float)
d3c = data3[data3["Country_Name"].isin(c3)].iloc[:,4:].values.astype(float)

d4a = data4[data4["Country_Name"].isin(c1)].iloc[:,4:].values.astype(float)
d4b = data4[data4["Country_Name"].isin(c2)].iloc[:,4:].values.astype(float)
d4c = data4[data4["Country_Name"].isin(c3)].iloc[:,4:].values.astype(float)

d5a = data5[data5["Country_Name"].isin(c1)].iloc[:,4:].values.astype(float)
d5b = data5[data5["Country_Name"].isin(c2)].iloc[:,4:].values.astype(float)
d5c = data5[data5["Country_Name"].isin(c3)].iloc[:,4:].values.astype(float)

d6a = data6[data6["Country_Name"].isin(c1)].iloc[:,4:].values.astype(float)
d6b = data6[data6["Country_Name"].isin(c2)].iloc[:,4:].values.astype(float)
d6c = data6[data6["Country_Name"].isin(c3)].iloc[:,4:].values.astype(float)


# In[37]:


d1a = d1a.sum(axis=0) / len(c1)
d1b = d1b.sum(axis=0) / len(c2)
d1c = d1c.sum(axis=0) / len(c3)
d2a = d2a.sum(axis=0) / len(c1)
d2b = d2b.sum(axis=0) / len(c2)
d2c = d2c.sum(axis=0) / len(c3)
d3a = d3a.sum(axis=0) / len(c1)
d3b = d3b.sum(axis=0) / len(c2)
d3c = d3c.sum(axis=0) / len(c3)
d4a = d4a.sum(axis=0) / len(c1)
d4b = d4b.sum(axis=0) / len(c2)
d4c = d4c.sum(axis=0) / len(c3)
d5a = d5a.sum(axis=0) / len(c1)
d5b = d5b.sum(axis=0) / len(c2)
d5c = d5c.sum(axis=0) / len(c3)
d6a = d6a.sum(axis=0) / len(c1)
d6b = d6b.sum(axis=0) / len(c2)
d6c = d6c.sum(axis=0) / len(c3)


# In[38]:


x = list(range(1990,2021))


# In[39]:


d1a.sum(axis=0)/len(c1)


# In[40]:


plt.figure(figsize=(10, 5))
plt.plot(x,d1a, label = "renewable")
plt.plot(x,d2a, label = "oil")
plt.plot(x,d3a, label = "nuclear")
plt.plot(x,d4a, label = "gas")
plt.plot(x,d5a, label = "hydro")
plt.plot(x,d6a, label = "coal")

plt.xlabel('years')
plt.ylabel('Fule used %')
 
plt.title('Developed country')
plt.legend()

plt.savefig("../Output/charts/Developed_FuelUse.png")
plt.show()


# In[41]:


plt.figure(figsize=(10, 5))
plt.plot(x,d1b, label = "renewable")
plt.plot(x,d2b, label = "oil")
plt.plot(x,d3b, label = "nuclear")
plt.plot(x,d4b, label = "gas")
plt.plot(x,d5b, label = "hydro")
plt.plot(x,d6b, label = "coal")

plt.xlabel('years')
plt.ylabel('Fule used %')
 
plt.title('Developing country')
plt.legend()

plt.savefig('../Output/charts/Developing_FuelUse.png')
plt.show()


# In[42]:



plt.figure(figsize=(10, 5))
plt.plot(x,d1c, label = "renewable")
plt.plot(x,d2c, label = "oil")
plt.plot(x,d3c, label = "nuclear")
plt.plot(x,d4c, label = "gas")
plt.plot(x,d5c, label = "hydro")
plt.plot(x,d6c, label = "coal")

plt.xlabel('years')
plt.ylabel('Fule used %')
 
plt.title('Under developed country')
plt.legend()

plt.savefig('../Output/charts/Under_developed_FuelUse.png')
plt.show()


# In[ ]:





# In[43]:


g1 = data1[data1["Country_Name"] == "World"].iloc[:,4:].values.astype(float).reshape(31,)
g2 = data2[data2["Country_Name"] == "World"].iloc[:,4:].values.astype(float).reshape(31,)
g3 = data3[data3["Country_Name"] == "World"].iloc[:,4:].values.astype(float).reshape(31,)
g4 = data4[data4["Country_Name"] == "World"].iloc[:,4:].values.astype(float).reshape(31,)
g5 = data5[data5["Country_Name"] == "World"].iloc[:,4:].values.astype(float).reshape(31,)
g6 = data6[data6["Country_Name"] == "World"].iloc[:,4:].values.astype(float).reshape(31,)
plt.figure(figsize=(10, 5))
plt.plot(x,g1, label = "renewable")
plt.plot(x,g2, label = "oil")
plt.plot(x,g3, label = "nuclear")
plt.plot(x,g4, label = "gas")
plt.plot(x,g5, label = "hydro")
plt.plot(x,g6, label = "coal")

plt.xlabel('years')
plt.ylabel('Fule used %')

plt.title('World')
plt.legend()


plt.savefig('../Output/charts/World_FuelUse.png')

plt.show()


# In[44]:


g1


# In[ ]:




