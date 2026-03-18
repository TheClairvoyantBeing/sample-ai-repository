# ============================================================
# 03 - Variables
# Variables are named containers that store data in memory.
# ============================================================

# ── Naming rules ─────────────────────────────────────────────
# ✅ Valid names
my_name    = "Dennis"     # snake_case  ← recommended for Python
myAge      = 25           # camelCase   ← common in other languages
GRAVITY    = 9.8          # ALL_CAPS    ← convention for constants
_private   = "hidden"     # leading underscore ← internal use hint

# ❌ These would cause a SyntaxError (commented out on purpose):
# 1name  = "bad"          # cannot start with a number
# my-var = "bad"          # hyphens not allowed
# my var = "bad"          # spaces not allowed

# ── Assigning multiple variables at once ─────────────────────
# Different values on one line
first, second, third = "Gold", "Silver", "Bronze"
print(first, second, third)     # → Gold Silver Bronze

# Same value to multiple variables
x = y = z = 0
print(x, y, z)                  # → 0 0 0

# ── Variables can hold any data type ─────────────────────────
name       = "Jacob"        # str
age        = 30             # int
height     = 5.11           # float
is_student = True           # bool

print(f"{name} is {age} years old, {height}ft tall.")
print(f"Is student: {is_student}")

# ── type() tells you what type a variable holds ──────────────
print(type(name))           # → <class 'str'>
print(type(age))            # → <class 'int'>
print(type(height))         # → <class 'float'>
print(type(is_student))     # → <class 'bool'>

# ── Variables can be reassigned at any time ──────────────────
score = 0
print(f"Starting score: {score}")
score = 100
print(f"Updated score:  {score}")
