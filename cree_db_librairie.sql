CREATE DATABASE "Librairie"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'French_France.1252'
    LC_CTYPE = 'French_France.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

GRANT ALL ON "Librairie" TO "Librairie" WITH GRANT OPTION;

GRANT ALL ON "Librairie" TO "Morgane" WITH GRANT OPTION;
