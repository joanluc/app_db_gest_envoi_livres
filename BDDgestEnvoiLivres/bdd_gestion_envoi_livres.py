#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 23:07:17 2017

@author: jlrmbug@outlook.fr
"""

class BDDgestEnvoiLivres:
    def __init__(self):
        pass
    

    def errDB(Message):
        print(Message)
        return

    
    def interrogeDataBase(self,tb_FiCvs):
        pass
    
    def recherche(self,typeRecherche):
        pass
    
    def rechercheLivre(self):
        pass
    
    def ajoutContact(self,listeInfoContact):
        pass
    
    def ajoutStructure(self,listeInfoStructure):
        pass

    def ajoutLivre(self,listeInfoLivre):
        pass
    
    def envoiLivre(self,titre,SP):
        pass
    
def responsa(Question):
    maResponsa=None
    while (maResponsa==None):
        maResponsa=input(format(Question))
    return(maResponsa)
    
def test_BDDgestEnvoiLivres (envoi=AppBDgestEnvoiLivres):
    pass

if __name__=="__main__" :
    ceLivre=responsa("Titre du livre ? \n")
    nouvEnvoiLivre = AppBDgestEnvoiLivres(ceLivre,Utilisateur,option)
    test_AppBDgestEnvoiLivres (nouvEnvoiLivre)
