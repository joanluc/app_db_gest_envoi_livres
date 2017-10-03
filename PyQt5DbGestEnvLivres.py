#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:52:50 2017

@author: joanluc
PyQt5DbGestEnvLivres.py
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLabel, QAction, QLineEdit, QMessageBox, QRadioButton
from PyQt5.QtGui import QIcon,QPixmap,QPainter
from PyQt5.QtCore import pyqtSlot,QRect
 
class PyQt5DbGestEnvLivres(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Base de données de gestion d'envoi de livres"
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #--- Affichage d'une photo de bibliothèque comme image de fond -------------
        # self.fond = QPixmap("bibli.jpg")  
        # redim si nécessaire à la taille de la case sans déformation
        # wpix, hpix =  self.fond.width(), self.fond.height()
        # afficher dans le rectagle calculé
        # QPainter.drawPixmap(self,10, 10, self.fond) 
        
        actContact = QAction(QIcon('contact.png'), 'Contact', self)
        actContact.setShortcut('Ctrl+C')
        actContact.setStatusTip('Contact application')
        actContact.triggered.connect(self.ongletContact)
        actEntreprise = QAction(QIcon('entreprise.png'), 'Entreprise', self)
        actEntreprise.setShortcut('Ctrl+E')
        actEntreprise.setStatusTip('Entreprise application')
        actEntreprise.triggered.connect(self.ongletEntreprise)
        exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Contact')
        fileMenu.addAction(actContact)
        fileMenu = menubar.addMenu('&Entreprise')
        fileMenu.addAction(actEntreprise)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)
        
        # self.ongletEntreprise()   
        
        self.bValide = QPushButton('Valider', self)
        self.bValide.setToolTip('Valider la saisie')
        self.bValide.move(400,450) 
        self.bValide.clicked.connect(self.accept)
        # self.bValide.clicked.connect(self.on_click)
        
        self.bCancel = QPushButton('Abandon', self)
        self.bCancel.setToolTip('Abandonner la saisie')
        self.bCancel.move(500,450) 
        self.bCancel.clicked.connect(self.reject)
        
        self.show()
        
    # def labelTextbox(self,Label,coordY):
        # self.labelLTB = QLabel(Label, self)        
        # self.labelLTB.move(50,coordY)
        # self.txboxLTB = QLineEdit(self)
        # self.txboxLTB.move(200, coordY)
        # self.txboxNom.resize(220,coordY)
        # valorTextbox = self.txboxLTB.text()
        # print(valorTextbox)
        # return(valorTextbox)
        
    # def on_click(self):
        # valorTextbox = self.textbox.text()
        # return (valorTextbox)
    # def labelRadio(self,Label,dimBt):
        # self.nomBouton = QRadioButton(self)
        # self.nomBouton.setGeometry(QtCore.QRect(dimBt[0], dimBt[1], dimBt[2], dimBt[3]))
        # self.nomBouton.setGeometry(QRect(dimBt[0], dimBt[1], dimBt[2], dimBt[3]))
        # self.nomBouton.setObjectName(nomBouton)
                
        
    def ongletContact(self):
        """
        Formulaire de saisie des infos par contact
        """
        # =self.labelTextbox('Raison sociale',50)
        self.nomPLabel = QLabel('Nom prénom', self)        
        self.nomPLabel.move(50,50)
        self.nomPTxBox = QLineEdit(self)
        self.nomPTxBox.move(200, 50)
        # self.rSocTxBox.resize(220,50)
        nomP=self.nomPTxBox.text()# adrP=self.labelTextbox('Adresse personelle',75)  
        self.adrPLabel = QLabel('Adresse personelle', self)       
        self.adrPLabel.move(50,75)
        self.adrPTxBox = QLineEdit(self)
        self.adrPTxBox.move(200, 75)
        # self.adrPTxBox.resize(220,75)
        adrP=self.adrPTxBox.text()
        # cpVi=self.labelTextbox('Code postal - Ville',100) 
        self.cpViLabel = QLabel('Code postal - Ville', self)       
        self.cpViLabel.move(50,100)
        self.cpViTxBox = QLineEdit(self)
        self.cpViTxBox.move(200, 100)
        # self.cpViTxBox.resize(220,100)
        cpVi=self.cpViTxBox.text()
        # telf=self.labelTextbox('Téléphone',125) 
        self.telfLabel = QLabel('Téléphone', self)       
        self.telfLabel.move(50,125)
        self.telfTxBox = QLineEdit(self)
        self.telfTxBox.move(200, 125)
        # self.telfTxBox.resize(220,125)
        telf=self.telfTxBox.text()
        # emel=self.labelTextbox('email',150) 
        self.emelLabel = QLabel('email', self)       
        self.emelLabel.move(50,150)
        self.emelTxBox = QLineEdit(self)
        self.emelTxBox.move(200, 150)
        # self.emelTxBox.resize(220,150)
        emel=self.emelTxBox.text()
        
    def ongletEntreprise(self):
        """
        Formulaire de saisie des infos par entreprise
        """
        # =self.labelTextbox('Raison sociale',50)
        self.rSocLabel = QLabel('Raison sociale', self)        
        self.rSocLabel.move(50,50)
        self.rSocTxBox = QLineEdit(self)
        self.rSocTxBox.move(200, 50)
        # self.rSocTxBox.resize(220,50)
        rSoc=self.rSocTxBox.text()
        # return(valorTextbox)
        # adrP=self.labelTextbox('Adresse personelle',75)  
        self.adrPLabel = QLabel('Adresse personelle', self)       
        self.adrPLabel.move(50,75)
        self.adrPTxBox = QLineEdit(self)
        self.adrPTxBox.move(200, 75)
        # self.adrPTxBox.resize(220,75)
        adrP=self.adrPTxBox.text()
        # cpVi=self.labelTextbox('Code postal - Ville',100) 
        self.cpViLabel = QLabel('Code postal - Ville', self)       
        self.cpViLabel.move(50,100)
        self.cpViTxBox = QLineEdit(self)
        self.cpViTxBox.move(200, 100)
        # self.cpViTxBox.resize(220,100)
        cpVi=self.cpViTxBox.text()
        # telf=self.labelTextbox('Téléphone',125) 
        self.telfLabel = QLabel('Téléphone', self)       
        self.telfLabel.move(50,125)
        self.telfTxBox = QLineEdit(self)
        self.telfTxBox.move(200, 125)
        # self.telfTxBox.resize(220,125)
        telf=self.telfTxBox.text()
        # emel=self.labelTextbox('email',150) 
        self.emelLabel = QLabel('email', self)       
        self.emelLabel.move(50,150)
        self.emelTxBox = QLineEdit(self)
        self.emelTxBox.move(200, 150)
        # self.emelTxBox.resize(220,150)
        emel=self.emelTxBox.text()
        # rpst=self.labelTextbox('représentant',175) 
        self.rpstLabel = QLabel('représentant', self)       
        self.rpstLabel.move(50,175)
        self.rpstTxBox = QLineEdit(self)
        self.rpstTxBox.move(200, 175)
        # self.rpstTxBox.resize(220,175)
        rpst=self.rpstTxBox.text()
        # grpm=self.labelTextbox('groupement',200) 
        self.grpmLabel = QLabel('groupement', self)       
        self.grpmLabel.move(50,200)
        self.grpmTxBox = QLineEdit(self)
        self.grpmTxBox.move(200, 200)
        # self.grpmTxBox.resize(220,200)
        grpm=self.grpmTxBox.text()
        
        
        self.lRadioTout = QLabel("Tout")    
        self.lRadioTout.move(140,240)
        self.bRadioTout = QRadioButton()
        # self.bRadioTout.setGeometry(QRect(190, 240, 61, 20))
        self.bRadioTout.setObjectName("bRadioTout")
        
        self.lRadioGenre = QLabel("Genre")  
        self.lRadioTout.move(210,240)
        self.bRadioGenre = QRadioButton()
        # self.bRadioGenre.setGeometry(QRect(260, 240, 71, 20))
        self.bRadioGenre.setObjectName("bRadioGenre")
        
        return([rSoc,adrP,cpVi,telf,emel,rpst,grpm])
        
    def error(self,Message):
        self.statusBar().showMessage(Message)
        
    @pyqtSlot()
    def accept(self):
        print('Validation '+format(self.ongletEntreprise))
        # self.error('PyQt5 button click validé'+format(self))
    @pyqtSlot()
    def reject(self):
        print('Abandon '+format(self))
        # self.error('PyQt5 button click validé'+format(self))
        
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PyQt5DbGestEnvLivres()
    sys.exit(app.exec_())