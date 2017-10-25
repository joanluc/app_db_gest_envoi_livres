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
        
        actContact = QAction(QIcon('contact.png'), 'Ajout contact', self)
        actContact.setShortcut('Ctrl+C')
        actContact.setStatusTip('Formulaire contact')
        # actContact.triggered.connect(self.ongletContact)
        actContact.triggered.connect(self.ongletContact("ajout"))
        actContact = QAction(QIcon('contact.png'), 'Recherche contact', self)
        actContact.setShortcut('Ctrl+C')
        actContact.setStatusTip('Formulaire contact')
        actContact.triggered.connect(self.ongletContact("recherche"))
        
        actEntreprise = QAction(QIcon('entreprise.png'), 'Ajout entreprise', self)
        actEntreprise.setShortcut('Ctrl+E')
        actEntreprise.setStatusTip('Formulaire entreprise')
        actEntreprise.triggered.connect(self.ongletEntreprise("ajout"))
        actEntreprise = QAction(QIcon('entreprise.png'), 'Recherche entreprise', self)
        actEntreprise.setShortcut('Ctrl+E')
        actEntreprise.setStatusTip('Formulaire entreprise')
        actEntreprise.triggered.connect(self.ongletEntreprise("recherche"))
        
        actLivre = QAction(QIcon('livre.png'), 'Livre', self)
        actLivre.setShortcut('Ctrl+L')
        actLivre.setStatusTip('Formulaire livre')
        actLivre.triggered.connect(self.ongletLivre)
        
        # Menu Fichier Create new action
        newAct = QAction(QIcon('img/new.png'), '&New', self)        
        newAct.setShortcut('Ctrl+N')
        newAct.setStatusTip('Nouveau fichier CVS')
        newAct.triggered.connect(self.newCall)
        openAct = QAction(QIcon('img/open.png'), '&Open', self)        
        openAct.setShortcut('Ctrl+O')
        openAct.setStatusTip('Ouvre fichier CVS')
        openAct.triggered.connect(self.openCall)        
        exitAct = QAction(QIcon('img/exit24.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)
        Aide = QAction(QIcon('img/aide.png'), '&aide', self)        
        Aide.setShortcut('Ctrl+A')
        Aide.setStatusTip('Aide')
        Aide.triggered.connect(self.Aide)        
        Preferences = QAction(QIcon('img/pref.png'), '&Prefs', self)        
        Preferences.setShortcut('Ctrl+P')
        Preferences.setStatusTip('Preferences')
        Preferences.triggered.connect(self.Preferences)        
        Apropos = QAction(QIcon('img/about.png'), '&aBout', self)        
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

        toolbar = self.addToolBar('Livre')
        toolbar.addAction(actLivre)
        toolbar.addAction(actContact)
        toolbar.addAction(actEntreprise)
        toolbar.addAction(exitAct)
        # self.ongletEntreprise()    
               
        #--- Affichage d'une photo de bibliothèque comme image de fond
        self.fond = QPixmap("img/bibli.jpg")
        # redim si nécessaire à la taille de la case sans déformation
        wpix, hpix =  self.fond.width(), self.fond.height()
        # afficher dans le rectagle calculé 
        # QPainter.drawPixmap (self, QRect targetRect, QPixmap pixmap, QRect sourceRect)
        bibli=QPainter()
        bibli.begin(self.fond)
        bibli.drawPixmap(wpix,hpix,self.fond) 
        bibli.end
        
        #### Test QLabel
        # self.titreLabel = QLabel('Test', self)        
        # self.titreLabel.move(50,50)
        # self.titreTxBox = QLineEdit(self)
        # self.titreTxBox.move(200, 50)
        # testLabel=format(self.titreTxBox.text())
        
        # self.bValide = QPushButton('Valider', self)
        # self.bValide.setToolTip('Valider la saisie')
        # self.bValide.move(400,450) 
        # if (self.bValide.clicked.connect(self.accept)) :
            # print(testLabel)
        # # self.bValide.clicked.connect(self.on_click)
        # self.error(testLabel)
        # self.bCancel = QPushButton('Abandon', self)
        # self.bCancel.setToolTip('Abandonner la saisie')
        # self.bCancel.move(500,450) 
        # self.bCancel.clicked.connect(self.reject)
        
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
        
    def ongletLivre(self,option):
        """
        Formulaire de saisie des infos par livre
        """
        # print(self.ongletLivre.__doc__)     
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        diaLivre = QMdiSubWindow()
        
        diaLivre.left = 10
        diaLivre.top = 10
        diaLivre.width = 500
        diaLivre.height = 200   
        
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
            
        
        diaLivre.bValide = QPushButton('Valider', diaLivre)
        diaLivre.bValide.setToolTip('Valider la saisie')
        diaLivre.bValide.move(300,150) 
        diaLivre.bValide.clicked.connect(self.accept)
        # self.bValide.clicked.connect(self.on_click)
        
        diaLivre.bCancel = QPushButton('Abandon', diaLivre)
        diaLivre.bCancel.setToolTip('Abandonner la saisie')
        diaLivre.bCancel.move(400,150) 
        diaLivre.bCancel.clicked.connect(self.reject)
        
        self.mdi.addSubWindow(diaLivre)
        diaLivre.show()
        
        print("Titre : "+titre+" ,auteur : "+auteur+" ,genre : "+genre)
        # AppBDgestEnvoiLivres.ajoutLivre([titre,auteur,genre])
        if (option == "ajout"):
            AppBDgestEnvoiLivres.ajoutLivre([titre,auteur,genre])
        elif (option == "recherche"):
            AppBDgestEnvoiLivres.rechercheLivre()
        return([titre,auteur,genre])
        
    def ongletContact(self,option):
        """
        Formulaire de saisie des infos par contact
        """
        # print(self.ongletContact.__doc__)
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)   
        diaContact = QMdiSubWindow()
        
        diaContact.left = 10
        diaContact.top = 10
        diaContact.width = 500
        diaContact.height = 200   
        
        # =self.labelTextbox('Raison sociale',50)
        diaContact.nomPLabel = QLabel('Nom prénom', diaContact)        
        diaContact.nomPLabel.move(50,50)
        diaContact.nomPTxBox = QLineEdit(diaContact)
        diaContact.nomPTxBox.move(200, 50)
        # self.rSocTxBox.resize(220,50)
        nomP=diaContact.nomPTxBox.text()# adrP=self.labelTextbox('Adresse personelle',75)  
        diaContact.adrPLabel = QLabel('Adresse personelle', diaContact)       
        diaContact.adrPLabel.move(50,75)
        diaContact.adrPTxBox = QLineEdit(diaContact)
        diaContact.adrPTxBox.move(200, 75)
        # self.adrPTxBox.resize(220,75)
        adrP=diaContact.adrPTxBox.text()
        # cpVi=self.labelTextbox('Code postal - Ville',100) 
        diaContact.cpViLabel = QLabel('Code postal - Ville', diaContact)       
        diaContact.cpViLabel.move(50,100)
        diaContact.cpViTxBox = QLineEdit(diaContact)
        diaContact.cpViTxBox.move(200, 100)
        # self.cpViTxBox.resize(220,100)
        cpVi=diaContact.cpViTxBox.text()
        # telf=self.labelTextbox('Téléphone',125) 
        diaContact.telfLabel = QLabel('Téléphone', diaContact)       
        diaContact.telfLabel.move(50,125)
        diaContact.telfTxBox = QLineEdit(diaContact)
        diaContact.telfTxBox.move(200, 125)
        # self.telfTxBox.resize(220,125)
        telf=diaContact.telfTxBox.text()
        # emel=self.labelTextbox('email',150) 
        diaContact.emelLabel = QLabel('email', diaContact)       
        diaContact.emelLabel.move(50,150)
        diaContact.emelTxBox = QLineEdit(diaContact)
        diaContact.emelTxBox.move(200, 150)
        # self.emelTxBox.resize(220,150)
        emel=diaContact.emelTxBox.text()
        # print(self.ongletContact.__module__)
            
        
        diaContact.bValide = QPushButton('Valider', diaContact)
        diaContact.bValide.setToolTip('Valider la saisie')
        diaContact.bValide.move(300,200) 
        diaContact.bValide.clicked.connect(self.accept)
        # self.bValide.clicked.connect(self.on_click)
        
        diaContact.bCancel = QPushButton('Abandon', diaContact)
        diaContact.bCancel.setToolTip('Abandonner la saisie')
        diaContact.bCancel.move(400,200) 
        diaContact.bCancel.clicked.connect(self.reject)
        
        self.mdi.addSubWindow(diaContact)
        
        diaContact.show()
        if (option == "ajout"):
            AppBDgestEnvoiLivres.ajoutContact([nomP,adrP,cpVi,telf,emel])
        elif (option == "recherche"):
            AppBDgestEnvoiLivres.recherche("contacts")
        
        return([nomP,adrP,cpVi,telf,emel])
        
    def ongletEntreprise(self,option):
        """
        Formulaire de saisie des infos par entreprise
        """
        # print(self.ongletEntreprise.__doc__)
        # =self.labelTextbox('Raison sociale',50)
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)   
        diaEntreprise = QMdiSubWindow()
        
        diaEntreprise.left = 10
        diaEntreprise.top = 10
        diaEntreprise.width = 500
        diaEntreprise.height = 200   
        
        
        diaEntreprise.rSocLabel = QLabel('Raison sociale', diaEntreprise)        
        diaEntreprise.rSocLabel.move(50,50)
        diaEntreprise.rSocTxBox = QLineEdit(diaEntreprise)
        diaEntreprise.rSocTxBox.move(200, 50)
        # self.rSocTxBox.resize(220,50)
        rSoc=diaEntreprise.rSocTxBox.text()
        # return(valorTextbox)
        # adrP=self.labelTextbox('Adresse personelle',75)  
        diaEntreprise.adrPLabel = QLabel('Adresse personelle', diaEntreprise)       
        diaEntreprise.adrPLabel.move(50,75)
        diaEntreprise.adrPTxBox = QLineEdit(diaEntreprise)
        diaEntreprise.adrPTxBox.move(200, 75)
        # self.adrPTxBox.resize(220,75)
        adrP=diaEntreprise.adrPTxBox.text()
        # cpVi=self.labelTextbox('Code postal - Ville',100) 
        diaEntreprise.cpViLabel = QLabel('Code postal - Ville', diaEntreprise)       
        diaEntreprise.cpViLabel.move(50,100)
        diaEntreprise.cpViTxBox = QLineEdit(diaEntreprise)
        diaEntreprise.cpViTxBox.move(200, 100)
        # self.cpViTxBox.resize(220,100)
        cpVi=diaEntreprise.cpViTxBox.text()
        # telf=self.labelTextbox('Téléphone',125) 
        diaEntreprise.telfLabel = QLabel('Téléphone', diaEntreprise)       
        diaEntreprise.telfLabel.move(50,125)
        diaEntreprise.telfTxBox = QLineEdit(diaEntreprise)
        diaEntreprise.telfTxBox.move(200, 125)
        # self.telfTxBox.resize(220,125)
        telf=diaEntreprise.telfTxBox.text()
        # emel=self.labelTextbox('email',150) 
        diaEntreprise.emelLabel = QLabel('email', diaEntreprise)       
        diaEntreprise.emelLabel.move(50,150)
        diaEntreprise.emelTxBox = QLineEdit(diaEntreprise)
        diaEntreprise.emelTxBox.move(200, 150)
        # self.emelTxBox.resize(220,150)
        emel=diaEntreprise.emelTxBox.text()
        # rpst=self.labelTextbox('représentant',175) 
        diaEntreprise.rpstLabel = QLabel('représentant', diaEntreprise)       
        diaEntreprise.rpstLabel.move(50,175)
        diaEntreprise.rpstTxBox = QLineEdit(diaEntreprise)
        diaEntreprise.rpstTxBox.move(200, 175)
        # self.rpstTxBox.resize(220,175)
        rpst=diaEntreprise.rpstTxBox.text()
        # grpm=self.labelTextbox('groupement',200) 
        diaEntreprise.grpmLabel = QLabel('groupement', diaEntreprise)       
        diaEntreprise.grpmLabel.move(50,200)
        diaEntreprise.grpmTxBox = QLineEdit(diaEntreprise)
        diaEntreprise.grpmTxBox.move(200, 200)
        # self.grpmTxBox.resize(220,200)
        grpm=diaEntreprise.grpmTxBox.text()
        
        
        diaEntreprise.lRadioTout = QLabel("Tout")    
        diaEntreprise.lRadioTout.move(140,240)
        diaEntreprise.bRadioTout = QRadioButton()
        # self.bRadioTout.setGeometry(QRect(190, 240, 61, 20))
        diaEntreprise.bRadioTout.setObjectName("bRadioTout")
        
        diaEntreprise.lRadioGenre = QLabel("Genre")  
        diaEntreprise.lRadioTout.move(210,240)
        diaEntreprise.bRadioGenre = QRadioButton()
        # self.bRadioGenre.setGeometry(QRect(260, 240, 71, 20))
        diaEntreprise.bRadioGenre.setObjectName("bRadioGenre")
            
        
        diaEntreprise.bValide = QPushButton('Valider', diaEntreprise)
        diaEntreprise.bValide.setToolTip('Valider la saisie')
        diaEntreprise.bValide.move(300,450) 
        diaEntreprise.bValide.clicked.connect(self.accept)
        # self.bValide.clicked.connect(self.on_click)
        
        diaEntreprise.bCancel = QPushButton('Abandon', diaEntreprise)
        diaEntreprise.bCancel.setToolTip('Abandonner la saisie')
        diaEntreprise.bCancel.move(400,450) 
        if (diaEntreprise.bCancel.clicked.connect(self.reject)) :
            diaEntreprise.close
        
        self.mdi.addSubWindow(diaEntreprise)
        
        diaEntreprise.show()
        
        # AppBDgestEnvoiLivres.ajoutStructure([rSoc,adrP,cpVi,telf,emel,rpst,grpm])
        if (option == "ajout"):
            AppBDgestEnvoiLivres.ajoutStructure([rSoc,adrP,cpVi,telf,emel,rpst,grpm])
        elif (option == "recherche"):
            AppBDgestEnvoiLivres.recherche(Structure([rSoc,adrP,cpVi,telf,emel,rpst,grpm]))
        
        # print(self.ongletEntreprise.__module__)
        
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