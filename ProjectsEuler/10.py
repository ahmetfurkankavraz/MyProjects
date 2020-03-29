"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""



toplam = 0
for i in range(2,2000000):
    j = 1
    bölünmesayısı = 0
    while j * j <= i :
        if i % j == 0:
            bölünmesayısı += 1
        if bölünmesayısı > 2:
            break
        j += 1
    if bölünmesayısı == 1: 
        toplam += i
    print(i)
print(toplam) 