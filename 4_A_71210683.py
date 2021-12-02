R = int(input("Input: "))
print("Output :")
T = 2
for K in range(1,R+1):
    for Y in range(1,(2*R)):
        if K+Y==R+1 or Y-K==R-1:
            print("*",end="")
        elif K==R and Y!=T:
            print("*",end="")
            T=T+2
        else:
            print(end=" ")
    print()