

#
#   CAR MANAGER
#   Application de gestion de remplissage de cars
#   Développé dans le cadre d'un exercice de Python
#   Développé par Thibault DOUCET et Mathéo EPIE
#   B3 DevOPS Classe 2
#


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QFormLayout, QLineEdit, QComboBox, QSpinBox
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
        self.vLayout = QVBoxLayout()
        self.layoutBoutons = QHBoxLayout()

        self.label = QLabel("")
        self.label.setWordWrap(True)
        self.appel = QPushButton("Faire l'appel")
        self.newCar = QPushButton("Ajouter un car")
        self.removeCar = QPushButton("Supprimer un car")
        self.newMember = QPushButton("Ajouter une personne")
        self.removeMember = QPushButton("Retirer une personne")
        self.newClass = QPushButton("Ajouter une classe")
        self.validateButton = QPushButton("Valider")
        self.moveToCar = QPushButton("Assigner à un car")
        
        self.moveToCar.clicked.connect(self.personMoveToCar)
        self.newCar.clicked.connect(self.addCar)
        #self.removeCar.clicked.connect(self.deleteCar)
        self.appel.clicked.connect(self.carAppel)
        self.newMember.clicked.connect(self.addMember)
        self.removeMember.clicked.connect(self.deleteMember)
        self.newClass.clicked.connect(self.addClass)
        self.validateButton.clicked.connect(self.validate)

        self.layout5.addWidget(self.afficher_cars)
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
        self.vLayout.addLayout(self.hLayout)

        self.vLayout.addWidget(self.validateButton)

        self.widget.setLayout(self.vLayout)
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
        result2 = self.listeCars.getCombo()
        for item in result1:
            if len(self.listeCars.listeCars[int(result2.text())].personnes)<self.listeCars.listeCars[int(result2.text())].nb_places_max:
                self.listeCars.listeCars[int(result2.text())].ajouterPersonne(item)
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Erreur")
                msg.setInformativeText('Un car ne peut pas avoir plus de %s personnes' % self.listeCars.listeCars[int(result2.text())].nb_places_max)
                msg.setWindowTitle("Erreur")
                msg.exec_()
    
    def carAppel(self):
        result2 = self.listeCars.getCombo()
        target = self.listeCars.listeCars[int(result2.text())]
        print("OK")
        AppelWidget(target).exec_()

    def validate(self):
        errors = []
        # Vérifier que tous les cars ont au moins un passager
        if self.listeCars.isOneEmpty() == True:
            errors.append("Au moins un car est vide")
        # Vérifier 1 prof = 10 élèves max
        if self.listeCars.isRatioRespected() == False:
            errors.append("Au moins un des cars possède trop d'élèves pour pas suffisamment de profs")
        # Vérifier que chaque élève a une classe
        if self.listeCars.hasEveryoneAClass(self.listePersonnes) == False:
            errors.append("Au moins un élève n'a pas de classe")
        # Vérifier qu'il n'y a pas plus de 3 classes
        if self.listeCars.hasTooMuchClasses() == True:
            errors.append("Il y a plus de 3 classes dans un des cars")
        for error in errors:
            print(error)
        if len(errors) > 0:
            msg = QMessageBox()
            errMsg = ''
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Erreur")
            for message in errors:
                errMsg = errMsg + '\n' + message
            msg.setInformativeText(errMsg)
            msg.setWindowTitle("Erreur")
            msg.exec_()

if __name__ == '__main__':
    app = MainUI()
    app.exec_()

