
#1
# 3 3
# 5 5 5
# 7 7 7 7
# 9 9 9 9 9
 

n=int(input("enter the num:"))
i=1
while i<=n:
    j=1
    while j<=i:
        print(i,end="")
        j+=2
    i+=2
    print()