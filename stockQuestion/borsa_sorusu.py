"""
Türkiye borsasında hisseler 3 ana başlık altında incelenirler.
Bunlar :
Yıldız Pazar ~ Z
Ana Pazar ~ N
Alt Pazar ~ T'dir.

Hisselerde spekülatif hareketleri önlemek amacıyla fiyat marjı uygulaması yapılmaktadır.
Fiyat marjı ile hisselerin yükselebileceği maksimum fiyat olan tavan fiyat, düşebileceği minimum fiyat olan taban fiyat belirlenir.
Örn: %10 fiyat marjı uygulanan bir hissenin fiyatı 10.24 olsun.
Taban fiyat = 10.24 - 10.24 * 10 / 100
Tavan fiyat = 10.24 - 10.24 * 10 / 100 ile bulunur.
Hissenin fiyat marjından daha fazla artıp azalmasını önlemek amacıyla bulunan tavan fiyat aşağıya, taban fiyat yukarıya yuvarlanır.

Salgın öncesinde %20 olan fiyat marjı, borsanın fazla zarar görmesini engellemek amacıyla %10a çekilmişti.
Yavaş yavaş normal hayata dönmek amacıyla yakında geçilecek uygulama ile:
Yıldız Pazar için marj %20
Ana Pazar için marj %15
Alt Pazar için marj %10 olacaktır.

Bunlarla birlikte hisse fiyatı:
20ye kadar olan hisseler her 1 kuruşta,
20 ila 50 arasında olan hisseler 2 kuruşta,
50 ila 100 arasında olan hisseler 5 kuruşta,
100den yukarısı ise 10 kuruşta bir işlem görürler.
Not: Borsada hisse fiyatlarında ondalıktan sonra 2 basamak yazılır.

Verilen bilgilere göre uygulama sonrasında geçilecek sisteme göre hissenin tavan/taban fiyatını belirleyiniz.

Inputlar:
Pazar tipi = x
hisse fiyatı = y
Örn:
x y

Outputlar:
Hisse tavan fiyatı = k
Hisse taban fiyatı = l
Örn:
k l

Örnekler:
1)
Input:
Z 13.53

Hisse pazar tipi "Z" yani hissemiz yıldız pazarda olduğundan %20 fiyat marjı uygulanacaktır.
Hisse fiyatı 13.53'tür.
Tavan fiyatını bulabilmek için 13.53 + 13.53 * 20 / 100 = 16.236
Taban fiyatını bulabilmek için 13.53 - 13.53 * 20 / 100 = 10.824 işlemlerini yaparız.
Hissemizin tavan fiyatı 16.236 20'den küçük olduğundan dolayı her 1 kuruşta işlem görür ve bir alt kuruşa yuvarlanır. => 16.236 ~ 13.23
Hissemizin taban fiyatı 10.824 20'den küçük olduğundan dolayı her 1 kuruşta işlem görür ve bir üst kuruşa yuvarlanır. => 10.824 ~ 10.83

Output:
16.23 10.83


2)
Input:
N 30.14

Hisse pazar tipi "N" yani hissemiz ana pazarda olduğundan %15 fiyat marjı uygulanacaktır.
Hisse fiyatı 30.14'tür.
Tavan fiyatını bulabilmek için 30.14 + 30.14 * 20 / 100 = 34.661
Taban fiyatını bulabilmek için 30.14 - 30.14 * 20 / 100 = 25.619 işlemlerini yaparız.
Hissemizin tavan fiyatı 34.661 20'den büyük, 50'den küçük olduğundan dolayı her 2 kuruşta işlem görür ve bir alt çift kuruşa yuvarlanır. => 34.661 ~ 34.66
Hissemizin taban fiyatı 25.619 20'den büyük, 50'den küçük olduğundan dolayı her 2 kuruşta işlem görür ve bir üst çift kuruşa yuvarlanır. => 25.619 ~ 25.62
Output:
34.66 25.62

"""
import random
def tavanyuvarla(x):
    if x < 20:
        x = int(x*100) / 100
    elif x < 50:
        x = int(x*100)
        if x % 2 == 1:
            x -= 1
        x /= 100
    elif x < 100:
        x = int(x*100)
        if x % 5 != 0:
            fark = x % 5
            x -= fark
        x /= 100
    else:
        x = int(x * 10)
        x /= 10
    return x

def tabanyuvarla(x):
    if x < 20:
        x = int(x*100 + 1) / 100
    elif x < 50:
        x = int(x*100+1)
        if x % 2 == 1:
            x += 1
        x /= 100
    elif x < 100:
        x = int(x*100)
        if x % 5 != 0:
            fark = x % 5
            x += 5 - fark
        x /= 100
    else:
        x = int(x * 10 + 1)
        x /= 10
    return x

def tavan(x, tip):
    if tip == "Z":
        x *= 1.2
    elif tip == "N":
        x *= 1.15
    elif tip == "T":
        x *= 1.1
    return tavanyuvarla(x)

def taban(x,tip):
    if tip == "Z":
        x *= 0.8
    elif tip == "N":
        x *= 0.85
    elif tip == "T":
        x *= 0.9
    return tabanyuvarla(x)


liste = ["Z", "N", "T"]
for x in range(13, 20):
    hisse_fiyatı = tabanyuvarla(int(random.random() * 140 * 100) / 100)
    tip = int(random.random()*3)
    yazi = liste[tip] + " " + str(hisse_fiyatı)
    dosya = open("borsa." + str(x + 1) + ".in", "w+")
    dosya.write(yazi)
    dosya.close()
    print(yazi)
    yazi = str(tavan(hisse_fiyatı, liste[tip])) + " " + str(taban(hisse_fiyatı, liste[tip]))
    dosya = open("borsa." + str(x + 1) + ".out", "w+")
    dosya.write(yazi)
    dosya.close()
    print(yazi)