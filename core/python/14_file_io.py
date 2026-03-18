# ============================================================
# 14 - File I/O (Reading & Writing Files)
# Python can read from and write to files on your computer.
# Always use the 'with' statement — it closes the file for you.
# ============================================================

import os

DATA_DIR = "../data"   # data/ lives one level up from lessons/

# ── 1. Write a file ──────────────────────────────────────────
# Mode "w" creates the file (or overwrites it if it already exists).
output_path = os.path.join(DATA_DIR, "output.txt")

with open(output_path, "w") as file:
    file.write("Line 1: Hello from Python!\n")
    file.write("Line 2: Writing files is easy.\n")
    file.write("Line 3: Always use 'with open()' — it's the safest way.\n")

print(f"✅ File written: {output_path}")

# ── 2. Read the whole file at once ───────────────────────────
print("\n── Read entire file ────────────────")
with open(output_path, "r") as file:
    content = file.read()
print(content)

# ── 3. Read line by line ─────────────────────────────────────
# Great for large files — reads one line at a time, saves memory.
print("── Read line by line ───────────────")
with open(output_path, "r") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"  [{line_number}] {line.strip()}")

# ── 4. Append to an existing file ────────────────────────────
# Mode "a" adds to the end — it never overwrites existing content.
with open(output_path, "a") as file:
    file.write("Line 4: Appended later without losing original content.\n")

print("\n✅ Line appended.")

# ── 5. Read from an existing file (test.txt from Python Basics) ─
print("\n── Read data/test.txt ──────────────")
test_path = os.path.join(DATA_DIR, "test.txt")
try:
    with open(test_path, "r") as file:
        lines = file.readlines()           # list of lines
    print(f"  File has {len(lines)} lines.")
    print(f"  First line: {lines[0].strip()}")
except FileNotFoundError:
    print(f"  '{test_path}' not found — skipping.")

# ── 6. Always handle file errors ─────────────────────────────
print("\n── Error handling ──────────────────")
try:
    with open("data/ghost.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("❌ File not found.")
except PermissionError:
    print("❌ You don't have permission to read that file.")
except Exception as e:
    print(f"❌ Unexpected error: {e}")

# ── File mode reference ──────────────────────────────────────
print("\n── File mode cheat sheet ───────────")
modes = {
    '"r"': "Read   — error if file doesn't exist",
    '"w"': "Write  — creates file, overwrites if exists",
    '"a"': "Append — creates file, adds to end if exists",
    '"x"': "Create — error if file already exists",
}
for mode, desc in modes.items():
    print(f"  {mode}  →  {desc}")
