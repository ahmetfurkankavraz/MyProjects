from bisect import bisect_left
def BinSearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i


liste = []
for i in range(1,1000):
    j = 1
    bölünmesayısı = 0
    while j * j <= i :
        if i % j == 0:
            bölünmesayısı += 1
        if bölünmesayısı > 1:
            break
        j += 1
    if bölünmesayısı == 1: 
        liste.append(i)


islem = input()
islem = int(islem)
x= 0
while x < islem:
    liste = input().rstrip().split()
    a = liste[0]
    b = liste[1]
    a = int(a)
    b = int(b)
    print(BinSearch(liste, a) - BinSearch(liste, b))
    x+=1