import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QFormLayout, QLineEdit, QComboBox, QSpinBox
from PyQt5 import QtCore
from classes import Meteo
from personne import Personne

meteo = Meteo()

def update_labels():
    labelMeteo.setText("Météo sur Marseille : %s (Min: %d°C / Max: %d°C)" % (meteo.get_meteo(), meteo.get_tmp()[0], meteo.get_tmp()[1]))

if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()

    w.resize(500, 120)
    w.move(300, 300)
    w.setWindowTitle('Car Manager')

    # Layout
    layout = QVBoxLayout()
    layoutBoutons = QHBoxLayout()

    labelMeteo = QLabel("")

    label = QLabel("")
    label.setWordWrap(True)
    previous = QPushButton("Supprimer un car")
    next = QPushButton("Ajouter un car")

    layoutBoutons.addWidget(previous)
    layoutBoutons.addWidget(next)

    layout.addWidget(labelMeteo)
    layout.addWidget(label)
    layout.addLayout(layoutBoutons)

    personne = Personne()

    # Update label every 10ms
    timer = QtCore.QTimer()
    timer.timeout.connect(update_labels)
    timer.start(10)

    w.setLayout(layout)
    w.show()

    sys.exit(personne.exec_())
    app.exec_()