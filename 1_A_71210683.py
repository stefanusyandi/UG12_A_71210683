v = input("Masukkan deret angka : ")
n = 0
z = (v.split(","))
print("Total :",end=" ")
for p in z:
    p=int(p)
    if p%2==1:
        n = n-p
        print(p*-1, end=" ")
    else: 
        n = n+p 
        print("+",p,end=" ")
print()
print("Hasil perhitungan diatas ialah", n)