def listetoplam(liste):
    toplam = 0
    for i in range(len(liste)):
        toplam += liste[i]
    return toplam

def bolentoplamı(a):
    liste = []
    for i in range(1,int(a/2+1)):
        if a % i == 0:
            liste.append(i)
    toplam = listetoplam(liste)
    if toplam > a:
        return a
    else:
        return 0

listeabundant = []
listedecendent = []
for i in range(1,28124):
    if bolentoplamı(i) != 0:
        listeabundant.append(i)
        print(i)
    elif bolentoplamı(i) == 0:
        listedecendent.append(i)

for i in range(len(listeabundant)):
    for j in range(len(listeabundant)):
        sayi = listeabundant[i] +listeabundant[j]
        listeabundant.append(sayi)
    print(i)

for i in range(len(listedecendent)):
    if listedecendent[i] in listeabundant:
        del listedecendent[i]
        i -= 1
    print(i)

toplam = 0
for x in listedecendent:
    toplam += x

print(toplam)