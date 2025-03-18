import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os
import logging
from imblearn.over_sampling import SMOTE

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


    print("\ndataset summary information: \n")
    print(df.info()) #df.info() is used to display the summary of the dataframe

    print("\nsummary statistics of the dataframe:\n")
    print(df.describe()) #df.describe() is used to display the summary statistics of the dataframe


    print("\nChecking for missing values in each column:")
    print(df.isnull().sum(), "\n") #df.isnull().sum() is used to display the number of missing values in each column of the dataframe  

    # Dynamically identify binary columns
    binary_columns = [col for col in df.columns if df[col].nunique() == 2]
    print(f"Binary columns identified: {binary_columns}")


    # Convert boolean columns to integers
    boolean_columns = df.select_dtypes(include=['bool']).columns

    if len(boolean_columns) > 0:

        df[boolean_columns] = df[boolean_columns].astype(int)
        print(f"Converted boolean columns to integers: {boolean_columns.tolist()}")

    print("Handling missing values in the 'TotalCharges' column: \n")

    # Convert 'TotalCharges' column to numeric values
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce') #pd.to_numeric() is used to convert the 'TotalCharges' column to numeric values
    missing_vals_before = df['TotalCharges'].isnull().sum()

    df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median()) #fill the missing values in the 'TotalCharges' column with the median value
    missing_vals_after = df['TotalCharges'].isnull().sum()

    logging.info(f"Missing values in 'TotalCharges': Before = {missing_vals_before}, After = {missing_vals_after}")

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

    else:
        print("No categorical columns found for one-hot encoding.")

    # Dynamically identify redundant columns to drop
    columns_to_drop = []
    if 'gender_Male' in df.columns and 'gender_Female' in df.columns:
        columns_to_drop.append('gender_Male')

    if 'Churn_No' in df.columns and 'Churn_Yes' in df.columns:
        columns_to_drop.append('Churn_No')

    if 'Partner_No' in df.columns:
        columns_to_drop.append('Partner_No')

    if columns_to_drop:

        df.drop(columns=columns_to_drop, inplace=True)
        print("Dropped redundant columns:", columns_to_drop)

    # Drop unnecessary columns
    if 'customerID' in df.columns:

        df.drop(["customerID"], axis=1, inplace=True)
        print("\nDropped 'customerID' column.\n")

    # Check for duplicate rows and log the number of duplicates dropped
    initial_row_count = df.shape[0]
    df.drop_duplicates(inplace=True)
    final_row_count = df.shape[0]
    logging.info(f"Dropped {initial_row_count - final_row_count} duplicate rows.")

    # Validate columns before scaling
    scaling_columns = ['tenure', 'MonthlyCharges', 'TotalCharges']
    scaling_columns = [col for col in scaling_columns if col in df.columns]
    
    if scaling_columns:
        scaler = MinMaxScaler()
        df[scaling_columns] = scaler.fit_transform(df[scaling_columns]) #fit_transform() is used to scale the data to a specified range which is 0 to 1 in this case
        print(f"\nScaled columns: {scaling_columns}\n")
    else:
        print("No columns found for scaling.")

    # Ensure no inconsistencies in binary columns
    if 'gender_Female' in df.columns and 'gender_Male' in df.columns:
        assert (df['gender_Female'] & df['gender_Male']).sum() == 0, "Inconsistency found in gender columns!" #assert is used to check if the condition is true, if not it raises an error

        assert (~df['gender_Female'] & ~df['gender_Male']).sum() == 0, "Inconsistency found in gender columns!"

    if 'Churn_No' in df.columns and 'Churn_Yes' in df.columns:
        assert (df['Churn_No'] & df['Churn_Yes']).sum() == 0, "Inconsistency found in Churn columns!"

        assert (~df['Churn_No'] & ~df['Churn_Yes']).sum() == 0, "Inconsistency found in Churn columns!"

        
    #checking the distribution of Churn_Yes and apply balancing techniques if needed
    print("Checking the distribution of Churn_Yes: \n")
    print(df['Churn_Yes'].value_counts())

    #convert boolean columns to integer values
    print("\nConverting boolean columns to integer values: \n")
    df = df.astype({col: 'int' for col in df.select_dtypes(include=['bool']).columns})


    OUTPUT_DIR = '../data'
    if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

    cleaned_file_path = os.path.join(OUTPUT_DIR, "cleaned_telco_data.csv")

    df.to_csv(cleaned_file_path, index=False) #save cleaned data to a new file
    print(f"✅ Cleaned dataset saved at: {cleaned_file_path}\n")

    print("Data cleaning completed!\n")

    return df


   
   




