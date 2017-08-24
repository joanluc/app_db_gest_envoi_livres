# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 23:07:17 2017

@author: Morgane Laborde <morgane.laborde@live.fr>
@author: joanluc <joanluc.laborda@free.fr>
"""

"""
Application de base de données pour la gestion des envois de livres gratuits

Pour les structures (librairies, centre culturel, journaux ...), il faudrait les infos générales (nom, adresse, tel, mail, représentant, groupement), le type de structure (lib, presse, gsc ou blog), un contact associé et pour chaque livre si un SP a été envoyé et quand (booléen pour l’envoi + champ avec « char » pour la date/"inconnu" si ça a été envoyé mais on sait plus quand). Certaines librairies ont un envoi systématique (all ou par genre).

Pour les contacts (responsables de librairie, blogueurs ...), il faut le même genre d’informations générales que pour les structures avec toutes les structures auxquelles ils sont associés. Il faut que ça soit lié pour que ça change automatiquement si il y a un changement d’emploi. Il faut pouvoir choisir le contact plutôt que la structure pour l’envoi pour pouvoir avoir l’adresse perso sur la liste d’envoi. Et il faut faire en sorte que ça ne fasse pas de doublons entre les contacts et les structures lors des envois.

Pour les envois, il faut pouvoir choisir le titre qui nous intéresse et avoir la liste de tous les envois à faire. Il faut aussi pouvoir spécifier lors des recherches si on veut une liste des envois pour le livre seul ou pour un envoi groupé (utiliser la date d’envoi ?).

Pour les recherches au niveau des contacts et des structures, il faudrait faire des tags pour chaque info pour avoir un large champs de recherche.
"""

import getpass, psycopg2
# import PyQt4
# http://initd.org/psycopg/docs/usage.html#passing-parameters-to-sql-queries

class AppBDgestEnvoiLivres :
    """
    Application de base de données pour la gestion des envois de livres gratuits
    * structures
    * contacts
    * envois
    Pour les recherches au niveau des contacts et des structures, il faudrait faire des tags pour chaque info pour avoir un large champs de recherche.    
    
    cas d'utilisation
    * envoi de livre
    * ajout livre
    * ajout contact
    * ajout structure
    """
    
    def __init__ (self,nomCherche,utilisateur,option="envoi",typeBase="CVS") :
#     def __init__ (self,nomCherche,utilisateur,option="envoi") :
        """
        Constructeur
        option 
        """
        self.typeBase=typeBase
        self.nomCherche=nomCherche
        self.option=option
        self.utilisateur=utilisateur
        self.u_secret=getpass.getpass()         
        self.requeteSql=""
        
    def NoSQL(self,FiCvs) :
        """
        Interpréter les requêtes SQL dans un environnement de fichiers CSV
        """
        if (self.requeteSql=="SELECT *") :
            # Opérations les plus courantes : lecture et recherche d'informations dans le fichier
            # analyse de la requête SQL "SELECT liste_de_champs_CVS FROM liste_de_tables_CVS WHERE condition"
            requeteSql=str(self.requeteSql)
            FROM=requeteSql.find("FROM") # index 27
            listeChamps=requeteSql.split()[2] # quand on n'a qu'un champ à sélectionner ça marche sinon il faut sélectionner entre 2 et la position de "FROM"
            data=fcvs.readline
        elif (self.requeteSql=="INSERT *") :
            # Opérations les plus simples : ajout de nouvelles données dans le fichier
            # analyse de la requête SQL "INSERT INTO table  (liste_de_champs_CVS) VALUE (liste_de_donnees_CVS)"
            nv_data=self.requeteSql()
            fcvs.write(nv_data)
        elif (self.requeteSql=="UPDATE *") :
            # Opérations complexes : recherche d'une donnée à modifier et écriture des modificatioons
            # analyse de la requête SQL "INSERT INTO table  (liste_de_champs_CVS) VALUE (liste_de_tables_CVS)"
            data=fcvs.readline
            fcvs.write(nv_data)
        else :
            # les autres cas de requête (DELETE | DROP | GRANT | CREATE) ne seront pas implémentés pour des raisons de sécurité des données et aussi parce qu'il est plus sumple d'utiliser un tableur
            print ("fonctionalité non implémentée")
        
    def interrogeDataBase(self,tb_FiCvs):
        """
        typeBase,tables
        """
        # print (self.typeBase)
        if (self.typeBase == "CVS"):
            fcvs=open(tb_FiCvs,"r")
            # dans tous les cas le nom de la table impliquée dans la requête sera 
            NoSQL(tb_FiCvs)
            fcvs.close
        else :
            # self.typeBase == "postgresql"
            pgConnect = psycopg2.connect(database="Librairie", user=self.utilisateur, password=self.u_secret)
            curseur=pgConnect.cursor()
            curseur.execute(self.requeteSql)
            reponses = curseur.fetchall()
        return (reponses)
    
    def recherche(self,typeRecherche):
        """
        typeRecherche = (contacts,structure)
        * fichier CVS "dbContacts.cvs"
        * table des contacts dans la base de données Postgres
        SELECT nom_contact 
            FROM table_contacts 
            WHERE nom_contact MATCHES nomCherche
        """
        if (self.typeBase == "CVS"):
            if (typeRecherche=="contacts"):
                tb_Recherche="dbContacts.cvs"
            else :
                tb_Recherche="dbStructures.cvs"
        else :  
            if (typeRecherche=="contacts"):
                tb_Recherche="tb_contacts"
            else :
                tb_Recherche="tb_structures"
        self.requeteSql=format("SELECT Nom_contact FROM "+tb_Recherche+"WHERE Nom_contact MATCHES "+self.nomCherche)
        self.interrogeDataBase(tb_Recherche)
    
#    def rechercheStructures(self):
#        """
#        * fichier CVS "dbStructures.cvs"
#            Nom,Contact,Adresse,Code Postal,Ville,Tel,Adresse
#        * table des structures dans la base de données Postgres
#        SELECT nom_structure 
#            FROM table_structure 
#            WHERE nom_contact MATCHES nomCherche
#        """
#        if (self.typeBase == "CVS"):
#            tb_structures="dbStructures.cvs"
#        else :  
#            tb_structures="tb_structures"
 #       self.interrogeDataBase("tb_structures")
    
    def rechercheLivre(self):
        """
        Recherche un ou plusieurs livres dans la base de données
        """
        if (self.typeBase == "CVS"):
            tb_livre=input("Nom fichier CVS ?")
        else : 
            tb_livre="tb_livres"
        self.requeteSql=format("SELECT Titre_livre FROM "+tb_livre+"WHERE Nom_contact MATCHES "+self.nomCherche)  
        self.interrogeDataBase(tb_livre)
    
    def ajoutContacts(self,Nom_contact,structure,Adresse_perso,Tel,E-mail):
        """
        * fichier CVS "dbContacts.cvs"
        * table des contacts dans la base de données Postgres
            ========
            Nom_contact	: clé primaire
            structure : clé étrangère
            Adresse perso	
            Tel
            E-mail	
            ========
        SELECT nom_contact 
            FROM table_contacts 
            WHERE nom_contact MATCHES nomCherche

        1		faire un système de libellés pour faciliter les recherches	. 
        Dans cette liste de résultats, seuls les noms des contacts, les villes et les pays sont nécessaires
	2		permettre l'association de plusieurs contact avec une structure	un seul envoi pour toutes les fiches associées, contact 1 par défaut
	3		permettre l'association d'un même contact avec plusieurs structures	
        lier les fiches associées pour pouvoir y accéder en passant de l’une à l’autre
        """
        if (self.typeBase == "CVS"):
            tb_contacts="tbContacts.cvs"
        else : 
            tb_contacts="tb_contacts"
        self.requeteSql=format('INSERT INTO "Librairie".'+ tb_contacts+' (Nom_contact,structure,Adresse_perso,Tel,E-mail) VALUES ('+Nom_contact+','+structure+',Adresse_perso+',',Tel+',',E-mail');'
        self.interrogeDataBase(tb_contacts)
    
    def ajoutStructures(self,Nom_librairie,Adresse_lib,cp_ville,Tel_lib,e-mail,Repre,Groupement,Remarque,typ_entreprise,envoi_sys):
        """
        * fichier CVS "dbStructures.cvs"
        * table des structures dans la base de données Postgres
            ==============
            Nom	 : clé primaire
            Adresse : donnée
            Code Postal	 	: clé étrangère
            Tel
            E-mail	
            Repré	(diffusion)
            Groupement	(associations de librairies - ex. librairies atlantique p. Aquitaine)
            SP (service de presse)		: clé étrangère			
            Remarque
            Contact	: clé étrangère
            Adresse perso	
            Tel
            E-mail	
            Code Postal	 	: clé étrangère
            Ville	
            SP		: clé étrangère	
            ==============
        SELECT nom_structure 
            FROM table_structure 
            WHERE nom_contact MATCHES nomCherche
		
        1		faire un système de libellés pour faciliter les recherches.	
	2		recherche par mot-clé, CP, ville ou pays	
	3		pouvoir rechercher par type de structure (librairie, GSC, presse, blog)	 
        Dans cette liste de résultats, seuls les noms des entreprises, les villes et les pays sont nécessaires
	1		lier les fiches associées pour pouvoir y accéder en passant de l’une à l’autre	en étant sur la fiche structure et en cliquant sur un contact je dois pouvoir aller sur la fiche contact correspondante + si changement d’emploi, changement automatique
	1		permettre l'association d'un même contact avec plusieurs structures	
        un seul envoi pour toutes les fiches associées
        """
        
        if (self.typeBase == "CVS"):
            tb_contacts="tb_structures.cvs"
        else : 
            tb_structures="tb_structures"
        self.requeteSql=format('INSERT INTO "Librairie".'+tb_structures+' (Nom_librairie,Adresse_lib,cp_ville,Tel_lib,e-mail,Repre,Groupement,Remarque,typ_entreprise,envoi_sys) VALUES ('+Nom_librairie+','+Adresse_lib+','+cp_ville+','+Tel_lib+','+e-mail+','+Repre+','+Groupement+','+Remarque+','+typ_entreprise+','+envoi_sys+');'  
        self.interrogeDataBase(tb_structures)
    
    def ajoutLivre(self):
        """
        Création d'un livre	
            1		le titre s'affiche directement dans le champ correspondant de l'interface (la partie SP des fiches ou tu parles d’un autre champ?)	
            2		Une ligne consacrée aux envois de SP du titre apparaît dans toutes les fiches structures et contact.	
            le titre s'affiche automatiquement dans la partie SP des fiches avec toutes les informations nécessaires (SP, destinataire, date)
	    1		Le SP du destinataire  s'affiche directement dans le champ correspondant de l'interface (le contact s'affiche automatiquement selon la fiche attribuée au SP) 	
	    2		Une liste d’envoi du livre se crée automatiquement dans la table « envoi »	
	    3	condition	Les fiche cochée « envoi systématique : all»	
	    4		 apparait directement dans la liste d’envoi du livre	
                liste d’envoi du titre comportant tous les destinataires et leurs adresses (à la création, seulement les systématiques normalement)
	    5	condition	fiche cochée « envoi systématique » par genre	
	    6		apparait directement dans la liste d’envoi du livre pour un genre identique	
                liste d’envoi du titre comportant tous les destinataires et leurs adresses (à la création, seulement les systématiques normalement)
     
        Recherche un ou plusieurs livres dans la base de données
        """
        self.interrogeDataBase("tb_livre")
    
    def envoiLivre(self):
        """
        Pour les envois, il faut pouvoir choisir le titre qui nous intéresse et avoir la liste de tous les envois à faire.
        * fichier CVS "envois_liste_espace+188.csv"
        * table des envois
        Titre = self.nomCherche
        Pour les envois, il faudrait que par défaut ça mette tous les envois à faire (peu importe le livre). 
        Et en options avancées, choisir le titre du livre, cocher la case envoi individuel ou groupé (grâce au champs d'envoi).
        Et il faudrait que la liste apparaisse sous cette forme pour avoir juste à l'imprimer :
            Titre,Entreprise,Contact,Adresse,CP,Ville Pays
	
           une fiche est cochée pour l'envoi d'un livre	
           1	la case SP d’un titre est cochée sans date d’envoi	
           2	l'envoi est enregistré à l'adresse de la fiche ? (préciser la signification) 	
	   3		La structure ou personne rejoint directement la liste d’envoi du titre	liste d’envoi du titre comportant tous les destinataires et leurs adresses
	   4		La structure ou personne est automatiquement notée comme « destinataire » de l’envoi dans ses fiches associées	
	   5		ça note automatiquement l'envoi sur les fiches associées pour éviter les doublons 	
           un seul envoi pour toutes les fiches associées
	   1		La structure ou personne est automatiquement notée comme « destinataire » de l’envoi dans ses fiches associées	
	   2		L’adresse notée sur la liste d’envoi est celle de la fiche cochée 	
	   je coche la fiche "lib. A" qui est associée avec "contact A" qui est lui-même associé avec "blog A"	
           1		seule "lib. A" apparait dans la liste d'envois	
	   2		 sur la fiche de "contact A" le livre soit noté envoyé à "lib. A". 	
	   3		 sur la fiche de "blog A" le livre soit noté envoyé à "lib. A". 	
	   Date d’envoi remplie	
               1	boucle	pour tous les autres titres en SP cochés	
	       2		le livre à envoyer est intégré dans la liste d’envoi des titres seuls	
	       3		fin de la liste des titres en SP cochés	le livre est intégré dans la liste d’envoi des titres seuls pour tous les SP cochés
	  Date d’envoi non remplie	
               1	boucle	pour 	
	       2	condition	au moins un autre titre en SP coché	
	       3	condition	tous les livres dont la case SP est cochée 	
	       4	et	 le champ d’envoi vide sont intégrés dans la liste des envois groupés	
               titre du livre et destinataire affichés, SP coché, date saisie ou « UNKNOWN »
	recherche par titre dans la liste d’envoi	
               1		si « seul »	liste sous forme : livre(s), structure et/ou contact, adresse, CP, ville, pays (plus facile pour impression et publipostage)
	       2		 Si  « groupé »	
         pour les envois de presse il faut mettre un argumentaire papier avec le livre.
        """   
        self.requeteSql='SELECT "Titre,Entreprise,Contact,Adresse,CP,Ville Pays" from FROM "tb_envoi" WHERE "tb_envoi"."Titre" MATCHES '+self.nomCherche
        self.interrogeDataBase("tb_envoi")
        
def test_AppBDgestEnvoiLivres (casUtilisation):
    """
    Gestion des livres	
        Création d'un livre	
            1		le titre s'affiche directement dans le champ correspondant de l'interface (la partie SP des fiches ou tu parles d’un autre champ?)	
            2		Une ligne consacrée aux envois de SP du titre apparaît dans toutes les fiches structures et contact.	
            le titre s'affiche automatiquement dans la partie SP des fiches avec toutes les informations nécessaires (SP, destinataire, date)
	    1		Le SP du destinataire  s'affiche directement dans le champ correspondant de l'interface (le contact s'affiche automatiquement selon la fiche attribuée au SP) 	
	    2		Une liste d’envoi du livre se crée automatiquement dans la table « envoi »	
	    3	condition	Les fiche cochée « envoi systématique : all»	
	    4		 apparait directement dans la liste d’envoi du livre	
                liste d’envoi du titre comportant tous les destinataires et leurs adresses (à la création, seulement les systématiques normalement)
	    5	condition	fiche cochée « envoi systématique » par genre	
	    6		apparait directement dans la liste d’envoi du livre pour un genre identique	
                liste d’envoi du titre comportant tous les destinataires et leurs adresses (à la création, seulement les systématiques normalement)
     Gestion des envois	
           une fiche est cochée pour l'envoi d'un livre	
           1	la case SP d’un titre est cochée sans date d’envoi	
           2	l'envoi est enregistré à l'adresse de la fiche ? (préciser la signification) 	
	   3		La structure ou personne rejoint directement la liste d’envoi du titre	liste d’envoi du titre comportant tous les destinataires et leurs adresses
	   4		La structure ou personne est automatiquement notée comme « destinataire » de l’envoi dans ses fiches associées	
	   5		ça note automatiquement l'envoi sur les fiches associées pour éviter les doublons 	
           un seul envoi pour toutes les fiches associées
	   1		La structure ou personne est automatiquement notée comme « destinataire » de l’envoi dans ses fiches associées	
	   2		L’adresse notée sur la liste d’envoi est celle de la fiche cochée 	
	   je coche la fiche "lib. A" qui est associée avec "contact A" qui est lui-même associé avec "blog A"	
           1		seule "lib. A" apparait dans la liste d'envois	
	   2		 sur la fiche de "contact A" le livre soit noté envoyé à "lib. A". 	
	   3		 sur la fiche de "blog A" le livre soit noté envoyé à "lib. A". 	
	   Date d’envoi remplie	
               1	boucle	pour tous les autres titres en SP cochés	
	       2		le livre à envoyer est intégré dans la liste d’envoi des titres seuls	
	       3		fin de la liste des titres en SP cochés	le livre est intégré dans la liste d’envoi des titres seuls pour tous les SP cochés
	  Date d’envoi non remplie	
               1	boucle	pour 	
	       2	condition	au moins un autre titre en SP coché	
	       3	condition	tous les livres dont la case SP est cochée 	
	       4	et	 le champ d’envoi vide sont intégrés dans la liste des envois groupés	
               titre du livre et destinataire affichés, SP coché, date saisie ou « UNKNOWN »
	recherche par titre dans la liste d’envoi	
               1		si « seul »	liste sous forme : livre(s), structure et/ou contact, adresse, CP, ville, pays (plus facile pour impression et publipostage)
	       2		 Si  « groupé »	
    Gestion des structure		
        1		faire un système de libellés pour faciliter les recherches.	
	2		recherche par mot-clé, CP, ville ou pays	
	3		pouvoir rechercher par type de structure (librairie, GSC, presse, blog)	 
        Dans cette liste de résultats, seuls les noms des entreprises, les villes et les pays sont nécessaires
	1		lier les fiches associées pour pouvoir y accéder en passant de l’une à l’autre	en étant sur la fiche structure et en cliquant sur un contact je dois pouvoir aller sur la fiche contact correspondante + si changement d’emploi, changement automatique
	1		permettre l'association d'un même contact avec plusieurs structures	
        un seul envoi pour toutes les fiches associées
    Gestion des  contacts 		
        1		faire un système de libellés pour faciliter les recherches	. 
        Dans cette liste de résultats, seuls les noms des contacts, les villes et les pays sont nécessaires
	2		permettre l'association de plusieurs contact avec une structure	un seul envoi pour toutes les fiches associées, contact 1 par défaut
	3		permettre l'association d'un même contact avec plusieurs structures	
        lier les fiches associées pour pouvoir y accéder en passant de l’une à l’autre
    """
    # casUtilisation.ajoutLivre()
    casUtilisation.ajoutStructure("Ma librairie" ,"" ,"33000" ,"0556876543" ,"" ,"" ,"Aquitaine" ,"" ,"" ,"all")    
    casUtilisation.ajoutContact("JL Laborde","oc+linux","6,allée des lapins, 33125 Hostens","06-22-46-51-25","joanluc.laborda@free.fr")
    casUtilisation.envoiLivre()
    
if __name__=="__main__" :
    Utilisateur=input("Nom utilisateur ?")
    nouvEnvoiLivre = AppBDgestEnvoiLivres("monLivre",Utilisateur)
    test_AppBDgestEnvoiLivres (nouvEnvoiLivre)
