"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
liste = []
for i in range(1,120000):
    j = 1
    bölünmesayısı = 0
    while j * j <= i :
        if i % j == 0:
            bölünmesayısı += 1
        j += 1
    if bölünmesayısı == 1: 
        liste.append(i)
    print(i)

print(liste[10001])  

#listede 1'i de saymaktadır. Dikkat!!!


