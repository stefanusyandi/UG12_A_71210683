b = str(input("Masukkan nama: "))
kr = []
dn = []
while b != "STOP":
    f = "Masukkan nomor kursi"+b+" :  "
    m = input(f)
    if m not in kr:
        kr.append(m)
        dn.append(b)
    else:
        print("Mohon maaf kursi tersebut telah terisi")
    b = str(input("Masukkan nama: "))
print("List kursi yang telah terisi :")
for i in range (len(kr)):
    print("Kursi nomor %s telah diisi oleh %s"%(kr[i],dn[i]))