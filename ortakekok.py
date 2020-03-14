// iki sayının ekokunu bulmak için yazılan bir fonksiyon

def ortakekok(a, b):
    z = a * b + 1
    liste = []
    if (b<a):
        for i in range(b, z):
            if (i % b == 0  and i % a == 0):
                liste += [i]

    else:
        for i in range(a, z):
            if (i % b == 0  and i % a == 0):
                liste += [i]
    print(liste[-1])

ortakekok(16, 5)
