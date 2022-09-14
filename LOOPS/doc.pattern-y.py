#           *  
#         * * * 
#       * * * * *  
#     * * * * * * *

n=int(input("enter the number"))
i=0
while i<n:
    j=n-i-1
    while j>0:
        print(end=" ")
        j-=1
    k=i+1
    while k>0:
        print("*",end=" ")
        k-=1
    i+=2
    print()

# n=int(input("enter the num:"))
i=5
while i>0:
    j=0
    while j<5:
        print(end=" ")
        j+=1
    k=i
    while k<=i:
        print("*", end=" ")
        k+=1
    i-=2
    print()
