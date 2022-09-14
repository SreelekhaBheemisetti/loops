# write a program to get the square of each digit
# for example:
# input=234  output=4916
# 2 square =4
# 3 square =9
# 4 square =16

# a=int(input("enter the a:"))
# s=0
# while a>0:
#     digit=a%10
#     s=digit*digit
#     a=a//10
#     print(s, end="")


# print from 1-100, initialisation is 50, without using the number 100

# a=50
# i=1
# while i<a:
#     i+=1
#     b=50+i
#     print(i,b)

# pattern
# 1 2 3 
# 2 3 4 
# 3 4 5
    
# i=1
# while i<4:
#     j=1
#     while j<4:
#         if i==2:
#             print(j+1,end=" ")
#         elif i==3:
#             print(j+2,end=" ")
#         else:
#             print(j, end=" ")
#         j+=1
#     i+=1
#     print()

# print_odd_continue_even_break
# if the number is odd continue and if the number is even break the loop

# while True:
#     a=int(input("enter the number:"))
#     if a%2!=0:
#         break
#     else:
#         continue

# without numbers !!
# Write a program that always returns 5
# you can't use any of the following characters: 0123456789*+-/

# a="Latha"
# b=len(str(a))
# print(b)


# The factors of 1 are just 1 itself.So the answer is YES. The factors of 2 are 1 and 2.
# It has even number of factors.The answer is NO. The factors of 7 are 1 and 7.It has even number of factors.
# The answer is NO.The factors of 169 are 1,13 and 169.It has odd number of factors.The answer is YES.

# n=int(input("enter the number:"))
# count=0
# i=1
# while n>0:
#     if n%i==0:
#         if n%2==0:
#             print("NO")
#         else:
#             print("YES")
#     i+=1

# Implement a program that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.
# The binary number returned should be a string.
# Examples:(Input1, Input2 --> Output (explanation)))
# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)

a=int(input("enter the a:"))
b=int(input("enter the b:"))
while a>0:
    c=a+b
    # a+=1
    print(bin(c))
    # a+=1