# def iAmGroo():
#     print('I am Groot')
# for i in range(0,10):
#     iAmGroo()

#Function with Arguments/parameters and Return Types
#Function with no Arugments/Paramenters and only Return Types
#Function with Arugments/parameters and No return Types
#Functions with No Arument and No Return Types

# def greet_someone(name):
#     print(f"Hello,{name}!")
#     print("Welcome to My Python Script")


# name=input("Please enter you name to Continue:")
# greet_someone(name)

# def sum(*args):
#     result = 0
#     for num in args:
#         result+=num
#     return result
    


# # a=int(input("Please enter Value A:"))
# # b=int(input("Please enter Value B:"))
# # c=int(input("Please enter Value c:"))

# # d=int(input("Please enter Value d:"))

# # e=int(input("Please enter Value e:"))
# #help(sum)
# print(sum(a=1,b=2,c,d,e))

def display_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

display_info(name="Dennis",age=20,sex="Male",married=False)
