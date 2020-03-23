#isimler -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
#soyisimler -----> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]


isim = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

#zip fonksiyonuile bize verilen listelerdeki elemanları birleştirdik ve bir listeye attık
print(list(zip(isim,soyisim)))

#isimleri teker teker bastırdık
for i,j in zip(isim,soyisim):
    print(i,j)

