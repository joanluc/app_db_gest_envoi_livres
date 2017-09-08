CREATE TABLE "Librairie".tb_envoi_livres
(
    tb_livres_fk "char"[] NOT NULL,
    "tb_contact_fk" "char"[] NOT NULL,
    date_envoi date,
    num_liv_contact_pk integer NOT NULL,
    CONSTRAINT tb_envoi_livres_pkey PRIMARY KEY (num_liv_contact_pk),
    CONSTRAINT tb_envoi_livres_tb_contact_fkey FOREIGN KEY ("tb_contact_fk")
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
    IS 'Clé étrangère pour table tb_livers';

COMMENT ON COLUMN "Librairie".tb_envoi_livres."tb_contact-fk"
    IS 'Clé étrangère pour la table tb_contacts';

COMMENT ON COLUMN "Librairie".tb_envoi_livres.num_liv_contact_pk
    IS 'Clé primaire pour la table tb_envoi_livres';

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
    TABLESPACE pg_default;