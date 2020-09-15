"""marketlist problemi"""

def takeSecond(elem):
    return elem[1]

sayi = input()
yazi = input().rstrip().split()
liste = ["A", "E" , "I", "O", "U", "a", "e", "i", "o", "u"]

sonyazi = ""
yeniyazi = ""
for x in yazi:
    yeni = []
    x = list(x)
    for y in liste:
        for z in range(len(x)):
            if x[z] == y:
                yeni += [(x[z], z)]
    yeni.sort(key=takeSecond)       
    for i in range(len(yeni)):
        x.remove(yeni[i][0])
    
    x = x[::-1]
    
    for i in range(len(yeni)):
        x.insert(yeni[i][1],yeni[i][0])
    
    for y in x:
        sonyazi += y

    sonyazi += " "

print(sonyazi)