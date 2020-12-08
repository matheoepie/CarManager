import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QFormLayout, QLineEdit, QComboBox, QSpinBox
from PyQt5 import QtCore
from classes.meteo import Meteo
from classes.personne import (Personne, Personnes)
from classes.car import Car

meteo = Meteo()
car = Car()
listePersonnes = Personnes()

def getPersonnesListe():
    return listePersonnes

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()

    w.resize(500, 120)
    w.move(300, 300)
    w.setWindowTitle('Car Manager')

    layout = QVBoxLayout()
    layoutBoutons = QHBoxLayout()

    label = QLabel("")
    label.setWordWrap(True)
    previous = QPushButton("Supprimer un car")
    next = QPushButton("Ajouter un car")
    newMember = QPushButton("Ajouter une personne")

    layoutBoutons.addWidget(previous)
    layoutBoutons.addWidget(next)
    layoutBoutons.addWidget(newMember)

    layout.addWidget(meteo.displayMeteo())
    layout.addWidget(car.displayCar())
    layout.addLayout(layoutBoutons)

    # Update label every 10ms
    timer = QtCore.QTimer()
    #timer.timeout.connect(update_labels)
    timer.start(10)

    w.setLayout(layout)
    w.show()

    app.exec_()