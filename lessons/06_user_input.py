# ============================================================
# 06 - User Input
# Programs become interactive when they can read from the user.
# ============================================================

# ── The input() function ─────────────────────────────────────
# input() always returns a STRING, no matter what the user types.
# Always give a clear, friendly prompt message.

name = input("What is your name? ")
print(f"Hello, {name}! Nice to meet you.")

# ── Type conversion is essential for numbers ─────────────────
# If you need to do maths, convert the string to int or float first.
age_str = input("How old are you? ")
age     = int(age_str)              # str → int
print(f"In 10 years you will be {age + 10} years old.")

# ── You can chain input() and int() on one line ───────────────
year = int(input("What year were you born? "))
current_year = 2026
print(f"You are approximately {current_year - year} years old.")

# ── float() for decimal input ────────────────────────────────
price = float(input("Enter item price: ₹"))
tax   = 0.18
print(f"Total with 18% tax: ₹{price * (1 + tax):.2f}")

# ── Safe input with error handling (preview of lesson 11) ────
try:
    lucky = int(input("Enter your lucky number: "))
    print(f"Your lucky number doubled is {lucky * 2}!")
except ValueError:
    print("That doesn't look like a number — please enter digits only.")