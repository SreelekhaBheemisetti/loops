# A
# B B
# C C C
# D D D D
# E E E E E


# i=65
# while i<=69:
#     j=65
#     while j<=i:
#         print(chr(i), end=" ")
#         j+=1
#     print()
#     i+=1

# A
# 1 1
# C C C
# 2 2 2 2 
# E E E E E

# i=1
# while i<=5:
#     j=1
#     while j<=i:
#         if i%2!=0:
#             print(chr(i+64),end="")
#         else:
#             print(i-1,end="")
#         j+=1
#     i+=1
#     print()
    


i=1
while i<=10:
    if i==6 or i==7:
        print("*",end="")
    else:
        print(i, end="")
    i+=1
    print()