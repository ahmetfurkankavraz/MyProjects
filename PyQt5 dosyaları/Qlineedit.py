import sys

from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.yeni_init()

        self.show()

    def yeni_init(self):

        self.yazıalanı = QtWidgets.QLineEdit()
        self.buton = QtWidgets.QPushButton("Temizle")
        self.buton2 = QtWidgets.QPushButton("Yazdır")

        v_lay = QtWidgets.QVBoxLayout() 
        v_lay.addWidget(self.yazıalanı)
        v_lay.addWidget(self.buton)
        v_lay.addWidget(self.buton2)
        
        self.setLayout(v_lay)
        
        self.buton.clicked.connect(self.click)
        self.buton2.clicked.connect(self.click)

    def click(self):
        sender = self.sender()
        
        if sender.text() == "Temizle":
            self.yazıalanı.clear() 
        else:
            text = self.yazıalanı.text()
            print(text)









app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())

