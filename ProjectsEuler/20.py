def factorial(x):
    product = 1
    for i in range(1,x+1):
        product *= i
    return product

def sumofdigits(a):
    a = str(a)
    toplam = 0
    for i in a:
        i = int(i)
        toplam += i
    print(toplam)

sumofdigits(factorial(100))
    