# ============================================================
# 09 - Functions
# Functions let you write reusable, organised blocks of code.
# Define once, call anywhere.
# ============================================================

# ── 1. Basic function — no parameters, no return ─────────────
def greet():
    print("Hello! Welcome to Python.")

greet()         # call the function
greet()         # call it again — no code duplication!

# ── 2. Function with parameters ──────────────────────────────
# Parameters are the inputs a function needs to do its job.
def greet_user(name):
    print(f"Hello, {name}! Glad you're here.")

greet_user("Dennis")
greet_user("Priya")

# ── 3. Function with a return value ──────────────────────────
# Use return to send a result back to the caller.
def add(a, b):
    return a + b

result = add(10, 25)
print(f"10 + 25 = {result}")       # → 10 + 25 = 35

# You can use the return value directly
print(f"5 * 7 = {add(5 * 1, 7)}")  # just for illustration

# ── 4. Default parameter values ──────────────────────────────
# If no argument is passed, the default is used.
def power(base, exponent=2):
    return base ** exponent

print(power(3))         # → 9   (uses default exponent=2)
print(power(3, 3))      # → 27  (overrides default)

# ── 5. *args — accept any number of positional arguments ─────
# *args collects extra positional arguments into a tuple.
def total(*args):
    result = 0
    for num in args:
        result += num
    return result

print(total(1, 2, 3))           # → 6
print(total(10, 20, 30, 40))    # → 100

# ── 6. **kwargs — accept any number of keyword arguments ─────
# **kwargs collects keyword arguments into a dictionary.
def display_profile(**kwargs):
    print("── Profile ─────────────")
    for key, value in kwargs.items():
        print(f"  {key.capitalize()}: {value}")

display_profile(name="Dennis", age=25, city="Bangalore", married=False)

# ── 7. Combining everything ──────────────────────────────────
def describe_order(item, quantity=1, *extras, **options):
    print(f"\nOrder: {quantity}x {item}")
    if extras:
        print(f"  Add-ons: {', '.join(extras)}")
    if options:
        for k, v in options.items():
            print(f"  {k}: {v}")

describe_order("Pizza", 2, "Extra Cheese", "Olives", size="Large", crust="Thin")
