import json
import requests
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QGroupBox, QProgressBar


class Car:
    personnes = []
    eleves = []
    prof = []
    nb_places_max = 40

    def __init__(self):
        super()

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
        carGroup = QGroupBox("Car")
        progress = QProgressBar()
        progress.setGeometry(0, 0, 300, 15)
        progress.setMaximum(self.nb_places_max)
        progress.setValue(len(self.personnes))
        layoutCar.addWidget(QLabel("Nombre d'élèves : %d" % (len(self.eleves))))
        layoutCar.addWidget(QLabel("Nombre de professeurs : %d" % (len(self.prof))))
        layoutCar.addWidget(QLabel("Ratio : %.1f" % (self.getRatio())))
        layoutCar.addWidget(QLabel("Remplissage : "))
        layoutCar.addWidget(progress)
        carGroup.setLayout(layoutCar)
        return carGroup