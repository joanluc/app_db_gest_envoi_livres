# Installation des modules sous Linux et MacOS
PIP=$(which pip3)
$PIP install  --user -U pip
$PIP install  --user  psycopg2
# Installation de PyQt4
#  (
#     function installModule () {(   
#         cd $1
#         python configure.py
#         make
#         sudo make install
#     )}
# 
#     cd /tmp
#                                     ### Pré-requis pour l'installation des modules
#     sudo  dnf install -y bison flex gcc-c++
# 
#                                                             ### SIP Linux / MacOS
#     wget https://www.riverbankcomputing.com/static/Downloads/sip/sip-4.19.4.dev1708131720.tar.gz
#     tar xzf sip-4.19.4.dev1708131720.tar.gz
#     installModule sip-4.19.4.dev1708131720
# 
#                                                             ### PyQt4 pour Linux
#     [ "$(uname -o)" == "GNU/Linux" ] && {
#         wget http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12.1/PyQt4_gpl_x11-4.12.1.tar.gz
#         tar xzf PyQt4_gpl_x11-4.12.1.tar.gz
#         installModule PyQt4_gpl_x11-4.12.1
#     }
#                                                             ### PyQt4 pour MacOS
#     [ "$(uname -o)" == "MacOS" ] && {
#         wget http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12.1/PyQt4_gpl_mac-4.12.1.tar.gz
#         tar xzf PyQt4_gpl_mac-4.12.1.tar.gz
#         installModule PyQt4_gpl_mac-4.12.1
#     }
#  )
# $PIP install   --user SIP
# $PIP install   --user PyQt
# $PIP install   --user PyQt4
$PIP install   --user PyQt5
