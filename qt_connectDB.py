import sys

from PyQt5 import QtCore, QtGui, QtWidgets # PyQt4.QtGui est divisé en Qt5 avec QtGui, QtPrintSupport et QtWidgets 
    
from qt5_connexion import Ui_Dialog
    
class QtConnectDB () :
    def __init__(self,parent=None):
        # super (QtConnectDB,self).__init__(parent)
        super (QtConnectDB,self).__init__()
        self.createWidgets()

    def createWidgets(self):
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # PyQt5.QtWidgets.QApplication
    myApp = QtConnectDB()
    myApp.show()
    sys.exit(app.exec_())
