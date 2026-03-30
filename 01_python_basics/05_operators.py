# ============================================================
# 05 - Operators
# Operators let you perform calculations and comparisons.
# ============================================================

a = 15
b = 4

# ── 1. Arithmetic Operators ───────────────────────────────────
print("── Arithmetic ──────────────")
print(f"{a} + {b}  =", a + b)    # Addition       → 19
print(f"{a} - {b}  =", a - b)    # Subtraction    → 11
print(f"{a} * {b}  =", a * b)    # Multiplication → 60
print(f"{a} / {b}  =", a / b)    # Division       → 3.75  (always float)
print(f"{a} // {b} =", a // b)   # Floor division → 3     (drops decimal)
print(f"{a} % {b}  =", a % b)    # Modulus        → 3     (remainder)
print(f"{a} ** {b} =", a ** b)   # Exponent       → 50625

# Real-world use of modulus: check if a number is even or odd
number = 7
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")     # → 7 is odd

# ── 2. Comparison Operators — always return True or False ────
print("\n── Comparison ──────────────")
print(a == b)    # Equal to              → False
print(a != b)    # Not equal             → True
print(a >  b)    # Greater than          → True
print(a <  b)    # Less than             → False
print(a >= b)    # Greater than or equal → True
print(a <= b)    # Less than or equal    → False

# ── 3. Logical Operators — combine conditions ────────────────
print("\n── Logical ─────────────────")
age         = 20
has_ticket  = True

# and → BOTH must be True
print(age >= 18 and has_ticket)     # → True

# or  → AT LEAST ONE must be True
is_member   = False
has_coupon  = True
print(is_member or has_coupon)      # → True

# not → inverts the value
is_raining = False
print(not is_raining)               # → True  (it is NOT raining)

# ── 4. Assignment Operators — shortcuts for updating values ──
print("\n── Assignment ──────────────")
score = 100
score += 10     # same as score = score + 10
print(score)    # → 110
score -= 5
print(score)    # → 105
score *= 2
print(score)    # → 210
score //= 3
print(score)    # → 70

# ── 5. PEMDAS — Order of operations ─────────────────────────
# Parentheses → Exponents → Multiply/Divide → Add/Subtract
print("\n── PEMDAS ──────────────────")
print(2 + 3 * 4)        # → 14  (multiply first)
print((2 + 3) * 4)      # → 20  (parentheses change order)
print(2 ** 3 + 1)       # → 9   (exponent first)