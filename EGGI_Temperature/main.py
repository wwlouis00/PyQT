from PyQt5.QtWidgets import QApplication,QMainWindow
from Sulink_Temperature_20211118 import *
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindows = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindows)
    mainWindows.show()
    sys.exit(app.exec_())
