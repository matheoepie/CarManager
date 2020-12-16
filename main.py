import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QFormLayout, QLineEdit, QComboBox, QSpinBox
from PyQt5 import QtCore
from Classes.meteo import Meteo
from Classes.personne import (Personne, Personnes, PersonnesWidget)
from Classes.car import (Car, Cars, CarsWidget, Appel)
from Classes.classe import (Classe, Classes)

class MainUI(QApplication):
    def __init__(self):
        super(MainUI, self).__init__([])

        self.meteo = Meteo()
        self.listeCars = Cars()
        self.listePersonnes = Personnes()
        self.afficher_liste = PersonnesWidget(self.listePersonnes)
        self.afficher_cars = CarsWidget(self.listeCars)
        self.listeClasses = Classes()


        self.widget = QWidget()

        self.widget.resize(500, 120)
        self.widget.move(300, 300)
        self.widget.setWindowTitle('Car Manager')

        self.layout = QVBoxLayout()
        self.layout2 = QVBoxLayout()
        self.layout3 = QHBoxLayout()
        self.layout4 = QHBoxLayout()
        self.layout5 = QVBoxLayout()
        self.layout6 = QVBoxLayout()
        self.hLayout = QHBoxLayout()
        self.layoutBoutons = QHBoxLayout()

        self.label = QLabel("")
        self.label.setWordWrap(True)
        self.previous = QPushButton("Car précédent")
        self.next = QPushButton("Car suivant")
        self.appel = QPushButton("Faire l'appel")
        self.newCar = QPushButton("Ajouter un car")
        self.removeCar = QPushButton("Supprimer un car")
        self.newMember = QPushButton("Ajouter une personne")
        self.removeMember = QPushButton("Retirer une personne")
        self.newClass = QPushButton("Ajouter une classe")
        self.moveToCar = QPushButton("Assigner à un car")
        self.moveToCar.clicked.connect(self.personMoveToCar)
        self.newCar.clicked.connect(self.addCar)
        #self.removeCar.clicked.connect(self.deleteCar)
        self.appel.clicked.connect(self.carAppel)
        self.next.clicked.connect(self.nextCar)
        self.previous.clicked.connect(self.previousCar)
        self.newMember.clicked.connect(self.addMember)
        self.removeMember.clicked.connect(self.deleteMember)
        self.newClass.clicked.connect(self.addClass)
        
        self.layout5.addWidget(self.afficher_cars)
        self.layout4.addWidget(self.previous)
        self.layout4.addWidget(self.next)
        self.layout5.addWidget(self.appel)
        self.layout5.addLayout(self.layout4)
        self.layoutBoutons.addWidget(self.newCar)
        self.layoutBoutons.addWidget(self.removeCar)

        self.layout.addWidget(self.meteo.displayMeteo())
        self.layout.addLayout(self.layoutBoutons)
          
        self.layout2.addWidget(self.afficher_liste)
        self.layout3.addWidget(self.newMember)
        self.layout3.addWidget(self.removeMember)
        self.layout2.addWidget(self.newClass)
        self.layout2.addWidget(self.moveToCar)
        


        self.layout2.addLayout(self.layout3)
        self.hLayout.addLayout(self.layout)
        self.hLayout.addLayout(self.layout5)
        self.hLayout.addLayout(self.layout2)
        self.hLayout.addLayout(self.layout6)
  

        self.widget.setLayout(self.hLayout)
        self.widget.show()
        self.afficher_liste.show()

    def nextCar(self):
        self.afficher_cars.next()
        self.afficher_cars.update()

    def previousCar(self):
        self.afficher_cars.previous()

    def addCar(self):
        self.listeCars.add()
        self.afficher_cars.update()

    def deleteCar(self):
        self.listeCar.remove()
    
    def addMember(self):
        Personne(self.listePersonnes, self.listeClasses).exec_()
        
    def addClass(self):
        Classe(self.listeClasses).exec_()

    def deleteMember(self):
        self.listePersonnes.remove()
    
    def personMoveToCar(self):
        result1 = self.listePersonnes.AddPersonToCar()
        print(result1)
        result2 = self.listeCars.getCombo()
        print(result2)
        listePersCar = Car(result2)
        for item in result1:
            listePersCar.ajouterPersonne(item)
    
    def carAppel(self):
        result2 = self.listeCars.getCombo()
        target = self.listeCars.listeCars[0]
        Appel(target).exec_()
            

if __name__ == '__main__':
    app = MainUI()
    app.exec_()

