import mysql.connector
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

print("Connecting to MySQL Database...")

# 1. Connect to your database
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="pranavisgreat1@",  # <-- REPLACE THIS WITH YOUR MYSQL PASSWORD
    database="MaterialQualityDB"
)

# 2. Extract the Data
query = """
SELECT 
    mb.carbon_percentage,
    mb.tensile_strength_mpa,
    mb.yield_stress_mpa,
    q.passed_inspection
FROM Material_Batches mb
JOIN Quality_Test_Results q ON mb.batch_id = q.batch_id;
"""
df = pd.read_sql(query, con=db_connection)
print("\n--- Data Successfully Extracted ---")
print(df.head())

# 3. Prepare the Data for Machine Learning
X = df[['carbon_percentage', 'tensile_strength_mpa', 'yield_stress_mpa']]
y = df['passed_inspection']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the Predictive Model
print("\nTraining the Random Forest Classifier...")
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 5. Evaluate the Model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"\n--- Model Results ---")
print(f"Model Accuracy: {accuracy * 100:.2f}%")
# 6. Test on a New, Unseen Batch
print("\n--- Testing Custom Batch ---")

# Define the physical properties of our imaginary material
new_batch = pd.DataFrame({
    'carbon_percentage': [1.40],
    'tensile_strength_mpa': [450],
    'yield_stress_mpa': [250]
})

print("Testing properties:")
print(new_batch.to_string(index=False))

# Ask the AI to make a prediction
prediction = model.predict(new_batch)

# Output the result in plain English
# Output the result in plain English
if prediction[0] == 1:
    print("\nPrediction: The batch will PASS inspection. (PASS)")
else:
    print("\nPrediction: The batch will FAIL inspection. (FAIL)")