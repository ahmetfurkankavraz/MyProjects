#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def asalsayı(x):
    liste= []
    i = 1
    while i < x:
        bölüm_sayısı = 0
        j = 1
        while j < x:
            if i % j == 0:
                bölüm_sayısı += 1
            j += 1
        if bölüm_sayısı == 2:
            liste.append(i)
        i += 1
    return liste


def üs_alma(x,liste):
    yeni_liste = []
    for i in liste:
        j = 1
        while i ** j <= x:
            j += 1
        j -=1
        sayı = i ** j
        yeni_liste.append(sayı)
    return yeni_liste


def çarpım(liste):
    çarpım = 1
    for i in liste:
        çarpım *= i
    print(çarpım)

liste = asalsayı(20)

çarpım( üs_alma( 20, liste ) ) 



