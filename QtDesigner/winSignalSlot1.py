from typing import Sequence
from PyQt5.QtWidgets import QPushButton ,QApplication,QWidget
from PyQt5.QtWidgets import QMessageBox
import sys
from PyQt5.QtCore import QObject , pyqtSignal

class QTypeSignal(QObject):
    #定義一個訊號
    sendmsg = pyqtSignal(object)
    def __init__(self):
        super(QTypeSignal,self).__init__()

    def run(self):
        self.sendmsg.emit("hello pyqt5")

class QTypeSlot(QObject):
    def get(self,msg):
        print("QSlot get msg =>" + msg)

if __name__ == '__main__':
    send = QTypeSignal()
    slot = QTypeSlot()
    #1
    print("---把訊號槽連結到槽函數上---")
    send.sendmsg.connect(slot.get)
    send.run()
    #2
    print("---斷開訊號槽連結到槽函數上---")
    send.sendmsg.disconnect(slot.get)
    send.run()

        