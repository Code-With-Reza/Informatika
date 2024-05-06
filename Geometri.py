kotake = int(input("ANGKA BANG\n"))
kotake = range(kotake)
for p in kotake:
    for l in kotake:
        print("*", end=" ")
    print("")

segitiga = int(input("ANGKA BANG\n"))
segitiga = range(segitiga)
i = 0
for p in segitiga:
        print(" " * p - i + "*" * p)
        i += 1