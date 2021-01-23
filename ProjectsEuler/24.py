def factorial(x):
    if x == 1:
        return 1
    elif x == 0:
        return 1
    else:
        return x * factorial(x-1)

index = 1000000
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
yazı = ""

while index != 0:
    if len(liste) == 0:
        break
    num = index / factorial(len(liste)-1)
    if num % 1 == 0:
        num = int(num) -1
    else:
        num = int(num)
    index -= num * factorial((len(liste)-1))
    yazı += str(liste[num])
    liste.remove(liste[num])

print(yazı)