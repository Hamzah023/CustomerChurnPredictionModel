import pandas as pd
from kaggleApi import getFilePath
import os


def cleanData(data):
   print("Cleaning data...\n")

   filePath = getFilePath()
   df = pd.read_csv(filePath)

   if data is None:
       print("Data not loaded. Please load data first.\n")
       return None
   else:
        print("Data loaded successfully!")
        print(df.head()) #df.head() is used to display the first 5 rows of the dataframe
        print(df.info()) #df.info() is used to display the summary of the dataframe
        print(df.describe()) #df.describe() is used to display the summary statistics of the dataframe
        print(df.columns) #df.columns is used to display the column names of the dataframe
        print(df.shape) #df.shape is used to display the number of rows and columns in the dataframe
        print(df.isnull().sum()) #df.isnull().sum() is used to display the number of missing values in each column of the dataframe   
        print(df.dtypes) #df.dtypes is used to display the data types of each column in the dataframe
        print(df['TotalCharges'].unique()) #df['TotalCharges'].unique() is used to display the unique values in the 'TotalCharges' column
        print(df['TotalCharges'].value_counts()) #df['TotalCharges'].value_counts() is used to display the frequency of each unique value in the 'TotalCharges' column
        print(df['TotalCharges'].replace(' ', 0, inplace=True))
        print(df['TotalCharges'].dtype)
        df['TotalCharges'] = df['TotalCharges'].astype(float)
        print(df['TotalCharges'].mean())
        print(df['TotalCharges'].median())
        print(df['TotalCharges'].mode())
        print(df['TotalCharges'].std())
        print(df['TotalCharges'].min())
        print(df['TotalCharges'].max())
        print(df['TotalCharges'].isnull().sum())
        print(df['TotalCharges'].fillna(df['TotalCharges'].mean(), inplace=True))
        print(df['TotalCharges'].isnull().sum())
        print(df['TotalCharges'].describe())
    
    #handle missing values
   df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce') #convert 'TotalCharges' column to numeric values
   df["TotalCharges"].fillna(df["TotalCharges"].mean(), inplace=True) #fill missing values in 'TotalCharges' column with the mean value
   
   print("Handled missing values.\n")
   print("Missing values check in the dataframe returns: f'{df.isnull().sum()}\n") #check for missing values in the dataframe

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
   print("Dropped 'customerID' column.\n")
   

   #check for duplicate rows
   df.drop_duplicates(inplace=True) #drop duplicate rows in the dataframe, the inplace parameter is true to make the changes permanent
   print("Dropped duplicate rows.\n")
   print(df.head())

   OUTPUT_DIR = '../data'
   cleaned_file_path = os.path.join(OUTPUT_DIR, "cleaned_telco_data.csv")
   df.to_csv(cleaned_file_path, index=True) #save cleaned data to a new file
   print(f"✅ Cleaned dataset saved at: {cleaned_file_path}\n")

   print("Data cleaning completed!\n")
   
   return df
   

   
   




