CREATE TABLE "Librairie".tb_librairie_presse
(
    "Nom_librairie" "char"[] NOT NULL,
    "Adresse_lib" "char"[],
    cp_ville "char"[],
    "Tel_lib" "char"[],
    "e-mail" inet[],
    "Repré" "char"[],
    "Groupement" "char"[],
    "Remarque" text COLLATE pg_catalog."default",
    typ_entreprise integer,
    envoi_sys integer,
    CONSTRAINT tb_librairie_pkey PRIMARY KEY ("Nom_librairie")
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE "Librairie".tb_librairie_presse
    OWNER to postgres;

GRANT ALL ON TABLE "Librairie".tb_librairie_presse TO "Librairie" WITH GRANT OPTION;

GRANT ALL ON TABLE "Librairie".tb_librairie_presse TO "Morgane" WITH GRANT OPTION;

GRANT ALL ON TABLE "Librairie".tb_librairie_presse TO postgres;

COMMENT ON TABLE "Librairie".tb_librairie_presse
    IS 'Table des librairies
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

SP		: clé étrangère	';

COMMENT ON COLUMN "Librairie".tb_librairie_presse.cp_ville
    IS 'Code Postal + ville + pays';