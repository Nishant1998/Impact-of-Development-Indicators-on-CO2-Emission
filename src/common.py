import os
import json

"""function to get absolute path of file"""
def getAbsPath(path):
    return os.path.abspath(path)
        
"""function to write json to file"""
def writeJsonToFile(data, path):
    writeToFile(json.dumps(data, indent=4), path)

"""function to check if the file is present"""
def isFile(path):
    return os.path.isfile(path)

def getColumns(start, end):
    result = []
    for year in range(start, end+1):
        result.append(str(year))

    return result
