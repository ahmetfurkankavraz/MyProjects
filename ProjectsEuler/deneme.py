def fantastic(x):
    x = str(x)
    uzunluk = len(list(x))
    uzunluk = uzunluk * 3
    x = int(x)
    while x < 3 ** uzunluk:
        uzunluk -= 1
    toplam = 0
    while uzunluk >= 0:
        toplam += 3 ** uzunluk
        if toplam > x:
            toplam -= 3 ** uzunluk

        uzunluk -= 1
    return toplam


sayi = input()
sayi = int(sayi)
x = 0
while x < sayi:
    yeni = input()
    
    sonuc = fantastic(yeni)
    print(sonuc)
    x += 1


