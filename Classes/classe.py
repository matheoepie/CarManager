import sys
from PyQt5.QtWidgets import (QFormLayout, QLabel, QGridLayout, QLineEdit,
        QGroupBox, QDialog, QDialogButtonBox, QVBoxLayout, QComboBox)

class Classe(QDialog):
    nom =''
    def __init__(self):
        super(Classe, self).__init__()
        self.createFormGroupBox()
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        
    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Ajouter une classe")
        layout = QFormLayout()
        layout.addRow(QLabel("Nom: "), QLineEdit())
        self.formGroupBox.setLayout(layout)