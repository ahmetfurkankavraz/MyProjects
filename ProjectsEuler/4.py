#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome(a):
    a = str(a)
    if a[-1] == a[0] and a[-2] == a[1] and a[-3] == a[2] and a[-4] == a[3] and a[-5] == a[4]:
        return "palindrome"
    else:
        return ""

for i in range(900,1000): 
    for j in range(930,1000):
        if palindrome(i*j) == "palindrome":
            print(i*j)









