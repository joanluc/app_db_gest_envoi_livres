--- Creation schema librairie

-- Schema: Librairie

-- DROP SCHEMA "Librairie";

CREATE SCHEMA "Librairie"
  AUTHORIZATION joanluc;

GRANT ALL ON SCHEMA "Librairie" TO joanluc;
GRANT ALL ON SCHEMA "Librairie" TO "Librairie" WITH GRANT OPTION;

--- Creation tables

-- Table: "Librairie".tb_contact

-- DROP TABLE "Librairie".tb_contact;

CREATE TABLE "Librairie".tb_contact
(
  "Nom_contact" "char"[] NOT NULL, -- CONSTRAINT tb_contacts_pkey PRIMARY KEY ("Nom_contact"),
  structure "char"[],
  "Adresse_perso" "char"[],
  cp_villes "char"[],
  telef "char"[],
  email "char"[], -- contient au moins '@' à une position >= 2 et au moins '.'
  "Nom_librairie" "char"[],
  CONSTRAINT tb_contacts_fk FOREIGN KEY ("Nom_librairie")
      REFERENCES "Librairie".tb_librairie_presse ("Nom_librairie") MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION, -- Clé étrangère de la table 'tb_contacts' sur la table 'tb_librairie_presse'
  CONSTRAINT tb_contacts_pkey UNIQUE ("Nom_contact")
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "Librairie".tb_contact
  OWNER TO joanluc;
COMMENT ON TABLE "Librairie".tb_contact
  IS 'CREATE TABLE "Librairie".tb_contacts
(
    "Nom_contact" "char"[] NOT NULL,
    "structure" "char"[],
    "Adresse_perso" "char"[],
    cp_villes "char"[],
    telef "char"[],
    email "char"[],
    CONSTRAINT tb_contacts_pkey PRIMARY KEY ("Nom_contact"),
    CONSTRAINT tb_contact_structure_fk FOREIGN KEY (" structure")
        REFERENCES "Librairie".tb_librairie_presse ("Nom_librairie") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE "Librairie".tb_contacts
    ADD "autresStructures" "char"[]

ALTER TABLE "Librairie".tb_contacts
    OWNER to postgres;

GRANT ALL ON TABLE "Librairie".tb_contacts TO "Librairie" WITH GRANT OPTION;

GRANT ALL ON TABLE "Librairie".tb_contacts TO "Morgane" WITH GRANT OPTION;

GRANT ALL ON TABLE "Librairie".tb_contacts TO postgres;

COMMENT ON TABLE "Librairie".tb_contacts
    IS ''Contacts
========
Nom_contact	: clé primaire
structure : clé étrangère
Adresse perso	
Tel
E-mail	'';

COMMENT ON COLUMN "Librairie".tb_contacts." structure"
    IS ''clé étrangère sur la table tb_librairie_presse'';

COMMENT ON COLUMN "Librairie".tb_contacts.telef
    IS ''Code Postal + ville + pays'';

COMMENT ON CONSTRAINT tb_contact_structure_fk ON "Librairie".tb_contacts
    IS ''Clé étrangère vers la table tb_librairie_presse'';

-- Index: fki_tb_contact_structure_fk

-- DROP INDEX "Librairie".fki_tb_contact_structure_fk;

CREATE INDEX fki_tb_contact_structure_fk
    ON "Librairie".tb_contacts USING btree
    ( structure)
    TABLESPACE pg_default;';
COMMENT ON COLUMN "Librairie".tb_contact."Nom_contact" IS 'CONSTRAINT tb_contacts_pkey PRIMARY KEY ("Nom_contact"),';
COMMENT ON COLUMN "Librairie".tb_contact.email IS 'contient au moins ''@'' à une position >= 2 et au moins ''.''';

COMMENT ON CONSTRAINT tb_contacts_fk ON "Librairie".tb_contact IS 'Clé étrangère de la table ''tb_contacts'' sur la table ''tb_librairie_presse''';


-- Index: "Librairie".fki_tb_contacts_fk

-- DROP INDEX "Librairie".fki_tb_contacts_fk;

CREATE INDEX fki_tb_contacts_fk
  ON "Librairie".tb_contact
  USING btree
  ("Nom_librairie");


-- Table: "Librairie".tb_envoi_livres

-- DROP TABLE "Librairie".tb_envoi_livres;

CREATE TABLE "Librairie".tb_envoi_livres
(
  tb_livres_fk "char"[] NOT NULL,
  tb_contact_fk "char"[] NOT NULL,
  date_envoi date,
  num_liv_contact_pk integer NOT NULL,
  CONSTRAINT num_liv_contact_pk PRIMARY KEY (num_liv_contact_pk),
  CONSTRAINT tb_envoi_livres_tb_contact_fkey FOREIGN KEY (tb_contact_fk)
      REFERENCES "Librairie".tb_contact ("Nom_contact") MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "Librairie".tb_envoi_livres
  OWNER TO joanluc;
COMMENT ON TABLE "Librairie".tb_envoi_livres
  IS 'CREATE TABLE "Librairie".tb_envoi_livres
(
    tb_livres_fk "char"[] NOT NULL,
    "tb_contact-fk" "char"[] NOT NULL,
    date_envoi date,
    num_liv_contact_pk integer NOT NULL,
    CONSTRAINT tb_envoi_livres_pkey PRIMARY KEY (num_liv_contact_pk),
    CONSTRAINT tb_envoi_livres_tb_contact_fkey FOREIGN KEY ("tb_contact-fk")
        REFERENCES "Librairie".tb_contacts ("Nom_contact") MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE "Librairie".tb_envoi_livres
    OWNER to postgres;

GRANT ALL ON TABLE "Librairie".tb_envoi_livres TO "Librairie" WITH GRANT OPTION;

GRANT ALL ON TABLE "Librairie".tb_envoi_livres TO "Morgane" WITH GRANT OPTION;

GRANT ALL ON TABLE "Librairie".tb_envoi_livres TO postgres;

COMMENT ON COLUMN "Librairie".tb_envoi_livres.tb_livres_fk
    IS ''Clé étrangère pour table tb_livers'';

COMMENT ON COLUMN "Librairie".tb_envoi_livres."tb_contact-fk"
    IS ''Clé étrangère pour la table tb_contacts'';

COMMENT ON COLUMN "Librairie".tb_envoi_livres.num_liv_contact_pk
    IS ''Clé primaire pour la table tb_envoi_livres'';

-- Index: fki_tb_livres_fk

-- DROP INDEX "Librairie".fki_tb_livres_fk;

CREATE INDEX fki_tb_livres_fk
    ON "Librairie".tb_envoi_livres USING btree
    (tb_livres_fk)
    TABLESPACE pg_default;

-- Index: ix_date

-- DROP INDEX "Librairie".ix_date;

CREATE INDEX ix_date
    ON "Librairie".tb_envoi_livres USING btree
    (date_envoi)
    TABLESPACE pg_default;

-- Index: tb_contacts_fk

-- DROP INDEX "Librairie".tb_contacts_fk;

CREATE INDEX tb_contacts_fk
    ON "Librairie".tb_envoi_livres USING btree
    (tb_contact-fk)
    TABLESPACE pg_default;';

-- Table: "Librairie".tb_librairie_presse

-- DROP TABLE "Librairie".tb_librairie_presse;

CREATE TABLE "Librairie".tb_librairie_presse
(
  "Nom_librairie" "char"[] NOT NULL,
  "Adresse_lib" "char"[],
  cp_ville "char"[],
  "Tel_lib" "char"[],
  email "char"[],
  "Repr" "char"[],
  "Groupement" "char"[],
  "Remarque" text,
  typ_entreprise integer,
  envoi_sys integer
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "Librairie".tb_librairie_presse
  OWNER TO joanluc;

-- Index: "Librairie".tb_libpresse_pk

-- DROP INDEX "Librairie".tb_libpresse_pk;

CREATE UNIQUE INDEX tb_libpresse_pk
  ON "Librairie".tb_librairie_presse
  USING btree
  ("Nom_librairie");
ALTER TABLE "Librairie".tb_librairie_presse CLUSTER ON tb_libpresse_pk;
COMMENT ON INDEX "Librairie".tb_libpresse_pk
  IS 'Clé primaire de la table "tb_librairie_presse"';


-- Table: "Librairie".tb_livre

-- DROP TABLE "Librairie".tb_livre;

CREATE TABLE "Librairie".tb_livre
(
  titre_livre "char"[] NOT NULL,
  genre "char"[],
  "SP" boolean NOT NULL DEFAULT false -- Service de presse
)
WITH (
  OIDS=FALSE
);
ALTER TABLE "Librairie".tb_livre
  OWNER TO joanluc;
COMMENT ON COLUMN "Librairie".tb_livre."SP" IS 'Service de presse';

