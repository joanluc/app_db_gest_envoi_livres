#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 14:56:04 2017

@author: joanluc
"""

import sqlite3

nomidb=input("Nomi de la baisha de donadas ? ")

cadena_connec = sqlite3.connect(nomidb)
curseur = cadena_connec.cursor()

# Create table
# curseur.execute('''CREATE TABLE "'''+nomidb+'''".tb_contact
"""
curseur.execute('''CREATE TABLE tb_contact
(
  "nom_contact" character varying NOT NULL, 
  "entreprise" character varying, 
  "adresse_perso" character varying,
  "cp_ville" character varying,
  "telefone" character varying,
  "email" character varying, 
  "nbr_autres_struct" smallint,
  "autres_structures" character varying) IF NOT EXISTS''')
curseur.execute('''CREATE TABLE tb_livre
             (titre_livre text, genre text, sp boolean) IF NOT EXISTS''')
"""
# Insert a row of data
curseur.execute("INSERT INTO tb_contact VALUES ('Joanluc','oc.linux','6 all. des lapins','33125 Hostens','0622465125','joanluc.laborda@free.fr',2,'CRPP,UB')")
curseur.execute("INSERT INTO tb_livre VALUES ('Une avalanche de conséquences','policier','True')")
ENT=('oc.linux',)
curseur.execute("SELECT nom_contact,telefone FROM tb_contact WHERE entreprise=?", ENT)
print(curseur.fetchone())

LIBRES=[('Les enfants du Graal','Roman','False'),
        ('Le jeu de Go','Tutoriel','False'),
        ('Aimat Lacapera','BD','True')]
curseur.executemany("INSERT INTO tb_livre VALUES (?,?,?)",LIBRES)
# curseur.fetchone()
for linha in curseur.execute("SELECT DISTINCT FROM tb_livre WHERE sp = 'True'"):
    print(linha)

# Save (commit) the changes
cadena_connec.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.

cadena_connec.close()