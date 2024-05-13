def Nested_Loop1():
    batas_perkalian = int(input("Masukkan batas perkalian: "))
    for i in range(1, batas_perkalian + 1): # Perulangan luar (baris)
      for j in range(1, batas_perkalian + 1): # Perulangan dalam (kolom)
        hasil_kali = i * j
        print(f"{i} x {j} = {hasil_kali:3}", end="\n")

      print() # Pindah ke baris baru setelah setiap baris

def Nested_Loop2():
    import random
    batas_tebakan = 10
    tebakan = 0
    angka_rahasia = random.randint(1, 100)

    while tebakan < batas_tebakan:
        while True:
            try:
                tebakan_user = int(input("Tebak angka antara 1 - 100 : "))
                tebakan += 1
                break
            except ValueError:
                print("Masukkan angka!")
    
        while tebakan_user != angka_rahasia:
            if tebakan_user < angka_rahasia:
                print("Terlalu rendah! Coba lagi.")
            else:
                print("Terlalu tinggi! Coba lagi.")
            
            while True:
                try:
                    tebakan_user = int(input("Tebak lagi : "))
                    tebakan += 1
                    break
                except ValueError:
                    print("Masukkan angka!")
    
            if tebakan_user == angka_rahasia:
               print(f"Selamat! Anda menebak angka rahasia dalam {tebakan} kali tebakan.")
               break
        break
    