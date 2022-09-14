 
#          1    
#        2 1  
#      3 2 1 
#    4 3 2 1 
#  5 4 3 2 1

n=int(input("enter the num:"))
i=1
while i<=n:
    j=n
    while j>=i:
        print(" ",end=" ")
        j-=1
    k=0
    while k<i:
        print(i-k,end=" ")
        k+=1
    i+=1
    print()

# n=5
# for x in range(1,n+1):
#     for y in range(n,0,-1):
#         if x>=y:
#             print(y,end=" ")
#         else:
#             print(" ",end=" ")
#     print()
