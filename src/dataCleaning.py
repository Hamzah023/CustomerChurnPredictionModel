import pandas as pd
from kaggleApi import getFilePath
import os


def cleanData(data):

   filePath = getFilePath()
   df = pd.read_csv(filePath)

   if data is None:
       print("Data not loaded. Please load data first.\n")
       return None
   else:
        print("Data loaded successfully!")

        print("the first 5 rows of the dataframe are: \n")
        print(df.head()) #df.head() is used to display the first 5 rows of the dataframe

        print("\ndataset summary information: \n")
        print(df.info()) #df.info() is used to display the summary of the dataframe

        print("\nsummary statistics of the dataframe:\n")
        print(df.describe()) #df.describe() is used to display the summary statistics of the dataframe

        print("\ncolumn names, number of rows and columns, missing values, data types, unique values and frequency of each unique value in the 'TotalCharges' column: \n")
        print(df.columns) #df.columns is used to display the column names of the dataframe

        print("\nDataset shape (rows, columns):")
        print(df.shape, "\n") #df.shape is used to display the number of rows and columns in the dataframe

        print("\nChecking for missing values in each column:")
        print(df.isnull().sum(), "\n") #df.isnull().sum() is used to display the number of missing values in each column of the dataframe   

        print("Data types of each column:")
        print(df.dtypes, "\n") #df.dtypes is used to display the data types of each column in the dataframe

        print("Unique values in the 'TotalCharges' column:")
        print(df['TotalCharges'].unique(), "\n") #df['TotalCharges'].unique() is used to display the unique values in the 'TotalCharges' column

        print("Frequency of each unique value in the 'TotalCharges' column:")
        print(df['TotalCharges'].value_counts(), "\n") #df['TotalCharges'].value_counts() is used to display the frequency of each unique value in the 'TotalCharges' column
        

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
        print("Unique values in the 'TotalCharges' column after handling missing values: \n")
        print(df["TotalCharges"].unique(), "\n")

        print("Frequency of each unique value in the 'TotalCharges' column after handling missing values: \n")
        print(df["TotalCharges"].value_counts(), "\n")


        #convert 'TotalCharges' column to numeric values
        df['TotalCharges'] = df['TotalCharges'].replace(' ', 0)#this code replaces empty ,strings with 0 in the 'TotalCharges' column, in place parameter is set to true to make the changes permanent

        print("Unique values in the 'TotalCharges' column after replacing empty strings with 0: \n")
        print(df['TotalCharges'], "\n")

        print("Data type of the 'TotalCharges' column: ")
        print(df['TotalCharges'].dtype, "\n") #this code displays the data type of the 'TotalCharges' column

        df['TotalCharges'] = pd.to_numeric(df['TotalCharges']) #this code converts the 'TotalCharges' column to numeric data type


        print("Data type of the 'TotalCharges' column after conversion: ")
        print(df['TotalCharges'].dtype, "\n") #this code displays the data type of the 'TotalCharges' column after conversion


        df['TotalCharges'] = df['TotalCharges'].astype(float) #this code converts the 'TotalCharges' column to float data type

        print("\n Statistical analysis of 'TotalCharges':")
        print(f"Mean: {df['TotalCharges'].mean()}")
        print(f"Median: {df['TotalCharges'].median()}")
        print(f"Mode: {df['TotalCharges'].mode()[0]}") # the 0 index is used to get the first mode value
        print(f"Standard Deviation: {df['TotalCharges'].std()}")
        print(f"Minimum: {df['TotalCharges'].min()}")
        print(f"Maximum: {df['TotalCharges'].max()}")
        print(f"Missing values: {df['TotalCharges'].isnull().sum()}\n")

        print(" Filling missing values in 'TotalCharges' with the mean...")
        missing_before = df["TotalCharges"].isnull()
        df['TotalCharges'].fillna(df['TotalCharges'].mean()) #fill missing values in the 'TotalCharges' column with the mean value
        #print the 

        print("Values filled with the mean value in the Total Charges Collumn: \n")
        print(df.loc[missing_before, "TotalCharges"], "\n")
        

        print("Final summary statistics for 'TotalCharges':")
        print(df['TotalCharges'].describe(), "\n")

    #handle missing values
   df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce') #convert 'TotalCharges' column to numeric values
   df["TotalCharges"].fillna(df["TotalCharges"].mean()) #fill missing values in 'TotalCharges' column with the mean value
   
   print("\n")
   print(f"Missing values check in the dataframe returns:\n{df.isnull().sum()}\n") #check for missing values in the dataframe

   #convert categorical columns to numerical
   categoricalCols = ["gender", "Partner", "Dependents", "PhoneService", "MultipleLines",
                        "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection",
                        "TechSupport", "StreamingTV", "StreamingMovies", "Contract",
                        "PaperlessBilling", "PaymentMethod"]
   
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
   df.to_csv(cleaned_file_path, index=True) #save cleaned data to a new file
   print(f"✅ Cleaned dataset saved at: {cleaned_file_path}\n")

   print("Data cleaning completed!\n")

   return df
   

   
   




