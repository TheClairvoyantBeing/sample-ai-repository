# ============================================================
# 04 - Data Types
# Python has 4 fundamental data types: str, int, float, bool.
# ============================================================

# ── 1. Strings (str) — text data ─────────────────────────────
greeting = "Hello, Python!"
language = 'Python'             # single or double quotes are fine

# Multi-line string
poem = """
Roses are red,
Violets are blue,
Python is awesome,
And so are you!
"""
print(poem)

# Common string operations
first = "Jacob"
last  = "Dennis"
full  = first + " " + last      # concatenation
print(full.upper())             # → JACOB DENNIS
print(full.lower())             # → jacob dennis
print(len(full))                # → 11 (total characters including space)
print(full[0])                  # → J  (indexing — starts at 0)
print(full[-1])                 # → s  (negative index = from the end)
print(full[0:5])                # → Jacob (slicing)
print("Dennis" in full)         # → True (membership test)

# ── 2. Integers (int) — whole numbers ────────────────────────
apples = 10
oranges = 3

print(apples + oranges)        # Addition       → 13
print(apples - oranges)        # Subtraction    → 7
print(apples * oranges)        # Multiplication → 30
print(apples // oranges)       # Floor division → 3  (no decimal)
print(apples % oranges)        # Modulus        → 1  (remainder)
print(apples ** 2)             # Exponent       → 100

# ── 3. Floats (float) — decimal numbers ──────────────────────
price = 19.99
tax   = 0.18

total = price + (price * tax)
print(f"Price after tax: {total:.2f}")  # → 23.59 (2 decimal places)

# Floating-point quirk — use round() to fix precision issues
print(0.1 + 0.2)                        # → 0.30000000000000004
print(round(0.1 + 0.2, 2))             # → 0.3

# ── 4. Booleans (bool) — True or False ───────────────────────
is_raining   = False
is_weekend   = True
age          = 20

# Booleans are often the result of a comparison
is_adult = age >= 18
print(f"Is adult: {is_adult}")          # → Is adult: True

# Any comparison returns a bool
print(10 > 5)    # → True
print(10 == 5)   # → False
print(10 != 5)   # → True

# ── Type conversion ──────────────────────────────────────────
# Convert between types using int(), float(), str(), bool()
num_str = "42"
num_int = int(num_str)          # "42" → 42
print(num_int + 8)              # → 50

pi_str  = str(3.14)             # 3.14 → "3.14"
print("Pi is " + pi_str)       # → Pi is 3.14

print(bool(0))                  # → False  (0 is falsy)
print(bool(1))                  # → True   (any non-zero is truthy)
print(bool(""))                 # → False  (empty string is falsy)
print(bool("hi"))               # → True
