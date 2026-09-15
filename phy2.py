
# # even_sum = 0
# # for i in range(1, 21):
# #     if i % 2 == 0:
# #         print("even number:", i)
# #         even_sum += i
# #         print("sum of even numbers:", even_sum)
# #     else:
# #         print("odd number:", i)
# # print("Final sum of even numbers:", even_sum)

# # rev_num = 0
# # n = int(input("Enter a number: "))
# # length = int(input("Enter the length of your number. This step is necessary else unexpected error will occur: "))
# # for i in range(0, length):
# #     rem = n % 10 
# #     rev_num = rev_num * 10 + rem
# #     n = n // 10
# # print("Reversed number:", rev_num)


# # a = int(input("Enter a: "))
# # b = int(input("Enter b: "))
# # c = int(input("Enter c: "))

# # if a > b and a > c:
# #     print("a is the largest number:", a)
# # elif b > a and b > c:
# #     print("b is the largest number:", b)
# # else:
# #     print("c is the largest number:", c)

# # even_or_odd = int(input("Enter a number to check if it is even or odd: "))
# # if even_or_odd % 2 == 0:
# #     print("The number is even.")
# # else:
# # #     print("The number is odd.")

# # prime = int(input("Enter a number to check if it is prime or not: "))
# # for i in range(1, prime):
# #     if prime % i == 0:
# #         print("The number is not prime")
# #         break
# #     else:
# #         print("The number is prime")
# #         break
# # if prime == 1:
# #     print("1 is not a prime number")
# # elif prime == 0:
# #     print("0 isn't prime number")

# # factorial_numb = int(input("Enter the number to do factorial: "))
# # final_factorial_numb = 1
# # for i in range(1, factorial_numb + 1):
# #     final_factorial_numb = final_factorial_numb * i
# # print(final_factorial_numb)


# # num1 = 0
# # fibonacci = int(input("Write till how long the fibonachi series do you want to run: "))
# # for i in range(0, fibonacci):
# #           num1 += num1 * i
# #           print(num1)


# # rev_num = 0
# # n = int(input("Enter a number: "))
# # a = n
# # characters_in_number = str(a)
# # length = len(characters_in_number)
# # for i in range(0, length):
# #     rem = n % 10 
# #     rev_num = rev_num * 10 + rem
# #     n = n // 10
# # if a == rev_num:
# #     print("The number is a pallindrome", rev_num)
# # else:
# #     print("The number is not a pallindrome")


# nam1 = int(input("Type the first number: "))
# nam2 = int(input("Type the second number: "))
# gcd = 0
# smallest_numb = 0
# if nam1 > nam2:
#     smallest_numb = nam2
# else:
#     print("Second is the largest number:")
#     smallest_numb = nam1

# for i in range(1, nam2 + 1):
#     gcd = i
#     if (nam1 % gcd == 0) & (nam2 % gcd == 0):
#         if smallest_numb == nam2 or nam1:
#             print(smallest_numb, "is the greatest divisor")
#             break
#         else:
#             print("UNEXPECTED ERROR")
#     else:
#         continue


