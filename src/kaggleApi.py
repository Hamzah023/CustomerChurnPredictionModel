import kaggle
import os   

def downloadData():
    dataSet = 'blastchar/telco-customer-churn'
    dataPath = '../data'

    if not os.path.exists(dataPath):
        os.makedirs(dataPath)


    kaggle.api.dataset_download_files(dataSet, path=dataPath, unzip=True)

    print("Data downloaded successfully!")

    filePath = os.path.join(dataPath, 'WA_Fn-UseC_-Telco-Customer-Churn.csv')

    print(f"Data file path: {filePath}")

    return filePath

def getFilePath():

    filePath = '../data/WA_Fn-UseC_-Telco-Customer-Churn.csv'

    if not os.path.exists(filePath): 
        print("Data file not found. Downloading data...\n")
        filePath = downloadData()

    return filePath

