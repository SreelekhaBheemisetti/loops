# *
# 2 2
# * * *
# 4 4 4 4
# * * * * *
# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         if i%2==0:
#             print(i,end=" ")
#         else:
#             print("*",end=" ")
#         j+=1
#     i+=1
#     print()

# 1 
# * 
# 1 2 
# * * 
# 1 2 3 
# * * * 
# 1 2 3 4 
# * * * * 
# 1 2 3 4 5 
# * * * * *
n=int(input("enter the no:"))
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end=" ")
        j=j+1
    print()
    k=1
    while k<=i:
        print("*",end=" ")
        k=k+1
    i=i+1
    print()

