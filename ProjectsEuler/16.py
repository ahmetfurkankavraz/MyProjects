def exp(a, n ):
    result = 1
    for i in range(n):
        result *= a
    return result


def sumdigits(a):
    a = str(a)
    toplam = 0
    for i in a:
        toplam += int(i)

    print(toplam)



sumdigits(exp(2, 1000))


