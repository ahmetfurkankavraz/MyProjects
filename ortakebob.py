def ortakebob(a, b):
    liste = []
    if (a<b):
        z = a + 1 
        for i in range(1, z):
            if (b % i == 0  and a % i == 0):
                liste += [i]

    else:
        z = b + 1 
        for i in range(1, z):
            if (b % i == 0  and a % i == 0):
                liste += [i]
    print(liste[-1])

ortakebob(320, 200)