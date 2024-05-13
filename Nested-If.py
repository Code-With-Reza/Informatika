while True:
    try:
        u = int(input("Masukkan Umur : "))
        k = input("Masukkan Jenis Kelamin (L/P) : ").upper()
        if k not in ['L', 'P']:
            raise ValueError("LP")
        break
    except ValueError as e:
        if str(e) == "LP":
            print("Masukkan 'L' atau 'P'!")
        else:
            print("Masukkan angka untuk umur!")
        
if u >= 40:
    if k == "L":
        status = "Pria Tua"
    elif k == "P":
        status = "Wanita Tua"
elif u >= 17:
    if k == "L":
        status = "Pria Dewasa"
    elif k == "P":
        status = "Wanita Dewasa"
else:
    if k == "L":
        status = "Perjaka"
    elif k == "P":
        status = "Gadis"

print(status)

