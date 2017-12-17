#!/bin/bash
# Created on Tue Sep  5 23:04:54 2017
# @author: joanluc
# installPostgreSQL.sh
__init() {
    [ -f /etc/redhat-release ] && {
        # Centos | Fedora | Redhat
        case $(cat /etc/redhat-release) in
            "Fedora release 22|23|24|25|26" ) 
                export INSTALL="sudo dnf install -y";
                export PG_SETUP = "sudo postgresql-setup --initdb --unit postgresql";
                return;;
            * ) export INSTALL="sudo yum install -y";;         
        esac
    }
    [ -f /etc/redhat-release ] || {
        # Une distribution Linux différente de la branche RH
        case $(cat /etc/issue) in
            "Debian|Ubuntu*" ) export INSTALL="sudo apt-get install -y";;
            * ) echo "Installation manuelle";exit;;
        esac
    }
    export PG_SETUP = "sudo postgresql-setup --initdb";
    return;
}

sysEnaPg () {
    systemctl  enable postgresql
}

installPg () {
    $INSTALL postgresql-server postgresql-contrib pgadmin3
    sudo systemctl  enable postgresql # sysEnaPg
    $PG_SETUP
}

securite () {
    # firewall
    # make it last after reboot
    firewall-cmd --permanent --add-port=5432/tcp
    # change runtime configuration
    firewall-cmd --add-port=5432/tcp
    
    # iptables
    iptables -A INPUT -p tcp --dport 5432 -m state --state NEW,ESTABLISHED -j ACCEPT

    # Selinux
    read -P "chg Pg location ? (/my/new/location(/.*)?)" MYNEWLOC
    semanage fcontext -a -t postgresql_db_t "$MYNEWLOC"
    semanage port -a -t postgresql_port_t -p tcp 5433
    setsebool -P httpd_can_network_connect_db on
    
    # Pg Passwd 
    echo "Shell interactif Postgres pour modifier le mot de passe"
    echo "# psql"
    echo "# \password postgres"
    sudo su - postgres

}

config () {
    sudo less  /var/lib/pgsql/data/postgresql.conf
    read -p "Editer postgresql.conf ?" EDT_PG_CFG
    [ "$EDT_PG_CFG" = "o|O" ] && $EDITOR /var/lib/pgsql/data/postgresql.conf
    echo "pg_hba.conf : Modifier la méthode d'authentification de postgres pour md5"
    read -p "Editer postgresql.conf ?" EDT_PG_CFG
    $EDITOR /var/lib/pgsql/data/pg_hba.conf 
}

# https://unix.stackexchange.com/questions/6345/how-can-i-get-distribution-name-and-version-number-in-a-simple-shell-script
__init
read -p "Installation initiale" INSTINI
[ "$INSTINI" = "o" ] && {
    installPg
    securite
    config
}
read -p "Redémarrer le service ?" RESTART
[ "$RESTART" = "o" ] && sudo service postgresql restart
exit
