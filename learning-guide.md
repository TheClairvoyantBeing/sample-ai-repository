# 🐍 Python Learning Guide

Work through the files **in order** — each one builds on the last.

---

## Table of Contents

1. [Hello World](#1-hello-world) — `01_hello_world.py`
2. [Output & Print](#2-output--print) — `02_output.py`
3. [Variables](#3-variables) — `03_variables.py`
4. [Data Types](#4-data-types) — `04_datatypes.py`
5. [Operators](#5-operators) — `05_operators.py`
6. [User Input](#6-user-input) — `06_user_input.py`
7. [Conditional Statements](#7-conditional-statements) — `07_conditional_statements.py`
8. [Looping Statements](#8-looping-statements) — `08_looping_statements.py`
9. [Functions](#9-functions) — `09_functions.py`
10. [Data Structures](#10-data-structures) — `10_data_structures.py`
11. [Exception Handling](#11-exception-handling) — `11_exception_handling.py`
12. [Modules](#12-modules) — `12_modules.py`
13. [Mini Projects](#13-mini-projects) — `13_mini_projects.py`

---

## 1. Hello World

> **File:** `01_hello_world.py`

Your very first Python program — print text, store a variable, and write a simple condition.

```python
print("Hello World")
print("This is my first program")

a = 10
name = "Jacob Dennis"

# Simple if condition
if 10 > 5:
    print("10 is greater than 5!")
```

---

## 2. Output & Print

> **File:** `02_output.py`

The `print()` function is how Python talks back to you.

```python
print("Lorem Ipsum Ist", end=" ")   # end keeps it on the same line
print(" Um Lorem")

print(1)        # Integer
print(5 + 3)    # Expression → 8
print("Hi I am Dennis, I am ", 55, "Years Old")   # Multiple values
```

---

## 3. Variables

> **File:** `03_variables.py`

A **variable** is a named container for storing data.

### Naming Rules

| ✅ Allowed    | ❌ Not Allowed                     |
| ------------- | ---------------------------------- |
| `my_age = 35` | `1myage = 35` (starts with number) |
| `myAge = 35`  | `my-var = 35` (hyphen)             |
| `MYAGE = 35`  | `my var = 35` (space)              |

### Multiple Assignment

```python
# Different values in one line
a, b, c = "Dennis", "Manjunath", "Sneha"

# Same value for multiple variables
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

## 4. Data Types

> **File:** `04_datatypes.py`

### Strings

```python
message = "Hey Bro Wassup"

# Multi-line string
poem = """
Roses are red,
Violets are blue,
Python is awesome,
Well so are you!
"""

# Concatenation & repetition
first_name = "jacob"
last_name  = "dennis"
fullname   = first_name + " " + last_name
print(fullname.upper())          # → JACOB DENNIS
print("*" * len(fullname))       # Repeating character
print(fullname[6])               # Indexing → d
```

### Integers

```python
a, b = 10, 20
print(a + b)    # 30
print(a - b)    # -10
print(a * b)    # 200
print(a / b)    # 0.5  (float result)
print(a // b)   # 0    (floor division)
print(a % b)    # 10   (remainder)
print(a ** b)   # 10^20
```

### Floats

```python
price = 20.99
total = price * 1.5
print(total)                       # 31.485

# Floating-point precision fix
print(round(0.1 + 0.345, 5))      # 0.445
```

### Booleans

```python
age = 10
is_adult = age >= 18    # Evaluates to False
```

---

## 5. Operators

> **File:** `05_operators.py`

### Arithmetic

| `+` | `-` | `*` | `/` | `//`      | `%`     | `**`     |
| --- | --- | --- | --- | --------- | ------- | -------- |
| Add | Sub | Mul | Div | Floor Div | Modulus | Exponent |

### Comparison

| `==`  | `!=`      | `>`     | `<`  | `>=` | `<=` |
| ----- | --------- | ------- | ---- | ---- | ---- |
| Equal | Not equal | Greater | Less | ≥    | ≤    |

### Logical

| `and`     | `or`              | `not`  |
| --------- | ----------------- | ------ |
| Both True | At least one True | Invert |

### Assignment Shortcuts

```python
a = 120
a += 1    # a = 121
a -= 1    # a = 120
a *= 2    # a = 240
a /= 2    # a = 120.0
```

### PEMDAS — Order of Operations

**P**arentheses → **E**xponents → **M**ul/**D**iv → **A**dd/**S**ub

```python
result = (2 + 3) * 4   # → 20, not 14
```

---

## 6. User Input

> **File:** `06_user_input.py`

`input()` always returns a **string** — cast it when you need a number.

```python
age_str = input("What's your age? ")
age = int(age_str)       # Convert string → integer
print(age + 1)
```

> ⚠️ Forgetting `int()` will cause a `TypeError` when doing maths.

---

## 7. Conditional Statements

> **File:** `07_conditional_statements.py`

### if / else

```python
if password == "secret@123":
    print("Access Granted")
else:
    print("Access Denied")
```

### if / elif / else

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
print("Grade:", grade)   # B
```

### Nested if

```python
age = 25
has_license = False
if age >= 18:
    print("Old enough to drive")
    if has_license:
        print("You can drive!")
    else:
        print("Get a licence first")
else:
    print("Too young to drive")
```

### and / or / not

```python
# and — both must be True
if age >= 18 and has_ticket:
    print("Enter the concert")

# or — at least one must be True
if day == "saturday" or day == "sunday":
    print("Weekend!")

# not — inverts condition
if not is_sunny:
    print("Take an umbrella")
```

### Ternary (one-liner)

```python
age = 21
status = "adult" if age >= 18 else "minor"
print(status)   # adult
```

---

## 8. Looping Statements

> **File:** `08_looping_statements.py`

### while loop

```python
count = 0
while count <= 10:
    print("Count is", count)
    count += 1
print("Done!")
```

### for loop with `range()`

```python
for i in range(0, 10):
    print(i)      # 0 → 9
```

### Nested loops — Star Pattern

```python
for row in range(1, 5):
    for col in range(row):
        print("*", end="")
    print()
# *
# **
# ***
# ****
```

### break / else on a loop

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
search_for = 5

for num in numbers:
    if num == search_for:
        print("Found it!")
        break
else:
    print("Not found")
# The else only runs if break was never hit
```

---

## 9. Functions

> **File:** `09_functions.py`

Functions let you write **reusable** blocks of code.

### Basic function

```python
def greet():
    print("I am Groot")

greet()    # Call it any number of times
```

### With parameters & return

```python
def greet(name):
    print(f"Hello, {name}! Welcome to Python.")

greet("Dennis")
```

### \*args — any number of positional arguments

```python
def add_all(*args):
    result = 0
    for num in args:
        result += num
    return result

print(add_all(1, 2, 3, 4, 5))   # 15
```

### \*\*kwargs — keyword arguments

```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Dennis", age=20, married=False)
```

### Function Types at a Glance

| Has params? | Has return? | Example                    |
| ----------- | ----------- | -------------------------- |
| ❌          | ❌          | `def greet():`             |
| ✅          | ❌          | `def greet(name):`         |
| ✅          | ✅          | `def add(a,b): return a+b` |
| ❌          | ✅          | `def pi(): return 3.14`    |

---

## 10. Data Structures

> **File:** `10_data_structures.py`

### List — ordered, mutable, allows duplicates

```python
students = ["Dennis", "Manjunath", "Kavya", "Sneha"]
numbers  = [1, 2, 3, 4, 4, 5]

students[1] = "Arun"              # Update
students.pop()                    # Remove last
print(len(students))              # Length
print(sum(numbers))               # Sum
print(min(numbers), max(numbers)) # Min / Max
print(numbers.count(4))           # Count occurrences
students.sort()                   # Sort
numbers.reverse()                 # Reverse
print("Dennis" in students)       # Membership → True

# Loop with index
for i, name in enumerate(students):
    print(f"{i}: {name}")

# List comprehension
squares = [i ** 2 for i in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]
```

### Tuple — ordered, **immutable**

```python
person = ("kavya", 25, "Chitradurga")
name, age, district = person       # Unpack
print(f"{name} is from {district}")
```

> 💡 Use tuples when data must **not** change (e.g., coordinates, RGB colours).

### Dictionary — key-value pairs

```python
student = {
    "name": "Dennis",
    "age":  25,
    "courses": ["Math", "Science"]
}

print(student["name"])
student["phone"] = "8908908900"          # Add key
student["age"] = 26                      # Update
student.pop("courses")                   # Delete

for key, value in student.items():
    print(f"{key}: {value}")
```

### Set — unordered, **no duplicates**

```python
numbers = [1, 2, 3, 1, 3, 4, 5, 5, 5]
unique  = set(numbers)
print(unique)                  # {1, 2, 3, 4, 5}
unique.discard(999)            # Safe remove (no error)
```

### Quick Comparison

|            | List  | Tuple | Dict    | Set |
| ---------- | ----- | ----- | ------- | --- |
| Ordered    | ✅    | ✅    | ✅      | ❌  |
| Mutable    | ✅    | ❌    | ✅      | ✅  |
| Duplicates | ✅    | ✅    | Keys ❌ | ❌  |
| Access     | Index | Index | Key     | —   |

---

## 11. Exception Handling

> **File:** `11_exception_handling.py`

Stop your program from crashing on bad input.

### try / except

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)
except ValueError:
    print("That is not a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Raising your own exceptions

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 200:
        raise ValueError("Invalid age")
    return age

try:
    validate_age(-10)
except ValueError as e:
    print(e)    # Age cannot be negative
```

---

## 12. Modules

> **File:** `12_modules.py`

Modules are ready-made libraries — `import` them to extend Python.

```python
import datetime
import os

print(datetime.datetime.now())   # Current date & time
print(os.getcwd())               # Current working directory
```

### Handy Built-in Modules

| Module     | Use                    |
| ---------- | ---------------------- |
| `datetime` | Dates and times        |
| `os`       | Files & paths          |
| `math`     | sqrt, ceil, floor, pi… |
| `random`   | Random numbers         |
| `json`     | Read/write JSON        |
| `sys`      | System operations      |

---

## 13. Mini Projects

> **File:** `13_mini_projects.py`

Put everything together with two small projects.

### Project 1 — ASCII Art Bot

```python
print("  ********  ")
print(" *        * ")
print("*  ^    ^  *")
print("*     >    *")
print("*  \\____/  *")
print(" ********** ")
print("Hi! Welcome — I just smile :)")
```

### Project 2 — Simple Calculator

```python
a  = float(input("First number : "))
b  = float(input("Second number: "))
op = input("Operator (+  -  *  /): ")

if op == "+":   print("Result:", a + b)
elif op == "-": print("Result:", a - b)
elif op == "*": print("Result:", a * b)
elif op == "/":
    print("Result:", a / b) if b != 0 else print("Cannot divide by zero!")
else:
    print("Invalid operator")
```

---

## 🗺️ Learning Path

```
01_hello_world.py
      ↓
02_output.py  →  03_variables.py  →  04_datatypes.py  →  05_operators.py
      ↓
06_user_input.py  →  07_conditional_statements.py  →  08_looping_statements.py
      ↓
09_functions.py  →  10_data_structures.py
      ↓
11_exception_handling.py  →  12_modules.py
      ↓
13_mini_projects.py  🎉
```

---

_Part of the [`sample-ai-repository`](https://github.com/TheClairvoyantBeing/sample-ai-repository) Python learning series._
