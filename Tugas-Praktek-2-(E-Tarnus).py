# Nomor 1
angka = [10, 5, 7, 3, 15, 20]
print("Angka terkecil:", min(angka))
print("Angka terbesar:", max(angka))

# Nomor 2
import random

angka_random = random.randint(1, 100)
tebakan = None
while tebakan != angka_random:
    tebakan = int(input("Tebak angka (antara 1 dan 100): "))
    if tebakan < angka_random:
        print("Tebakan terlalu kecil.")
    elif tebakan > angka_random:
        print("Tebakan terlalu besar.")
print("Selamat! Anda berhasil menebak angka", angka_random)
sleep(2)

# Nomor 3
def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)

for i in range(1, 101):
    print("Faktorial dari", i, "adalah", faktorial(i))

