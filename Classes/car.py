import json
import requests
from PyQt5.QtWidgets import QVBoxLayout, QListWidget, QHBoxLayout, QLabel, QGroupBox, QProgressBar, QWidget
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *


class Car:
    def __init__(self):
        self.personnes = []
        self.eleves = []
        self.prof = []
        self.id = ''
        self.nb_places_max = 40

    def ajouterPersonne(self, personne):
        self.personnes.append(personne)

    def ajouterEleve(self, eleve):
        self.eleves.append(eleve)

    def ajouterProf(self, prof):
        self.prof.append(prof)

    def getRatio(self):
        if len(self.prof) == 0 or len(self.eleves) == 0:
            return 0
        else:
            return len(self.eleves) / len(self.prof)

    def displayCar(self):
        # Layout Car
        layoutCar = QVBoxLayout()
        hLayoutCar = QHBoxLayout()
        carGroup = QGroupBox("Car")
        progress = QProgressBar()
        progress.setGeometry(0, 0, 300, 15)
        progress.setMaximum(self.nb_places_max)
        progress.setValue(len(self.personnes))
        layoutCar.addWidget(QLabel("Nombre d'élèves : %d" % (len(self.eleves))))
        layoutCar.addWidget(QLabel("Nombre de professeurs : %d" % (len(self.prof))))
        layoutCar.addWidget(QLabel("Ratio : %.1f" % (self.getRatio())))
        hLayoutCar.addLayout(layoutCar)
        hLayoutCar.addWidget(progress)
        carGroup.setLayout(hLayoutCar)
        return carGroup

class Cars():
    def __init__(self):
        self.listeCars = []
        self.widget = QListWidget()
        
    def debugListe(self):
        print("Liste des cars : ")
        for item in self.listeCars:
            print(item.id)

    def add(self, car):
        self.listeCars.append(car)
        self.debugListe()
        
    def remove(self):
        selectedItems = self.widget.selectedItems()
        if not selectedItems:
            return
        for item in selectedItems:
            index = self.widget.row(item)
            self.widget.takeItem(index)
            self.listeCars.pop(index)

    def displayCars(self):
        self.listeGroupBox = QGroupBox("Cars")
        layout = QVBoxLayout()
        layout.addWidget(self.widget)
        self.listeGroupBox.setLayout(layout)
        return self.listeGroupBox

class CarsWidget(QWidget):
    def __init__(self, listeCars):
        self.listeCars = listeCars
        super(CarsWidget, self).__init__()
        self.afficher_liste = QListWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.afficher_liste)
        self.setLayout(layout)

    def _trigger_refresh(self):
        self.update()
        

        