import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class Activetime(QWidget):
    #初始化
    def __init__(self):
        super(Activetime, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("動態顯示時間")
        self.resize(200,100)

        self.lable=QLabel("顯示當前時間")
        self.button1=QPushButton("開始時間")
        self.button2=QPushButton("結束")
        #設定網格佈局
        layout=QGridLayout()

        self.timer=QTimer()
        self.timer.timeout.connect(self.showtime)#這個通過呼叫槽函式來重新整理時間
        layout.addWidget(self.lable,0,0,1,2)
        layout.addWidget(self.button1,1,0)
        layout.addWidget(self.button2,1,1)

        self.button1.clicked.connect(self.starttimer)
        self.button2.clicked.connect(self.endtimer)
        self.setLayout(layout)


    def showtime(self):
        time=QDateTime.currentDateTime()#獲取當前時間
        timedisplay=time.toString("yyyy-MM-dd hh:mm:ss dddd")#格式化一下時間
        print(timedisplay)
        self.lable.setText(timedisplay)

    def starttimer(self):
        self.timer.start(1000)#每隔一秒重新整理一次，這裡設定為1000ms
        self.button1.setEnabled(False)
        self.button2.setEnabled(True)

    def endtimer(self):
        self.timer.stop()
        self.button1.setEnabled(True)
        self.button2.setEnabled(False)

if __name__=="__main__":
    app=QApplication(sys.argv)
    main=Activetime()
    main.show()
    sys.exit(app.exec_())