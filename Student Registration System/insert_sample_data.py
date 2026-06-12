import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

students = [
    ("Arjun Kumar", "101", "IT", "3", "arjun@gmail.com", "9876543210", "Male", "Chennai"),
    ("Priya Sharma", "102", "CSE", "2", "priya@gmail.com", "9876543211", "Female", "Bangalore"),
    ("Rahul Verma", "103", "ECE", "4", "rahul@gmail.com", "9876543212", "Male", "Hyderabad"),
    ("Sneha Reddy", "104", "IT", "1", "sneha@gmail.com", "9876543213", "Female", "Salem"),
    ("Kiran Kumar", "105", "EEE", "2", "kiran@gmail.com", "9876543214", "Male", "Coimbatore"),
    ("Anjali Devi", "106", "CSE", "3", "anjali@gmail.com", "9876543215", "Female", "Madurai"),
    ("Vikram Singh", "107", "MECH", "4", "vikram@gmail.com", "9876543216", "Male", "Delhi"),
    ("Deepika Nair", "108", "IT", "1", "deepika@gmail.com", "9876543217", "Female", "Kochi"),
    ("Surya Prakash", "109", "ECE", "2", "surya@gmail.com", "9876543218", "Male", "Trichy"),
    ("Divya Lakshmi", "110", "CSE", "3", "divya@gmail.com", "9876543219", "Female", "Erode")
]

cursor.executemany("""
INSERT INTO students
(name, roll_number, department, year, email, phone, gender, address)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", students)

conn.commit()
conn.close()

print("✅ 10 sample student records inserted successfully!")