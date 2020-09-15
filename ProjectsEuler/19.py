firstyear = 1901
lastyear = 2000
year = firstyear

days = 0
aylargunsayisi = [31,28,31,30,31,30,31,31,30,31,30,31]

counter = 0
k = 0
while year <= lastyear:
    for i in range(0,len(aylargunsayisi)):
        if year % 4 == 0:
            aylargunsayisi[1] = 29
        if year % 400 == 0:
            aylargunsayisi[1] = 28
        days += aylargunsayisi[i]
        print(days)

        if days % 7 == 6:
            counter += 1


    year+=1


    print(counter)





