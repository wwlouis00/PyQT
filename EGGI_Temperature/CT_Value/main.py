import sys
#from Sulink_Temperature_ver1 import *   #執行
from CT_Display1221 import *
# from Sulink_Temperature_20211217 import *   #執行

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindows = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindows)
    mainWindows.show()
    sys.exit(app.exec_())