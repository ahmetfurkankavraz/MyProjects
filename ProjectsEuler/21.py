def dividesum(n):
    toplam = 0
    for i in range(1,n):
        if n % i == 0:
            toplam += i
    return (toplam)


liste = []
for i in range(1,10000):
    sayi = dividesum(i)
    sayi2 = dividesum(sayi)
    if sayi2 == i and sayi != i:
        liste.append(sayi)

toplam = 0
for i in range(len(liste)):
    toplam += liste[i]


print(toplam)
