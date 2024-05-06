def Nomor_1():
    angka = [10, 5, 7, 3, 15, 20]
    print("Angka terkecil :", min(angka))
    print("Angka terbesar :", max(angka))

def Nomor_2():
    import random
    
    angka_random = random.randint(1, 100)
    tebakan = None
    while tebakan != angka_random:
        tebakan = int(input("Tebak angka (antara 1 dan 100) : "))
        if tebakan < angka_random:
            print("Tebakan terlalu kecil.")
        elif tebakan > angka_random:
            print("Tebakan terlalu besar.")
    print("Selamat! Anda berhasil menebak angka", angka_random)
    sleep(2)

def Nomor_3():
    for banyak in range(1,101):
        inputs = int(banyak)
        bil = range(1,inputs+1)
        hasil = 1
        
        for x in bil:
            hasil = hasil * x
        
        print(str(inputs)+"! =",hasil)

