# 📊 Telco Customer Churn Prediction Model

## 📝 Project Overview
The Telco Customer Churn Prediction Model is an end-to-end machine learning pipeline designed to predict customer churn for a telecommunications company. It covers data cleaning, class imbalance handling, model training, and database storage, with final insights visualized using tools like **Power BI** or **Tableau**.

---

## 🚀 Features
- **Data Download:** Automatically downloads the dataset from **Kaggle** using the Kaggle API.
- **Data Cleaning:** Handles missing values, encodes categorical variables, scales numerical features, and removes duplicates.
- **Class Imbalance Handling:** Uses **SMOTE (Synthetic Minority Oversampling Technique)** to balance the dataset.
- **Model Training:** Trains a **Random Forest Classifier** to predict customer churn.
- **Performance Evaluation:** Analyzes accuracy, precision, recall, and F1-score.
- **Database Integration:** Saves the processed data into an **SQLite** database.
- **Visualization:** Supports integration with **Power BI** or **Tableau** for creating dashboards.

---

## 🧠 Model Performance
The **Random Forest Classifier** achieved the following performance metrics on the test dataset:

| Metric            | Class 0 (No Churn) | Class 1 (Churn) | Macro Avg | Weighted Avg |
|--------------------|--------------------|-----------------|-----------|--------------|
| **Precision**      | 0.86               | 0.82            | 0.84      | 0.84         |
| **Recall**         | 0.81               | 0.87            | 0.84      | 0.84         |
| **F1-Score**       | 0.84               | 0.84            | 0.84      | 0.84         |
| **Accuracy**       | -                  | -               | -         | **84%**      |

**Confusion Matrix:**
|                   | Predicted No Churn (0) | Predicted Churn (1) |
|-------------------|------------------------|---------------------|
| **Actual No Churn (0)** | 840                    | 194                 |
| **Actual Churn (1)**   | 136                    | 896                 |

---

## 🛠️ How It Works
### **1. Download Data**
- Automatically downloads the dataset from **Kaggle** using the API.
- Saved as `WA_Fn-UseC_-Telco-Customer-Churn.csv`.

### **2. Data Cleaning**
- Fills missing values with the median.
- Applies **One-Hot Encoding** for categorical variables.
- Uses **Min-Max Scaling** for numerical columns.

### **3. Class Imbalance Handling**
- Uses **SMOTE** to generate synthetic samples for the minority class (Churn).

### **4. Model Training**
- Trains a **Random Forest Classifier** using the balanced data.

### **5. Save to Database**
- Saves both the cleaned and balanced datasets to an **SQLite** database (`customer_churn.db`).

### **6. Visualization**
- Connect to the database using **Power BI** or **Tableau** to create dashboards.

---

## 📂 Project Structure
```
CustomerChurnPredictionModel/
├── data/
│   ├── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   ├── cleaned_telco_data.csv
│   ├── balanced_telco_data.csv
├── docs/
│   └── documentation.txt
├── src/
│   ├── main.py
│   ├── kaggleApi.py
│   ├── dataCleaning.py
│   ├── handleClassImbalance.py
│   ├── customerChurnPredictionModel.ipynb
├── models/
│   └── churn_prediction_model.pkl
├── customer_churn.db
└── README.md
```

---

## 🖥️ How to Run the Project
### **Prerequisites**
- Python 3.8+ installed
- Install required libraries using:
```bash
pip install pandas scikit-learn imbalanced-learn matplotlib seaborn SQLAlchemy
```
- Set up the **Kaggle API**:
  - Download your `kaggle.json` API key from Kaggle.
  - Place it in `~/.kaggle/` (Linux/Mac) or `%USERPROFILE%\.kaggle\` (Windows).

### **Run the Project**
1. Clone the repository:
```bash
git clone <repository_url>
cd CustomerChurnPredictionModel
```

2. Run the main script:
```bash
python src/main.py
```
3. Follow the menu options:
- **Option 1:** Download data using Kaggle API.
- **Option 2:** Clean the data.
- **Option 3:** Train the churn prediction model.
- **Option 4:** Run the complete pipeline (download, clean, balance, save).
- **Option 5:** Exit.

---

## 🧑‍💻 Key Concepts Used
- **Min-Max Scaling:**
  - Rescales numerical features to a range of [0, 1].
  - Formula:
  \[ X' = \frac{X - X_{min}}{X_{max} - X_{min}} \]

- **One-Hot Encoding:**
  - Converts categorical variables into binary columns.

- **SMOTE:**
  - Balances class distribution by generating synthetic samples for the minority class.

- **SQLite:**
  - File-based database to store processed data.

---

## 🌟 Future Enhancements
- Add support for **PostgreSQL** or **MySQL**.
- Implement automated Power BI dashboard refresh using cloud services.

---

## 📧 Contact
For any questions or collaboration opportunities, feel free to reach out!

- **GitHub:** [Your GitHub Profile](https://github.com/Hamzah023)
- **LinkedIn:** [Your LinkedIn Profile](#)

