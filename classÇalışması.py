import time

class Hayvanlar():
    def __init__(self, isim, tür, boy, hız):
        self.isim = isim
        self.tür = tür
        self.boy = boy
        self.hız = hız

    def __len__(self):
        return self.boy

    def __str__(self):
        return self.isim
    
    def bilgilerigöster(self):
        return "İsim: {}\nTürü: {}\nBoy: {}\nHız:{}\n ".format(self.isim, self.tür, self.boy, self.hız)

    def boydegistirme(self):
        yeniboy = input("Boy giriniz")
        print("Boy değiştiriliyor...")
        self.boy = yeniboy
        return "Yeniboy: {}".format(self.boy)

ramazan = Hayvanlar("Boncuk", "Köpek", 150, 30)

print(ramazan)
print(len(ramazan))
print(Hayvanlar.bilgilerigöster(ramazan))
print(Hayvanlar.boydegistirme(ramazan))
print(Hayvanlar.bilgilerigöster(ramazan))