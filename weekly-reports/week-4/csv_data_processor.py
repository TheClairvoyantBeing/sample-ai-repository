"""
Week 4 — CSV Data Processing with File I/O
Demonstrates: list comprehensions, tuples, dictionaries, CSV read/write, exception handling.
Run:  python weekly-reports/week-4/csv_data_processor.py
"""

import csv
import os
from datetime import datetime


def create_sample_data(filepath):
    """Create a sample employee dataset CSV if it doesn't exist."""
    headers = ["ID", "Name", "Department", "Salary", "Join_Date", "Rating"]
    employees = [
        (101, "Alice Johnson", "Engineering", 95000, "2022-03-15", 4.5),
        (102, "Bob Smith", "Marketing", 72000, "2021-07-20", 3.8),
        (103, "Charlie Lee", "Engineering", 105000, "2020-01-10", 4.9),
        (104, "Diana Patel", "HR", 68000, "2023-06-01", 4.2),
        (105, "Ethan Brown", "Marketing", 78000, "2022-11-30", 3.5),
        (106, "Fiona Davis", "Engineering", 112000, "2019-08-22", 4.7),
        (107, "George Wilson", "HR", 65000, "2023-02-14", 3.9),
        (108, "Hannah Clark", "Data Science", 98000, "2021-04-18", 4.6),
        (109, "Ivan Torres", "Data Science", 102000, "2020-09-05", 4.8),
        (110, "Julia Adams", "Marketing", 70000, "2023-01-25", 4.0),
    ]

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(employees)
    print(f"  ✅ Sample data created → {filepath}")


def read_and_analyze(filepath):
    """Read CSV with DictReader, analyze using list comprehensions & dicts."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            employees = [row for row in reader]  # list comprehension
    except FileNotFoundError:
        print(f"  ❌ FileNotFoundError: '{filepath}' not found!")
        print("  ℹ️  Creating sample data...")
        create_sample_data(filepath)
        return read_and_analyze(filepath)

    print(f"\n  📊 Loaded {len(employees)} employee records\n")

    # ── Dictionary: department-wise grouping ──
    dept_groups = {}
    for emp in employees:
        dept = emp["Department"]
        salary = float(emp["Salary"])
        dept_groups.setdefault(dept, []).append(salary)

    print("  ┌─────────────────────────────────────────────┐")
    print("  │       DEPARTMENT-WISE SALARY ANALYSIS        │")
    print("  ├──────────────┬──────────┬──────────┬─────────┤")
    print("  │ Department   │ Avg ($)  │ Max ($)  │ Count   │")
    print("  ├──────────────┼──────────┼──────────┼─────────┤")
    for dept, salaries in sorted(dept_groups.items()):
        avg_sal = sum(salaries) / len(salaries)
        max_sal = max(salaries)
        count = len(salaries)
        print(f"  │ {dept:<12} │ {avg_sal:>8,.0f} │ {max_sal:>8,.0f} │ {count:>7} │")
    print("  └──────────────┴──────────┴──────────┴─────────┘")

    # ── List comprehension: filter high performers ──
    high_performers = [
        (emp["Name"], emp["Department"], float(emp["Rating"]))
        for emp in employees
        if float(emp["Rating"]) >= 4.5
    ]  # returns list of tuples

    print(f"\n  ⭐ High Performers (Rating ≥ 4.5): {len(high_performers)}")
    print("  " + "─" * 42)
    for name, dept, rating in high_performers:
        stars = "★" * int(rating) + "☆" * (5 - int(rating))
        print(f"    {name:<18} │ {dept:<14} │ {stars}")

    # ── Write filtered output to new CSV ──
    output_path = os.path.join(os.path.dirname(filepath), "high_performers.csv")
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Department", "Rating"])
        writer.writerows(high_performers)
    print(f"\n  💾 High performers exported → {output_path}")


def main():
    print("=" * 55)
    print("    📁 WEEK 4 — CSV DATA PROCESSOR")
    print(f"    🕐 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 55)

    data_dir = os.path.join(os.path.dirname(__file__), "..", "evidence")
    os.makedirs(data_dir, exist_ok=True)
    csv_path = os.path.join(data_dir, "employees.csv")

    create_sample_data(csv_path)
    read_and_analyze(csv_path)

    print("\n" + "=" * 55)
    print("  ✅ File I/O operations completed successfully!")
    print("=" * 55)


if __name__ == "__main__":
    main()
