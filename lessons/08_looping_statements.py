# ============================================================
# 08 - Looping Statements
# Loops let you repeat a block of code without duplicating it.
# ============================================================

# ── 1. while loop — repeat WHILE a condition is True ─────────
# Use when you don't know in advance how many times to loop.
print("── while loop ──────────────")
count = 1
while count <= 5:
    print(f"  Count: {count}")
    count += 1          # IMPORTANT: always update the condition variable
                        # or you get an infinite loop!
print("  Done!")

# ── 2. for loop with range() — repeat a fixed number of times ─
print("\n── for loop with range() ───")
# range(start, stop, step) — stop is excluded
for i in range(1, 6):           # 1, 2, 3, 4, 5
    print(f"  Item {i}")

# Count backwards
for i in range(5, 0, -1):      # 5, 4, 3, 2, 1
    print(i, end=" ")
print()                         # newline after

# ── 3. for loop over a list ──────────────────────────────────
print("\n── for loop over a list ────")
fruits = ["apple", "banana", "cherry", "mango"]
for fruit in fruits:
    print(f"  I like {fruit}")

# ── 4. Nested loops — a loop inside a loop ───────────────────
# Classic example: print a star pattern
print("\n── Nested loops (star pattern)")
for row in range(1, 6):
    for col in range(row):
        print("*", end="")
    print()                 # newline after each row
# *
# **
# ***
# ****
# *****

# ── 5. break — exit the loop early ──────────────────────────
print("\n── break ───────────────────")
numbers = [3, 7, 12, 5, 19, 4]
target  = 12

for num in numbers:
    if num == target:
        print(f"  Found {target}! Stopping search.")
        break               # exits the loop immediately
    print(f"  Checked {num}...")

# ── 6. continue — skip to the next iteration ────────────────
print("\n── continue ────────────────")
for i in range(1, 11):
    if i % 2 == 0:
        continue            # skip even numbers
    print(i, end=" ")       # prints only odd numbers: 1 3 5 7 9
print()

# ── 7. else on a loop ────────────────────────────────────────
# The else block runs ONLY if the loop completed without a break
print("\n── loop else ───────────────")
search_for = 99
for num in [1, 2, 3, 4, 5]:
    if num == search_for:
        print("Found it!")
        break
else:
    print(f"  {search_for} was not found in the list.")