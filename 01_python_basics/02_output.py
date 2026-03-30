# ============================================================
# 02 - Output & the print() Function
# Learn every way Python can display information to the screen.
# ============================================================

# ── Basic print ──────────────────────────────────────────────
print("Hello, World!")          # String
print(42)                       # Integer
print(3.14)                     # Float
print(True)                     # Boolean

# ── Printing expressions directly ────────────────────────────
print(5 + 3)                    # → 8  (Python evaluates first)
print(10 * 2 - 5)               # → 15

# ── Multiple values in one print ─────────────────────────────
# Python adds a space between each value automatically
print("Name:", "Dennis", "| Age:", 25)

# ── The end parameter ────────────────────────────────────────
# By default print() adds a newline (\n) at the end.
# Use end="" to keep the cursor on the same line.
print("Loading", end="")
print(".", end="")
print(".", end="")
print(". Done!")                # → Loading... Done!

# ── The sep parameter ────────────────────────────────────────
# sep controls what goes BETWEEN multiple values (default is a space)
print("2026", "02", "25", sep="-")   # → 2026-02-25
print("a", "b", "c", sep=" | ")      # → a | b | c

# ── f-strings (most modern and readable way to format output) ─
name   = "Dennis"
age    = 25
height = 5.9

print(f"Hi, I am {name}.")
print(f"I am {age} years old and {height:.1f} feet tall.")
# {height:.1f} formats the float to 1 decimal place → 5.9