from os import system 
system('exec /usr/bin/psql <<EOF
\x
CREATE TABLE "Librairie".tb_contacts
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
    IS 'Contacts
========
Nom_contact	: clé primaire
structure : clé étrangère
Adresse perso	
Tel
E-mail	';

COMMENT ON COLUMN "Librairie".tb_contacts." structure"
    IS 'clé étrangère sur la table tb_librairie_presse';

COMMENT ON COLUMN "Librairie".tb_contacts.telef
    IS 'Code Postal + ville + pays';

COMMENT ON CONSTRAINT tb_contact_structure_fk ON "Librairie".tb_contacts
    IS 'Clé étrangère vers la table tb_librairie_presse';

-- Index: fki_tb_contact_structure_fk

-- DROP INDEX "Librairie".fki_tb_contact_structure_fk;

CREATE INDEX fki_tb_contact_structure_fk
    ON "Librairie".tb_contacts USING btree
    ( structure)
    TABLESPACE pg_default;
EOF   
') 