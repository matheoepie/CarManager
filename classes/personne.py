import sys
from PyQt5.QtWidgets import (QFormLayout, QLabel, QGridLayout, QLineEdit,
        QGroupBox, QDialog, QDialogButtonBox, QVBoxLayout, QComboBox)

class Personne(QDialog):
    def __init__(self, personnes):
        super(Personne, self).__init__()

        self.nom = ''
        self.prenom = ''
        self.status = ''
        self.personnes = personnes
        self.statusList = ['Eleve', 'Professeur']
        self.lastname = QLineEdit()
        self.firstname = QLineEdit()

        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.acceptPersonne)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Ajouter une personne")

    def acceptPersonne(self):
        self.nom = self.lastname.text()
        self.prenom = self.firstname.text()
        self.status = self.statusBox.currentText()
        self.personnes.ajouterPersonne(self)
        self.close()
        
    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Ajouter une personne")
        liste = QComboBox()
        liste.addItems(self.statusList)

        layout = QFormLayout()
        layout.addRow(QLabel("Nom: "), self.lastname)
        layout.addRow(QLabel("Prénom: "), self.firstname)
        layout.addRow(QLabel("Statut : "), liste)
        self.formGroupBox.setLayout(layout)

class Personnes():
    personnes = []

    def __init__(self):
        super()

    def ajouterPersonne(self, personne):
        self.personnes.append(personne)