  # Procedure menu()
def menu():
    print("Kalkulator Bermenu")
    print("1. Tambah")
    print("2. Tolak")
    print("3. Darab")
    print("4. Bahagi")
    print("5. Tamat")

  # Function dptPilihanPengguna()
def dptPilihanPengguna():
    noPilihan = 0
    while (noPilihan < 1) or (noPilihan > 5):
        noPilihan = int(input("Pilihan anda [1 hingga 5]: "))
    return noPilihan

  # Function dptDuaNombor()
def dptDuaNombor():
    nombor_1 = int(input("Masukkan nombor pertama: "))
    nombor_2 = int(input("Masukkan nombor kedua: "))
    return nombor_1,nombor_2

  # Procedure kiraCerak()
def kiraCerak(jenisOperator,a,b):
    if jenisOperator == 1:
        print("Output: "+str(a)+" + "+str(b)+" = "+str(a+b)+"\n")
    elif jenisOperator == 2:
        print("Output: "+str(a)+" - "+str(b)+" = "+str(a-b)+"\n")
    elif jenisOperator == 3:
        print("Output: "+str(a)+" * "+str(b)+" = "+str(a*b)+"\n")
    elif jenisOperator == 4:
        print("Output: "+str(a)+" / "+str(b)+" = "+str(a/b)+"\n")

  # main -------------------------------------------------------------------------
aktif = 1
while aktif == 1:
    menu()
    jenisOperator = dptPilihanPengguna()
    if jenisOperator == 5:
        aktif = 0
    else:
        [nom_1,nom_2] = dptDuaNombor()
        kiraCerak(jenisOperator,nom_1,nom_2)
print("Terimah kasih kerana menggunakan saya. ")