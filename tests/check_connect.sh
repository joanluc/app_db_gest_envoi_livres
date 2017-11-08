#!/usr/bin/bash
 
source ./init_test.sh
export PGPASSWORD=$CLASS_APP_BD_GEST_ENVOI_LIVRES

if ! psql -c "select 1" $db >/dev/null 2>&1 ; then
    echo "$(date) : L'instance est arretee "
    echo "===================================="
else
    echo "$(date) : Connexion sur la base $db : ok"
    echo "===================================="
fi
