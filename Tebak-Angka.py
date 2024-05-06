import random

angkabuanyaq = random.randrange(1,20)


wongedannebak = int(input("Tebak bang!\n"))

while wongedannebak != angkabuanyaq:
    if wongedannebak > angkabuanyaq:
        message = "kebanyakan"
    elif wongedannebak < angkabuanyaq:
        message = "kecil kali"
    #print("Debug : "+str(angkabuanyaq))
    print("salah! ente "+message)
    wongedannebak = int(input("Tebak bang!\n"))

print("BENER!")