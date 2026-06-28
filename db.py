import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="raza.1290",
    database="student_tracker"
)

cursor = db.cursor()
print("✅ Connected to MySQL Successfully!")