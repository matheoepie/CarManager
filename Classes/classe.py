import sys
from PyQt5.QtWidgets import (QFormLayout, QLabel, QGridLayout, QLineEdit,
        QGroupBox, QDialog, QDialogButtonBox, QVBoxLayout, QComboBox)

class Classe(QDialog):
    nom =''
    def __init__(self, classes):
        super(Classe, self).__init__()
        self.nameLineEdit = QLineEdit()  
        self.classes = classes
        self.nom = ''
        self.createFormGroupBox()
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.validate)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        
    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Ajouter une classe")
        
        layout = QFormLayout()
        layout.addRow(QLabel("Nom: "), self.nameLineEdit)
        self.formGroupBox.setLayout(layout)

    def validate(self):
        self.nom = self.nameLineEdit.text()
        self.classes.add(self.nom)
        self.close()
        
class Classes:
    def __init__(self):
        self.listClasses = []
        self.listClassesstr =''
    
    def add(self, classe):
        self.listClasses.append(classe)
        
    def displayClasses(self):       
        for classe in self.listClasses:
           self.listClassesstr  = "['{}']".format(classe)
        return self.listClassesstr