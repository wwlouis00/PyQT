#--------------說明欄----------------
#     PF是PASS/FAIL意思
#     T_On 開始運作  溫度下降
#     T_Off 關閉運作 溫度上升
#___________________________________
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QFileDialog
from PyQt5.QtCore import *
import time
from datetime import datetime
import os
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from pandas.core.indexes.base import Index
from pandas.core.series import Series
from io import SEEK_CUR
import csv
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
import time
import datetime
from datetime import datetime, timedelta
import statistics
import numpy as np
from openpyxl import load_workbook
from heapq import nsmallest
from pandas.core.indexes.base import Index
from pandas.core.series import Series

import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsPixmapItem

now_output_time = str(datetime.now().strftime('%Y-%m-%d %H-%M-%S'))+"output.xlsx"

class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)

        # self.face_recong = face.Recognition()
        self.timer_camera = QtCore.QTimer()
        self.CAM_NUM = 0
        self.x = 0
        self.count = 0
        self.timer = QTimer()

    # browsefile開啟檔案功能
    def browsefile(self):
        self.CH1_data = []
        self.CH2_data = []
        self.CH3_data = []
        self.CH4_data = []
        self.CH5_data = []
        self.CH6_data = []
        self.CH7_data = []
        self.CH8_data = []
        CH1_T_On = []
        CH1_T_Off  = []
        CH2_T_On = []
        CH2_T_Off = []
        CH3_T_On = []
        CH3_T_Off  = []
        CH4_T_On = []
        CH4_T_Off = []
        CH5_T_On = []
        CH5_T_Off  = []
        CH6_T_On = []
        CH6_T_Off = []
        CH7_T_On = []
        CH7_T_Off  = []
        CH8_T_On = []
        CH8_T_Off = []


        self.fname = QFileDialog.getOpenFileName(self, '開啟txt檔案', 'C:\Program Files (x86)', 'txt files (*.txt)')
        # " C:\python\Learn_Python\Temperature" 是自己的電腦位置路徑
        self.input_file.setText(self.fname[0])
        print(self.fname[0])
        self.df = pd.read_csv(self.fname[0],delimiter='\t')
        self.df.columns = ['time', 'index', 'CH1', 'CH2', 'CH3', 'CH4', 'CH5', 'CH6', 'CH7', 'CH8']#在開啟檔案上面新增一行
        print(self.df)
        #存取每個Channel的值到陣列
        for CH_data in range(0,len(self.df.index),1):
            self.CH1_data.append(self.df.loc[CH_data,'CH1'])
            self.CH2_data.append(self.df.loc[CH_data,'CH2'])
            self.CH3_data.append(self.df.loc[CH_data,'CH3'])
            self.CH4_data.append(self.df.loc[CH_data,'CH4'])
            self.CH5_data.append(self.df.loc[CH_data,'CH5'])
            self.CH6_data.append(self.df.loc[CH_data,'CH6'])
            self.CH7_data.append(self.df.loc[CH_data,'CH7'])
            self.CH8_data.append(self.df.loc[CH_data,'CH8'])
        print(len(self.CH1_data))

        for CH_slope in range(0,len(self.df.index)-1,1):
            #CH1
            CH1_GAP = float(self.CH1_data[CH_slope+1]) - float(self.CH1_data[CH_slope])
            CH = (CH_slope+1) - CH_slope
            CH1_quo = CH1_GAP/CH
            if CH1_quo < 0 and self.CH1_data[CH_slope] >= 109:
                CH1_T_On.append(self.CH1_data[CH_slope])
            elif CH1_quo > 0 and self.CH1_data[CH_slope] <=74:
                CH1_T_Off.append(self.CH1_data[CH_slope])
            #CH2
            CH2_GAP = float(self.CH2_data[CH_slope + 1]) - float(self.CH2_data[CH_slope])
            CH2_quo = CH2_GAP / CH
            if CH2_quo < 0 and self.CH2_data[CH_slope] >= 109:
                CH2_T_On.append(self.CH2_data[CH_slope])
            elif CH2_quo > 0 and self.CH2_data[CH_slope] <= 74:
                CH2_T_Off.append(self.CH2_data[CH_slope])
            # elif self.CH2[CH_slope] < 0:
            #     CH2_T_On.append(0)
            #     CH2_T_Off.append(0)
        print(CH1_T_On)
        print(CH2_T_On)
        self.ch1_T_On.setText(str(CH1_T_On[0]))
        self.ch1_T_Off.setText(str(CH1_T_Off[0]))
        # self.ch2_T_On.setText =str(CH2_T_On[0])
        # self.ch2_T_Off.setText(str(CH2_T_Off[0]))
        # self.ch3_T_On.setText(str(CH3_T_On[0]))
        # self.ch3_T_Off.setText(str(CH3_T_Off[0]))
        # self.ch4_T_On.setText(str(CH4_T_On[0]))
        # self.ch4_T_Off.setText(str(CH4_T_Off[0]))
        # self.ch5_T_On.setText(str(test_large[0]))
        # self.ch5_T_Off.setText(str(test_small[0]))
        # self.ch6_T_On.setText(str(test_large[0]))
        # self.ch6_T_Off.setText(str(test_small[0]))
        # self.ch7_T_On.setText(str(test_large[0]))
        # self.ch7_T_Off.setText(str(test_small[0]))
        # self.ch8_T_On.setText(str(test_large[0]))
        # self.ch8_T_Off.setText(str(test_small[0]))

        self.df.to_excel('./'+ now_output_time,encoding="utf_8_sg")

        #以下為顯示qrcode圖片
        #讀取影象
        img=cv2.imread("image\ch01.jpg")                              
        img2=cv2.imread("image\ch02.jpg")
        img3=cv2.imread("image\ch03.jpg")
        img4=cv2.imread("image\ch04.jpg")
        img5=cv2.imread("image\ch05.jpg")
        img6=cv2.imread("image\ch06.jpg")
        img7=cv2.imread("image\ch07.jpg")
        img8=cv2.imread("image\ch08.jpg")
        #轉換影象通道
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
        img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)
        img5 = cv2.cvtColor(img5, cv2.COLOR_BGR2RGB)
        img6 = cv2.cvtColor(img6, cv2.COLOR_BGR2RGB)
        img7 = cv2.cvtColor(img7, cv2.COLOR_BGR2RGB)
        img8 = cv2.cvtColor(img8, cv2.COLOR_BGR2RGB) 
        #獲取影象大小             
        x = img.shape[1]                                        
        y = img.shape[0]
        x2 = img2.shape[1]                                        
        y2 = img2.shape[0]
        x3 = img3.shape[1]                                        
        y3 = img3.shape[0]
        x4 = img4.shape[1]                                        
        y4 = img4.shape[0]
        x5 = img5.shape[1]                                        
        y5 = img5.shape[0]
        x6 = img6.shape[1]                                        
        y6 = img6.shape[0]
        x7 = img7.shape[1]                                        
        y7 = img7.shape[0]
        x8 = img8.shape[1]                                        
        y8 = img8.shape[0]
        #圖片放縮尺度
        self.zoomscale=1                                        
        frame = QImage(img, x, y,x*3, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)
        frame2 = QImage(img2, x2, y2,x2*3, QImage.Format_RGB888)
        pix2 = QPixmap.fromImage(frame2)
        frame3 = QImage(img3, x3, y3,x3*3, QImage.Format_RGB888)
        pix3 = QPixmap.fromImage(frame3)
        frame4 = QImage(img4, x4, y4,x4*3, QImage.Format_RGB888)
        pix4 = QPixmap.fromImage(frame4)
        frame5 = QImage(img5, x5, y5,x5*3, QImage.Format_RGB888)
        pix5 = QPixmap.fromImage(frame5)
        frame6 = QImage(img6, x6, y6,x6*3, QImage.Format_RGB888)
        pix6 = QPixmap.fromImage(frame6)
        frame7 = QImage(img7, x7, y7,x7*3, QImage.Format_RGB888)
        pix7 = QPixmap.fromImage(frame7)
        frame8 = QImage(img8, x8, y8,x8*3, QImage.Format_RGB888)
        pix8 = QPixmap.fromImage(frame8)
        #建立畫素圖元
        self.item=QGraphicsPixmapItem(pix)   
        self.item2=QGraphicsPixmapItem(pix2)
        self.item3=QGraphicsPixmapItem(pix3)
        self.item4=QGraphicsPixmapItem(pix4)
        self.item5=QGraphicsPixmapItem(pix5)
        self.item6=QGraphicsPixmapItem(pix6)
        self.item7=QGraphicsPixmapItem(pix7)
        self.item8=QGraphicsPixmapItem(pix8)                   
        #self.item.setScale(self.zoomscale)
        #建立場景
        self.scene=QGraphicsScene() 
        self.scene2=QGraphicsScene() 
        self.scene3=QGraphicsScene()
        self.scene4=QGraphicsScene()
        self.scene5=QGraphicsScene()
        self.scene6=QGraphicsScene()
        self.scene7=QGraphicsScene()
        self.scene8=QGraphicsScene()                           
        self.scene.addItem(self.item)
        self.scene2.addItem(self.item2)
        self.scene3.addItem(self.item3)
        self.scene4.addItem(self.item4)
        self.scene5.addItem(self.item5)
        self.scene6.addItem(self.item6)
        self.scene7.addItem(self.item7)
        self.scene8.addItem(self.item8)
         #將場景新增至檢視
        self.ch1_qrcode.setScene(self.scene)
        self.ch2_qrcode.setScene(self.scene2)  
        self.ch3_qrcode.setScene(self.scene3)  
        self.ch4_qrcode.setScene(self.scene4)  
        self.ch5_qrcode.setScene(self.scene5)  
        self.ch6_qrcode.setScene(self.scene6)  
        self.ch7_qrcode.setScene(self.scene7)  
        self.ch8_qrcode.setScene(self.scene8)                         


        

    def save_log(self):
        self.save_excel = pd.DataFrame({'操作人員':[str(self.input_name.setText)],'日期':[str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))],'txt檔案':[str(self.fname[0])]})
        self.save_excel.to_excel('./'+'history'+now_output_time,encoding="utf_8_sig")
    def clean_log(self):
        #T_On全關
        self.ch1_T_On.setText("")
        self.ch2_T_On.setText("")
        self.ch3_T_On.setText("")
        self.ch4_T_On.setText("")
        self.ch5_T_On.setText("")
        self.ch6_T_On.setText("")
        self.ch7_T_On.setText("")
        self.ch8_T_On.setText("")
        # T_Off全關
        self.ch1_T_Off.setText("")
        self.ch2_T_Off.setText("")
        self.ch3_T_Off.setText("")
        self.ch4_T_Off.setText("")
        self.ch5_T_Off.setText("")
        self.ch6_T_Off.setText("")
        self.ch7_T_Off.setText("")
        self.ch8_T_Off.setText("")
        # PF全關
        self.ch1_PF.setText("")
        self.ch2_PF.setText("")
        self.ch3_PF.setText("")
        self.ch4_PF.setText("")
        self.ch5_PF.setText("")
        self.ch6_PF.setText("")
        self.ch7_PF.setText("")
        self.ch8_PF.setText("")
        #欄位
        self.input_file.setText("")
        self.input_name.setText("")


    # 顯示現在時間
    def showtime(self):
        self.time = QDateTime.currentDateTime()
        timedisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")  # 格式化一下時間
        self.time.setText(timedisplay)



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 799)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Input_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Input_box.setGeometry(QtCore.QRect(10, 90, 761, 181))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Input_box.setFont(font)
        self.Input_box.setObjectName("Input_box")
        self.btn_opentxt = QtWidgets.QPushButton(self.Input_box)
        self.btn_opentxt.setGeometry(QtCore.QRect(650, 36, 91, 43))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_opentxt.setFont(font)
        self.btn_opentxt.setObjectName("btn_opentxt")
        self.btn_save = QtWidgets.QPushButton(self.Input_box)
        self.btn_save.setGeometry(QtCore.QRect(650, 78, 91, 43))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save.setFont(font)
        self.btn_save.setObjectName("btn_save")
        self.btn_clean = QtWidgets.QPushButton(self.Input_box)
        self.btn_clean.setGeometry(QtCore.QRect(650, 120, 91, 43))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clean.setFont(font)
        self.btn_clean.setObjectName("btn_clean")
        self.label_name = QtWidgets.QLabel(self.Input_box)
        self.label_name.setGeometry(QtCore.QRect(21, 57, 72, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.input_name = QtWidgets.QLineEdit(self.Input_box)
        self.input_name.setGeometry(QtCore.QRect(100, 57, 245, 29))
        self.input_name.setObjectName("input_name")
        self.label_datetime = QtWidgets.QLabel(self.Input_box)
        self.label_datetime.setGeometry(QtCore.QRect(352, 57, 36, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_datetime.setFont(font)
        self.label_datetime.setAlignment(QtCore.Qt.AlignCenter)
        self.label_datetime.setObjectName("label_datetime")
        self.output_datetime = QtWidgets.QLineEdit(self.Input_box)
        self.output_datetime.setGeometry(QtCore.QRect(395, 57, 245, 29))
        self.output_datetime.setObjectName("output_datetime")
        self.label_txt_2 = QtWidgets.QLabel(self.Input_box)
        self.label_txt_2.setGeometry(QtCore.QRect(21, 113, 68, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_txt_2.setFont(font)
        self.label_txt_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_txt_2.setObjectName("label_txt_2")
        self.input_file = QtWidgets.QLineEdit(self.Input_box)
        self.input_file.setGeometry(QtCore.QRect(100, 113, 540, 29))
        self.input_file.setObjectName("input_file")
        self.EGGI_Title = QtWidgets.QLabel(self.centralwidget)
        self.EGGI_Title.setGeometry(QtCore.QRect(10, 6, 1351, 76))
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
        self.Chart_box.setGeometry(QtCore.QRect(10, 282, 761, 331))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Chart_box.setFont(font)
        self.Chart_box.setObjectName("Chart_box")
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
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 36, 731, 265))
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
        self.Result_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Result_box.setGeometry(QtCore.QRect(800, 90, 561, 691))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Result_box.setFont(font)
        self.Result_box.setObjectName("Result_box")
        self.layoutWidget = QtWidgets.QWidget(self.Result_box)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 530, 361))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ch7_T_Off = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch7_T_Off.setObjectName("ch7_T_Off")
        self.gridLayout.addWidget(self.ch7_T_Off, 7, 5, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 5, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.ch6_T_Off = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch6_T_Off.setObjectName("ch6_T_Off")
        self.gridLayout.addWidget(self.ch6_T_Off, 6, 5, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 8, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 7, 2, 1, 1)
        self.ch8_T_On = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch8_T_On.setObjectName("ch8_T_On")
        self.gridLayout.addWidget(self.ch8_T_On, 8, 4, 1, 1)
        self.ch2_T_Off = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch2_T_Off.setObjectName("ch2_T_Off")
        self.gridLayout.addWidget(self.ch2_T_Off, 2, 5, 1, 1)
        self.label_ch3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch3.setFont(font)
        self.label_ch3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch3.setObjectName("label_ch3")
        self.gridLayout.addWidget(self.label_ch3, 3, 1, 1, 1)
        self.label_ch7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch7.setFont(font)
        self.label_ch7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch7.setObjectName("label_ch7")
        self.gridLayout.addWidget(self.label_ch7, 7, 1, 1, 1)
        self.label_qrcode = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_qrcode.setFont(font)
        self.label_qrcode.setAlignment(QtCore.Qt.AlignCenter)
        self.label_qrcode.setObjectName("label_qrcode")
        self.gridLayout.addWidget(self.label_qrcode, 0, 3, 1, 1)
        self.ch5_PF = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch5_PF.setObjectName("ch5_PF")
        self.gridLayout.addWidget(self.ch5_PF, 5, 6, 1, 1)
        self.label_ch6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch6.setFont(font)
        self.label_ch6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch6.setObjectName("label_ch6")
        self.gridLayout.addWidget(self.label_ch6, 6, 1, 1, 1)
        self.ch5_T_On = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch5_T_On.setObjectName("ch5_T_On")
        self.gridLayout.addWidget(self.ch5_T_On, 5, 4, 1, 1)
        self.ch2_PF = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch2_PF.setObjectName("ch2_PF")
        self.gridLayout.addWidget(self.ch2_PF, 2, 6, 1, 1)
        self.label_ch2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch2.setFont(font)
        self.label_ch2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch2.setObjectName("label_ch2")
        self.gridLayout.addWidget(self.label_ch2, 2, 1, 1, 1)
        self.ch1_PF = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch1_PF.setObjectName("ch1_PF")
        self.gridLayout.addWidget(self.ch1_PF, 1, 6, 1, 1)
        self.ch4_PF = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch4_PF.setObjectName("ch4_PF")
        self.gridLayout.addWidget(self.ch4_PF, 4, 6, 1, 1)
        self.ch1_T_Off = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch1_T_Off.setObjectName("ch1_T_Off")
        self.gridLayout.addWidget(self.ch1_T_Off, 1, 5, 1, 1)
        self.ch3_PF = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch3_PF.setObjectName("ch3_PF")
        self.gridLayout.addWidget(self.ch3_PF, 3, 6, 1, 1)
        self.ch8_PF = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch8_PF.setObjectName("ch8_PF")
        self.gridLayout.addWidget(self.ch8_PF, 8, 6, 1, 1)
        self.ch7_T_On = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch7_T_On.setObjectName("ch7_T_On")
        self.gridLayout.addWidget(self.ch7_T_On, 7, 4, 1, 1)
        self.ch4_T_On = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch4_T_On.setObjectName("ch4_T_On")
        self.gridLayout.addWidget(self.ch4_T_On, 4, 4, 1, 1)
        self.label_ch5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch5.setFont(font)
        self.label_ch5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch5.setObjectName("label_ch5")
        self.gridLayout.addWidget(self.label_ch5, 5, 1, 1, 1)
        self.ch4_T_Off = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch4_T_Off.setObjectName("ch4_T_Off")
        self.gridLayout.addWidget(self.ch4_T_Off, 4, 5, 1, 1)
        self.ch6_T_On = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch6_T_On.setObjectName("ch6_T_On")
        self.gridLayout.addWidget(self.ch6_T_On, 6, 4, 1, 1)
        self.label_T_On_14 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_T_On_14.setFont(font)
        self.label_T_On_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T_On_14.setObjectName("label_T_On_14")
        self.gridLayout.addWidget(self.label_T_On_14, 0, 6, 1, 1)
        self.label_ch8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch8.setFont(font)
        self.label_ch8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch8.setObjectName("label_ch8")
        self.gridLayout.addWidget(self.label_ch8, 8, 1, 1, 1)
        self.ch3_T_On = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch3_T_On.setObjectName("ch3_T_On")
        self.gridLayout.addWidget(self.ch3_T_On, 3, 4, 1, 1)
        self.label_T_Off = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_T_Off.setFont(font)
        self.label_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T_Off.setObjectName("label_T_Off")
        self.gridLayout.addWidget(self.label_T_Off, 0, 5, 1, 1)
        self.label_ch1 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch1.setFont(font)
        self.label_ch1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch1.setObjectName("label_ch1")
        self.gridLayout.addWidget(self.label_ch1, 1, 1, 1, 1)
        self.ch7_PF = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch7_PF.setObjectName("ch7_PF")
        self.gridLayout.addWidget(self.ch7_PF, 7, 6, 1, 1)
        self.label_ch4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch4.setFont(font)
        self.label_ch4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch4.setObjectName("label_ch4")
        self.gridLayout.addWidget(self.label_ch4, 4, 1, 1, 1)
        self.ch1_T_On = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch1_T_On.setObjectName("ch1_T_On")
        self.gridLayout.addWidget(self.ch1_T_On, 1, 4, 1, 1)
        self.ch3_T_Off = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch3_T_Off.setObjectName("ch3_T_Off")
        self.gridLayout.addWidget(self.ch3_T_Off, 3, 5, 1, 1)
        self.ch5_T_Off = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch5_T_Off.setObjectName("ch5_T_Off")
        self.gridLayout.addWidget(self.ch5_T_Off, 5, 5, 1, 1)
        self.ch2_T_On = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch2_T_On.setObjectName("ch2_T_On")
        self.gridLayout.addWidget(self.ch2_T_On, 2, 4, 1, 1)
        self.ch8_T_Off = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch8_T_Off.setObjectName("ch8_T_Off")
        self.gridLayout.addWidget(self.ch8_T_Off, 8, 5, 1, 1)
        self.ch6_PF = QtWidgets.QLineEdit(self.layoutWidget)
        self.ch6_PF.setObjectName("ch6_PF")
        self.gridLayout.addWidget(self.ch6_PF, 6, 6, 1, 1)
        self.label_T_On = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_T_On.setFont(font)
        self.label_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T_On.setObjectName("label_T_On")
        self.gridLayout.addWidget(self.label_T_On, 0, 4, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 6, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 3, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 624, 761, 163))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(20, 24, 721, 115))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_opentxt.clicked.connect(self.btn_opentxt.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    
    #文字設定檔案
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "溫控檢測程式"))
        # -------------------------Input區-----------------------------------
        self.Input_box.setTitle(_translate("MainWindow", "Input"))
        self.btn_opentxt.setText(_translate("MainWindow", "打開"))
        self.btn_save.setText(_translate("MainWindow", "儲存"))
        self.btn_clean.setText(_translate("MainWindow", "清除"))
        self.label_name.setText(_translate("MainWindow", "操作人員"))
        self.label_datetime.setText(_translate("MainWindow", "日期"))
        self.label_txt_2.setText(_translate("MainWindow", "TXT檔案"))
        self.EGGI_Title.setText(_translate("MainWindow", "EGGI 產測"))
        self.Chart_box.setTitle(_translate("MainWindow", "Chart"))
        self.Result_box.setTitle(_translate("MainWindow", "Result"))
        self.pushButton_5.setText(_translate("MainWindow", "CH5-QRCODE"))
        self.pushButton_3.setText(_translate("MainWindow", "CH3-QRCODE"))
        self.pushButton_4.setText(_translate("MainWindow", "CH4-QRCODE"))
        self.pushButton.setText(_translate("MainWindow", "CH1-QRCODE"))
        self.pushButton_2.setText(_translate("MainWindow", "CH2-QRCODE"))
        self.pushButton_8.setText(_translate("MainWindow", "CH8-QRCODE"))
        self.pushButton_7.setText(_translate("MainWindow", "CH7-QRCODE"))
        self.label_ch3.setText(_translate("MainWindow", "CH3"))
        self.label_ch7.setText(_translate("MainWindow", "CH7"))
        self.label_qrcode.setText(_translate("MainWindow", "QRCODE"))
        self.label_ch6.setText(_translate("MainWindow", "CH6"))
        self.label_ch2.setText(_translate("MainWindow", "CH2"))
        self.label_ch5.setText(_translate("MainWindow", "CH5"))
        self.label_T_On_14.setText(_translate("MainWindow", "PASS/FAIL"))
        self.label_ch8.setText(_translate("MainWindow", "CH8"))
        self.label_T_Off.setText(_translate("MainWindow", "T_Off"))
        self.label_ch1.setText(_translate("MainWindow", "CH1"))
        self.label_ch4.setText(_translate("MainWindow", "CH4"))
        self.label_T_On.setText(_translate("MainWindow", "T_On"))
        self.pushButton_6.setText(_translate("MainWindow", "CH6-QRCODE"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox.setTitle(_translate("MainWindow", "Output"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))

