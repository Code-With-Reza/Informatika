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