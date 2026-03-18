# ============================================================
# 13 - Mini Projects
# Combine everything you've learnt into two small programs.
# ============================================================


# ============================================================
# PROJECT 1: ASCII Art Bot 🤖
# Practises: print(), strings
# ============================================================
print("╔══════════════════════╗")
print("║   ASCII Art Bot 🤖   ║")
print("╚══════════════════════╝")
print()
print("  ┌──────────┐  ")
print("  │ ^      ^ │  ")
print("  │    >>    │  ")
print("  │  \\____/  │  ")
print("  └──────────┘  ")
print("Hi! I'm your Python bot. I just smile 😊")
print()


# ============================================================
# PROJECT 2: Interactive Calculator 🧮
# Practises: input(), type conversion, conditionals, functions,
#            loops, exception handling
# ============================================================
print("╔══════════════════════╗")
print("║   Calculator 🧮      ║")
print("╚══════════════════════╝")

def calculate(a, b, op):
    """Perform one calculation and return the result as a string."""
    if op == "+":
        return f"{a} + {b} = {a + b}"
    elif op == "-":
        return f"{a} - {b} = {a - b}"
    elif op == "*":
        return f"{a} × {b} = {a * b}"
    elif op == "/":
        if b == 0:
            return "❌ Cannot divide by zero."
        return f"{a} ÷ {b} = {a / b:.4f}"
    elif op == "**":
        return f"{a} ^ {b} = {a ** b}"
    elif op == "%":
        return f"{a} mod {b} = {a % b}"
    else:
        return f"❌ Unknown operator '{op}'. Use: + - * / ** %"

# Keep asking until the user types 'quit'
while True:
    print("\nType 'quit' to exit.")
    user_input = input("Enter calculation (e.g. 10 + 5): ").strip()

    if user_input.lower() == "quit":
        print("Goodbye! 👋")
        break

    # Parse: split "10 + 5" into ['10', '+', '5']
    parts = user_input.split()
    if len(parts) != 3:
        print("❌ Format: <number> <operator> <number>  e.g. 10 + 5")
        continue

    try:
        num1 = float(parts[0])
        op   = parts[1]
        num2 = float(parts[2])

        # Use int display if the numbers are whole numbers
        num1 = int(num1) if num1.is_integer() else num1
        num2 = int(num2) if num2.is_integer() else num2

        print(calculate(num1, num2, op))
    except ValueError:
        print("❌ First and third values must be numbers.")
