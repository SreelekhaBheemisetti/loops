i=0
while i<7:
    j=0
    while j<4:
        if j==0 and i<3 or i==3 or j==3 and i!=0:
            print("*", end=" ")
        else:
            print(end="  ")
        j+=1
    i+=1
    print()