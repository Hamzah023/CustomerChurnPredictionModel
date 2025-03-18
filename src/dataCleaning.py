import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os
import logging

logging.basicConfig(level=logging.INFO)

def cleanData(df: pd.DataFrame) -> pd.DataFrame:

    if df.empty:
        logging.error("Data not loaded. Please check the file.")
        raise ValueError("Data not loaded. Please check the file.")

    # Ensure required columns exist
    required_columns = ["TotalCharges", "customerID"]
    for col in required_columns:
        if col not in df.columns:
            logging.error(f"Missing required column: {col}")
            raise ValueError(f"Missing required column: {col}")

    logging.info("Data loaded successfully!")

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

    # Dynamically identify categorical columns
    categoricalCols = df.select_dtypes(include=['object', 'category']).columns.tolist()

    excludeCols = ['customerID'] 
    categoricalCols = [col for col in categoricalCols if col not in excludeCols]

    # Check if there are any categorical columns to encode
    if categoricalCols:
        print(f"Categorical columns identified for one-hot encoding: {categoricalCols}")
        # Apply one-hot encoding
        df = pd.get_dummies(df, columns=categoricalCols)
        print("\nConverted categorical columns to numerical using one-hot encoding.\n")
        print(df.head())
    else:
        print("No categorical columns found for one-hot encoding.")


   #drop unnecessary columns
    df.drop(["customerID"], axis=1, inplace=True) #drop 'customerID' column, axis 1 means that we are dropping a column
    print("\nDropped 'customerID' column.\n")
   

   #check for duplicate rows
    df.drop_duplicates(inplace=True) #drop duplicate rows in the dataframe, the inplace parameter is true to make the changes permanent
    print(df.head())

    # Check for non-numeric or missing values in TotalCharges
    print("\nThis should be 0 if there are no non-numeric or missing values in TotalChange: ", df['TotalCharges'].isnull().sum())  # Should be 0

    #Check for the data type of the TotalCharges column

    print("The data type of the totalChange column: ",df['TotalCharges'].dtype, "\n")  # Should be float64 or int64

    # Check for inconsistencies in binary columns
    print("this should be 0: ", (df['gender_Female'] & df['gender_Male']).sum())  # Should be 0
    print("this should be 0: ", (~df['gender_Female'] & ~df['gender_Male']).sum(), "\n")  # Should be 0

    # Check for inconsistencies in Churn columns
    print("this should be 0: ", (df['Churn_No'] & df['Churn_Yes']).sum())  # Should be 0
    print("this should be 0: ", (~df['Churn_No'] & ~df['Churn_Yes']).sum(), "\n")  # Should be 0

    #check for missing values after cleaning
    print("Missing values after cleaning: ")
    print(df.isnull().sum())

    print("check the data types of the columns after cleaning:\n ")
    print(df.dtypes)

    scaler = MinMaxScaler() #A MinMaxScaler is used to scale the data to a specified range, in this case, between 0 and 1
    df[['tenure',
    'MonthlyCharges',
    'TotalCharges']] = scaler.fit_transform(df[['tenure',
    'MonthlyCharges',
    'TotalCharges']])
    print("\nScaled 'tenure', 'MonthlyCharges', and 'TotalCharges' columns.\n")

    # Ensure no inconsistencies in binary columns
    if 'gender_Female' in df.columns and 'gender_Male' in df.columns:
        assert (df['gender_Female'] & df['gender_Male']).sum() == 0, "Inconsistency found in gender columns!"
        assert (~df['gender_Female'] & ~df['gender_Male']).sum() == 0, "Inconsistency found in gender columns!"

    if 'Churn_No' in df.columns and 'Churn_Yes' in df.columns:
        assert (df['Churn_No'] & df['Churn_Yes']).sum() == 0, "Inconsistency found in Churn columns!"
        assert (~df['Churn_No'] & ~df['Churn_Yes']).sum() == 0, "Inconsistency found in Churn columns!"

    # Dynamically drop redundant columns
    columns_to_drop = []
    if 'gender_Male' in df.columns and 'gender_Female' in df.columns:
        columns_to_drop.append('gender_Male')
    if 'Churn_No' in df.columns and 'Churn_Yes' in df.columns:
        columns_to_drop.append('Churn_No')

    df.drop(columns=columns_to_drop, inplace=True)
    print("Dropped redundant columns:", columns_to_drop)
        # Dynamically identify redundant columns to drop
    columns_to_drop = []

    if 'gender_Male' in df.columns and 'gender_Female' in df.columns:
        columns_to_drop.append('gender_Male')

    if 'Churn_No' in df.columns and 'Churn_Yes' in df.columns:
        columns_to_drop.append('Churn_No')

    # Drop the identified columns
    df.drop(columns=columns_to_drop, inplace=True)
    print("Dropped redundant columns:", columns_to_drop)

    OUTPUT_DIR = '../data'
    if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

    cleaned_file_path = os.path.join(OUTPUT_DIR, "cleaned_telco_data.csv")
    df.to_csv(cleaned_file_path, index=False) #save cleaned data to a new file
    print(f"✅ Cleaned dataset saved at: {cleaned_file_path}\n")

    print("Data cleaning completed!\n")

    return df


   
   




