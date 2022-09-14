# n=int(input("enter the number:"))
# temp=n
# r=0
# while n>0:
#     digit=n%10
#     r=r*10+digit
#     n=n//10
# if temp==r:
#     print(temp, "is a palindrome number")
# else:
#     print("not palindrome")n=int(input("enter the number:"))

string=input("enter the name:")
i=-1
b=""
while i>=-len(string):
    c=string[i]
    b=b+c
    i=i-1
if b==string:
    print("palindrome")
else:
    print("not palindrome")

