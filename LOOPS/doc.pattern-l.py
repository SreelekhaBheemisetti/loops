# 1
# 2 3
# 4 5 6
# 7 8 9 10

n=int(input("enter the number:"))
i=1
k=1
while i<n:
    j=1
    while j<=i:
        print(k, end=" ")
        j+=1
        k+=1
    print()
    i+=1
