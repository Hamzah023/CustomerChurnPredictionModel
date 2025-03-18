import os
import pandas as pd
from kaggleApi import downloadData, getFilePath
from dataCleaning import cleanData
from handleClassImbalance import handleClassImbalance

def loadData():
    print("Loading data using Kaggle API...\n")
    filePath = getFilePath()
    df = pd.read_csv(filePath) # 

    if df is not None:
        print("Data loaded successfully!")

    return df

def cleanDataMain(df):
    print("Cleaning data...\n")
    cleaned_df = cleanData(df)

    if cleaned_df is not None:
        print("Data cleaned successfully!\n")

        print("Handling class imbalance...\n")
        balanced_df = handleClassImbalance(cleaned_df)
        return cleaned_df, balanced_df
    
    else:
        error = "Data not cleaned. Please check the file."

    return error

def customer_churn_prediction():
    print("Running customer churn prediction model...\n")

    #Placeholder for the customer churn prediction model

    print("Customer churn prediction model executed!\n")

def main():
    df = None
    while True:
        print("Telco Customer Churn Prediction Model\n")
        print("1. Load Data using Kaggle API")
        print("2. Clean Data")
        print("3. Run Customer Churn Prediction Model")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            df = loadData()
        elif choice == '2':
            if df is None:
                print("Data not loaded. Please load data first.\n")
            else:
                df = cleanDataMain(df)
        elif choice == '3':
            if df is None:
                print("Data not loaded. Please load data first.\n")
            else:
                customer_churn_prediction()
        elif choice == '4':
            print("Exiting...\n")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

