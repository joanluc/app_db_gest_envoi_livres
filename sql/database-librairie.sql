-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.9.0-alpha1
-- PostgreSQL version: 9.6
-- Project Site: pgmodeler.com.br
-- Model Author: ---

-- object: "Librairie" | type: ROLE --
DROP ROLE IF EXISTS "Librairie";
CREATE ROLE "Librairie" WITH ;
-- ddl-end --
COMMENT ON ROLE "Librairie" IS 'Groupe Librairie';
-- ddl-end --

-- object: morgane | type: ROLE --
DROP ROLE IF EXISTS morgane;
CREATE ROLE morgane WITH 
	INHERIT
	LOGIN
	REPLICATION
	ENCRYPTED PASSWORD 'M1ddl3H34rt'
	ADMIN "Librairie";
-- ddl-end --

-- object: joanluc | type: ROLE --
-- DROP ROLE IF EXISTS joanluc;
--CREATE ROLE joanluc WITH 
--	SUPERUSER
--	CREATEDB
--	CREATEROLE
--	INHERIT
--	LOGIN
--	REPLICATION
--	ENCRYPTED PASSWORD '1v1L4n++'
--	ROLE postgres;
-- ddl-end --


-- Database creation must be done outside an multicommand file.
-- These commands were put in this file only for convenience.
-- -- object: new_database | type: DATABASE --
-- -- DROP DATABASE IF EXISTS new_database;
-- CREATE DATABASE new_database
-- ;
-- -- ddl-end --
-- 

-- object: "Librairie" | type: SCHEMA --
DROP SCHEMA IF EXISTS "Librairie" CASCADE;

-- Prepended SQL commands --
CREATE SCHEMA "Librairie"
  AUTHORIZATION morgane; -- joanluc;

 -- GRANT ALL ON SCHEMA "Librairie" TO joanluc;
GRANT ALL ON SCHEMA "Librairie" TO "Librairie" WITH GRANT OPTION;

-- ddl-end --

 -- CREATE SCHEMA "Librairie";
-- ddl-end --
 -- ALTER SCHEMA "Librairie" OWNER TO joanluc;
-- ddl-end --

-- Appended SQL commands --
-- SELECT * FROM tb_contact;
-- ddl-end --

SET search_path TO pg_catalog,public,"Librairie";
-- ddl-end --

-- object: "Librairie".tb_contact | type: TABLE --
-- DROP TABLE IF EXISTS "Librairie".tb_contact;

-- Prepended SQL commands --

CREATE TABLE "Librairie".tb_contact
(
  "nom_contact" character varying NOT NULL, 
  "entreprise" character varying, 
  "Adresse_perso" character varying,
  "cp_villes" character varying,
  "telefone" character varying,
  "email" character varying, 
  "nbr_autres_struct" smallint,
  "autres_structures" character varying,
  CONSTRAINT tb_contacts_pk UNIQUE ("nom_contact")
)
WITH (
  OIDS=FALSE
)
TABLESPACE pg_default;
-- ALTER TABLE "Librairie".tb_contact
--   OWNER TO joanluc;
-- ddl-end --

 -- CREATE TABLE "Librairie".tb_contact(
 -- 	nom_contact character varying NOT NULL,
 -- 	entreprise character varying,
 -- 	adresse_perso character varying,
 -- 	cp_ville character varying,
 -- 	telefone character varying,
 -- 	email character varying DEFAULT nom@domaine,
 -- 	nbr_autres_struct smallint DEFAULT 0,
 -- 	autres_structures character varying,
 -- 	CONSTRAINT tb_contact_pk PRIMARY KEY (nom_contact)

 -- )
 -- TABLESPACE pg_default;
-- ddl-end --
COMMENT ON TABLE "Librairie".tb_contact IS 'Table des contacts';
-- ddl-end --
COMMENT ON COLUMN "Librairie".tb_contact.nbr_autres_struct IS 'Nombre d''autres structures où le contact est référencé';
-- ddl-end --
COMMENT ON COLUMN "Librairie".tb_contact.autres_structures IS 'Une chaine de caractère par structure, les noms composés reliés par _';
-- ddl-end --
ALTER TABLE "Librairie".tb_contact OWNER TO postgres;
-- ddl-end --

-- Appended SQL commands --
-- INSERT INTO "Librairie".tb_contact (nom_contact,structure,adresse_perso,cp_ville,telephone,email) VALUES ("joanluc","oc.linux","6 allée des lapins","33125 Hostens","0622465125","joanluc.laborda@free.fr");
-- ddl-end --

-- object: "Librairie".tb_librairie_presse | type: TABLE --
-- DROP TABLE IF EXISTS "Librairie".tb_librairie_presse CASCADE;
CREATE TABLE "Librairie".tb_librairie_presse(
	nom_librairie character varying NOT NULL,
	adresse_librairie character varying,
	cp_ville character varying,
	tel_lib_presse character varying(13),
	email character varying DEFAULT nom@domaine,
	representant character varying,
	groupement character varying,
	remarque text,
	type_entreprise character varying,
	envoi_systematique boolean NOT NULL DEFAULT False,
	envoi_genre character varying,
	nbr_autres_contacts smallint,
	autres_contrats character varying,
	CONSTRAINT tb_libpresse_pk PRIMARY KEY (nom_librairie)

);
-- ddl-end --
COMMENT ON COLUMN "Librairie".tb_librairie_presse.type_entreprise IS 'Librairie / Presse / Centre culturel';
-- ddl-end --
COMMENT ON COLUMN "Librairie".tb_librairie_presse.envoi_systematique IS 'envoi systématique : « all » ou par genre';
-- ddl-end --
COMMENT ON COLUMN "Librairie".tb_librairie_presse.envoi_genre IS 'Envoi par genre';
-- ddl-end --
COMMENT ON COLUMN "Librairie".tb_librairie_presse.nbr_autres_contacts IS 'Nombre d''autres contacts référencés dans l''a structure';
-- ddl-end --
COMMENT ON COLUMN "Librairie".tb_librairie_presse.autres_contrats IS 'Liste des autres contacts';
-- ddl-end --
ALTER TABLE "Librairie".tb_librairie_presse OWNER TO "Librairie";
-- ddl-end --

-- Rajout contrainte clé étrangère sur tb_contact
ALTER TABLE "Librairie".tb_contact 
  ADD CONSTRAINT tb_contacts_fk FOREIGN KEY ("nom_librairie")
      REFERENCES "Librairie".tb_librairie_presse ("nom_librairie") MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION;
      
-- object: "Librairie".tb_livre | type: TABLE --
-- DROP TABLE IF EXISTS "Librairie".tb_livre CASCADE;
CREATE TABLE "Librairie".tb_livre(
	titre_livre character varying NOT NULL,
	genre character varying NOT NULL,
	sp boolean NOT NULL,
	CONSTRAINT tb_livres_pk PRIMARY KEY (titre_livre,genre)

);
-- ddl-end --
COMMENT ON COLUMN "Librairie".tb_livre.genre IS 'Sci-Fi/Policier/Roman';
-- ddl-end --
COMMENT ON COLUMN "Librairie".tb_livre.sp IS 'Service de presse : envoi systématique';
-- ddl-end --
ALTER TABLE "Librairie".tb_livre OWNER TO "Librairie";
-- ddl-end --

-- object: "Librairie".tb_envoi_livre | type: TABLE --
-- DROP TABLE IF EXISTS "Librairie".tb_envoi_livre CASCADE;
CREATE TABLE "Librairie".tb_envoi_livre(
	tb_livre_fk character varying NOT NULL,
	tb_contact_fk character varying NOT NULL,
	date_envoi date,
	num_livre_contact_pk integer NOT NULL,
	CONSTRAINT num_livre_contact_pk PRIMARY KEY (num_livre_contact_pk)

);
-- ddl-end --
COMMENT ON COLUMN "Librairie".tb_envoi_livre.date_envoi IS 'Date d''envoi du livre si envoyé, sinon NULL';
-- ddl-end --
COMMENT ON COLUMN "Librairie".tb_envoi_livre.num_livre_contact_pk IS 'numéro d''envoi';
-- ddl-end --
COMMENT ON CONSTRAINT num_livre_contact_pk ON "Librairie".tb_envoi_livre  IS 'numéro d''envoi';
-- ddl-end --
ALTER TABLE "Librairie".tb_envoi_livre OWNER TO "Librairie";
-- ddl-end --

-- object: "Librairie".entreprise | type: VIEW --
-- DROP VIEW IF EXISTS "Librairie".entreprise CASCADE;
CREATE VIEW "Librairie".entreprise
AS 

SELECT
   ent.*,
   contact.nom_contact AS nom_contact,
   livre.titre_livre AS titre,
   livre.genre AS genre,
   livre.sp AS sp
FROM
   "Librairie".tb_contact AS contact,
   "Librairie".tb_livre AS livre,
   "Librairie".tb_livre AS livre,
   "Librairie".tb_livre AS livre;
-- ddl-end --
ALTER VIEW "Librairie".entreprise OWNER TO "Librairie";
-- ddl-end --

-- object: "Librairie".envoi | type: VIEW --
-- DROP VIEW IF EXISTS "Librairie".envoi CASCADE;
CREATE VIEW "Librairie".envoi
AS 

SELECT
   livre.titre_livre AS titre,
   entreprise.nom_librairie AS raison_sociale,
   contact.nom_contact AS nom,
   contact.adresse_perso AS adresse,
   contact.cp_ville AS ville
FROM
   "Librairie".tb_livre AS livre,
   "Librairie".tb_librairie_presse AS entreprise,
   "Librairie".tb_contact AS contact,
   "Librairie".tb_contact AS contact,
   "Librairie".tb_contact AS contact;
-- ddl-end --
ALTER VIEW "Librairie".envoi OWNER TO "Librairie";
-- ddl-end --

-- object: "Librairie".contact | type: VIEW --
-- DROP VIEW IF EXISTS "Librairie".contact CASCADE;
CREATE VIEW "Librairie".contact
AS 

SELECT
   contact.*,
   entreprise.nom_librairie AS raison_sociale,
   livre.titre_livre AS titre,
   envoi.date_envoi AS date
FROM
   "Librairie".tb_contact AS contact,
   "Librairie".tb_librairie_presse AS entreprise,
   "Librairie".tb_livre AS livre,
   "Librairie".tb_envoi_livre AS envoi;
-- ddl-end --
ALTER VIEW "Librairie".contact OWNER TO "Librairie";
-- ddl-end --

-- object: tb_contact_fk_tb_libp | type: CONSTRAINT --
-- ALTER TABLE "Librairie".tb_contact DROP CONSTRAINT IF EXISTS tb_contact_fk_tb_libp CASCADE;
ALTER TABLE "Librairie".tb_contact ADD CONSTRAINT tb_contact_fk_tb_libp FOREIGN KEY (entreprise)
REFERENCES "Librairie".tb_librairie_presse (nom_librairie) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: tb_libp_fk_contact | type: CONSTRAINT --
-- ALTER TABLE "Librairie".tb_librairie_presse DROP CONSTRAINT IF EXISTS tb_libp_fk_contact CASCADE;
ALTER TABLE "Librairie".tb_librairie_presse ADD CONSTRAINT tb_libp_fk_contact FOREIGN KEY (representant)
REFERENCES "Librairie".tb_contact (nom_contact) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: tb_livre_genresp_fk | type: CONSTRAINT --
-- ALTER TABLE "Librairie".tb_librairie_presse DROP CONSTRAINT IF EXISTS tb_livre_genresp_fk CASCADE;
ALTER TABLE "Librairie".tb_librairie_presse ADD CONSTRAINT tb_livre_genresp_fk FOREIGN KEY (envoi_systematique,envoi_genre)
REFERENCES "Librairie".tb_livre (genre,sp) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: tb_livre_fk | type: CONSTRAINT --
-- ALTER TABLE "Librairie".tb_envoi_livre DROP CONSTRAINT IF EXISTS tb_livre_fk CASCADE;
ALTER TABLE "Librairie".tb_envoi_livre ADD CONSTRAINT tb_livre_fk FOREIGN KEY (tb_livre_fk)
REFERENCES "Librairie".tb_livre (titre_livre) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: tb_contact_fk | type: CONSTRAINT --
-- ALTER TABLE "Librairie".tb_envoi_livre DROP CONSTRAINT IF EXISTS tb_contact_fk CASCADE;
ALTER TABLE "Librairie".tb_envoi_livre ADD CONSTRAINT tb_contact_fk FOREIGN KEY (tb_livre_fk)
REFERENCES "Librairie".tb_contact (nom_contact) MATCH FULL
ON DELETE NO ACTION ON UPDATE NO ACTION;
-- ddl-end --

-- object: grant_1a01b96a74 | type: PERMISSION --
GRANT USAGE
   ON SCHEMA "Librairie"
   TO "Librairie" WITH GRANT OPTION;
-- ddl-end --

-- object: grant_c7082dee9d | type: PERMISSION --
GRANT CREATE,USAGE
   ON SCHEMA "Librairie"
   TO morgane;
-- ddl-end --

-- object: grant_ac639af3da | type: PERMISSION --
GRANT SELECT,INSERT,UPDATE,REFERENCES
  (entreprise) ON TABLE "Librairie".tb_contact
   TO "Librairie";
-- ddl-end --

-- object: grant_29b5969ef7 | type: PERMISSION --
GRANT SELECT,INSERT,UPDATE,REFERENCES
  (entreprise) ON TABLE "Librairie".tb_contact
   TO morgane WITH GRANT OPTION;
-- ddl-end --


