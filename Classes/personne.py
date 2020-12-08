import sys
from PyQt5.QtWidgets import (QFormLayout, QLabel, QGridLayout, QLineEdit,
        QGroupBox, QDialog, QDialogButtonBox, QVBoxLayout, QComboBox)

class Personne(QDialog):
    def __init__(self, personnes):
        super(Personne, self).__init__()

        self.lastnameLineEdit = QLineEdit()
        self.firstnameLineEdit = QLineEdit()
        self.statusBox = QComboBox()
        self.personnes = personnes

        self.nom = self.lastnameLineEdit.text()
        self.prenom = self.firstnameLineEdit.text()
        self.status = self.statusBox.currentText()
        self.statusList = ['Eleve', 'Professeur']

        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.validate)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

    def validate(self):
        self.personnes.add(self)
        self.close()

    def getLastame(self):
        return self.nom

    def getFirstname(self):
        return self.prenom

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Ajouter une personne")
        liste = QComboBox()
        liste.addItems(self.statusList)

        layout = QFormLayout()
        layout.addRow(QLabel("Nom: "), QLineEdit())
        layout.addRow(QLabel("Prénom: "), QLineEdit())
        layout.addRow(QLabel("Statut : "), liste)
        self.formGroupBox.setLayout(layout)
        self.setWindowTitle("Ajouter")

class Personnes():
    def __init__(self):
        self.listePersonnes = []

    def add(self, personne):
        self.listePersonnes.append(personne)

    def displayPersonnes(self):
        self.listeGroupBox = QGroupBox("Personnes")
        layout = QVBoxLayout()
        for item in self.listePersonnes:
            layout.addWidget(QLabel("%s %s" % (item.getLastname(), item.getFirstname())))
        self.listeGroupBox.setLayout(layout)
        return self.listeGroupBox