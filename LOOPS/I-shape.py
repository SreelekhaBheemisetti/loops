i=0
while i<7:
    j=0
    while j<5:
        if j==3 or i==0 or i==6:
            print("*",end="  ")
        else:
            print(end="  ")
        j+=1
    i+=1
    print()