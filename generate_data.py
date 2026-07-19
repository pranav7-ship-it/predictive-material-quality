import mysql.connector
import random

print("Connecting to database to generate data...")

# 1. Connect to database
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="pranavisgreat1@", 
    database="MaterialQualityDB"
)
cursor = db.cursor()

# 2. Insert 3 Global Suppliers
suppliers = [
    (1, 'Global Steel', 'USA', 0.95),
    (2, 'Titanium Works', 'Germany', 0.88),
    (3, 'Alloy Partners', 'India', 0.75)
]
# We use INSERT IGNORE so it doesn't crash if you run this script twice
cursor.executemany("INSERT IGNORE INTO Suppliers (supplier_id, company_name, country, reliability_score) VALUES (%s, %s, %s, %s)", suppliers)

# 3. Generate 500 Batches of Material Data
print("Generating 500 batches of material data...")
for i in range(100, 600):
    batch_id = i
    supplier_id = random.choice([1, 2, 3])
    material = random.choice(['Steel Alloy', 'Titanium', 'Aluminum'])
    carbon = round(random.uniform(0.1, 1.5), 2)
    tensile = random.randint(300, 1000)
    yield_stress = random.randint(200, tensile - 50) 
    
    # Insert Batch Properties
    cursor.execute(
        "INSERT IGNORE INTO Material_Batches (batch_id, supplier_id, material_type, carbon_percentage, tensile_strength_mpa, yield_stress_mpa) VALUES (%s, %s, %s, %s, %s, %s)",
        (batch_id, supplier_id, material, carbon, tensile, yield_stress)
    )
    
    # 4. The Hidden Pattern (High carbon + low tensile = Failure)
    if carbon > 1.0 and tensile < 600:
        passed = False
        reason = "Brittle Fracture"
    elif yield_stress < 300:
        passed = False
        reason = "Failed Stress Test"
    else:
        # 90% chance to pass otherwise
        passed = random.random() > 0.1
        reason = "None" if passed else "Micro-fissures"
        
    # Insert Inspection Results
    cursor.execute(
        "INSERT IGNORE INTO Quality_Test_Results (test_id, batch_id, test_date, passed_inspection, failure_reason) VALUES (%s, %s, '2026-07-19', %s, %s)",
        (batch_id, batch_id, passed, reason)
    )

# Save the changes to the database
db.commit()
print("Data generation complete! 500 rows successfully added.")