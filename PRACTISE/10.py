for i in range(1,6):
    print(" "*(5-i),end="")
    for j in range(i):
        print("*",end="")

    for j in range(i,1,-1):
        print("*", end="")
    print()