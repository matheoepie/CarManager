import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import (QFormLayout, QLabel, QGridLayout, QLineEdit, QGroupBox, QListWidget, QDialog, QDialogButtonBox, QVBoxLayout, QComboBox, QWidget, QListWidgetItem)
from Classes.classe import Classes
from Classes.car import (Cars, Car)

class Personne(QDialog):
    nom = ''
    prenom = ''
    status = ''
    classe = ''
    statusList = ['Eleve', 'Professeur']

    def __init__(self, personnes, classes):
        super(Personne, self).__init__()

        self.lastnameLineEdit = QLineEdit()
        self.firstnameLineEdit = QLineEdit()
        self.statusBox = QComboBox()
        self.classBox = QComboBox()
        self.personnes = personnes
        self.classes = classes.listClasses

        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.validate)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

    def validate(self):
        self.nom = self.lastnameLineEdit.text()
        self.prenom = self.firstnameLineEdit.text()
        self.status = self.statusBox.currentText()
        self.classe = self.classBox.currentText()
        print(self.classe)
        print(self.classBox.currentText())
        print(self.statusBox.currentText())
        self.personnes.add(self)
        self.close()

    def getLastame(self):
        return self.nom

    def getFirstname(self):
        return self.prenom

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Ajouter une personne")
        liste = self.statusBox
        liste.addItems(self.statusList)
        listeClass = self.classBox
        listeClass.addItems(self.classes)

        layout = QFormLayout()
        layout.addRow(QLabel("Nom: "), self.lastnameLineEdit)
        layout.addRow(QLabel("Prénom: "), self.firstnameLineEdit)
        layout.addRow(QLabel("Statut : "), liste)
        layout.addRow(QLabel("Classe : "), listeClass)
        self.formGroupBox.setLayout(layout)
        self.setWindowTitle("Ajouter")

class Personnes():
    def __init__(self):
        self.listePersonnes = []
        self.widget = QListWidget()
        self.widget.itemClicked.connect(self.changeCheck)

    def debugListe(self):
        print("Liste des personnes : ")
        for item in self.listePersonnes:
            print(item.nom + " " + item.prenom)

    def add(self, personne):
        self.listePersonnes.append(personne)
        qitem = QListWidgetItem()
        qitem.setText(personne.nom + ' ' + personne.prenom + ' (' + personne.status + ')'+ personne.classe)
        qitem.setCheckState(QtCore.Qt.Unchecked)
        self.widget.addItem(qitem)
        self.debugListe()

    def remove(self):
        selectedItems = self.widget.selectedItems()
        if not selectedItems:
            return
        for item in selectedItems:
            index = self.widget.row(item)
            self.widget.takeItem(index)
            self.listePersonnes.pop(index)
    
    def AddPersonToCar(self):
        selectedItemsPerson = self.widget.selectedItems() 
        if not selectedItemsPerson:
            return
        else:
            return selectedItemsPerson
            
    
    def getList(self):
        return self.listePersonnes

    def displayPersonnes(self):
        self.listeGroupBox = QGroupBox("Personnes")
        layout = QVBoxLayout()
        layout.addWidget(self.widget)
        self.listeGroupBox.setLayout(layout)
        return self.listeGroupBox

    def changeCheck(self, qitem):
        ligne = qitem.listWidget().row(qitem)
        item = qitem.text()
        coche = True if qitem.checkState() == QtCore.Qt.Checked else False
        print("ligne:", ligne, "item:", item, "=>", coche)

class PersonnesWidget(QWidget):
    def __init__(self, listePersonnes):
        self.listePersonnes = listePersonnes
        super(PersonnesWidget, self).__init__()
        self.afficher_liste = self.listePersonnes.displayPersonnes()
        layout = QVBoxLayout()
        layout.addWidget(self.afficher_liste)
        self.setLayout(layout)

    def _trigger_refresh(self):
        self.update()