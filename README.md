# Telco Customer Churn Prediction Model

##📋 Project Overview
The Telco Customer Churn Prediction Model is a machine learning pipeline designed to predict customer churn for a telecommunications company. The project includes data cleaning, handling class imbalance, training a machine learning model, and exporting the processed data to a database for further analysis and visualization. The final insights can be visualized using tools like Power BI or Tableau.

---

## 🚀 Features
Data Download: Automatically downloads the dataset from Kaggle using the Kaggle API.
Data Cleaning: Handles missing values, encodes categorical variables, scales numerical features, and removes duplicates.
Class Imbalance Handling: Uses SMOTE (Synthetic Minority Oversampling Technique) to balance the dataset.
Model Training: Trains a Random Forest Classifier to predict customer churn.
Model Performance: Evaluates the model using metrics such as accuracy, precision, recall, and F1-score.
Database Integration: Saves cleaned and balanced data to an SQLite database (customer_churn.db).
Visualization: Supports integration with Power BI or other visualization tools for creating dashboards.

---

##🧠 Model Performance
The Random Forest Classifier achieved the following performance metrics on the test dataset:

Confusion Matrix
Predicted No Churn (0)	Predicted Churn (1)
Actual No Churn (0)	840	194
Actual Churn (1)	136	896
Classification Report
Metric	Class 0 (No Churn)	Class 1 (Churn)	Macro Avg	Weighted Avg
Precision	0.86	0.82	0.84	0.84
Recall	0.81	0.87	0.84	0.84
F1-Score	0.84	0.84	0.84	0.84
Accuracy				84%

## 🛠️ How It Works
Download Data:

The dataset is downloaded from Kaggle using the Kaggle API.
The file is saved in the data directory as WA_Fn-UseC_-Telco-Customer-Churn.csv.

Data Cleaning:

Missing values in the TotalCharges column are filled with the median.
Categorical columns are one-hot encoded.
Redundant columns (e.g., gender_Male, Partner_No) are dropped to avoid multicollinearity.
Numerical columns (tenure, MonthlyCharges, TotalCharges) are scaled using Min-Max Scaling.

Class Imbalance Handling:

The dataset is balanced using SMOTE, which generates synthetic samples for the minority class (Churn_Yes).

Model Training:

A Random Forest Classifier is trained on the balanced dataset to predict customer churn.

Save to Database:

The cleaned and balanced datasets are saved to an SQLite database (customer_churn.db) with two tables:
cleaned_data: Contains the cleaned dataset.
balanced_data: Contains the balanced dataset.
Visualization:

The SQLite database can be connected to Power BI, Tableau, or other tools for creating dashboards.

---

## 📂 Project Structure
CustomerChurnPredictionModel/
├── data/                     # Directory for storing the dataset
│   ├── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   ├── cleaned_telco_data.csv
│   ├── balanced_telco_data.csv
├── docs/                     # Documentation files
│   └── documentation.txt
├── src/                      # Source code
│   ├── main.py               # Main script with the data pipeline and menu
│   ├── kaggleApi.py          # Script to download data using Kaggle API
│   ├── dataCleaning.py       # Script for cleaning the dataset
│   ├── handleClassImbalance.py # Script for handling class imbalance using SMOTE
│   ├── customerChurnPredictionModel.ipynb # Jupyter Notebook for model training
├── models/                   # Directory for storing trained models
│   └── churn_prediction_model.pkl
├── customer_churn.db         # SQLite database (created after running the pipeline)
└── README.md                 # Project documentation

---

## 🖥️ How to Run the Project

###Prerequisites
1. Python 3.8+ installed on your system.
2. Install the required Python libraries:
   
pip install pandas scikit-learn imbalanced-learn matplotlib seaborn

Set up the Kaggle API:
Download your Kaggle API key (kaggle.json) from your Kaggle account.
Place the file in ~/.kaggle/ (Linux/Mac) or %USERPROFILE%\.kaggle\ (Windows).

Steps to Run
Clone the repository:
git clone <repository_url>
cd CustomerChurnPredictionModel

Run the main script:
python src/main.py

Follow the menu options:

Option 1: Download the dataset using Kaggle API.
Option 2: Clean the dataset.
Option 3: Run the customer churn prediction model (placeholder).
Option 4: Run the full data pipeline (downloads, cleans, balances, and saves data to SQLite).
Option 5: Exit the program.
🧠 Key Concepts Used

Min-Max Scaling:
    Rescales numerical features to a range of [0, 1].
    Formula:
    X' = (X - X_min) / (X_max - X_min)

One-Hot Encoding:
    Converts categorical variables into binary columns.
    
SMOTE (Synthetic Minority Oversampling Technique):
    Balances the dataset by generating synthetic samples for the minority class.
    
SQLite:
    Lightweight, file-based database for storing cleaned and balanced data.

Random Forest Classification for Churn Prediction

The Random Forest Classification algorithm is an ensemble learning method that uses multiple decision trees to predict whether a customer will churn (e.g., Churn = Yes or Churn = No). It works by combining the predictions of individual decision trees to improve accuracy and reduce overfitting.

How It Works
Bootstrap Sampling:
   Random subsets of the training data are created using sampling with replacement.
   Each subset is used to train a separate decision tree.
   
Feature Randomness:
   At each split in a decision tree, only a random subset of features is considered to reduce correlation between trees.
   
Training Decision Trees:
   Each decision tree is trained independently on its respective subset of data.
   The trees learn to classify customers as Churn = Yes or Churn = No.
   
Prediction Aggregation:

   For a new customer, each tree predicts a class (Yes or No).
   The final prediction is made by majority voting (the class predicted by the most trees).
   
Advantages for Churn Prediction
Handles Imbalanced Data:
   Works well with techniques like SMOTE to balance the dataset before training.
Feature Importance:
   Identifies which features (e.g., tenure, MonthlyCharges) are most important for predicting churn.
Robustness:
   Reduces overfitting by averaging predictions from multiple trees.
Nonlinear Relationships:
   Captures complex patterns in customer behavior.

Steps in Churn Prediction
Data Preparation:
   Clean the dataset (handle missing values, encode categorical variables, scale numerical features).
   Balance the dataset using SMOTE to address class imbalance.

Train the Random Forest Model:
   Use the balanced dataset to train the model.
   Example: RandomForestClassifier(n_estimators=100, random_state=42).
   
Evaluate the Model:
   Use metrics like accuracy, precision, recall, F1-score, and a confusion matrix to assess performance.
   Example:
   Accuracy: 84%
   Precision (Churn): 82%
   Recall (Churn): 87%
   F1-Score (Churn): 84%
   
Make Predictions:
   Predict whether a customer will churn based on their features (e.g., tenure, MonthlyCharges, TotalCharges).
   
Why Random Forest is Effective for Churn
   Handles High-Dimensional Data: Works well with datasets containing many features.
   Reduces Overfitting: Combines multiple trees to generalize better on unseen data.
   Interpretable: Provides feature importance scores to understand key drivers of churn.

🛠️ Future Enhancements
Add support for other databases like PostgreSQL or MySQL.
Automate Power BI dashboard refresh using cloud services.
