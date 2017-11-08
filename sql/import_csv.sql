CREATE EXTENSION file_fdw;
CREATE SERVER srv_savoie FOREIGN DATA WRAPPER postgres_fdw OPTIONS (host '194.214.86.66', dbname 'savoie');
CREATE USER MAPPING FOR postgres SERVER srv_savoie OPTIONS(user ’postgres’, password ’bdd2014-15’);
IMPORT FOREIGN SCHEMA poisson LIMIT TO (espece) FROM SERVER srv_savoie INTO public;
SELECT * FROM espece;
