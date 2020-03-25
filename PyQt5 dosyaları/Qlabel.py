import sys

from PyQt5 import QtWidgets

def Pencere():
    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()

    h_lay1 = QtWidgets.QHBoxLayout()
    h_lay2 = QtWidgets.QHBoxLayout()
    h_lay3 = QtWidgets.QHBoxLayout()

    v_lay1 = QtWidgets.QVBoxLayout()
    
    buton1 = QtWidgets.QPushButton("1")
    buton2 = QtWidgets.QPushButton("2")
    buton3 = QtWidgets.QPushButton("3")
    buton4 = QtWidgets.QPushButton("4")
    buton5 = QtWidgets.QPushButton("5")
    buton6 = QtWidgets.QPushButton("6")
    buton7 = QtWidgets.QPushButton("7")
    buton8 = QtWidgets.QPushButton("8")
    buton9 = QtWidgets.QPushButton("9")

    pencere.setWindowTitle("Hesap Makinesi")
    pencere.setGeometry(100,100,500,500)

    h_lay1.addStretch()
    h_lay1.addWidget(buton1)
    h_lay1.addWidget(buton2)
    h_lay1.addWidget(buton3)
    h_lay1.addStretch()

    h_lay2.addStretch()
    h_lay2.addWidget(buton4)
    h_lay2.addWidget(buton5)
    h_lay2.addWidget(buton6)
    h_lay2.addStretch()

    h_lay3.addStretch()
    h_lay3.addWidget(buton7)
    h_lay3.addWidget(buton8)
    h_lay3.addWidget(buton9)
    h_lay3.addStretch()

    v_lay1.addStretch()
    v_lay1.addLayout(h_lay1)
    v_lay1.addLayout(h_lay2)
    v_lay1.addLayout(h_lay3)
    v_lay1.addStretch()

    pencere.setLayout(v_lay1)

    pencere.show()

    sys.exit(app.exec_())

Pencere()