# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 00:20:01 2017

@author: joanluc

@author: Morgane Laborde <morgane.laborde@live.fr>
@author: joanluc <joanluc.laborda@free.fr>
"""

"""
interface graphique pour AppBDgestEnvoiLivres
Les interfaces.ui doivent être converties en python avec l'outil pyuic4

installation de l'outil :
    sudo yum install python3-PyQt4-devel-4.11.3-5.fc21.x86_64
Conversion des interfaces :
    pyuic4 contact.ui -o contact.py
    pyuic4 entreprise.ui -o entreprise.py
    """
import AppBDgestEnvoiLivres


from PyQt4 import QtGui, QtCore
import sys

# import PyQt4

class QtgestEnvoiLivres ():
    """
    Interface graphique pour AppBDgestEnvoiLivres
    contact.py et entreprise.py
    """
    import Ui_ContactWindow,Ui_EntrepriseWindow