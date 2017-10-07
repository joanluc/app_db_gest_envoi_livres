#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 21:52:50 2017

@author: joanluc
PyQt5DbGestEnvLivres.py
"""

# Exemples PyQt -> https://pythonprogramminglanguage.com/pyqt-menu/

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, \
QLabel, QAction, QLineEdit, QMessageBox, QDialog, QRadioButton, QMdiArea, QMdiSubWindow
from PyQt5.QtGui import QIcon,QPixmap,QPainter
from PyQt5.QtCore import pyqtSlot,QRect
import AppBDgestEnvoiLivres
 
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
        actContact.setStatusTip('Formulaire contact')
        actContact.triggered.connect(self.ongletContact)
        
        actEntreprise = QAction(QIcon('entreprise.png'), 'Entreprise', self)
        actEntreprise.setShortcut('Ctrl+E')
        actEntreprise.setStatusTip('Formulaire entreprise')
        actEntreprise.triggered.connect(self.ongletEntreprise)
        
        actLivre = QAction(QIcon('livre.png'), 'Livre', self)
        actLivre.setShortcut('Ctrl+L')
        actLivre.setStatusTip('Formulaire livre')
        actLivre.triggered.connect(self.ongletLivre)
        
        # Menu Fichier Create new action
        newAct = QAction(QIcon('new.png'), '&New', self)        
        newAct.setShortcut('Ctrl+N')
        newAct.setStatusTip('Nouveau fichier CVS')
        newAct.triggered.connect(self.newCall)
        openAct = QAction(QIcon('open.png'), '&Open', self)        
        openAct.setShortcut('Ctrl+O')
        openAct.setStatusTip('Ouvre fichier CVS')
        openAct.triggered.connect(self.openCall)        
        exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)
        Aide = QAction(QIcon('aide.png'), '&aide', self)        
        Aide.setShortcut('Ctrl+A')
        Aide.setStatusTip('Aide')
        Aide.triggered.connect(self.Aide)        
        Preferences = QAction(QIcon('pref.png'), '&Prefs', self)        
        Preferences.setShortcut('Ctrl+P')
        Preferences.setStatusTip('Preferences')
        Preferences.triggered.connect(self.Preferences)        
        Apropos = QAction(QIcon('about.png'), '&aBout', self)        
        Apropos.setShortcut('Ctrl+B')
        Apropos.setStatusTip('Apropos')
        Apropos.triggered.connect(self.about)        

        # Menu Fichier 
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Fichier')
        fileMenu.addAction(newAct)
        fileMenu.addAction(openAct)
        fileMenu.addAction(exitAct)
        fileMenu = menubar.addMenu('&Aide')
        fileMenu.addAction(Aide)
        fileMenu.addAction(Preferences)
        fileMenu.addAction(Apropos)
        
        fileMenu = menubar.addMenu('&Contact')
        fileMenu.addAction(actContact)
        fileMenu = menubar.addMenu('&Entreprise')
        fileMenu.addAction(actEntreprise)
        fileMenu = menubar.addMenu('&Livre')
        fileMenu.addAction(actLivre)
        # fileMenu.triggered[QAction].connect(self)  #  windowaction PyQT4

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)
        toolbar.addAction(actContact)
        toolbar.addAction(actEntreprise)
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


    def error(self,Message):
        dialog = QMessageBox()
        dialog.setText(Message)
        dret=dialog.exec()                
        
    def Aide(self):
        self.error("Aide : fonction pas encore implémentée")
        
    def Preferences(self):
        self.error("Preferences : fonction pas encore implémentée")
        
    def about(self):
        self.error("A propos")
        self.errort(self.__doc__)
        self.error(AppBDgestEnvoiLivres.__doc__)
        
    def newCall(self):
        self.error("Nouveau fichier CVS")
        
    def openCall(self):
        self.error("Ouvre fichier CVS")
        
        
    def Contact(self):
        monContact=self.ongletContact()
        envoiMonContact=AppBDgestEnvoiLivres(monContact)
        
    def Entreprise(self):
        monEntr=self.ongletEntreprise()
        envoiMonEntr=AppBDgestEnvoiLivres(monEntr)
    def Livre(self):
        monLivre=self.ongletLivre()
        envoiMonLivre=AppBDgestEnvoiLivres(monLivre)
        
    def ongletLivre(self):
        """
        Formulaire de saisie des infos par livre
        """
        # print(self.ongletLivre.__doc__)     
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)   
        diaLivre = QMdiSubWindow()
        diaLivre.setWindowTitle(self.ongletLivre.__doc__)
        diaLivre.titreLabel = QLabel('Titre livre', diaLivre)        
        diaLivre.titreLabel.move(50,50)
        diaLivre.titreTxBox = QLineEdit(diaLivre)
        diaLivre.titreTxBox.move(200, 50)
        titre=diaLivre.titreTxBox.text()
        diaLivre.auteurLabel = QLabel('Auteur', diaLivre)        
        diaLivre.auteurLabel.move(50,75)
        diaLivre.auteurTxBox = QLineEdit(diaLivre)
        diaLivre.auteurTxBox.move(200, 75)
        auteur=diaLivre.auteurTxBox.text()
        diaLivre.genreLabel = QLabel('Genre', diaLivre)        
        diaLivre.genreLabel.move(50,100)
        diaLivre.genreTxBox = QLineEdit(diaLivre)
        diaLivre.genreTxBox.move(200, 100)
        genre=diaLivre.genreTxBox.text()
        
        # print(self.ongletLivre.__module__)
        self.mdi.addSubWindow(diaLivre)
        diaLivre.show()   
        
        return([titre,auteur,genre])
        
    def ongletContact(self):
        """
        Formulaire de saisie des infos par contact
        """
        print(self.ongletContact.__doc__)
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
        print(self.ongletContact.__module__)
        
        self.show()
        
        return([nomP,adrP,cpVi,telf,emel])
        
    def ongletEntreprise(self):
        """
        Formulaire de saisie des infos par entreprise
        """
        print(self.ongletEntreprise.__doc__)
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
        
        self.show()
        print(self.ongletEntreprise.__module__)
        
        return([rSoc,adrP,cpVi,telf,emel,rpst,grpm])
        
    @pyqtSlot()
    def accept(self):
        # print('Validation '+format(self.ongletEntreprise))
        self.error('PyQt5 button click validé'+format(self))
        
    @pyqtSlot()
    def reject(self):
        # print('Abandon '+format(self))
        self.error('PyQt5 button click validé'+format(self))
        
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PyQt5DbGestEnvLivres()
    sys.exit(app.exec_())