# 0  
# 0 1  
# 0 2 4  
# 0 3 6 9  
# 0 4 8 12 16  
n=int(input("enter the num:"))
i=1
while i<n:
    j=0
    while j<=i:
        print(j*i, end=" ")
        j+=1
    i+=1
    print()