#Lists
students=["Dennis","Manjunath","Kavya","Sneha"]
numbers=[1,2,3,4,4,5]
mixed=[1,"Dennis",25.4,True]

#print(students)
#students[1]="Arun"
#students.pop()
# print(students)
# #Length
# print("Lenght of students listy is ",len(students))
# #sum,min,mx
# print("Sum of all numbers in Numbers list is ",sum(numbers))
# print("min number in the numbers list is ",min(numbers))
# print("max number in the numbers list is ",max(numbers))
# #count
# print("Total number of occurences of number 4 is ",numbers.count(4))
# #find index
# print("The index of the List Item Manjunath is ",students.index("Manjunath"))
# #sort
# students.sort()
# print(students)
# #revese
# numbers.reverse()
# print(numbers)
# #Check Membership
# print("Manjunath"  in students)
# for name in students:
#     print(name)

# print(range(len(students)))

# for i in range(len(students)):
#     print(f"{i}: {students[i]}")

# print(enumerate(students))
# for k,v in enumerate(students):
#     print(f"{k}: {v}")

#squares = []
# for i in range(1,6):
#     squares.append(i ** 2)

# squares = [i ** 2 for i in range(1,6)]   
# print(squares)

#Tuples
coordinates=(10,20)
person = ("kavya",25,"Chitradurga")
#print(person[2])

name,age,district=person

#print(f"I am {name}, from {district}. I am {age} years old")

#Dictionaries
mathClass={}

student={
    "name":"Dennis",
    "age":25,
    "grade":"A",
    "courses":["Math","Science","Social Science"]
}

#print(student["name"])
student["phone"]="8908908900"

#print(student.get("phone","User's Phone number doesn't exist"))

student['age']=26
#print(student)

#student.pop("grade")
#print(student)
# for key in student:
#     print(f"{key}: {student[key]}")

# for key,value in student.items():
#     print(f"{key}:{value}")

#Sets

empty_set=set()
numbers=[1,2,3,1,3,4,3,6,7,888,9,2,4,5,5,5,5,5,5]
unique_numbers=set(numbers)
print(numbers)
print(unique_numbers)

unique_numbers.discard(999)