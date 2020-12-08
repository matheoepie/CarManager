import sys
from PyQt5.QtWidgets import (QFormLayout, QLabel, QGridLayout, QLineEdit,
        QGroupBox)

class Personne:
    
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        
    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Form layout")
        layout = QFormLayout()
        layout.addRow(QLabel("Nom:"), QLineEdit())
        layout.addRow(QLabel("Prénom:"), QLineEdit())
        self.formGroupBox.setLayout(layout)