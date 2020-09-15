def rule(n):
    if n % 2 == 0:
        n = int(n/2)
    else:
        n = int(n * 3 + 1)
    return n

def chain(n):
    counter = 0
    while n != 1:
        n = rule(n)
        counter += 1
    return counter


def findlongestchain(lastnumber):
    biggestnum = 5
    biggestcounter = 2
    for i in range(biggestnum, lastnumber):
        if (chain(i)) > biggestcounter:
            biggestnum = int(i)
            biggestcounter = chain(biggestnum)
    return biggestnum

print(findlongestchain(1000000))