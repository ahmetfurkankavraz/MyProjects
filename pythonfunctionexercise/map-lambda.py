# [(3,4),(10,3),(5,6),(1,9)] tuple içindeki elemanları çarparak şu sonuca ulaşmak:  [12, 30, 30, 9]

liste = [(3,4),(10,3),(5,6),(1,9)]


#bize verilen listelerin içindeki tuppleların belirtilen indexindeki elemanları list comprehension yaparak farklı listeler oluşturduğumuz yer
ilksayılar = [i[0] for i in liste]
print(ilksayılar)
ikincisayılar = [i[1] for i in liste]
print(ikincisayılar)

#map ve lambda fonksiyonları ile sonuca ulaştığımız yer 
son_liste = list(map(lambda x,y: x*y , ilksayılar,ikincisayılar) )

print(son_liste)

