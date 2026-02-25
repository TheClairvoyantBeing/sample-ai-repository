# =============================================================
# 13 - Mini Projects
# Two fun beginner projects to practise everything you've learnt
# =============================================================


# -------------------------------------------------------------
# Project 1: ASCII Art Bot
# -------------------------------------------------------------

print("--- ASCII Art Bot ---")
print("  ********  ")
print(" *        * ")
print("*  ^    ^  *")
print("*     >    *")
print("*  \\____/  *")
print("*          *")
print(" ********** ")
print("Hi! Welcome — I just smile :)")


# -------------------------------------------------------------
# Project 2: Simple Calculator
# -------------------------------------------------------------

print("\n--- Simple Calculator ---")

a  = float(input("Enter first number : "))
b  = float(input("Enter second number: "))
op = input("Enter operator (+  -  *  /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Error: Invalid operator. Use one of +  -  *  /")
