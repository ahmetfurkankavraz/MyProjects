def factorial(x):
    product = 1
    for i in range(1,x+1):
        product *= i
    return product


def combination(n,r):
    result = (factorial(n)/factorial(r))/factorial(n-r)
    return result

print(combination(40,20)) 
