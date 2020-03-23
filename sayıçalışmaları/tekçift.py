#bir sayının tek mi yoksa çift mi olduğunu try, except ve raise ile bulmak

liste = [5,6,1,15,8,44,62,51,66,84, 85, 9, 25,96 ]
def tekçift(a):
    if (a%2) != 0 :
        raise ValueError
    else:
        return (a)

for i in liste:
    try:
        print(tekçift(i))
    except ValueError:
        pass
