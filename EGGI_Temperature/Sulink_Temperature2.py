#--------------說明欄----------------
#     PF是PASS/FAIL意思
#     T_On 開始運作  溫度下降
#     T_Off 關閉運作 溫度上升
#___________________________________
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QFileDialog
from PyQt5.QtCore import *


from PyQt5.uic import loadUi


class Ui_MainWindow(QtWidgets.QWidget):

    #browsefile開啟檔案功能
    def browsefile(self):
        fname = QFileDialog.getOpenFileName(self,'open file','C:\Program Files (x86)','txt files (*.txt)')
        # " C:\python\Learn_Python\Temperature" 是自己的電腦位置路徑
        self.output_txtfile.setText(fname[0])
    #顯示現在時間
    def showtime(self):
        time = QDateTime.currentDateTime()
        timedisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")#格式化一下時間
        self.input_datetime.setText(timedisplay)

    def slot_init(self):
        self.btn_opentxt.clicked.connect(self.browsefile)
        self.input_datetime.setText(self.showtime())
    #Ui畫面設置
    def setupUi(self,MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Input_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Input_box.setGeometry(QtCore.QRect(10, 90, 701, 115))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Input_box.setFont(font)
        self.Input_box.setObjectName("Input_box")
        self.layoutWidget = QtWidgets.QWidget(self.Input_box)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 33, 531, 67))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_datetime = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_datetime.setFont(font)
        self.label_datetime.setAlignment(QtCore.Qt.AlignCenter)
        self.label_datetime.setObjectName("label_datetime")
        self.gridLayout_2.addWidget(self.label_datetime, 1, 0, 1, 1)
        self.output_txtfile = QtWidgets.QLineEdit(self.layoutWidget)
        self.output_txtfile.setObjectName("output_txtfile")
        self.gridLayout_2.addWidget(self.output_txtfile, 0, 3, 1, 1)
        self.input_datetime = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_datetime.setObjectName("input_datetime")
        self.gridLayout_2.addWidget(self.input_datetime, 1, 1, 1, 1)
        self.label_name = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.gridLayout_2.addWidget(self.label_name, 0, 0, 1, 1)
        self.label_txt = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_txt.setFont(font)
        self.label_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.label_txt.setObjectName("label_txt")
        self.gridLayout_2.addWidget(self.label_txt, 0, 2, 1, 1)
        self.input_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_name.setObjectName("input_name")
        self.gridLayout_2.addWidget(self.input_name, 0, 1, 1, 1)
        #開啟檔案
        self.btn_opentxt = QtWidgets.QPushButton(self.Input_box)
        # self.btn_opentxt.clicked.connect(self.browsefile)
        self.btn_opentxt.setGeometry(QtCore.QRect(550, 36, 121, 55))
        self.btn_opentxt.clicked.connect(self.browsefile)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_opentxt.setFont(font)
        self.btn_opentxt.setObjectName("btn_opentxt")
        self.EGGI_Title = QtWidgets.QLabel(self.centralwidget)
        self.EGGI_Title.setGeometry(QtCore.QRect(10, 6, 1101, 76))
        font = QtGui.QFont()
        font.setPointSize(38)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.EGGI_Title.setFont(font)
        self.EGGI_Title.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.EGGI_Title.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.EGGI_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.EGGI_Title.setObjectName("EGGI_Title")
        self.Chart_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Chart_box.setGeometry(QtCore.QRect(10, 210, 701, 355))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Chart_box.setFont(font)
        self.Chart_box.setObjectName("Chart_box")
        self.btn_clean = QtWidgets.QPushButton(self.Chart_box)
        self.btn_clean.setGeometry(QtCore.QRect(560, 288, 121, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clean.setFont(font)
        #set object name
        self.btn_clean.setObjectName("btn_clean")
        self.splitter_2 = QtWidgets.QSplitter(self.Chart_box)
        self.splitter_2.setGeometry(QtCore.QRect(16, 156, 0, 0))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.widget_6 = QtWidgets.QWidget(self.splitter_2)
        self.widget_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_6.setObjectName("widget_6")
        self.widget_7 = QtWidgets.QWidget(self.splitter_2)
        self.widget_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_7.setObjectName("widget_7")
        self.widget_8 = QtWidgets.QWidget(self.splitter_2)
        self.widget_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_8.setObjectName("widget_8")
        self.widget_5 = QtWidgets.QWidget(self.splitter_2)
        self.widget_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_5.setObjectName("widget_5")
        self.layoutWidget_2 = QtWidgets.QWidget(self.Chart_box)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 30, 661, 211))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ch3_chart = QtWidgets.QWidget(self.layoutWidget_2)
        self.ch3_chart.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.ch3_chart.setObjectName("ch3_chart")
        self.gridLayout_3.addWidget(self.ch3_chart, 0, 2, 1, 1)
        self.ch7_chart = QtWidgets.QWidget(self.layoutWidget_2)
        self.ch7_chart.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.ch7_chart.setObjectName("ch7_chart")
        self.gridLayout_3.addWidget(self.ch7_chart, 2, 2, 1, 1)
        self.ch6_chart = QtWidgets.QWidget(self.layoutWidget_2)
        self.ch6_chart.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.ch6_chart.setObjectName("ch6_chart")
        self.gridLayout_3.addWidget(self.ch6_chart, 2, 1, 1, 1)
        self.ch1_chart = QtWidgets.QWidget(self.layoutWidget_2)
        self.ch1_chart.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.ch1_chart.setObjectName("ch1_chart")
        self.gridLayout_3.addWidget(self.ch1_chart, 0, 0, 1, 1)
        self.ch8_chart = QtWidgets.QWidget(self.layoutWidget_2)
        self.ch8_chart.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.ch8_chart.setObjectName("ch8_chart")
        self.gridLayout_3.addWidget(self.ch8_chart, 2, 3, 1, 1)
        self.ch4_chart = QtWidgets.QWidget(self.layoutWidget_2)
        self.ch4_chart.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.ch4_chart.setObjectName("ch4_chart")
        self.gridLayout_3.addWidget(self.ch4_chart, 0, 3, 1, 1)
        self.ch5_chart = QtWidgets.QWidget(self.layoutWidget_2)
        self.ch5_chart.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.ch5_chart.setObjectName("ch5_chart")
        self.gridLayout_3.addWidget(self.ch5_chart, 2, 0, 1, 1)
        self.ch2_chart = QtWidgets.QWidget(self.layoutWidget_2)
        self.ch2_chart.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.ch2_chart.setObjectName("ch2_chart")
        self.gridLayout_3.addWidget(self.ch2_chart, 0, 1, 1, 1)
        self.btn_save = QtWidgets.QPushButton(self.Chart_box)
        self.btn_save.setGeometry(QtCore.QRect(430, 288, 121, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save.setFont(font)
        self.btn_save.setObjectName("btn_save")
        self.Result_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Result_box.setGeometry(QtCore.QRect(720, 90, 391, 475))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Result_box.setFont(font)
        self.Result_box.setObjectName("Result_box")
        self.layoutWidget_3 = QtWidgets.QWidget(self.Result_box)
        self.layoutWidget_3.setGeometry(QtCore.QRect(20, 30, 352, 295))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.ch4_T_On = QtWidgets.QLineEdit(self.layoutWidget_3)
        
        self.gridLayout_7.addWidget(self.ch4_T_On, 4, 1, 1, 1)
        self.label_ch5 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_ch5.setAlignment(QtCore.Qt.AlignCenter)
        
        self.gridLayout_7.addWidget(self.label_ch5, 5, 0, 1, 1)
        self.ch7_T_On = QtWidgets.QLineEdit(self.layoutWidget_3)
        
        self.gridLayout_7.addWidget(self.ch7_T_On, 8, 1, 1, 1)
        self.label_ch6 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_ch6.setAlignment(QtCore.Qt.AlignCenter)
        
        self.gridLayout_7.addWidget(self.label_ch6, 6, 0, 1, 1)
        self.ch8_PF = QtWidgets.QLabel(self.layoutWidget_3)
        self.ch8_PF.setAlignment(QtCore.Qt.AlignCenter)
        
        self.gridLayout_7.addWidget(self.ch8_PF, 10, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        
        self.gridLayout_7.addWidget(self.label_10, 0, 0, 1, 1)
        self.ch8_T_On = QtWidgets.QLineEdit(self.layoutWidget_3)
        
        self.gridLayout_7.addWidget(self.ch8_T_On, 10, 1, 1, 1)
        self.ch7_T_Off = QtWidgets.QLineEdit(self.layoutWidget_3)
        
        self.gridLayout_7.addWidget(self.ch7_T_Off, 8, 2, 1, 1)
        self.ch1_T_On = QtWidgets.QLineEdit(self.layoutWidget_3)
        
        self.gridLayout_7.addWidget(self.ch1_T_On, 1, 1, 1, 1)
        self.label_ch1 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_ch1.setAlignment(QtCore.Qt.AlignCenter)
        
        self.gridLayout_7.addWidget(self.label_ch1, 1, 0, 1, 1)
        self.label_ch7 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_ch7.setAlignment(QtCore.Qt.AlignCenter)
        
        self.gridLayout_7.addWidget(self.label_ch7, 8, 0, 1, 1)
        self.ch5_T_On = QtWidgets.QLineEdit(self.layoutWidget_3)
        
        self.gridLayout_7.addWidget(self.ch5_T_On, 5, 1, 1, 1)
        self.ch8_T_Off = QtWidgets.QLineEdit(self.layoutWidget_3)
        
        self.gridLayout_7.addWidget(self.ch8_T_Off, 10, 2, 1, 1)
        self.label_ch4 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_ch4.setAlignment(QtCore.Qt.AlignCenter)
        
        self.gridLayout_7.addWidget(self.label_ch4, 4, 0, 1, 1)
        self.label_T_Off = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        
        self.gridLayout_7.addWidget(self.label_T_Off, 0, 2, 1, 1)
        self.ch3_T_Off = QtWidgets.QLineEdit(self.layoutWidget_3)
        
        self.gridLayout_7.addWidget(self.ch3_T_Off, 3, 2, 1, 1)
        self.ch6_T_Off = QtWidgets.QLineEdit(self.layoutWidget_3)
        
        self.gridLayout_7.addWidget(self.ch6_T_Off, 6, 2, 1, 1)
        self.ch4_T_Off = QtWidgets.QLineEdit(self.layoutWidget_3)
        
        self.gridLayout_7.addWidget(self.ch4_T_Off, 4, 2, 1, 1)
        self.ch3_T_On = QtWidgets.QLineEdit(self.layoutWidget_3)
        
        self.gridLayout_7.addWidget(self.ch3_T_On, 3, 1, 1, 1)
        self.ch5_T_Off = QtWidgets.QLineEdit(self.layoutWidget_3)
        
        self.gridLayout_7.addWidget(self.ch5_T_Off, 5, 2, 1, 1)
        self.label_ch2 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_ch2.setAlignment(QtCore.Qt.AlignCenter)
        
        self.gridLayout_7.addWidget(self.label_ch2, 2, 0, 1, 1)
        self.label_T_On = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_T_On.setAlignment(QtCore.Qt.AlignCenter)
        
        self.gridLayout_7.addWidget(self.label_T_On, 0, 1, 1, 1)
        self.label_PF = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_PF.setAlignment(QtCore.Qt.AlignCenter)
        
        self.gridLayout_7.addWidget(self.label_PF, 0, 3, 1, 1)
        self.label_ch3 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_ch3.setAlignment(QtCore.Qt.AlignCenter)
        
        self.gridLayout_7.addWidget(self.label_ch3, 3, 0, 1, 1)
        self.label_ch8 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_ch8.setAlignment(QtCore.Qt.AlignCenter)
        
        self.gridLayout_7.addWidget(self.label_ch8, 10, 0, 1, 1)
        self.ch1_T_Off = QtWidgets.QLineEdit(self.layoutWidget_3)
        
        self.gridLayout_7.addWidget(self.ch1_T_Off, 1, 2, 1, 1)
        self.ch2_T_Off = QtWidgets.QLineEdit(self.layoutWidget_3)
        
        self.gridLayout_7.addWidget(self.ch2_T_Off, 2, 2, 1, 1)
        self.ch6_T_On = QtWidgets.QLineEdit(self.layoutWidget_3)
        
        self.gridLayout_7.addWidget(self.ch6_T_On, 6, 1, 1, 1)
        self.ch2_T_On = QtWidgets.QLineEdit(self.layoutWidget_3)
        
        self.gridLayout_7.addWidget(self.ch2_T_On, 2, 1, 1, 1)
        self.ch7_PF = QtWidgets.QLabel(self.layoutWidget_3)
        self.ch7_PF.setAlignment(QtCore.Qt.AlignCenter)
        
        self.gridLayout_7.addWidget(self.ch7_PF, 8, 3, 1, 1)
        self.ch6_PF = QtWidgets.QLabel(self.layoutWidget_3)
        self.ch6_PF.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.ch6_PF, 6, 3, 1, 1)
        self.ch5_PF = QtWidgets.QLabel(self.layoutWidget_3)
        self.ch5_PF.setAlignment(QtCore.Qt.AlignCenter)
        
        self.gridLayout_7.addWidget(self.ch5_PF, 5, 3, 1, 1)
        self.ch4_PF = QtWidgets.QLabel(self.layoutWidget_3)
        self.ch4_PF.setAlignment(QtCore.Qt.AlignCenter)
        
        self.gridLayout_7.addWidget(self.ch4_PF, 4, 3, 1, 1)
        self.ch3_PF = QtWidgets.QLabel(self.layoutWidget_3)
        self.ch3_PF.setAlignment(QtCore.Qt.AlignCenter)
        
        self.gridLayout_7.addWidget(self.ch3_PF, 3, 3, 1, 1)
        self.ch2_PF = QtWidgets.QLabel(self.layoutWidget_3)
        self.ch2_PF.setAlignment(QtCore.Qt.AlignCenter)
        
        self.gridLayout_7.addWidget(self.ch2_PF, 2, 3, 1, 1)
        self.ch1_PF = QtWidgets.QLabel(self.layoutWidget_3)
        self.ch1_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_7.addWidget(self.ch1_PF, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        #ch_T_Off
        self.ch1_T_Off.setObjectName("ch1_T_Off")
        self.ch2_T_Off.setObjectName("ch2_T_Off")
        self.ch3_T_Off.setObjectName("ch3_T_Off")
        self.ch4_T_Off.setObjectName("ch4_T_Off")
        self.ch5_T_Off.setObjectName("ch5_T_Off")
        self.ch6_T_Off.setObjectName("ch6_T_Off")
        self.ch7_T_Off.setObjectName("ch7_T_Off")
        self.ch8_T_Off.setObjectName("ch8_T_Off")
        
        #ch_T_On
        self.ch1_T_On.setObjectName("ch1_T_On")
        self.ch2_T_On.setObjectName("ch2_T_On")
        self.ch3_T_On.setObjectName("ch3_T_On")
        self.ch4_T_On.setObjectName("ch4_T_On")
        self.ch5_T_On.setObjectName("ch5_T_On")
        self.ch6_T_On.setObjectName("ch6_T_On")
        self.ch7_T_On.setObjectName("ch7_T_On")
        self.ch8_T_On.setObjectName("ch8_T_On")
        
        #label_項目名
        self.label_10.setObjectName("label_10")
        self.label_T_On.setObjectName("label_T_On")
        self.label_T_Off.setObjectName("label_T_Off")
        self.label_PF.setObjectName("label_PF")
        
        #label_ch
        self.label_ch1.setObjectName("label_ch1")
        self.label_ch2.setObjectName("label_ch2")
        self.label_ch3.setObjectName("label_ch3")
        self.label_ch4.setObjectName("label_ch4")
        self.label_ch5.setObjectName("label_ch5")
        self.label_ch6.setObjectName("label_ch6")
        self.label_ch7.setObjectName("label_ch7")
        self.label_ch8.setObjectName("label_ch8")
        
        #ch_PF
        self.ch1_PF.setObjectName("ch1_PF")
        self.ch2_PF.setObjectName("ch2_PF")
        self.ch3_PF.setObjectName("ch3_PF")
        self.ch4_PF.setObjectName("ch4_PF")
        self.ch5_PF.setObjectName("ch5_PF")
        self.ch6_PF.setObjectName("ch6_PF")
        self.ch7_PF.setObjectName("ch7_PF")
        self.ch8_PF.setObjectName("ch8_PF")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    #文字檔設置
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.EGGI_Title.setText(_translate("MainWindow", "EGGI 產測"))
        
        #-------------------------Input區-----------------------------------
        self.Input_box.setTitle(_translate("MainWindow", "Input"))
        self.label_name.setText(_translate("MainWindow", "操作人員"))
        self.label_datetime.setText(_translate("MainWindow", "日期"))
        self.label_txt.setText(_translate("MainWindow", "TXT檔案"))
        self.btn_opentxt.setText(_translate("MainWindow", "打開"))
        
        #-------------------------Chart區-----------------------------------
        self.Chart_box.setTitle(_translate("MainWindow", "Chart"))
        self.btn_clean.setText(_translate("MainWindow", "清除"))
        self.btn_save.setText(_translate("MainWindow", "儲存"))
        
        #-------------------------Result區-----------------------------------
        self.Result_box.setTitle(_translate("MainWindow", "Result"))
        #Result區 項目欄的文字
        self.label_10.setText(_translate("MainWindow", "CH"))        
        self.label_T_Off.setText(_translate("MainWindow", "T_Off"))
        self.label_T_On.setText(_translate("MainWindow", "T_On"))
        self.label_PF.setText(_translate("MainWindow", "PASS/FAIL"))
        #Result區 各個Channel的文字
        self.label_ch1.setText(_translate("MainWindow", "CH1"))
        self.label_ch2.setText(_translate("MainWindow", "CH2"))
        self.label_ch3.setText(_translate("MainWindow", "CH3"))
        self.label_ch4.setText(_translate("MainWindow", "CH4"))
        self.label_ch5.setText(_translate("MainWindow", "CH5"))
        self.label_ch6.setText(_translate("MainWindow", "CH6"))
        self.label_ch7.setText(_translate("MainWindow", "CH7"))
        self.label_ch8.setText(_translate("MainWindow", "CH8"))
        #Result區 各個Channel回讀PASS或FAIL
        self.ch8_PF.setText(_translate("MainWindow", "Pass/Fail"))
        self.ch7_PF.setText(_translate("MainWindow", "Pass/Fail"))
        self.ch6_PF.setText(_translate("MainWindow", "Pass/Fail"))
        self.ch5_PF.setText(_translate("MainWindow", "Pass/Fail"))
        self.ch4_PF.setText(_translate("MainWindow", "Pass/Fail"))
        self.ch3_PF.setText(_translate("MainWindow", "Pass/Fail"))
        self.ch2_PF.setText(_translate("MainWindow", "Pass/Fail"))
        self.ch1_PF.setText(_translate("MainWindow", "Pass/Fail"))
