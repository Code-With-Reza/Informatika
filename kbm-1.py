print("==== Tugas 1 ====")
number = int(input("masukkan nilai : "))
if number % 10 == 0:
    gg = "genap"
else:
    gg = "ganjil"

if number == 0:
    pn = "nol"
elif number > 0:
    pn = "positif"
else:
    pn = "negatif"

print(pn+"\n"+gg)


print("\n==== Tugas 2 ====")

try:
    b1 = int(input("masukkan bilangan pertama : "))
    op = input("+ atau - atau * atau / : ")
    b2 = int(input("masukkan bilangan kedua : "))
    if op == "+":
        output = b1+b2
    elif op == "-":
        output = b1-b2
    elif op == "*":
        output = b1*b2
    elif op == "/":
        output = b1/b2
    else:
        output = "operator salah!"
    print(output)
except:
    print("masukkan angka!")
