fibo = 1
eskifibo = 0
counter = 1
while len(str(fibo)) != 1000:
    temp = fibo
    fibo += eskifibo
    eskifibo = temp
    counter += 1
print(counter)