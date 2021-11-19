#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pearsonCorrelation import pearson_rvalue


# In[3]:


def main(data,plot):
    for i in range(len(data)):
        path1 = data.iloc[i][0]
        name1 = data.iloc[i][1]
        path2 = data.iloc[i][2]
        name2 = data.iloc[i][3]
        output_path = data.iloc[i][4]
    
        output_df = pearson_rvalue(path1,path2,name1,name2,plot=False)
    
        correlationDirection = []
        isSignificant = []
        for i in range(len(output_df)):
            c = output_df.R.to_list()[i]
            p = output_df.P_Value.to_list()[i]
    
            if(p <= 0.05):
                isSignificant.append(True)
            else:
                isSignificant.append(False)
        
            if(c < 0):
                correlationDirection.append("NEG")
            elif(c > 0):
                correlationDirection.append("POS")
            else:
                correlationDirection.append("NO")
            
        output_df["correlation"] = correlationDirection
        output_df["Significant"] = isSignificant
        output_df.to_csv(output_path, index=False)


# In[4]:


if __name__ == "__main__":
    data = pd.read_csv("../config/features_for_correlation.csv")
    main(data,False)

