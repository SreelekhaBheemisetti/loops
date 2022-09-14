# 1  1  1  1  1
# 2  2  2  2  2
# 3  3  3  3  3
# 4  4  4  4  4
# 5  5  5  5  5

n=int(input("enter the number:"))
i=1
while i<=n:
    j=1
    while j<=n:
        print(i, end=" ")
        j+=1
    i+=1
    print()