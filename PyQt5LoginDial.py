#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 00:51:02 2017

@author: joanluc
PyQt5LoginDial.py
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QAction, QLineEdit


class PyQt5DbLoginDial(QWidget):
    """
    Dialogue de login pour l'utilisation du programme et la connexion à la base de données
    """
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Login"
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 240
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.SrvLabel = QLabel('Serveur', self)        
        self.SrvLabel.move(50,50)
        self.SrvTxBox = QLineEdit(self)
        self.SrvTxBox.move(200, 50)
        Srv=self.SrvTxBox.text()
        self.BdrPLabel = QLabel('Base de données', self)       
        self.BdrPLabel.move(50,75)
        self.BdrPTxBox = QLineEdit(self)
        self.BdrPTxBox.move(200, 75)
        Bdr=self.BdrPTxBox.text()
        self.nomLabel = QLabel('Utilisateur', self)       
        self.nomLabel.move(50,100)
        self.nomTxBox = QLineEdit(self)
        self.nomTxBox.move(200, 100)
        nom=self.nomTxBox.text()
        self.mdpLabel = QLabel('Mot de passe', self)       
        self.mdpLabel.move(50,125)
        self.mdpTxBox = QLineEdit(self)
        self.mdpTxBox.move(200, 125)
        mdp=self.mdpTxBox.text()
        
        bValide = QPushButton('Valider', self)
        bValide.setToolTip('Valider la saisie')
        bValide.move(220,220) 
        bValide.clicked.connect(self.accept)
        self.Connecte(dataConnect=(Srv,Bdr,nom,mdp))
        
        
        bCancel = QPushButton('Abandon', self)
        bCancel.setToolTip('Abandonner la saisie')
        bCancel.move(150,220) 
        bCancel.clicked.connect(self.reject)
        
        self.show()
        
    
    def __quit__():
        exit
        
    def Connecte(dataConnect):
        import AppBDgestEnvoiLivres
        nouvEnvoiLivre = AppBDgestEnvoiLivres("",dataConnect[2],dataConnect[3],"","postgresql",dataConnect[0],dataConnect[1])
        nouvEnvoiLivre.interrogeDataBase
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PyQt5DbLoginDial()
    sys.exit(app.exec_())