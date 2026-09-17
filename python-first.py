from pyparsing import nums


print("hello world")
x = 10
print(x)
y = "hello"
print(y)
print("datatype of x is: " + str(type(x)))
print("datatype of y is: " + str(type(y)))

img_numb = 2 + 3j
print(img_numb)
print(type(img_numb))
a = [1,2,3,4]
print(a)
b = [1, "alasdjf", 2,3]
print(b)
print(type(b))
# aklj ;asd fasd;l f asdlfk;j asdlk 
fruits = ["apple", "orange", "banana"]
print(fruits)
fruits.append("grapes")
print(fruits)
point = (1,2,3)
print(point)
print(type(point))
nums = {1,2,3,4,5}
print(type(nums))

name = "Prangshu"
greet = "hello " + name
print(greet)
print(greet[0:15])

<<<<<<< HEAD
# # # # student = {
# # # #     "name": "Prangshu",
# # # #     "age": 20,
# # # #     "grade": "A"
# # # # }
# # # # print(student)
# # # # print(student["name"])
# # # # student["age"] = 21
# # # # print(student)
# # # # Full_name = "Prangshu"

# # # import math
# # # radius = 5
# # # def area(r):
# # #     area = math.pi * r * r
# # #     return area
# # # print(area(radius))


# # # # for fruit in ["apple", "banana", "cherry"]:
# # # #     print(fruit)

# # for j in range(1, 7):
# #     print("*" * 6)

# # for i in range(1, 7):
# #     print("*" * (i+0))

    
# # for i in range(1, 7):
# #     print(" " * (6 - i) + "*" * (2 * i - 1))


# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print(number, "is an even number")
# else:
#     print(number, "is an odd number")

# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")


# score = 0
# for i in range(1, 101):
#     score = i
#     if score >= 90:
#         print( "Your score:", score, "Grade: A")
#     elif score >= 80:
#         print( "Your score:", score, "Grade: B")
#     elif score >= 70:
#         print( "Your score:", score, "Grade: C")
#     elif score >= 60:
#         print( "Your score:", score, "Grade: D")
#     elif score >= 50:
#         print( "Your score:", score, "Grade: E")
#     else:
#         print( "Your score:", score, "Grade: F")

# print("Check the score and grade criteria above ---^ ")
# print("Check your score and grade below ---v ")
# score = int(input("Enter your score: "))
# if score >= 90:
#         print( "Your score:", score, "Grade: A")
# elif score >= 80:
#         print( "Your score:", score, "Grade: B")
# elif score >= 70:
#         print( "Your score:", score, "Grade: C")
# elif score >= 60:
#         print( "Your score:", score, "Grade: D")
# elif score >= 50:
#         print( "Your score:", score, "Grade: E")
# else:
#         print( "Your score:", score, "Grade: F")


=======
student = {
    "name": "Prangshu",
    "age": 20,
    "grade": "A"
}
print(student)
print(student["name"])
student["age"] = 21
print(student)
Full_name = "Prangshu Pranjal Saikia"
>>>>>>> parent of bd7578e (4th)
