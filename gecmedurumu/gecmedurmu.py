
#Fonksiyon girilen notlardan "geçme durumunu" hesaplayıp en sonunda bir liste döndürmektedir.
def isimVegecmedurumu(liste):
    #split fonksiyonu yazıların arasında "," gördüğü zaman listenin diğer elemanına geçer.
    #örn: Ahmet,Furkan,Kavraz yazını [Ahmet, Furkan, Kavraz] şekline dönüştürür.
    yeniliste = liste.split(",")


    isim = yeniliste[0]
    not1 = yeniliste[1]
    not2 = yeniliste[2]
    not3 = yeniliste[3]

    #burada özel olarak her satırın sonunda "\n" olduğu için integera çevirmeden önce "\n"leri silmemiz gerekiyordu.
    not3 = not3[0:2]
    sonnot = int(not1) * 3/10 + int(not2) * 3/10 + int(not3) * 4/10

    #geçme durumunu yazacağımız bölüm
    if sonnot>60:
        gecmedurumu = "geçti"
    else:
        gecmedurumu = "kaldı"
    
    #Burada her ismin sonuna "\n" eklememiz gerekiyor. 
    #Eğerki bu işlemi yapmazsak dosyaya yazma işlemi sırasında isimleri boşluk bırakmadan yazacaktır
    #Ancak satır satır yazdırarak daha hoş bir görüntü elde ettirebiliriz.
    isim = isim + "\n"
    
    #yazacağımız yazıyı istediğimiz format haline getirdiğimiz bölüm.
    return [isim, gecmedurumu]


#LÜTFEN ÖNCE BURAYA BAKINIZ.

#Burada yazdığımıız kod original.txt dosyasından isim ve notları alıp, kalanlar.txt ve geçenler.txt dosyasına geçme durumuna göre isim EKLEMEKtedir. 
#Kod her çalıştığında bir daha ekleyecektir. Lütfen tek sefer çalıştırın.


#original.txt dosyasını okuduğumuz bölüm ("r+" dosyayı hem okuyup hem de dosyaya yazı yazmamızı sağlar.)
with open("original.txt", "r+", encoding= "utf-8") as file:
    
    #readlines ile dosyanın her bir satırı bir liste olarak okunur.
    liste = file.readlines()

    #isimVegecmedurumu fonksiyonunun Returnlediği her bir listeyi "kalanlar.txt" ve "geçenler.txt" dosyasına Appendlediği(eklediği) bölüm
    #Burada fonksiyonun nasıl çalıştığına bakabilirsiniz.
    for i in liste:
        a = isimVegecmedurumu(i)
        
        if a[1] == "geçti":
            with open("geçenler.txt", "a", encoding="utf-8") as file:
                file.write(a[0])
        else:
            with open("kalanlar.txt", "a", encoding="utf-8") as file:
                file.write(a[0])

