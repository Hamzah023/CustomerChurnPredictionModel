import pandas as pd
import os
from imblearn.over_sampling import SMOTE
import pandas as pd

def handleClassImbalance(df: pd.DataFrame) -> pd.DataFrame:

    # Separate features and target
    X = df.drop(columns=['Churn_Yes']) 
    y = df['Churn_Yes']

    # Apply SMOTE to balance the dataset
    print("\nApplying SMOTE to handle class imbalance...\n")
    smote = SMOTE(random_state=42) #42 is the seed value, this is used to ensure reproducibility of the results
    X_resampled, y_resampled = smote.fit_resample(X, y) #fit_resample() is used to resample the dataset

    # Combine resampled features and target into a new DataFrame
    df_resampled = pd.concat([pd.DataFrame(X_resampled, columns=X.columns), pd.DataFrame(y_resampled, columns=['Churn_Yes'])], axis=1)

    # Assuming your dataset is loaded into a DataFrame called df
    churn_counts = df['Churn_Yes'].value_counts()
    print("\nOriginal class distribution: ")
    print(churn_counts)

    # Calculate the ratio
    churn_ratio = churn_counts[1] / churn_counts.sum()
    print(f"\nOriginal Churn Ratio: {churn_ratio:.2%}")
    

    print("Class distribution after SMOTE: ")
    print(df_resampled['Churn_Yes'].value_counts())

    # Calculate the ratio
    churn_ratio_resampled = df_resampled['Churn_Yes'].value_counts()[1] / df_resampled['Churn_Yes'].value_counts().sum()
    print(f"\nChurn Ratio after SMOTE: {churn_ratio_resampled:.2%}")
    


    # Save the balanced dataset
    OUTPUT_DIR = '../data'
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    balanced_file_path = os.path.join(OUTPUT_DIR, "balanced_telco_data.csv")
    df_resampled.to_csv(balanced_file_path, index=False)
    print(f"✅ Balanced dataset saved at: {balanced_file_path}\n")

    return df_resampled

