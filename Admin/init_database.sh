#!/usr/bin/bash
# app_db_gest_envoi_livres/init_database.sh

export PSQL="/usr/bin/psql -d Librairie -U joanluc " # alias PSQL
(cd $(dirname $0)/sql; pwd;
$PSQL -c create_schema_librairie.sql;
$PSQL -c create_table-tb_contact.sql;
$PSQL -c create_table-tb_envoi_livre.sql;
$PSQL -c create_table-tb_librairie_presse.sql;
$PSQL -c create_table-tb_livre.sql;
$PSQL -c create_view-contact.sql;
$PSQL -c create_view-entreprise.sql;
$PSQL -c create_view-envoi.sql;
)
