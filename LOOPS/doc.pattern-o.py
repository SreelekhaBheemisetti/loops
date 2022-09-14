# 0
# 0 1
# 0 1 4
# 0 1 4 9
# 0 1 4 9 16

n=int(input("enter the num:"))
i=1
while i<n:
    j=0
    while j<i:
        print(j*j, end=" ")
        j+=1
    i+=1
    print() 
