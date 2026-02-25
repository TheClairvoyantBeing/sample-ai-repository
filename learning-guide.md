# 🐍 Python Learning Guide

A beginner-to-intermediate guide built from the code examples in this repository.

---

## Table of Contents

1. [Output & Print](#1-output--print)
2. [Variables](#2-variables)
3. [Data Types](#3-data-types)
4. [Operators](#4-operators)
5. [User Input](#5-user-input)
6. [Conditional Statements](#6-conditional-statements)
7. [Looping Statements](#7-looping-statements)
8. [Functions](#8-functions)
9. [Data Structures](#9-data-structures)
10. [Exception Handling](#10-exception-handling)
11. [Modules](#11-modules)
12. [Mini Projects](#12-mini-projects)

---

## 1. Output & Print

> **File:** `output.py`, `script.py`

The `print()` function is how Python communicates back to you.

```python
print("Hello World")              # Basic string
print(1)                          # Integer
print(5 + 3)                      # Expression result → 8
print("Hi I am Dennis, I am ", 55, "Years Old")  # Multiple values
```

### `end` parameter

By default, `print()` adds a newline. Use `end` to change it:

```python
print("Lorem Ipsum Ist", end=" ")
print(" Um Lorem")
# Output: Lorem Ipsum Ist  Um Lorem
```

---

## 2. Variables

> **File:** `variables.py`

A **variable** is a named container for storing data.

### Naming Rules

| ✅ Allowed               | ❌ Not Allowed                     |
| ------------------------ | ---------------------------------- |
| `myage = 35`             | `1myage = 35` (starts with number) |
| `my_age = 35`            | `my-var = 35` (hyphen not allowed) |
| `_my_age = 35`           | `my var = 35` (spaces not allowed) |
| `myAge = 35` (camelCase) |                                    |
| `MYAGE = 35` (UPPERCASE) |                                    |

### Multiple Assignment

```python
# Different values
a, b, c = "Dennis", "Manjunath", "Sneha"

# Same value
d = e = f = "Dennis"
```

### Example

```python
name = "dennis"
age = 35
height = 5.6
is_married = True

print("Hi I am", name)
print("I am", age, "Years old")
print("My Height is", height, "feet")
```

---

## 3. Data Types

> **File:** `datatypes.py`

Python has several built-in data types:

### Strings

```python
message = "Hey Bro Wassup"
name = 'Python'

# Multi-line string
poem = """
Roses are red,
Violets are blue,
Python is awesome,
Well so are you!
"""

# Operations
first_name = "jacob"
last_name = "dennis"
fullname = first_name + " " + last_name   # Concatenation
print(fullname.upper())                    # → JACOB DENNIS
line = "*" * len(fullname)                 # Repetition
print(fullname[6])                         # Indexing → d
```

### Integers

```python
a = 10
b = 20

print(a + b)    # Addition       → 30
print(a - b)    # Subtraction    → -10
print(a * b)    # Multiplication → 200
print(a / b)    # Division       → 0.5
print(a // b)   # Floor Division → 0
print(a % b)    # Modulus        → 10
print(a ** b)   # Exponent       → 100000000000000000000
```

### Floats

```python
price = 20.99
PI = 3.14285
temp = 99.8

total = price * 1.5
print(total)                       # → 31.485

# Floating point precision
print(0.1 + 0.345)                 # → 0.44500000000000006
print(round(0.1 + 0.345, 5))      # → 0.445
```

### Booleans

```python
is_raining = False
is_holiday = False
age = 10

is_adult = age >= 18              # Evaluates to False
```

---

## 4. Operators

> **File:** `operators.py`

### Arithmetic Operators

| Operator | Operation      | Example  |
| -------- | -------------- | -------- |
| `+`      | Addition       | `a + b`  |
| `-`      | Subtraction    | `a - b`  |
| `*`      | Multiplication | `a * b`  |
| `/`      | Division       | `a / b`  |
| `//`     | Floor Division | `a // b` |
| `%`      | Modulus        | `a % b`  |
| `**`     | Exponentiation | `a ** b` |

### Comparison Operators

| Operator | Meaning               | Example  |
| -------- | --------------------- | -------- |
| `==`     | Equal to              | `x == y` |
| `!=`     | Not equal to          | `x != y` |
| `>`      | Greater than          | `x > y`  |
| `<`      | Less than             | `x < y`  |
| `>=`     | Greater than or equal | `x >= y` |
| `<=`     | Less than or equal    | `x <= y` |

### Logical Operators

| Operator | Description                                |
| -------- | ------------------------------------------ |
| `and`    | True if **both** conditions are True       |
| `or`     | True if **at least one** condition is True |
| `not`    | Reverses the boolean value                 |

### Assignment Operators

```python
a = 120
a += 1    # a = a + 1
a -= 1    # a = a - 1
a *= 2    # a = a * 2
a /= 2    # a = a / 2
```

### PEMDAS (Order of Operations)

**P**arentheses → **E**xponents → **M**ultiply/**D**ivide → **A**dd/**S**ubtract

```python
result = (2 + 3) * 4   # → 20  (not 14!)
```

---

## 5. User Input

> **File:** `user-input.py`

The `input()` function reads text from the user. It **always returns a string**, so convert to the needed type.

```python
age_str = input("What's your age?")   # Returns a string
age = int(age_str)                     # Convert to integer
print(age + 1)
```

> ⚠️ **Tip:** Always cast `input()` when you need a number — doing math on a string will cause a `TypeError`.

---

## 6. Conditional Statements

> **File:** `conditional-statements.py`

### if / else

```python
password = "secret@123"
if password == "secret@123":
    print("Access Granted")
else:
    print("Access Denied")
```

### if / elif / else (Grade Example)

```python
score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Your Grade is:", grade)   # → B
```

### Nested if / else

```python
age = 25
has_license = False

if age >= 18:
    print("You are old enough to drive")
    if has_license:
        print("You can Drive!")
    else:
        print("But you need a License")
else:
    print("Too Young to drive")
```

### Using `and` / `or` / `not`

```python
# AND - both must be True
age = 20
has_ticket = False
if age >= 18 and has_ticket:
    print("You can enter the concert")

# OR - at least one must be True
day = "monday"
if day == "saturday" or day == "sunday":
    print("It's the Weekend!")

# NOT - inverts the condition
is_sunny = True
if not is_sunny:
    print("Take an umbrella")
```

### Ternary Operator (One-liner)

```python
age = 21
status = "adult" if age >= 18 else "minor"
print(status)   # → adult
```

---

## 7. Looping Statements

> **File:** `looping-statements.py`

### while Loop

```python
count = 0
while count <= 10:
    print("Count is", count)
    count += 1
print("Done!")
```

### for Loop with `range()`

```python
for count in range(0, 10):
    print(count)   # Prints 0 through 9
```

### Nested Loops (Star Pattern)

```python
for row in range(1, 5):
    for col in range(row):
        print("*", end="")
    print()
# Output:
# *
# **
# ***
# ****
```

### Loop with `break` (Search Example)

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
search_for = 5

for num in numbers:
    if num == search_for:
        print("Found it")
        break
else:
    print("Not found")
```

> 💡 The `else` block on a `for` loop runs only if the loop was **not** broken out of early.

---

## 8. Functions

> **File:** `functions.py`

Functions let you write reusable blocks of code.

### Basic Function

```python
def iAmGroot():
    print("I am Groot")

for i in range(0, 10):
    iAmGroot()
```

### Function with Parameters & Return

```python
def greet_someone(name):
    print(f"Hello, {name}!")
    print("Welcome to My Python Script")

name = input("Please enter your name to Continue:")
greet_someone(name)
```

### `*args` — Variable Positional Arguments

```python
def sum_all(*args):
    result = 0
    for num in args:
        result += num
    return result

print(sum_all(1, 2, 3, 4, 5))   # → 15
```

### `**kwargs` — Variable Keyword Arguments

```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Dennis", age=20, sex="Male", married=False)
# Output:
# name: Dennis
# age: 20
# sex: Male
# married: False
```

### Function Types Summary

| Type                        | Has Parameters? | Has Return? |
| --------------------------- | --------------- | ----------- |
| `def greet()`               | ❌              | ❌          |
| `def greet(name)`           | ✅              | ❌          |
| `def add(a, b): return a+b` | ✅              | ✅          |
| `def get_pi(): return 3.14` | ❌              | ✅          |

---

## 9. Data Structures

> **File:** `data-structures.py`

### Lists — Ordered, Mutable, Allows Duplicates

```python
students = ["Dennis", "Manjunath", "Kavya", "Sneha"]
numbers = [1, 2, 3, 4, 4, 5]
mixed = [1, "Dennis", 25.4, True]

# Common operations
students[1] = "Arun"           # Update item
students.pop()                 # Remove last item
print(len(students))           # Length
print(sum(numbers))            # Sum
print(min(numbers))            # Min
print(max(numbers))            # Max
print(numbers.count(4))        # Count occurrences of 4
print(students.index("Arun"))  # Find index
students.sort()                # Sort alphabetically
numbers.reverse()              # Reverse order
print("Dennis" in students)    # Membership check → True

# Looping
for name in students:
    print(name)

# With index using enumerate()
for i, name in enumerate(students):
    print(f"{i}: {name}")

# List Comprehension
squares = [i ** 2 for i in range(1, 6)]
print(squares)   # → [1, 4, 9, 16, 25]
```

### Tuples — Ordered, **Immutable**

```python
coordinates = (10, 20)
person = ("kavya", 25, "Chitradurga")

print(person[2])           # Indexing → Chitradurga

# Tuple unpacking
name, age, district = person
print(f"I am {name}, from {district}. I am {age} years old")
```

> 💡 Use tuples when data **should not change** (e.g., coordinates, RGB colors).

### Dictionaries — Key-Value Pairs, Ordered (Python 3.7+)

```python
student = {
    "name": "Dennis",
    "age": 25,
    "grade": "A",
    "courses": ["Math", "Science", "Social Science"]
}

# Access
print(student["name"])
print(student.get("phone", "Not found"))   # Safe access with default

# Add / Update
student["phone"] = "8908908900"
student["age"] = 26

# Delete
student.pop("grade")

# Loop
for key, value in student.items():
    print(f"{key}: {value}")
```

### Sets — Unordered, **No Duplicates**

```python
numbers = [1, 2, 3, 1, 3, 4, 3, 6, 7, 888, 9, 2, 4, 5, 5, 5]
unique_numbers = set(numbers)
print(unique_numbers)   # All duplicates removed

unique_numbers.discard(999)   # Remove safely (no error if not found)
```

### Quick Comparison

| Feature    | List  | Tuple | Dictionary | Set |
| ---------- | ----- | ----- | ---------- | --- |
| Ordered    | ✅    | ✅    | ✅         | ❌  |
| Mutable    | ✅    | ❌    | ✅         | ✅  |
| Duplicates | ✅    | ✅    | Keys: ❌   | ❌  |
| Access by  | Index | Index | Key        | —   |

---

## 10. Exception Handling

> **File:** `exceptionhandling.py`

Exceptions prevent your program from crashing on bad input.

### try / except

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)
except ValueError:
    print("That is not a number, please enter a valid number")
except ZeroDivisionError:
    print("You cannot divide by zero")
except Exception as e:
    print(f"An error occurred: {e}")
```

### Raising Your Own Exceptions

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 200:
        raise ValueError("Invalid Age")
    return age

try:
    validate_age(-10)
except ValueError as e:
    print(e)   # → Age cannot be negative
```

---

## 11. Modules

> **File:** `modules.py`

Modules are pre-built libraries you can import to add functionality.

```python
import datetime
import os

print(datetime.datetime.now())   # Current date and time
print(os.getcwd())               # Current working directory
```

### Common Built-in Modules

| Module     | Use Case                |
| ---------- | ----------------------- |
| `datetime` | Dates and times         |
| `os`       | File system and paths   |
| `math`     | Mathematical functions  |
| `random`   | Random numbers          |
| `json`     | JSON encoding/decoding  |
| `sys`      | System-level operations |

---

## 12. Mini Projects

### ASCII Art Bot

> **File:** `acsii-art.py`

```python
print("  ********  ")
print(" *        * ")
print("*  ^    ^  *")
print("*     >    *")
print("*  \\____/  *")
print("*          *")
print(" ********** ")
print("Hi Welcome to a Bot I just smile")
```

### Simple Calculator Starter

> **File:** `calculator.py`

A placeholder — here's a fully working extension:

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operator")
```

---

## 🗺️ Suggested Learning Path

```
output.py  →  variables.py  →  datatypes.py  →  operators.py
     ↓
user-input.py  →  conditional-statements.py  →  looping-statements.py
     ↓
functions.py  →  data-structures.py  →  exceptionhandling.py  →  modules.py
     ↓
       acsii-art.py / calculator.py  (mini projects!)
```

---

_Generated from the [`sample-ai-repository`](https://github.com/TheClairvoyantBeing/sample-ai-repository) Python learning files._
