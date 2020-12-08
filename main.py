import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QFormLayout, QLineEdit, QComboBox, QSpinBox
from PyQt5 import QtCore
from Classes.meteo import Meteo
from Classes.personne import (Personne, Personnes)
from Classes.car import Car

meteo = Meteo()
car = Car()
listePersonnes = Personnes()

def addMember():
    Personne(listePersonnes).exec_()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()

    w.resize(500, 120)
    w.move(300, 300)
    w.setWindowTitle('Car Manager')

    layout = QVBoxLayout()
    layout2 = QVBoxLayout()
    hLayout = QHBoxLayout()
    layoutBoutons = QHBoxLayout()

    label = QLabel("")
    label.setWordWrap(True)
    previous = QPushButton("Supprimer un car")
    next = QPushButton("Ajouter un car")
    newMember = QPushButton("Ajouter une personne")
    newMember.clicked.connect(addMember)

    layoutBoutons.addWidget(previous)
    layoutBoutons.addWidget(next)

    layout.addWidget(meteo.displayMeteo())
    layout.addWidget(car.displayCar())
    layout.addLayout(layoutBoutons)
    layout2.addWidget(listePersonnes.displayPersonnes())
    layout2.addWidget(newMember)

    hLayout.addLayout(layout)
    hLayout.addLayout(layout2)

    # Update label every 10ms
    timer = QtCore.QTimer()
    #timer.timeout.connect(updateListe)
    timer.start(10)

    w.setLayout(hLayout)
    w.show()

    app.exec_()