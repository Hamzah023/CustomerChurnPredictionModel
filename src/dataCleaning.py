import pandas as pd
from kaggleApi import getFilePath
import os


def cleanData(df: pd.DataFrame) -> pd.DataFrame:

    if df.empty:
        print("Data not loaded. Please check the file.\n")
        return None

    try:
        filePath = getFilePath()
        df = pd.read_csv(filePath)
    except Exception as e:
        print(f"Error loading file: {e}")
        return None
    
    if df.empty:
       print("Data not loaded. Please load data first.\n")
       return None
    else:

        required_columns = ["TotalCharges", "customerID"]
        for col in required_columns:
            if col not in df.columns:
                print(f"Missing required column: {col}")
                return None
            
        print("Data loaded successfully!")

        print("\ndataset summary information: \n")
        print(df.info()) #df.info() is used to display the summary of the dataframe

        print("\nsummary statistics of the dataframe:\n")
        print(df.describe()) #df.describe() is used to display the summary statistics of the dataframe

        print("\ncolumn names, number of rows and columns, missing values, data types, unique values and frequency of each unique value in the 'TotalCharges' column: \n")
        print(df.columns) #df.columns is used to display the column names of the dataframe

        print("\nChecking for missing values in each column:")
        print(df.isnull().sum(), "\n") #df.isnull().sum() is used to display the number of missing values in each column of the dataframe   

        print("Handling missing values in the 'TotalCharges' column: \n")

        
        #convert 'TotalCharges' column to numeric values
        print("Converting 'TotalCharges' column to numeric values...")
        df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
        
        #count the missing values in the 'TotalCharges' column
        missingVals = df["TotalCharges"].isnull().sum()

        print("Missing values in the 'TotalCharges' column: \n")
        print(missingVals, "\n")

        #replace missing values with 0
        df["TotalCharges"] = df["TotalCharges"].fillna(0)

        # Verify the changes
        print(f"Total unique values in 'TotalCharges': {df['TotalCharges'].nunique()}")
        print("Sample unique values:", df["TotalCharges"].unique()[:10])

        print("Top 5 most common values in 'TotalCharges':")

        print(df["TotalCharges"].value_counts().head())

        # Ensure 'TotalCharges' is of type float
        df["TotalCharges"] = df["TotalCharges"].astype(float)

        print("\n Statistical analysis of 'TotalCharges':")
        print(f"Mean: {df['TotalCharges'].mean()}")
        print(f"Median: {df['TotalCharges'].median()}")
        print(f"Mode: {df['TotalCharges'].mode()[0]}") # the 0 index is used to get the first mode value
        print(f"Standard Deviation: {df['TotalCharges'].std()}")
        print(f"Minimum: {df['TotalCharges'].min()}")
        print(f"Maximum: {df['TotalCharges'].max()}")
        print(f"Missing values: {df['TotalCharges'].isnull().sum()}\n")

        print("Final summary statistics for 'TotalCharges':")
        print(df['TotalCharges'].describe(), "\n")

   #convert categorical columns to numerical
    categoricalCols = ["gender", "Partner", "Dependents", "PhoneService", "MultipleLines",
                        "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection",
                        "TechSupport", "StreamingTV", "StreamingMovies", "Contract",
                        "PaperlessBilling", "PaymentMethod"]
   
    categoricalCols = [col for col in categoricalCols if col in df.columns] #check if the column exists in the dataframe before converting it to numerical
    df = pd.get_dummies(df, columns=categoricalCols) #convert categorical columns to numerical using one-hot encoding
    print("Converted categorical columns to numerical using one-hot encoding.\n")
    print(df.head())

   #drop unnecessary columns
    df.drop(["customerID"], axis=1, inplace=True) #drop 'customerID' column, axis 1 means that we are dropping a column
    print("\nDropped 'customerID' column.\n")
   

   #check for duplicate rows
    df.drop_duplicates(inplace=True) #drop duplicate rows in the dataframe, the inplace parameter is true to make the changes permanent
    print(df.head())

    OUTPUT_DIR = '../data'
    if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

    cleaned_file_path = os.path.join(OUTPUT_DIR, "cleaned_telco_data.csv")
    df.to_csv(cleaned_file_path, index=False) #save cleaned data to a new file
    print(f"✅ Cleaned dataset saved at: {cleaned_file_path}\n")

    print("Data cleaning completed!\n")

    return df


   
   




