#pisagor sayılarının yazdıran program

pisagorsayilar = []
for a in range(1, 101):
    for b in range(1, 101):
        z = (a**2 + b**2) ** (1/2)
        if int(z) == float(z):
            z = int(z)
            pisagorsayilar.append((a, b, z))
print(pisagorsayilar)