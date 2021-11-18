#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
from pearsonCorrelation import pearson_rvalue


def main(data,plot):
    for i in range(len(data)):
        # get path and name of feature from file 
        path1 = data.iloc[i][0]
        name1 = data.iloc[i][1]
        path2 = data.iloc[i][2]
        name2 = data.iloc[i][3]
        output_path = data.iloc[i][4]
    
        # Here we calculate pearson correlation R and its p value
        # pearson_rvalue is a funtion in pearsonCorrelation.py file in src
        output_df = pearson_rvalue(path1,path2,name1,name2,plot=False)
    
        correlationDirection = []
        isSignificant = []
        for j in range(len(output_df)):
            # for each country get r and pvalue
            c = output_df.R.to_list()[j]
            p = output_df.P_Value.to_list()[j]
    
            # if p<= 0.05 we consider it correlation significant
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


if __name__ == "__main__":
    # Read features_for_correlation.csv in config folder 
    # this file file path of two feature we want to find correlation between 
    data = pd.read_csv("../config/features_for_correlation.csv")
    # We pass the data to main funtion.
    main(data,False)

