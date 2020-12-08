import sys
from PyQt5.QtWidgets import (QFormLayout, QLabel, QGridLayout, QLineEdit,
        QGroupBox, QDialog, QDialogButtonBox, QVBoxLayout, QComboBox)

class Personne(QDialog):
    nom = ''
    prenom = ''
    status = ['Eleve', 'Professeur']

    def __init__(self):
        super(Personne, self).__init__()
        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        
    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Ajouter une personne")
        liste = QComboBox()
        liste.addItems(self.status)

        layout = QFormLayout()
        layout.addRow(QLabel("Nom: "), QLineEdit())
        layout.addRow(QLabel("Prénom: "), QLineEdit())
        layout.addRow(QLabel("Statut : "), liste)
        self.formGroupBox.setLayout(layout)