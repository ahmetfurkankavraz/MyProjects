import sys

from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_yeni()

    def init_yeni(self):

        self.yazıalanı = QtWidgets.QLabel("Bana hiç tıklanmadı.")
        self.buton = QtWidgets.QPushButton("Arttırmak için lütfen tıklayın.")
        self.sayı = 0
        
        v_lay = QtWidgets.QVBoxLayout()

        v_lay.addStretch()
        v_lay.addWidget(self.buton)
        v_lay.addWidget(self.yazıalanı)        
        v_lay.addStretch()


        h_lay = QtWidgets.QHBoxLayout()
        h_lay.addStretch()
        h_lay.addLayout(v_lay)
        h_lay.addStretch()

        self.setLayout(h_lay)

        self.buton.clicked.connect(self.sayma)
      
        self.show()

    def sayma(self):
        self.sayı += 1
        self.yazıalanı.setText("Bana " + str(self.sayı) + " kere tıklandı.")


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())

