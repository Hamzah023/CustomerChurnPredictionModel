# Customer Churn Prediction Model & Data Pipeline

## Overview

This project predicts customer churn and visualizes the insights in an interactive Power BI dashboard. It involves building a data pipeline that automates the process from data downloading, cleaning, and transformation to model training and visualization.

The workflow consists of the following steps:
1. **Download the Data**: Automatically fetch the customer churn dataset from Kaggle.
2. **Data Cleaning & Preprocessing**: Clean and preprocess the data using Python (Pandas).
3. **Store Cleaned Data in SQL**: Save the cleaned data into an SQL database.
4. **Data Transformation**: Use Power Query in Excel to transform the data for analysis.
5. **Customer Churn Prediction**: Train a machine learning model (e.g., Random Forest) to predict customer churn.
6. **Create Power BI Dashboards**: Use Power BI to visualize insights and create interactive dashboards.
7. **Automate the Pipeline**: Set up automation to run the pipeline daily for fresh data.

## Technologies

- **Python (Pandas)**: Data cleaning, feature engineering, and machine learning model training.
- **SQL Database**: Storing cleaned data for further transformation and analysis.
- **Power Query (Excel)**: Data transformation and cleaning in Excel.
- **Power BI**: Creating interactive dashboards and visualizing the churn prediction results.
- **Kaggle API**: Automating the data download from Kaggle.
- **SQLAlchemy**: Connecting Python to SQL databases for data storage.
- **Scikit-learn**: Machine learning model training and evaluation.

## Prerequisites

Before running this project, you will need to set up the following:

1. **Python (3.x)**: Install the necessary Python libraries using `pip`.
    ```bash
    pip install pandas sqlalchemy scikit-learn kaggle
    ```

2. **Kaggle API Key**: To download the dataset from Kaggle, you need to set up your Kaggle API key. Follow the steps [here](https://www.kaggle.com/docs/api) to obtain the key and set it up in your environment.

3. **SQL Database**: You need an SQL database to store the cleaned data. This project uses PostgreSQL, but you can adapt it for other databases (MySQL, SQLite, etc.).

4. **Power BI**: Available for Windows. For macOS, you can use Power BI Web for visualization.

5. **Excel with Power Query**: Power Query is available in Excel for Mac and Windows and can be used for transforming the data.

## Project Structure

. ├── data/ # Folder for raw and cleaned data │ └── churn_data.csv # Raw churn dataset ├── scripts/ # Python scripts for automation │ ├── data_cleaning.py # Data cleaning and preprocessing │ ├── model_training.py # Machine learning model training │ └── download_data.py # Script to download data from Kaggle ├── notebooks/ # Jupyter Notebooks for analysis (optional) ├── README.md # This file └── requirements.txt # List of Python dependencies

python
Copy
Edit

## Step-by-Step Guide to Run the Project

### 1. Download Data from Kaggle

To begin, download the dataset from Kaggle using the Kaggle API.

- **Install Kaggle API**:
    ```bash
    pip install kaggle
    ```

- **Download Dataset**:
    Create a Python script (`download_data.py`) to automatically download the dataset:

    ```python
    from kaggle.api.kaggle_api_extended import KaggleApi

    api = KaggleApi()
    api.authenticate()

    # Replace 'dataset-name' with the actual dataset name on Kaggle
    api.dataset_download_files('dataset-name', path='./data', unzip=True)
    ```

This will download and unzip the dataset into the `data/` folder.

### 2. Data Cleaning and Preprocessing with Python (Pandas)

Once the data is downloaded, load it into a pandas DataFrame and clean it:

- **Preprocessing**: Handle missing values, encode categorical variables, and perform feature engineering.
- **Save to SQL**: Use SQLAlchemy to connect to the SQL database and save the cleaned data.

Here is an example of how you can clean the data and save it:

```python
import pandas as pd
from sqlalchemy import create_engine

# Load and clean the data
df = pd.read_csv('data/churn_data.csv')
df.dropna(inplace=True)  # Handle missing values
df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})  # Encode categorical columns

# Create SQLAlchemy engine to connect to your database
engine = create_engine('postgresql://user:password@localhost:5432/mydatabase')

# Save cleaned data to SQL
df.to_sql('churn_data', engine, if_exists='replace', index=False)
This script will save the cleaned data to your SQL database.

3. Data Transformation with Power Query in Excel
Open Excel and navigate to Data > Get Data > From SQL Server.
Connect to your SQL database and import the cleaned churn data.
Use Power Query to apply any necessary transformations (e.g., filtering, grouping).
Once the data is transformed, load it into Excel for further analysis.
4. Customer Churn Prediction Model
You can now build a machine learning model to predict customer churn. Split the data into training and testing sets, train the model, and evaluate its performance.

Here’s an example of how to train and evaluate a Random Forest model:

python
Copy
Edit
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Split data into features and labels
X = df.drop('churn', axis=1)
y = df['churn']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Model prediction
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy}')
5. Create Power BI Dashboards
Connect Power BI to SQL Database: In Power BI, connect to the SQL database where the cleaned data is stored.
Create Visualizations: Use Power BI’s built-in tools to create bar charts, pie charts, and line graphs to visualize customer churn patterns and predictions.
Build Interactive Dashboards: Build interactive dashboards to explore churn trends, customer demographics, and predictive insights.
6. Automate the Data Pipeline
To automate the process:

Set up a cron job (on macOS or Linux) or Task Scheduler (on Windows) to run the data download and cleaning scripts periodically.
Schedule the Python scripts to run daily and update the database with fresh data.
Example cron job:

bash
Copy
Edit
0 0 * * * /usr/bin/python3 /path/to/your/script.py
7. Visualizing the Churn Prediction in Power BI
Import the cleaned and transformed data from SQL into Power BI.
Create interactive visualizations to display churn rates, key metrics, and other insights.
Design a dashboard that shows insights like:
Total churn rate
Predictive churn probabilities
Customer segment breakdown
Future Improvements
Hyperparameter Tuning: Improve model performance by tuning the machine learning model.
Advanced Models: Implement more advanced algorithms like XGBoost, Neural Networks, etc.
Real-time Data Integration: Set up real-time data processing for continuous monitoring of churn.
Deployment: Deploy the churn prediction model as an API for easy access by other applications.
License
This project is open-source and available under the MIT License. See the LICENSE file for more details.

vbnet
Copy
Edit

This markdown file provides a complete, easy-to-copy README for your project. Let me know if you need further adjustments!








