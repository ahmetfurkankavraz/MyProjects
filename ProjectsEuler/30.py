liste = []
for i in range(2, 100000000):
    length = len(str(i))
    sum = 0
    for j in range(length):
        sum += int(str(i)[j]) ** 5
    if i == sum:
        liste += [i]
    print(i)
    print(liste)