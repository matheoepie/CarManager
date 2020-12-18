import json
import requests
from PyQt5.QtWidgets import QVBoxLayout, QListWidget, QMessageBox, QListWidgetItem, QDialogButtonBox, QDialog, QComboBox, QHBoxLayout, QLabel, QGroupBox, QProgressBar, QWidget, QTreeWidget, QTreeView, QTreeWidgetItem
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from collections import deque
from PyQt5 import QtCore, QtGui


class Car:
    def __init__(self, id):
        self.personnes = []
        self.eleves = []
        self.prof = []
        self.name = "Car n°"
        self.id = id
        self.nb_places_max = 40
        self.widget = QListWidget()
        self.aFaitAppel = False

    def ajouterPersonne(self, personne):
        self.personnes.append(personne.text())
        qitem = QListWidgetItem()
        qitem.setText(personne.text())
        qitem.setCheckState(QtCore.Qt.Unchecked)
        self.widget.addItem(qitem)
        

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

    def displayMembres(self):
        print("Display of car")
        self.listeGroupBox = QGroupBox("Car n°%d" % (self.id))
        self.widget.addItem("%d" % (self.id))
        layout = QVBoxLayout()
        layout.addWidget(self.widget)
        self.listeGroupBox.setLayout(layout)
        print("End - Display of car")
        return self.listeGroupBox
    
    def displayAppel(self):
        self.listeGroupBox = QGroupBox("Appel")
        layout = QVBoxLayout()
        layout.addWidget(self.widget)
        self.listeGroupBox.setLayout(layout)
        return self.listeGroupBox
    
    
    def validate(self):
        nbabsent = 0
        items = []
        for index in range(self.widget.count()):
            items.append(self.widget.item(index))
        for item in items:
            coche = True if item.checkState() == QtCore.Qt.Checked else False
            if coche == False:
                nbabsent = nbabsent +1
        if nbabsent>0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Erreur")
            msg.setInformativeText('il ya des absents')
            msg.setWindowTitle("Erreur")
            msg.exec_()
        else:
            self.aFaitAppel = True
            return True
            
            

class Cars():
    def __init__(self):
        self.listeCars = []
        self.widget = QListWidget()

    def debugListe(self):
        print("Liste des cars : ")
        for item in self.listeCars:
            print(item.id)

    def add(self):
        if (len(self.listeCars) > 0):
            id = self.listeCars[len(self.listeCars)-1].id+1
            car = Car(id)
            self.listeCars.append(car)
            self.widget.addItem(str(car.id))
        else:
            id = 0
            self.listeCars.append(Car(id))
        
        self.debugListe()
        
    def remove(self):
        selectedItems = self.widget.selectedItems()
        if not selectedItems:
            return
        for item in selectedItems:
            index = self.widget.row(item)
            self.widget.takeItem(index)
            self.listeCars.pop(index)
            
    def getCombo(self):
        selectedItems = self.widget.selectedItems()
        if not selectedItems:
            return
        else:
            return selectedItems[0]

    def getClasseFromStr(self, pers):
        index = pers.index(')')
        return pers[index+1:len(pers)]

    def isOneEmpty(self):
        result = False
        for car in self.listeCars:
            if car.id != 0:
                if len(car.personnes) == 0:
                    result = True
                    break
        return result

    def isRatioRespected(self):
        result = True
        for car in self.listeCars:
            for personne in car.personnes:
                status = personne[len(personne)-6:len(personne)-1]
                if status == "Eleve":
                    car.eleves.append(personne)
                else:
                    car.prof.append(personne)
                if len(car.prof) == 0:
                    result = False
                else:
                    if len(car.eleves)/len(car.prof) > 10:
                        result = False
        return result

    def hasEveryoneAClass(self, listePers):
        result = True
        for personne in listePers.listePersonnes:
            if personne.status == "Eleve" and personne.classe == '':
                result = False
        return result

    def hasTooMuchClasses(self):
        result = False
        listClasses = []
        for car in self.listeCars:
            for pers in car.personnes:
                classe = self.getClasseFromStr(pers)
                if not classe in listClasses:
                    listClasses.append(classe)
        if len(listClasses) > 3:
            result = True
        return result

    def displayCars(self):
        self.listeGroupBox = QGroupBox("Cars")
        layout = QVBoxLayout()
        layout.addWidget(self.widget)
        self.listeGroupBox.setLayout(layout)
        return self.listeGroupBox
    


class CarsWidget(QWidget):
    def __init__(self, listeCars):
        self.id = 0
        self.listeCarsTotal = listeCars
        self.listeCarsTotal.add()
        super(CarsWidget, self).__init__()
        print(len(self.listeCarsTotal.listeCars))
        if (len(self.listeCarsTotal.listeCars) > 0):
            self.afficher_liste = self.listeCarsTotal.displayCars()
        layout = QVBoxLayout()
        #if (len(self.listeCarsTotal.listeCars) > 0):
        layout.addWidget(self.afficher_liste)
        self.setLayout(layout)

    def next(self):
        if (self.id == 0 and len(self.listeCarsTotal.listeCars) > 0):
            self.id = 1
            print(self.id)
        elif (self.id < len(self.listeCarsTotal.listeCars)-1):
            self.id = self.id + 1
            print(self.id)
        else:
            return

    def previous(self):
        if (self.id > 0):
            self.id = self.id - 1
            print(self.id)
        else:
            return

    def _trigger_refresh(self):
        self.update()
        
class AppelWidget(QDialog):
    def __init__(self, car):
        self.list = car
        super(AppelWidget, self).__init__()
        self.afficher_liste = self.list.displayAppel()
        layout = QVBoxLayout()
        layout.addWidget(self.afficher_liste)
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.valid)
        buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.reject)
        layout.addWidget(buttonBox)
        self.setLayout(layout)

    def valid(self):
        if self.list.validate():
            self.close()

