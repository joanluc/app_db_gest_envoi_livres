#!/bin/bash
 
source ./init_test.sh
export PGPASSWORD=$CLASS_APP_BD_GEST_ENVOI_LIVRES

logfile=$(dirname $0)/gen_activity.log
 
while $(true); do
    if ! psql -c "select 1" $db >/dev/null 2>&1 ; then
        echo "$(date) : L'instance est arretee " >> $logfile
        echo "====================================" >> $logfile
        sleep 5
        continue
    fi
    echo "$(date) : Insertion d'une ligne dans la table de suivi :" >> $logfile
    psql -c "insert into suivi (datetime, timeline) values (
        now(),
        trim(leading '0' from substr(
            pg_xlogfile_name(
                pg_current_xlog_location()
            ), 1, 8))) RETURNING *;" $db >> $logfile
    echo "====================================" >> $logfile
    sleep 5
done
