#[1,2,3,4,5,6,7,8,9,10]
#Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın.

#öncelikler reduce fonksiyonunu import etmemiz gerekiyor
from functools import reduce

liste = [1,2,3,4,5,6,7,8,9,10]

#çiftsayı olanları aldığımız değer
çiftsayılar = list(filter(lambda x: x%2 == 0, liste))
print(çiftsayılar)

#toplamlarını bulduğumuz yer
sondeğer = reduce(lambda x,y : x+y,çiftsayılar)
print(sondeğer)




