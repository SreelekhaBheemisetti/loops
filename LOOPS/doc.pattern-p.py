# 1
# 4 4
# 9 9 9
# 16 16 16 16
# 25 25 25 25 25
n=int(input("enter the num:"))
i=1
while i<n:
    j=1
    while j<=i:
        print(i*i, end=" ")
        j+=1
    i+=1
    print()