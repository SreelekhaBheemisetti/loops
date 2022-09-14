i=0
while i<7:
    j=0
    while j<4:
        if i==0 and (j!=0 and j!=3) or i==1 and (j!=1 and j!=2) or i==2 and j==3 or i==3 and j==2 or i==4 and j==1 or i==5 and j==0 or i==6:
            print("*", end="  ")
        else:
            print(end="  ")
        j+=1
    i+=1
    print()