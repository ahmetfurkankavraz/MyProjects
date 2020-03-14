birler = ['' , 'bir', 'iki', 'üç', 'dört', 'beş', 'altı', 'yedi','sekiz', 'dokuz']
onlar = [ '','on','yirmi', 'otuz', 'kırk', 'elli', 'altmış', 'yetmiş', 'seksen', 'doksan']
yüzler = []

for x in range(10):
    if x == 0:
        yüzler.append('')
    elif x == 1:
        yüzler.append('yüz')
    else:
        liste = birler[x] + ' yüz'
        yüzler.append(liste)

def sayiyazdirma(a):
    ilkbasamak = a // 100000000 % 10
    ikincibasamak = a // 10000000 % 10
    üçüncübasamak = a // 1000000 % 10
    dördüncübasamak = a // 100000 % 10
    beşincibasamak = a // 10000 % 10
    altıncıbasamak = a // 1000 % 10
    yedincibasamak = a // 100 % 10
    sekizincibasamak = a // 10 % 10
    dokuzuncubasamak = a % 10
    if a >= 1000000:
        sayiyazimi = yüzler[ilkbasamak] + ' ' + onlar[ikincibasamak] + ' ' + birler[üçüncübasamak] + ' milyon ' + yüzler[dördüncübasamak] + ' ' + onlar[beşincibasamak] + ' ' + birler[altıncıbasamak] + ' bin ' + yüzler[yedincibasamak] + ' ' + onlar[sekizincibasamak] + ' ' + birler[dokuzuncubasamak]
    elif a >= 1000:
        sayiyazimi = yüzler[dördüncübasamak] + ' ' + onlar[beşincibasamak] + ' ' + birler[altıncıbasamak] + ' bin ' + yüzler[yedincibasamak] + ' ' + onlar[sekizincibasamak] + ' ' + birler[dokuzuncubasamak]
    else:
        sayiyazimi =  yüzler[yedincibasamak] + ' ' + onlar[sekizincibasamak] + ' ' + birler[dokuzuncubasamak]
    return (sayiyazimi)    

print(sayiyazdirma(16859153))