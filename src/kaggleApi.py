import kaggle
import os   

dataSet = 'blastchar/telco-customer-churn'
dataPath = './data'

if not os.path.exists(dataPath):
    os.makedirs(dataPath)


kaggle.api.dataset_download_files(dataSet, path='./data', unzip=True)

print("Data downloaded successfully!")

