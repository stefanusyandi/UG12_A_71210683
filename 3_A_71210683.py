q = input("input : ")
w = len(q)
print("Output :",end="")
for o in range(w):
    print(q[:o])
for l in range(w,0,-1):
    print(q[:l])