from common import *
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec

COUNTRY_DETAILS = getAbsPath("Output/CountriesList.csv")

def plotIndicator(filepath, outfile):
    countries = pd.read_csv(COUNTRY_DETAILS)
    countries_data = pd.read_csv(filepath, skiprows=[0,1,2,3])
    countries["Economy_Type"] = countries["Economy_Type"].str.strip()

    developed = countries.loc[countries["Economy_Type"]=="developed"]
    under_developed = countries.loc[countries["Economy_Type"]=="under_developed"]
    developing = countries.loc[countries["Economy_Type"]=="developing"]

    developing_data = countries_data[countries_data["Country Name"].isin(developing["Name"])]
    under_developed_data = countries_data[countries_data["Country Name"].isin(under_developed["Name"])]
    developed_data = countries_data[countries_data["Country Name"].isin(developed["Name"])]

    columns = ["Country Name"] + getColumns(1960, 2020)
    chart_developing = developing_data[columns]
    chart_developing = chart_developing.set_index("Country Name")
    chart_developing = chart_developing.mean()
    chart_developing = chart_developing.transpose()

    chart_developed = developed_data[columns]
    chart_developed = chart_developed.set_index("Country Name")
    chart_developed = chart_developed.mean()
    chart_developed = chart_developed.transpose()

    chart_under_developed = under_developed_data[columns]
    chart_under_developed = chart_under_developed.set_index("Country Name")
    chart_under_developed = chart_under_developed.mean()
    chart_under_developed = chart_under_developed.transpose()

    chart_data = pd.concat([chart_developing,chart_developed,chart_under_developed], axis=1)
    chart_data.columns = ["developing", "developed", "under developed"]
    print(chart_data)
    
    plot = chart_data.plot(figsize=(15, 10))
    fig = plot.get_figure()
    fig.savefig(getAbsPath("Output/charts/%s.jpeg" % (outfile)))
    
    return chart_data

def plotData(filepath, outfile):
    data = pd.read_csv(filepath, skiprows=[0,1,2,3])

    columns = ["Country Name"] + getColumns(1960, 2020)

    chart_data = data[columns]
    chart_data = chart_data.set_index("Country Name")
    chart_data = chart_data.mean()
    chart_data = chart_data.transpose()

    plot = chart_data.plot(figsize=(15, 10))
    fig = plot.get_figure()
    fig.savefig(getAbsPath("Output/charts/%s.jpeg" % (outfile)))

def run():
    plotIndicator(getAbsPath("data/worldbank/Resources/TM.VAL.FUEL.ZS.UN.csv"), "fuelImports")
    plotIndicator(getAbsPath("data/worldbank/Resources/TM.VAL.FOOD.ZS.UN.csv"), "foodImports")
    
    plotData(getAbsPath("data/worldbank/Emission/EN.ATM.CO2E.KT.csv"), "CO2 Emissions")
    

if __name__ == "__main__":
    run()