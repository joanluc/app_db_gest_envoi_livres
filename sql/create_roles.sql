-- Cree roles postgres

-- Role: Librairie

-- DROP ROLE "Librairie";

CREATE ROLE "Librairie"
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;

-- Role: morgane

-- DROP ROLE morgane;

CREATE ROLE morgane LOGIN
  ENCRYPTED PASSWORD 'md5580ab8cf8b37dcc31dcaacf50829267e'
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE REPLICATION VALID UNTIL '2018-02-08 00:00:00';
GRANT "Librairie" TO morgane;
GRANT pg_signal_backend TO morgane;
COMMENT ON ROLE morgane IS 'MiddleHeart';


-- Role: app_db_gest_envoi_livres

-- DROP ROLE app_db_gest_envoi_livres;

CREATE ROLE app_db_gest_envoi_livres LOGIN
  ENCRYPTED PASSWORD 'md5533b6f2e620212b22f3fd1c6fe2ccc25'
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;
GRANT "Librairie" TO app_db_gest_envoi_livres;
COMMENT ON ROLE app_db_gest_envoi_livres IS 'app_db_gest_envoi_livres.py

classAppBDgestEnvoiLivres:';
