#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on jeu. déc. 21 22:11:05 CET 2017

@author: Morgane Laborde <morgane.laborde@live.fr>
@author: joanluc <joanluc.laborda@free.fr>
"""

import csv
import sqlparse
from sqlparse.tokens import Keyword, DML

class NoSQL:
    """
    Interpréter les requêtes SQL dans un environnement de fichiers CSV        
    """
    def __init__(self,dbnam):
        self.dbnam=dbnam
        with open(tb_FiCvs,"r") as fcvs :
            data=csv.DictReader(fcvs)
            # __enter__(self)
            # __exit__(self):
        
    def __enter__(self):
        
    def __exit__(self):
        fcvs.close

    def isSelect(self,request)::
            # Opérations les plus courantes : lecture et recherche d'informations dans le fichier
            # analyse de la requête SQL "SELECT liste_de_champs_CVS FROM liste_de_tables_CVS WHERE condition"
            requestaSql=str(self.requestaSql)
            DISTINCT=requestaSql.find("DISTINCT")
            FROM=requestaSql.find("FROM")
            WHERE=requestaSql.find("WHERE")
            AND=requestaSql.find("AND")
            OR=requestaSql.find("OR")
            NOT=requestaSql.find("NOT")
            # data=fcvs.readline
        pass

    def isInsert(self,request):
        # Opérations les plus simples : ajout de nouvelles données dans le fichier
        # analyse de la requête SQL "INSERT INTO table  (liste_de_champs_CVS) VALUE (liste_de_donnees_CVS)"
        nv_data=self.request()
        fcvs.write(nv_data)
        pass

    def isUpdate(self,request):
        # Opérations complexes : recherche d'une donnée à modifier et écriture des modificatioons
        # analyse de la requête SQL "INSERT INTO table  (liste_de_champs_CVS) VALUE (liste_de_tables_CVS)"
        data=fcvs.readline
        fcvs.write(nv_data)
        pass
        
