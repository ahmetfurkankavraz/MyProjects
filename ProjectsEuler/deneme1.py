


def asalsayi(a,b):
    sayac = 0
    for x in range(a,b+1):
        counter = 0
        y = 1
        while y*y <= x:
            if x % y == 0:
                counter += 1
            if counter >2:
                break
            y += 1
                
        if counter == 1:
            sayac += 1
    return sayac

islem = input()
islem = int(islem)
x= 0
while x < islem:
    liste = input().rstrip().split()
    a = liste[0]
    b = liste[1]
    a = int(a)
    b = int(b)
    print(asalsayi(a,b))
    x+=1


