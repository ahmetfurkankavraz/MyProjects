
#Fonksiyon girilen notlardan harf notu hesaplayıp en sonunda bir string döndürmektedir. Format kısmında görülebilir.
def notHesapla(liste):
    #split fonksiyonu yazıların arasında "," gördüğü zaman listenin diğer elemanına geçer.
    #örn: Ahmet,Furkan,Kavraz yazını [Ahmet, Furkan, Kavraz] şekline dönüştürür.
    yeniliste = liste.split(",")

    isim = yeniliste[0]
    not1 = yeniliste[1]
    not2 = yeniliste[2]
    not3 = yeniliste[3]

    #burada özel olarak her satırın sonunda "\n" olduğu için integera çevirmeden önce "\n"leri silmemiz gerekiyordu.
    not3 = not3[0:2]

    #harf notu hesaplama bölümü

    sonnot = int(not1) * 3/10 + int(not2) * 3/10 + int(not3) * 4/10
    if sonnot > 90:
        harfnotu = "AA"
    elif sonnot>85:
        harfnotu = "BA"
    elif sonnot>80:
        harfnotu = "BB"
    elif sonnot>75:
        harfnotu = "CB"
    elif sonnot>70:
        harfnotu = "CC"
    elif sonnot>65:
        harfnotu = "DC"
    elif sonnot>60:
        harfnotu = "DD"
    else:
        harfnotu = "FF"
    
     
    #yazacağımız yazıyı istediğimiz format haline getirdiğimiz bölüm.
    sonyazi = "{} ------> {}\n".format(isim, harfnotu)

    return sonyazi



#LÜTFEN ÖNCE BURAYA BAKINIZ.

#Burada yazdığımıız kod original.txt dosyasından isim ve notları alıp, harfnotları.txt dosyasına isim ve harf notu EKLEMEKtedir. 
#Kod her çalıştığında bir daha ekleyecektir. Lütfen tek sefer çalıştırın.

#original.txt dosyasını okuduğumuz bölüm ("r+" dosyayı hem okuyup hem de dosyaya yazı yazmamızı sağlar.)
with open("original.txt", "r+", encoding= "utf-8") as file:
    
    #readlines ile dosyanın her bir satırı bir liste olarak okunur.
    liste = file.readlines()

    #notHesapla fonksiyonunun Returnlediği her bir satırı "harfnotları.txt" dosyasına Appendlediği(eklediği) bölüm
    for i in liste:
        a = notHesapla(i)
        with open("harfnotları.txt", "a", encoding="utf-8") as file:
            file.write(a)



