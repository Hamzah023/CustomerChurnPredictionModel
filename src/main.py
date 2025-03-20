import os
import pandas as pd
from kaggleApi import downloadData, getFilePath
from dataCleaning import cleanData
from handleClassImbalance import handleClassImbalance
from sqlalchemy import create_engine

# Function to save data to SQL

def save_to_sql(df, table_name, db_url):

    engine = create_engine(db_url)

    df.to_sql(table_name, engine, if_exists='replace', index=False) #this function is used to save the dataframe to a SQL table, if the table already exists it will be replaced
    print(f"✅ Data saved to SQL table: {table_name}")

# Data pipeline function
def data_pipeline():

    print("Starting data pipeline...\n")

    print("Downloading data using Kaggle API...\n")
    downloadData()
    file_path = getFilePath()
    if not os.path.exists(file_path):
        print("Error: Dataset not found. Please check the Kaggle API configuration.")
        return

    print("Loading dataset...\n")
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully!")


    print("Cleaning data...\n")
    cleaned_df = cleanData(df)
    print("Data cleaned successfully!")

    print("Handling class imbalance...\n")
    balanced_df = handleClassImbalance(cleaned_df)
    print("Class imbalance handled successfully!")


    print("Saving data to SQL database...\n")
    db_url = "sqlite:///customer_churn.db"  # SQLite database
    save_to_sql(cleaned_df, "cleaned_data", db_url)
    save_to_sql(balanced_df, "balanced_data", db_url)

    print("✅ Data pipeline completed successfully!")

# Main function with menu
def main():

    df = None

    while True:
        print("Telco Customer Churn Prediction Model\n")
        print("1. Load Data using Kaggle API")
        print("2. Clean Data")
        print("3. Run Customer Churn Prediction Model")
        print("4. Run Full Data Pipeline")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            downloadData()

            file_path = getFilePath()

            if not os.path.exists(file_path):
                print("Error: Dataset not found. Please check the Kaggle API configuration.")
                df = None
            else:
                df = pd.read_csv(file_path)
                print("Dataset loaded successfully!")

        elif choice == '2':
            if df is None:
                print("Data not loaded. Please load data first.\n")
            else:
                df = cleanData(df)

        elif choice == '3':
            if df is None:
                print("Data not loaded. Please load data first.\n")
            else:
                print("Customer churn prediction functionality is implemented on jupyter notebook, open the file and run it.\n")

        elif choice == '4':

            data_pipeline()  # Run the full data pipeline
        elif choice == '5':

            print("Exiting...\n")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()