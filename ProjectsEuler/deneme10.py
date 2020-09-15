def trace(liste):
    sayi = 0
    for i in range(len(liste)):
        sayi1 = liste[i][i]
        sayi += int(sayi1)
    return sayi
    
def rowlatinsquares(liste):
    n = len(liste)
    new = []
    
    for i in range(n):
        yeniliste = liste[i]
        yeniliste = sorted(yeniliste)
        counter = 0
        for j in range(0,len(yeniliste) - 1):
            if yeniliste[j] == yeniliste[j+1]:
                counter += 1
        if counter > 0:
            counter += 1
        new += [counter]
        if counter > 0:
            counter += 1
    new = sorted(new)
    son = new[-1]
    return son
        
        
def collatinsquares(liste):
    n = len(liste)
    new = []
    
    liste = [[row[i] for row in liste] for i in range(len(liste))]

    for i in range(n):
        yeniliste = liste[i]
        yeniliste = sorted(yeniliste)
        counter = 0
        for j in range(len(yeniliste) - 1):
            if yeniliste[j] == yeniliste[j+1]:
                counter += 1
        if counter > 0:
            counter += 1
        new += [counter]
    new = sorted(new)
    son = new[-1]
    return son
        
sayi = input()
sayi = int(sayi)
i = 0
while i<sayi:
    ikincisayi = input()
    ikincisayi = int(ikincisayi)
    liste = []
    for x in range(ikincisayi):
        liste += [input().rstrip().split()]
    yazi = i+1    
    yazi = "Case #{}: {} {} {}".format(yazi,trace(liste), rowlatinsquares(liste),collatinsquares(liste) ) 
    print(yazi)
    i += 1
    
    
    
liste = [[2,2,3],[1,2,3],[2,2,3]]

print(collatinsquares(liste))