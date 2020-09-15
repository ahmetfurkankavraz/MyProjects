def bolensayisi(num):
    i = 1
    counter = 0
    while i*i < num:
        if num % i == 0:
            counter += 2
        i+=1 
    if i*i == num:
        counter += 1
    return counter

for n in range(0,1000000):
    num = n *(n+1) /2
    num = int(num)
    if bolensayisi(num) > 500:
        print(num)