import sys
from PyQt5.QtWidgets import (QFormLayout, QLabel, QGridLayout, QLineEdit,
        QGroupBox, QListWidget, QDialog, QDialogButtonBox, QVBoxLayout, QComboBox, QWidget)

class Personne(QDialog):
    nom = ''
    prenom = ''
    status = ''
    statusList = ['Eleve', 'Professeur']

    def __init__(self, personnes):
        super(Personne, self).__init__()

        self.lastnameLineEdit = QLineEdit()
        self.firstnameLineEdit = QLineEdit()
        self.statusBox = QComboBox()
        self.personnes = personnes

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

        layout = QFormLayout()
        layout.addRow(QLabel("Nom: "), self.lastnameLineEdit)
        layout.addRow(QLabel("Prénom: "), self.firstnameLineEdit)
        layout.addRow(QLabel("Statut : "), liste)
        self.formGroupBox.setLayout(layout)
        self.setWindowTitle("Ajouter")

class Personnes():
    def __init__(self):
        self.listePersonnes = []
        self.widget = QListWidget()

    def debugListe(self):
        print("Liste des personnes : ")
        for item in self.listePersonnes:
            print(item.nom + " " + item.prenom)

    def add(self, personne):
        self.listePersonnes.append(personne)
        self.widget.addItem(personne.nom + ' ' + personne.prenom + ' (' + personne.status + ')')
        self.debugListe()

    def remove(self):
        selectedItems = self.widget.selectedItems()
        if not selectedItems:
            return
        for item in selectedItems:
            index = self.widget.row(item)
            self.widget.takeItem(index)
            self.listePersonnes.pop(index)

    def getList(self):
        return self.listePersonnes

    def displayPersonnes(self):
        self.listeGroupBox = QGroupBox("Personnes")
        layout = QVBoxLayout()
        layout.addWidget(self.widget)
        self.listeGroupBox.setLayout(layout)
        return self.listeGroupBox

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
        