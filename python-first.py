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