# ============================================================
# 07 - Conditional Statements
# Make decisions in your code based on conditions.
# ============================================================

# ── 1. Basic if / else ───────────────────────────────────────
password = "secret@123"

if password == "secret@123":
    print("✅ Access Granted")
else:
    print("❌ Access Denied")

# ── 2. if / elif / else — multiple branches ──────────────────
# elif = "else if" — checked only when all above conditions are False
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score} → Grade: {grade}")   # → Score: 85 → Grade: B

# ── 3. Nested if — conditions inside conditions ──────────────
age         = 20
has_license = True

if age >= 18:
    print("Old enough to drive.")
    if has_license:
        print("✅ You can drive!")
    else:
        print("⚠️  Get a licence first.")
else:
    print("❌ Too young to drive.")

# ── 4. Logical operators in conditions ───────────────────────

# and — BOTH conditions must be True
age        = 20
has_ticket = True
if age >= 18 and has_ticket:
    print("🎵 Enjoy the concert!")
else:
    print("Cannot enter the concert.")

# or — AT LEAST ONE condition must be True
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("🎉 It's the weekend!")
else:
    print("Back to work.")

# not — inverts a condition
is_banned = False
if not is_banned:
    print("Welcome to the platform.")

# ── 5. Ternary operator — one-line if/else ───────────────────
# Syntax: value_if_true  if  condition  else  value_if_false
age    = 21
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")                  # → Status: adult

# Common use: picking a label without a full if/else block
temperature = 38
weather = "Hot 🌞" if temperature > 30 else "Cool 🌤️"
print(f"Weather: {weather}")
