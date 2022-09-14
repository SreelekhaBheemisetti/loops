# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         if j%2!=0:
#             print(chr(j), end=" ")
#         else:
#             print(j-1, end=" ")
#         j+=1
#     i+=1
#     print()

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         if i%2==0:
#             print(i, end=" ")
#         else:
#             print(chr(j+64), end=" ")
#         j+=1
#     i+=1
#     print()


# i=10
# while i<=50:
#     j=10
#     while j<i:
#         print(i-j,end=" ")
#         j+=10
#     i+=10
#     print()



# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         if j%2!=0:
#             print(chr(j+64),end=" ")
#         else:
#             print(j-1,end=" ")
#         j=j+1
#     i=i+1
#     print()



# multiplication tabel

user=int(input("enter the number:"))
i=0
product=1
while i<10:
    i=i+1
    product=user*i
    print(user,"*",i,"=",product)



# take 2 user inputs and multiply both without using multiplication

# a=int(input("enter the a:"))
# b=int(input("enter the b:"))
# c=0
# while a>0:
#         a=a-1
#         c=c+b
# print(a+c)