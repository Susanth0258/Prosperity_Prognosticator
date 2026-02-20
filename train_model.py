import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

# Create models directory if it doesn't exist
if not os.path.exists('models'):
    os.makedirs('models')

# 1. Load Dataset
print("Loading dataset...")
df = pd.read_csv('dataset/startup_data.csv')

# 2. Preprocessing
print("Preprocessing...")

# Target Variable
# acquired -> 1, closed -> 0
df['status_encoded'] = df['status'].apply(lambda x: 1 if x == 'acquired' else 0)

# Feature Selection
features = [
    'relationships', 
    'funding_rounds', 
    'funding_total_usd', 
    'milestones', 
    'avg_participants',
    'age_first_funding_year',
    'age_last_funding_year',
    'age_first_milestone_year',
    'age_last_milestone_year'
]

X = df[features]
y = df['status_encoded']

# Handle Missing Values (Simple imputation with 0 or mean, assuming 0 for money/counts)
X = X.fillna(0) 

# 3. Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Model Building
print("Training Random Forest Classifier...")
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# 5. Evaluation
y_pred = rf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")
print("Classification Report:\n", classification_report(y_test, y_pred))

# 6. Save Model
with open('models/model.pkl', 'wb') as f:
    pickle.dump(rf, f)
print("Model saved to models/model.pkl")

# Save the feature names
with open('models/columns.pkl', 'wb') as f:
    pickle.dump(features, f)
print("Model features saved to models/columns.pkl")
