# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_gest_envoi_livres.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(586, 692)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gestEnvoi = QtWidgets.QTabWidget(self.centralwidget)
        self.gestEnvoi.setGeometry(QtCore.QRect(10, 0, 561, 601))
        self.gestEnvoi.setUsesScrollButtons(False)
        self.gestEnvoi.setObjectName("gestEnvoi")
        self.Entreprises = QtWidgets.QWidget()
        self.Entreprises.setObjectName("Entreprises")
        self.groupBox = QtWidgets.QGroupBox(self.Entreprises)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 521, 541))
        self.groupBox.setObjectName("groupBox")
        self.nom_prenom = QtWidgets.QLineEdit(self.groupBox)
        self.nom_prenom.setGeometry(QtCore.QRect(122, 20, 91, 21))
        self.nom_prenom.setObjectName("nom_prenom")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.label.setObjectName("label")
        self.adresse_perso = QtWidgets.QLineEdit(self.groupBox)
        self.adresse_perso.setGeometry(QtCore.QRect(120, 54, 91, 20))
        self.adresse_perso.setObjectName("adresse_perso")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 91, 20))
        self.label_2.setObjectName("label_2")
        self.cp_ville_pays = QtWidgets.QLineEdit(self.groupBox)
        self.cp_ville_pays.setGeometry(QtCore.QRect(120, 88, 91, 21))
        self.cp_ville_pays.setText("")
        self.cp_ville_pays.setObjectName("cp_ville_pays")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 91, 16))
        self.label_3.setObjectName("label_3")
        self.telephone = QtWidgets.QLineEdit(self.groupBox)
        self.telephone.setGeometry(QtCore.QRect(122, 118, 91, 21))
        self.telephone.setText("")
        self.telephone.setObjectName("telephone")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 91, 16))
        self.label_4.setObjectName("label_4")
        self.email_entreprise = QtWidgets.QLineEdit(self.groupBox)
        self.email_entreprise.setGeometry(QtCore.QRect(122, 150, 231, 21))
        self.email_entreprise.setObjectName("email_entreprise")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 150, 91, 16))
        self.label_5.setObjectName("label_5")
        self.nom_prenom_contact_1 = QtWidgets.QLineEdit(self.groupBox)
        self.nom_prenom_contact_1.setGeometry(QtCore.QRect(182, 268, 171, 21))
        self.nom_prenom_contact_1.setObjectName("nom_prenom_contact_1")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 270, 151, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(8, 302, 151, 16))
        self.label_7.setObjectName("label_7")
        self.nom_prenom_contact_2 = QtWidgets.QLineEdit(self.groupBox)
        self.nom_prenom_contact_2.setGeometry(QtCore.QRect(180, 300, 171, 21))
        self.nom_prenom_contact_2.setObjectName("nom_prenom_contact_2")
        self.Remarques = QtWidgets.QTextEdit(self.groupBox)
        self.Remarques.setGeometry(QtCore.QRect(130, 330, 371, 64))
        self.Remarques.setObjectName("Remarques")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 330, 81, 16))
        self.label_8.setObjectName("label_8")
        self.Button_tout = QtWidgets.QRadioButton(self.groupBox)
        self.Button_tout.setGeometry(QtCore.QRect(190, 420, 61, 20))
        self.Button_tout.setObjectName("Button_tout")
        self.par_genre = QtWidgets.QRadioButton(self.groupBox)
        self.par_genre.setGeometry(QtCore.QRect(260, 420, 71, 20))
        self.par_genre.setObjectName("par_genre")
        self.choix_genre = QtWidgets.QScrollArea(self.groupBox)
        self.choix_genre.setGeometry(QtCore.QRect(340, 400, 161, 41))
        self.choix_genre.setWidgetResizable(True)
        self.choix_genre.setObjectName("choix_genre")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 159, 39))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.choix_genre.setWidget(self.scrollAreaWidgetContents)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(20, 420, 141, 16))
        self.label_9.setObjectName("label_9")
        self.frameIdEntreprise = QtWidgets.QFrame(self.groupBox)
        self.frameIdEntreprise.setGeometry(QtCore.QRect(10, 20, 501, 231))
        self.frameIdEntreprise.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameIdEntreprise.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameIdEntreprise.setObjectName("frameIdEntreprise")
        self.frameEnvoiLivre = QtWidgets.QFrame(self.groupBox)
        self.frameEnvoiLivre.setGeometry(QtCore.QRect(10, 460, 501, 71))
        self.frameEnvoiLivre.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameEnvoiLivre.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameEnvoiLivre.setObjectName("frameEnvoiLivre")
        self.frame_2 = QtWidgets.QFrame(self.frameEnvoiLivre)
        self.frame_2.setGeometry(QtCore.QRect(-10, -190, 501, 201))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.frameEnvoiLivre)
        self.dateTimeEdit.setGeometry(QtCore.QRect(300, 40, 194, 21))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_10 = QtWidgets.QLabel(self.frameEnvoiLivre)
        self.label_10.setGeometry(QtCore.QRect(8, 10, 91, 16))
        self.label_10.setObjectName("label_10")
        self.checkBox = QtWidgets.QCheckBox(self.frameEnvoiLivre)
        self.checkBox.setGeometry(QtCore.QRect(10, 40, 87, 20))
        self.checkBox.setObjectName("checkBox")
        self.entreprise = QtWidgets.QRadioButton(self.frameEnvoiLivre)
        self.entreprise.setGeometry(QtCore.QRect(200, 40, 111, 20))
        self.entreprise.setObjectName("entreprise")
        self.titre_livre = QtWidgets.QLineEdit(self.frameEnvoiLivre)
        self.titre_livre.setGeometry(QtCore.QRect(220, 10, 91, 21))
        self.titre_livre.setObjectName("titre_livre")
        self.contact = QtWidgets.QRadioButton(self.frameEnvoiLivre)
        self.contact.setGeometry(QtCore.QRect(110, 40, 81, 20))
        self.contact.setObjectName("contact")
        self.label_11 = QtWidgets.QLabel(self.frameEnvoiLivre)
        self.label_11.setGeometry(QtCore.QRect(108, 10, 91, 16))
        self.label_11.setObjectName("label_11")
        self.reprsentant = QtWidgets.QLineEdit(self.groupBox)
        self.reprsentant.setGeometry(QtCore.QRect(120, 180, 91, 21))
        self.reprsentant.setObjectName("reprsentant")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(10, 180, 91, 16))
        self.label_12.setObjectName("label_12")
        self.groupement = QtWidgets.QLineEdit(self.groupBox)
        self.groupement.setGeometry(QtCore.QRect(120, 210, 91, 21))
        self.groupement.setText("")
        self.groupement.setObjectName("groupement")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(10, 210, 91, 16))
        self.label_13.setObjectName("label_13")
        self.gestEnvoi.addTab(self.Entreprises, "")
        self.contacts = QtWidgets.QWidget()
        self.contacts.setObjectName("contacts")
        self.groupBox_2 = QtWidgets.QGroupBox(self.contacts)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 521, 541))
        self.groupBox_2.setObjectName("groupBox_2")
        self.nom_prenom_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.nom_prenom_2.setGeometry(QtCore.QRect(122, 20, 91, 21))
        self.nom_prenom_2.setObjectName("nom_prenom_2")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.label_14.setObjectName("label_14")
        self.adresse_perso_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.adresse_perso_2.setGeometry(QtCore.QRect(120, 54, 91, 20))
        self.adresse_perso_2.setObjectName("adresse_perso_2")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(10, 60, 91, 20))
        self.label_15.setObjectName("label_15")
        self.cp_ville_pays_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.cp_ville_pays_2.setGeometry(QtCore.QRect(120, 88, 91, 21))
        self.cp_ville_pays_2.setText("")
        self.cp_ville_pays_2.setObjectName("cp_ville_pays_2")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(10, 90, 91, 16))
        self.label_16.setObjectName("label_16")
        self.telephone_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.telephone_2.setGeometry(QtCore.QRect(122, 118, 91, 21))
        self.telephone_2.setText("")
        self.telephone_2.setObjectName("telephone_2")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(10, 120, 91, 16))
        self.label_17.setObjectName("label_17")
        self.email_contact = QtWidgets.QLineEdit(self.groupBox_2)
        self.email_contact.setGeometry(QtCore.QRect(122, 150, 231, 21))
        self.email_contact.setObjectName("email_contact")
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(10, 150, 91, 16))
        self.label_18.setObjectName("label_18")
        self.entreprise_associee_1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.entreprise_associee_1.setGeometry(QtCore.QRect(182, 188, 171, 21))
        self.entreprise_associee_1.setObjectName("entreprise_associee_1")
        self.label_19 = QtWidgets.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(10, 190, 151, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(8, 222, 151, 16))
        self.label_20.setObjectName("label_20")
        self.entreprise_associee_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.entreprise_associee_2.setGeometry(QtCore.QRect(180, 220, 171, 21))
        self.entreprise_associee_2.setObjectName("entreprise_associee_2")
        self.Remarques_2 = QtWidgets.QTextEdit(self.groupBox_2)
        self.Remarques_2.setGeometry(QtCore.QRect(130, 250, 371, 64))
        self.Remarques_2.setObjectName("Remarques_2")
        self.label_21 = QtWidgets.QLabel(self.groupBox_2)
        self.label_21.setGeometry(QtCore.QRect(10, 250, 81, 16))
        self.label_21.setObjectName("label_21")
        self.Button_tout_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.Button_tout_2.setGeometry(QtCore.QRect(190, 320, 61, 20))
        self.Button_tout_2.setObjectName("Button_tout_2")
        self.par_genre_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.par_genre_2.setGeometry(QtCore.QRect(260, 320, 71, 20))
        self.par_genre_2.setObjectName("par_genre_2")
        self.choix_genre_2 = QtWidgets.QScrollArea(self.groupBox_2)
        self.choix_genre_2.setGeometry(QtCore.QRect(339, 320, 161, 41))
        self.choix_genre_2.setWidgetResizable(True)
        self.choix_genre_2.setObjectName("choix_genre_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 159, 39))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.choix_genre_2.setWidget(self.scrollAreaWidgetContents_2)
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        self.label_22.setGeometry(QtCore.QRect(20, 320, 141, 16))
        self.label_22.setObjectName("label_22")
        self.titre_livre_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.titre_livre_2.setGeometry(QtCore.QRect(230, 390, 91, 21))
        self.titre_livre_2.setObjectName("titre_livre_2")
        self.label_23 = QtWidgets.QLabel(self.groupBox_2)
        self.label_23.setGeometry(QtCore.QRect(118, 390, 91, 16))
        self.label_23.setObjectName("label_23")
        self.SP = QtWidgets.QCheckBox(self.groupBox_2)
        self.SP.setGeometry(QtCore.QRect(20, 390, 87, 20))
        self.SP.setObjectName("SP")
        self.contact_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.contact_2.setGeometry(QtCore.QRect(20, 420, 81, 20))
        self.contact_2.setObjectName("contact_2")
        self.entreprise_2 = QtWidgets.QRadioButton(self.groupBox_2)
        self.entreprise_2.setGeometry(QtCore.QRect(110, 420, 111, 20))
        self.entreprise_2.setObjectName("entreprise_2")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.groupBox_2)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(310, 420, 194, 21))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.frame_4 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_4.setGeometry(QtCore.QRect(10, 19, 501, 161))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_5.setGeometry(QtCore.QRect(9, 179, 501, 191))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_6 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_6.setGeometry(QtCore.QRect(10, 370, 501, 81))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gestEnvoi.addTab(self.contacts, "")
        self.livres = QtWidgets.QWidget()
        self.livres.setObjectName("livres")
        self.label_24 = QtWidgets.QLabel(self.livres)
        self.label_24.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.label_24.setObjectName("label_24")
        self.frame_7 = QtWidgets.QFrame(self.livres)
        self.frame_7.setGeometry(QtCore.QRect(20, 40, 501, 161))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_25 = QtWidgets.QLabel(self.frame_7)
        self.label_25.setGeometry(QtCore.QRect(10, 10, 141, 16))
        self.label_25.setObjectName("label_25")
        self.titre_livre_3 = QtWidgets.QLineEdit(self.frame_7)
        self.titre_livre_3.setGeometry(QtCore.QRect(110, 10, 91, 21))
        self.titre_livre_3.setObjectName("titre_livre_3")
        self.titre_livre_4 = QtWidgets.QLineEdit(self.frame_7)
        self.titre_livre_4.setGeometry(QtCore.QRect(110, 40, 91, 21))
        self.titre_livre_4.setObjectName("titre_livre_4")
        self.label_26 = QtWidgets.QLabel(self.frame_7)
        self.label_26.setGeometry(QtCore.QRect(10, 40, 81, 16))
        self.label_26.setObjectName("label_26")
        self.titre_livre_5 = QtWidgets.QLineEdit(self.frame_7)
        self.titre_livre_5.setGeometry(QtCore.QRect(110, 70, 91, 21))
        self.titre_livre_5.setObjectName("titre_livre_5")
        self.label_27 = QtWidgets.QLabel(self.frame_7)
        self.label_27.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label_27.setObjectName("label_27")
        self.gestEnvoi.addTab(self.livres, "")
        self.abandon = QtWidgets.QPushButton(self.centralwidget)
        self.abandon.setGeometry(QtCore.QRect(490, 620, 80, 22))
        self.abandon.setObjectName("abandon")
        self.valide = QtWidgets.QPushButton(self.centralwidget)
        self.valide.setGeometry(QtCore.QRect(390, 620, 80, 22))
        self.valide.setObjectName("valide")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 586, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.gestEnvoi.setCurrentIndex(0)
        self.valide.pressed.connect(MainWindow.update)
        self.abandon.pressed.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Entreprise"))
        self.label.setText(_translate("MainWindow", "Raison sociale"))
        self.label_2.setText(_translate("MainWindow", "Adresse perso"))
        self.label_3.setText(_translate("MainWindow", "CP, Ville, Pays"))
        self.label_4.setText(_translate("MainWindow", "Téléphone"))
        self.label_5.setText(_translate("MainWindow", "email"))
        self.label_6.setText(_translate("MainWindow", "Nom prénom contact 1"))
        self.label_7.setText(_translate("MainWindow", "Nom prénom contact  2"))
        self.label_8.setText(_translate("MainWindow", "Remarques"))
        self.Button_tout.setText(_translate("MainWindow", "Tout"))
        self.par_genre.setText(_translate("MainWindow", "Genre"))
        self.label_9.setText(_translate("MainWindow", "Envoi systématique"))
        self.label_10.setText(_translate("MainWindow", "Liste des SP"))
        self.checkBox.setText(_translate("MainWindow", "envoyé"))
        self.entreprise.setText(_translate("MainWindow", "entreprise"))
        self.contact.setText(_translate("MainWindow", "contact"))
        self.label_11.setText(_translate("MainWindow", "Titre du livre"))
        self.label_12.setText(_translate("MainWindow", "Représentant"))
        self.label_13.setText(_translate("MainWindow", "Groupement"))
        self.gestEnvoi.setTabText(self.gestEnvoi.indexOf(self.Entreprises), _translate("MainWindow", "Onglet entreprise"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Contact"))
        self.label_14.setText(_translate("MainWindow", "Nom prénom"))
        self.label_15.setText(_translate("MainWindow", "Adresse perso"))
        self.label_16.setText(_translate("MainWindow", "CP, Ville, Pays"))
        self.label_17.setText(_translate("MainWindow", "Téléphone"))
        self.label_18.setText(_translate("MainWindow", "email"))
        self.label_19.setText(_translate("MainWindow", "Entreprise associée 1"))
        self.label_20.setText(_translate("MainWindow", "Entreprise associée 2"))
        self.label_21.setText(_translate("MainWindow", "Remarques"))
        self.Button_tout_2.setText(_translate("MainWindow", "Tout"))
        self.par_genre_2.setText(_translate("MainWindow", "Genre"))
        self.label_22.setText(_translate("MainWindow", "Envoi systématique"))
        self.label_23.setText(_translate("MainWindow", "Titre du livre"))
        self.SP.setText(_translate("MainWindow", "SP"))
        self.contact_2.setText(_translate("MainWindow", "contact"))
        self.entreprise_2.setText(_translate("MainWindow", "entreprise"))
        self.gestEnvoi.setTabText(self.gestEnvoi.indexOf(self.contacts), _translate("MainWindow", "Onglet contact"))
        self.label_24.setText(_translate("MainWindow", "Envoi de livre"))
        self.label_25.setText(_translate("MainWindow", "Titre du livre"))
        self.titre_livre_3.setText(_translate("MainWindow", "Titre"))
        self.titre_livre_4.setText(_translate("MainWindow", "Auteur"))
        self.label_26.setText(_translate("MainWindow", "Auteur"))
        self.titre_livre_5.setText(_translate("MainWindow", "Genre"))
        self.label_27.setText(_translate("MainWindow", "Auteur"))
        self.gestEnvoi.setTabText(self.gestEnvoi.indexOf(self.livres), _translate("MainWindow", "Onglet livre"))
        self.abandon.setText(_translate("MainWindow", "Abandon"))
        self.valide.setText(_translate("MainWindow", "Valider"))
