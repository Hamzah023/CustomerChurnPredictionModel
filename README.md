# Telco Customer Churn Prediction Model

## 📋 Project Overview
The **Telco Customer Churn Prediction Model** is a machine learning pipeline designed to predict customer churn for a telecommunications company. The project includes data cleaning, handling class imbalance, and exporting the processed data to a database for further analysis and visualization. The final insights can be visualized using tools like Power BI or Tableau.

---

## 🚀 Features
1. **Data Download**: Automatically downloads the dataset from Kaggle using the Kaggle API.
2. **Data Cleaning**: Handles missing values, encodes categorical variables, scales numerical features, and removes duplicates.
3. **Class Imbalance Handling**: Uses **SMOTE (Synthetic Minority Oversampling Technique)** to balance the dataset.
4. **Database Integration**: Saves cleaned and balanced data to an SQLite database (`customer_churn.db`).
5. **Visualization**: Supports integration with Power BI or other visualization tools for creating dashboards.

---

## 🛠️ How It Works
1. **Download Data**:
   - The dataset is downloaded from Kaggle using the Kaggle API.
   - The file is saved in the `data` directory as `WA_Fn-UseC_-Telco-Customer-Churn.csv`.

2. **Data Cleaning**:
   - Missing values in the `TotalCharges` column are filled with the median.
   - Categorical columns are one-hot encoded.
   - Redundant columns (e.g., `gender_Male`, `Partner_No`) are dropped to avoid multicollinearity.
   - Numerical columns (`tenure`, `MonthlyCharges`, `TotalCharges`) are scaled using Min-Max Scaling.

3. **Class Imbalance Handling**:
   - The dataset is balanced using **SMOTE**, which generates synthetic samples for the minority class (`Churn_Yes`).

4. **Save to Database**:
   - The cleaned and balanced datasets are saved to an SQLite database (`customer_churn.db`) with two tables:
     - `cleaned_data`: Contains the cleaned dataset.
     - `balanced_data`: Contains the balanced dataset.

5. **Visualization**:
   - The SQLite database can be connected to Power BI, Tableau, or other tools for creating dashboards.

---

## 📂 Project Structure
CustomerChurnPredictionModel/ ├── data/ # Directory for storing the dataset │ └── WA_Fn-UseC_-Telco-Customer-Churn.csv ├── docs/ # Documentation files │ └── documentation.txt ├── src/ # Source code │ ├── main.py # Main script with the data pipeline and menu │ ├── kaggleApi.py # Script to download data using Kaggle API │ ├── dataCleaning.py # Script for cleaning the dataset │ ├── handleClassImbalance.py # Script for handling class imbalance using SMOTE ├── customer_churn.db # SQLite database (created after running the pipeline) └── README.md # Project documentation

---

## 🖥️ How to Run the Project

### Prerequisites
1. **Python 3.8+** installed on your system.
2. Install the required Python libraries:
   ```bash
   pip install pandas scikit-learn imbalanced-learn sqlalch
3. Set up the Kaggle API:
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

🛠️ Future Enhancements
Implement the customer churn prediction model using machine learning.
Add support for other databases like PostgreSQL or MySQL.
Automate Power BI dashboard refresh using cloud services.
