import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import MyWin


def main():
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()

