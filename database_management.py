import sqlite3

# Connect Database
conn = sqlite3.connect("business.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
)
""")

conn.commit()

print("Database Created Successfully!")

# Get Input
emp_id = int(input("Enter ID: "))
name = input("Enter Name: ")
dept = input("Enter Department: ")
salary = float(input("Enter Salary: "))

# Insert Data
cursor.execute(
    "INSERT INTO employees VALUES (?, ?, ?, ?)",
    (emp_id, name, dept, salary)
)

conn.commit()

print("Employee Added Successfully!")

# Display Records
print("\nEmployee Records:")

cursor.execute("SELECT * FROM employees")

rows = cursor.fetchall()

for row in rows:
    print(row)

# Close Database
conn.close()