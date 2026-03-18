# ============================================================
# 15 - CSV File Operations
# CSV (Comma-Separated Values) is the most common format for
# storing and sharing tabular data (like spreadsheets).
# Python's built-in 'csv' module makes reading/writing easy.
# ============================================================

import csv
import os

DATA_DIR = "../data"   # data/ lives one level up from lessons/

# ── 1. Write a CSV file ──────────────────────────────────────
# csv.writer handles commas inside values, quoting, etc. automatically.
students_path = os.path.join(DATA_DIR, "students.csv")

students = [
    ["name",   "age", "grade", "city"],
    ["Dennis",  25,   "A",     "Bangalore"],
    ["Priya",   22,   "B",     "Chennai"],
    ["Jerome",  23,   "A+",    "Mumbai"],
    ["Kavya",   24,   "B+",    "Mysore"],
]

with open(students_path, "w", newline="") as file:
    # newline="" is REQUIRED on Windows to prevent blank rows appearing
    writer = csv.writer(file)
    writer.writerows(students)          # write all rows at once

print(f"✅ CSV written: {students_path}")

# ── 2. Read a CSV file ───────────────────────────────────────
print("\n── Reading students.csv ────────────")
with open(students_path, "r") as file:
    reader = csv.reader(file)
    header = next(reader)               # grab the first row as header
    print(f"  Columns: {header}")
    print()
    for row in reader:
        name, age, grade, city = row
        print(f"  {name} (Age {age}) — Grade: {grade}, City: {city}")

# ── 3. DictReader — rows become dictionaries (most readable) ──
# Each row is a dict with column names as keys — much cleaner!
print("\n── DictReader (rows as dicts) ──────")
with open(students_path, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"  {row['name']} scored {row['grade']} from {row['city']}")

# ── 4. DictWriter — write from a list of dicts ───────────────
new_path = os.path.join(DATA_DIR, "new_student.csv")

new_students = [
    {"name": "Arun",  "age": 21, "grade": "A",  "city": "Pune"},
    {"name": "Sneha", "age": 23, "grade": "B+", "city": "Delhi"},
]

with open(new_path, "w", newline="") as file:
    fieldnames = ["name", "age", "grade", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()                # writes the column name row
    writer.writerows(new_students)

print(f"\n✅ new_student.csv written: {new_path}")

# ── 5. Read the db.csv (original data from Python Basics) ────
db_path = os.path.join(DATA_DIR, "db.csv")
print(f"\n── Reading db.csv ──────────────────")
try:
    with open(db_path, "r") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            print(f"  {row}")
            if i >= 4:                  # show first 5 rows only
                print("  ...")
                break
except FileNotFoundError:
    print(f"  '{db_path}' not found — skipping.")

# ── Cheat sheet ───────────────────────────────────────────────
print("\n── CSV cheat sheet ─────────────────")
print("  csv.writer     → write rows (lists)")
print("  csv.reader     → read  rows (lists)")
print("  csv.DictWriter → write rows (dicts) — column names as keys")
print("  csv.DictReader → read  rows (dicts) — most readable option")
print("  newline=''     → REQUIRED on Windows when writing CSVs")
