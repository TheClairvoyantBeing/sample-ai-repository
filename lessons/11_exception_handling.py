# ============================================================
# 11 - Exception Handling
# Errors happen — handle them gracefully so your program
# doesn't crash and the user gets a helpful message instead.
# ============================================================

# ── 1. Basic try / except ────────────────────────────────────
# Wrap risky code in 'try'. If an error occurs, 'except' catches it.
print("── Basic try/except ────────────────")
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"100 ÷ {number} = {result}")
except ValueError:
    # Raised when the input can't be converted to int (e.g. user types "abc")
    print("❌ That's not a valid number. Please enter digits only.")
except ZeroDivisionError:
    # Raised when dividing by zero
    print("❌ Can't divide by zero.")

# ── 2. Catching multiple exceptions + a generic fallback ─────
print("\n── Multiple exceptions ─────────────")
try:
    data = [1, 2, 3]
    print(data[10])             # IndexError — index doesn't exist
except IndexError:
    print("❌ Index out of range.")
except Exception as e:
    # 'Exception as e' catches anything else and gives you the message
    print(f"❌ Unexpected error: {e}")

# ── 3. else — runs only if NO exception occurred ─────────────
print("\n── try / except / else ─────────────")
try:
    val = int("42")             # this will succeed
except ValueError:
    print("Conversion failed.")
else:
    print(f"✅ Conversion succeeded: {val}")   # → runs this

# ── 4. finally — ALWAYS runs, success or failure ─────────────
# Use for cleanup tasks: closing files, DB connections, etc.
print("\n── finally ─────────────────────────")
try:
    f = open("data/test.txt", "r")
    content = f.read()
    print(content[:50])         # print first 50 chars
except FileNotFoundError:
    print("❌ File not found.")
finally:
    print("(Cleanup done — this always runs)")

# ── 5. Raising your own exceptions ───────────────────────────
# Use 'raise' to enforce rules inside your own functions.
print("\n── raise custom exceptions ─────────")

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer.")
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age > 150:
        raise ValueError("Age seems unrealistic.")
    return age

for test_age in [-5, 200, 25]:
    try:
        valid = validate_age(test_age)
        print(f"✅ Valid age: {valid}")
    except (ValueError, TypeError) as e:
        print(f"❌ {e}")