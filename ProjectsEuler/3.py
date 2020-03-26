#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

sayı = 600851475143
i = 3
liste = []
while sayı != 1 :
    for i in range(3,int(sayı+1)):
        if sayı % i == 0:
            sayı = sayı / i 
            print(i)
            print(sayı)
            break
        i += 2
