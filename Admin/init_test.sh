#!/usr/bin/bash
[ ! $1 ] && { echo "Usatge $0 util_pg mdsc";exit; }
# [ ! $2 ] && { echo "Usatge $0 util_pg mdsc";exit; }
[ ! $2 ] && read -p "MDSC ? " MDSC 
# [ $2 ] && MDSC = $2
set MDSC = $2
export db=Librairie
export PGHOST=127.0.0.1
export PGUSER=$1
export APPLICATION=$MDSC
