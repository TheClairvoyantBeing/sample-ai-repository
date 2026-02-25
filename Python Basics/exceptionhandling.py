# try:
#     number=int(input("Enter a number: "))
#     result=100/number
#     print(result)
# except ValueError:
#     print("That is not a number, please enter a valid number")
# except ZeroDivisionError:
#     print("You cannot divide by zero, please enter a valid number")
# except Exception as e:
#     print(f"An error occured: {e}")

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age >200:
        raise ValueError("Invalid Age")
    return age

try: 
    validate_age(-10)
except ValueError as e:
    print(e)