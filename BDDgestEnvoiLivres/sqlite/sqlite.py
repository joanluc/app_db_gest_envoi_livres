#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on jeu. déc. 21 22:11:05 CET 2017

@author: Morgane Laborde <morgane.laborde@live.fr>
@author: joanluc <joanluc.laborda@free.fr>
"""
import sqlite3
class bd_sqlite3:
    def __init__(self,dbnam):
        self.dbnam=dbnam
        with open(self.dbnam,"r") as db:
            connec=sqlite3.connect('{self.dbnam}')
            fcvs.__enter__(self)
            fcvs.__exit__(self)
            
    def __enter__(self):
        return self

    def __exit__(self,*arg):
        fermeDb(*arg)
        return False

    def fermeDb(self,*arg):
        print(arg,self.dbnam)
        connec.close
        
    def accesDb(self):
        curseur = cadena_connec.cursor()
        try :
            curseur.execute(self.requestaSql)
            cadena_connec.commit()
        except:
            fermeDb
