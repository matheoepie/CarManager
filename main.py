import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QFormLayout, QLineEdit, QComboBox, QSpinBox
from PyQt5 import QtCore
from Classes.meteo import Meteo
from Classes.personne import (Personne, Personnes, PersonnesWidget)
from Classes.car import Car
from Classes.classe import (Classe, Classes)

class MainUI(QApplication):
    def __init__(self):
        super(MainUI, self).__init__([])

        self.meteo = Meteo()
        self.car = Car()
        self.listePersonnes = Personnes()
        self.afficher_liste = PersonnesWidget(self.listePersonnes)
        self.listeClasses = Classes()

        self.widget = QWidget()

        self.widget.resize(500, 120)
        self.widget.move(300, 300)
        self.widget.setWindowTitle('Car Manager')

        self.layout = QVBoxLayout()
        self.layout2 = QVBoxLayout()
        self.layout3 = QHBoxLayout()
        self.hLayout = QHBoxLayout()
        self.layoutBoutons = QHBoxLayout()

        self.label = QLabel("")
        self.label.setWordWrap(True)
        self.previous = QPushButton("Supprimer un car")
        self.next = QPushButton("Ajouter un car")
        self.newMember = QPushButton("Ajouter une personne")
        self.removeMember = QPushButton("Retirer une personne")
        self.newClass = QPushButton("Ajouter une classe")
        self.newMember.clicked.connect(self.addMember)
        self.removeMember.clicked.connect(self.deleteMember)
        self.newClass.clicked.connect(self.addClass)

        self.layoutBoutons.addWidget(self.previous)
        self.layoutBoutons.addWidget(self.next)

        self.layout.addWidget(self.meteo.displayMeteo())
        self.layout.addWidget(self.car.displayCar())
        self.layout.addLayout(self.layoutBoutons)
          
        self.layout2.addWidget(self.afficher_liste)
        self.layout3.addWidget(self.newMember)
        self.layout3.addWidget(self.removeMember)
        self.layout2.addWidget(self.newClass)

        self.layout2.addLayout(self.layout3)
        self.hLayout.addLayout(self.layout)
        self.hLayout.addLayout(self.layout2)

        self.widget.setLayout(self.hLayout)
        self.widget.show()
        self.afficher_liste.show()

    def addMember(self):
        Personne(self.listePersonnes, self.listeClasses).exec_()
        
    def addClass(self):
        Classe(self.listeClasses).exec_()

    def deleteMember(self):
        self.listePersonnes.remove()

if __name__ == '__main__':
    app = MainUI()
    app.exec_()

