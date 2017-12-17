#!/usr/bin/bash
# TP DUMP / RESTORE
# dump de la base tp_sql
# detruire la base tp_sql
# restorer la base tp_sql

source $(dirname $0)/init_test.sh $1 $2
PGPASSWD=$APPLICATION
read -p "PGDATABASE ? " PGDATABASE

function list_database() 
{
    psql -c "SELECT datname FROM pg_database;"
}

function backup_txt() 
{
    # pg_dump [OPTION]... [NOMBASE]less
    # /usr/bin/pg_dump -Fp -d tp_sql -U postgres > /pgbackups/dumps/tp_sql.dump 
    /usr/bin/pg_dump -Fp -d $PGDATABASE -U $PGUSER -f /pgbackups/dumps/$PGDATABASE.dump 
    psql -U $PGUSER -c "drop database $PGDATABASE;"
}

function backup_bin() 
{
    /usr/bin/pg_dump -Fc -d $PGDATABASE -f  /pgbackups/dumps/$PGDATABASE.dump
    psql -U $PGUSER -c "drop database $PGDATABASE;"
}

function dumpall_base ()
{
    [ $1 == "global" ] && {
        # Permet de sauvegarder les utilisateurs et les rôles, à
        /usr/bin/pg_dumpall -g -f  /pgbackups/dumps/global.dump
        }
    [ $1 == "global" ] || {
        # Permet de sauvegarder les utilisateurs et les rôles, à
        backup_txt $PGDATABASE  /pgbackups/dumps/$PGDATABASE.dump
    }
}

function restore () 
{
    psql -d $PGUSER -U $PGUSER -c "create database $PGDATABASE;"
    psql -d tp_sql  -U $PGUSER -f /pgbackups/dumps/$PGDATABASE.dump 
}

function misajorn() 
{
    pg_lsclusters 
    pg_ctlcluster 9.6 main stop 
    dumpall_base global
    for base in $(psql -d $PGDATABASE -U $PGUSER -c "SELECT datname FROM pg_database;");do 
        echo $base;
        echo "dumpall_base $base";
    done
    # DEHAR Misajorn fiquiers de config /etc/postgresql/*/postgresql.conf  /var/lib/postgresql/*/data/
}

# echo $(basename $0)
[ "$(basename $0)" = "tp_sql.sh" ] && { 
    read -p "Menu foncions : $(grep function $0)\ " FONC
    $FONC
}
