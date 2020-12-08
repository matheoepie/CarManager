import json
import requests
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QGroupBox
from exceptions import *

class Meteo:
    token = "d54887352b0771a0185439e4d71da42d07392d1b1e0a8971b37485ea54a437a0"
    code_insee = "2011101"
    api_url = 'https://api.meteo-concept.com/api/forecast/daily/0?token=' + token + '&insee=' + code_insee
    headers = {'Content-Type': 'application/json'}
    weather = 0
    tmin = 0
    tmax = 0

    def __init__(self):
        print("Code insee météo : " + self.code_insee)
        print("Token API : " + self.token)
        print("API URL : " + self.api_url)
        self.new_query()

    def new_query(self):
        """
            Permet de faire appel à l'API météo l'URL a été définie dans la construction de la classe.
            Le résultat de la requête est stocké dans les attributs de la classe
        """
        response = requests.get(self.api_url, headers=self.headers)
        if response.status_code == 200:
            result = json.loads(response.content.decode('utf-8'))
            self.weather = result['forecast']['weather']
            self.tmin = result['forecast']['tmin']
            self.tmax = result['forecast']['tmax']
        else:
            raise ApiError('Impossible de récupérer la méteo depuis l\'API')


    def get_meteo(self):
        if self.weather == 0:
            return "Beau temps"
        return "Mauvais temps"

    def get_tmp(self):
        return [self.tmin, self.tmax]

    def displayMeteo(self):
        # Layout Météo
        layoutMeteo = QVBoxLayout()
        meteoGroup = QGroupBox("Météo")
        labelMeteo1 = QLabel("Météo sur Marseille : %s" % (self.get_meteo()))
        labelMeteo2 = QLabel("Température minimale : %d°C" % (self.get_tmp()[0]))
        labelMeteo3 = QLabel("Température maximale : %d°C" % (self.get_tmp()[1]))
        layoutMeteo.addWidget(labelMeteo1)
        layoutMeteo.addWidget(labelMeteo2)
        layoutMeteo.addWidget(labelMeteo3)
        meteoGroup.setLayout(layoutMeteo)
        return meteoGroup