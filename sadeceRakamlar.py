#liste içinde sadece rakamlardan oluşan elemanları bulmak

liste = ["345","sadas","324a","14","kemal"]
for a in liste:
    try:
        print(int(a))
    except:
        pass

