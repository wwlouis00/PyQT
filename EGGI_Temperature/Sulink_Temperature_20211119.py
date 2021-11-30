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
from pyzbar import pyzbar

import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsPixmapItem

now_output_time = str(datetime.now().strftime('%Y-%m-%d %H-%M-%S'))+"output.xlsx"


# CH_total = [i for i in range(1,sh.max_row + 1,1)]

def scan_qrcode(qrcode):
    data = pyzbar.decode(qrcode)
    return data[0].data.decode('utf-8')


class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)

        # self.face_recong = face.Recognition()
        self.timer_camera = QtCore.QTimer()
        self.CAM_NUM = 0
        self.x = 0
        self.count = 0
        self.timer = QTimer()


    def qrcode1(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('scan qrcode1', frame)
            # 解析二維條碼
            text = None
            try:
                text = scan_qrcode(frame)
            except Exception as e:
                pass
            if text:
                print(text)
                self.label1.setText(text)
                break
            key = cv2.waitKey(10)
            if key == ord('q'):
                break
        cv2.destroyAllWindows()
    def qrcode2(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('scan qrcode2', frame)
            # 解析二維條碼
            text = None
            try:
                text = scan_qrcode(frame)
            except Exception as e:
                pass
            if text:
                print(text)
                self.label2.setText(text)
                break
            key = cv2.waitKey(10)
            if key == ord('q'):
                break
        cv2.destroyAllWindows()
    def qrcode3(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('scan qrcode3', frame)
            # 解析二維條碼
            text = None
            try:
                text = scan_qrcode(frame)
            except Exception as e:
                pass
            if text:
                print(text)
                self.label3.setText(text)
                break
            key = cv2.waitKey(10)
            if key == ord('q'):
                break
        cv2.destroyAllWindows()
    def qrcode4(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('scan qrcode4', frame)
            # 解析二維條碼
            text = None
            try:
                text = scan_qrcode(frame)
            except Exception as e:
                pass
            if text:
                print(text)
                self.label4.setText(text)
                break
            key = cv2.waitKey(10)
            if key == ord('q'):
                break
        cv2.destroyAllWindows()
    def qrcode5(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('scan qrcode5', frame)
            # 解析二維條碼
            text = None
            try:
                text = scan_qrcode(frame)
            except Exception as e:
                pass
            if text:
                print(text)
                self.label5.setText(text)
                break
            key = cv2.waitKey(10)
            if key == ord('q'):
                break
        cv2.destroyAllWindows()
    def qrcode6(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('scan qrcode6', frame)
            # 解析二維條碼
            text = None
            try:
                text = scan_qrcode(frame)
            except Exception as e:
                pass
            if text:
                print(text)
                self.label6.setText(text)
                break
            key = cv2.waitKey(10)
            if key == ord('q'):
                break
        cv2.destroyAllWindows()
    def qrcode7(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('scan qrcode7', frame)
            # 解析二維條碼
            text = None
            try:
                text = scan_qrcode(frame)
            except Exception as e:
                pass
            if text:
                print(text)
                self.label7.setText(text)
                break
            key = cv2.waitKey(10)
            if key == ord('q'):
                break
        cv2.destroyAllWindows()
    def qrcode8(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow('scan qrcode8', frame)
            # 解析二維條碼
            text = None
            try:
                text = scan_qrcode(frame)
            except Exception as e:
                pass
            if text:
                print(text)
                self.label8.setText(text)
                break
            key = cv2.waitKey(10)
            if key == ord('q'):
                break
        cv2.destroyAllWindows()

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

        '''
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
        '''

        

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
        MainWindow.resize(1372, 824)
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

        self.btn_clean = QtWidgets.QPushButton(self.Input_box)
        self.btn_clean.setGeometry(QtCore.QRect(650, 120, 91, 43))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clean.setFont(font)
        self.btn_save.setObjectName("btn_save")
        self.btn_clean.setObjectName("btn_clean")
        self.widget = QtWidgets.QWidget(self.Input_box)
        self.widget.setGeometry(QtCore.QRect(20, 36, 621, 127))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_name = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.gridLayout_2.addWidget(self.label_name, 0, 0, 1, 1)
        self.input_name = QtWidgets.QLineEdit(self.widget)
        self.input_name.setObjectName("input_name")
        self.gridLayout_2.addWidget(self.input_name, 0, 1, 1, 1)
        self.label_datetime = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_datetime.setFont(font)
        self.label_datetime.setAlignment(QtCore.Qt.AlignCenter)
        self.label_datetime.setObjectName("label_datetime")
        self.gridLayout_2.addWidget(self.label_datetime, 0, 2, 1, 1)
        self.output_datetime = QtWidgets.QLineEdit(self.widget)
        self.output_datetime.setObjectName("output_datetime")
        self.gridLayout_2.addWidget(self.output_datetime, 0, 3, 1, 1)
        self.label_txt_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_txt_2.setFont(font)
        self.label_txt_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_txt_2.setObjectName("label_txt_2")
        self.gridLayout_2.addWidget(self.label_txt_2, 1, 0, 1, 1)
        self.input_file = QtWidgets.QLineEdit(self.widget)
        self.input_file.setObjectName("input_file")
        self.gridLayout_2.addWidget(self.input_file, 1, 1, 1, 3)
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
        self.Result_box.setGeometry(QtCore.QRect(800, 90, 591, 697))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Result_box.setFont(font)
        self.Result_box.setObjectName("Result_box")
        self.widget1 = QtWidgets.QWidget(self.Result_box)
        self.widget1.setGeometry(QtCore.QRect(40, 30, 481, 651))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        #
        self.ch6_T_Off = QtWidgets.QLineEdit(self.widget1)
        self.ch6_T_Off.setObjectName("ch6_T_Off")
        self.gridLayout.addWidget(self.ch6_T_Off, 6, 4, 1, 1)
        #
        self.ch7_T_Off = QtWidgets.QLineEdit(self.widget1)
        self.ch7_T_Off.setObjectName("ch7_T_Off")
        self.gridLayout.addWidget(self.ch7_T_Off, 7, 4, 1, 1)
        #
        self.ch8_T_On = QtWidgets.QLineEdit(self.widget1)
        self.ch8_T_On.setObjectName("ch8_T_On")
        self.gridLayout.addWidget(self.ch8_T_On, 8, 3, 1, 1)
        #
        self.label_ch7 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch7.setFont(font)
        self.label_ch7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch7.setObjectName("label_ch7")
        self.gridLayout.addWidget(self.label_ch7, 7, 0, 1, 1)
        #
        self.ch2_T_Off = QtWidgets.QLineEdit(self.widget1)
        self.ch2_T_Off.setObjectName("ch2_T_Off")
        self.gridLayout.addWidget(self.ch2_T_Off, 2, 4, 1, 1)
        #
        self.label_qrcode = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_qrcode.setFont(font)
        self.label_qrcode.setFixedSize(100, 80)
        self.label_qrcode.setAlignment(QtCore.Qt.AlignCenter)
        self.label_qrcode.setObjectName("label_qrcode")
        self.gridLayout.addWidget(self.label_qrcode, 0, 2, 1, 1)
        #
        self.label_qrcode0 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_qrcode0.setFont(font)
        self.label_qrcode0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_qrcode0.setObjectName("label0_qrcode")
        self.gridLayout.addWidget(self.label_qrcode0, 0, 1, 1, 1)
        #
        self.label_ch3 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch3.setFont(font)
        self.label_ch3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch3.setObjectName("label_ch3")
        self.gridLayout.addWidget(self.label_ch3, 3, 0, 1, 1)
        #
        self.ch5_PF = QtWidgets.QLineEdit(self.widget1)
        self.ch5_PF.setObjectName("ch5_PF")
        self.gridLayout.addWidget(self.ch5_PF, 5, 5, 1, 1)
        #
        self.label_ch2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch2.setFont(font)
        self.label_ch2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch2.setObjectName("label_ch2")
        self.gridLayout.addWidget(self.label_ch2, 2, 0, 1, 1)
        #
        self.label_ch6 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch6.setFont(font)
        self.label_ch6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch6.setObjectName("label_ch6")
        self.gridLayout.addWidget(self.label_ch6, 6, 0, 1, 1)
        #label1資料
        self.label1 = QtWidgets.QLabel(self.widget1)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 1, 2, 1, 1)
        #label2資料
        self.label2 = QtWidgets.QLabel(self.widget1)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 2, 2, 1, 1)
        #label3資料
        self.label3 = QtWidgets.QLabel(self.widget1)
        self.label3.setObjectName("label3")
        self.gridLayout.addWidget(self.label3, 3, 2, 1, 1)
        #label4資料
        self.label4 = QtWidgets.QLabel(self.widget1)
        self.label4.setObjectName("label4")
        self.gridLayout.addWidget(self.label4, 4, 2, 1, 1)
        #label5資料
        self.label5 = QtWidgets.QLabel(self.widget1)
        self.label5.setObjectName("label5")
        self.gridLayout.addWidget(self.label5, 5, 2, 1, 1)
        #label6資料
        self.label6 = QtWidgets.QLabel(self.widget1)
        self.label6.setObjectName("label6")
        self.gridLayout.addWidget(self.label6, 6, 2, 1, 1)
        #label7資料
        self.label7 = QtWidgets.QLabel(self.widget1)
        self.label7.setObjectName("label7")
        self.gridLayout.addWidget(self.label7, 7, 2, 1, 1)
        #label8資料
        self.label8 = QtWidgets.QLabel(self.widget1)
        self.label8.setObjectName("label8")
        self.gridLayout.addWidget(self.label8, 8, 2, 1, 1)
        
        #ch5_T_On
        self.ch5_T_On = QtWidgets.QLineEdit(self.widget1)
        self.ch5_T_On.setObjectName("ch5_T_On")
        self.gridLayout.addWidget(self.ch5_T_On, 5, 3, 1, 1)
        #ch2_T_On
        self.ch2_PF = QtWidgets.QLineEdit(self.widget1)
        self.gridLayout.addWidget(self.ch2_PF, 2, 5, 1, 1)
        #ch1_T_Off
        self.ch1_T_Off = QtWidgets.QLineEdit(self.widget1)
        self.ch1_T_Off.setObjectName("ch1_T_Off")
        self.gridLayout.addWidget(self.ch1_T_Off, 1, 4, 1, 1)
        #ch3_PF
        self.ch3_PF = QtWidgets.QLineEdit(self.widget1)
        self.ch3_PF.setObjectName("ch3_PF")
        self.gridLayout.addWidget(self.ch3_PF, 3, 5, 1, 1)
        #
        self.ch4_PF = QtWidgets.QLineEdit(self.widget1)
        self.gridLayout.addWidget(self.ch4_PF, 4, 5, 1, 1)
        #
        self.ch8_PF = QtWidgets.QLineEdit(self.widget1)
        self.ch8_PF.setObjectName("ch8_PF")
        self.gridLayout.addWidget(self.ch8_PF, 8, 5, 1, 1)
        #
        self.ch1_PF = QtWidgets.QLineEdit(self.widget1)
        self.gridLayout.addWidget(self.ch1_PF, 1, 5, 1, 1)
        #
        self.ch6_T_On = QtWidgets.QLineEdit(self.widget1)
        self.ch6_T_On.setObjectName("ch6_T_On")
        self.gridLayout.addWidget(self.ch6_T_On, 6, 3, 1, 1)
        #
        self.ch4_T_On = QtWidgets.QLineEdit(self.widget1)
        self.ch4_T_On.setObjectName("ch4_T_On")
        self.gridLayout.addWidget(self.ch4_T_On, 4, 3, 1, 1)
        #
        self.ch4_T_Off = QtWidgets.QLineEdit(self.widget1)
        self.ch4_T_Off.setObjectName("ch4_T_Off")
        self.gridLayout.addWidget(self.ch4_T_Off, 4, 4, 1, 1)
        #
        self.ch7_T_On = QtWidgets.QLineEdit(self.widget1)
        self.ch7_T_On.setObjectName("ch7_T_On")
        self.gridLayout.addWidget(self.ch7_T_On, 7, 3, 1, 1)
        #
        self.label_ch5 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch5.setFont(font)
        self.label_ch5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch5.setObjectName("label_ch5")
        self.gridLayout.addWidget(self.label_ch5, 5, 0, 1, 1)
        #
        self.label_ch8 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch8.setFont(font)
        self.label_ch8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch8.setObjectName("label_ch8")
        self.gridLayout.addWidget(self.label_ch8, 8, 0, 1, 1)
        #
        self.label_ch1 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch1.setFont(font)
        self.label_ch1.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.label_ch1, 1, 0, 1, 1)
        #
        self.label_T_Off = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_T_Off.setFont(font)
        
        self.label_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T_Off.setObjectName("label_T_Off")
        self.gridLayout.addWidget(self.label_T_Off, 0, 4, 1, 1)
        #
        self.label_T_On_14 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_T_On_14.setFont(font)
        self.label_T_On_14.setFixedSize(100, 70)
        self.label_T_On_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T_On_14.setObjectName("label_T_On_14")
        self.gridLayout.addWidget(self.label_T_On_14, 0, 5, 1, 1)
        #
        self.ch3_T_On = QtWidgets.QLineEdit(self.widget1)
        self.ch3_T_On.setObjectName("ch3_T_On")
        self.gridLayout.addWidget(self.ch3_T_On, 3, 3, 1, 1)
        #
        self.ch2_qrcode = QtWidgets.QPushButton(self.widget1)
        self.ch2_qrcode.setObjectName("ch2_qrcode")
        self.gridLayout.addWidget(self.ch2_qrcode, 2, 1, 1, 1)

        #ch1_qrcode開關設定
        self.ch1_qrcode = QtWidgets.QPushButton(self.widget1)
        #self.ch1_qrcode.setObjectName("ch1_qrcode")
        self.ch1_qrcode.setObjectName("ch1_qrcode")
        self.gridLayout.addWidget(self.ch1_qrcode, 1, 1, 1, 1)

        self.ch7_PF = QtWidgets.QLineEdit(self.widget1)
        self.ch7_PF.setObjectName("ch7_PF")
        self.gridLayout.addWidget(self.ch7_PF, 7, 5, 1, 1)
        #self.graphicsView_8 = QtWidgets.QGraphicsView(self.widget1)
        #self.graphicsView_8.setObjectName("graphicsView_8")
        #self.gridLayout.addWidget(self.graphicsView_8, 8, 1, 1, 1)
        #
        self.label_ch4 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch4.setFont(font)
        self.label_ch4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch4.setObjectName("label_ch4")
        self.gridLayout.addWidget(self.label_ch4, 4, 0, 1, 1)
        #
        self.ch1_T_On = QtWidgets.QLineEdit(self.widget1)
        self.ch1_T_On.setObjectName("ch1_T_On")
        self.gridLayout.addWidget(self.ch1_T_On, 1, 3, 1, 1)
        #
        self.ch7_qrcode = QtWidgets.QPushButton(self.widget1)
        self.ch7_qrcode.setObjectName("ch7_qrcode")
        self.gridLayout.addWidget(self.ch7_qrcode, 7, 1, 1, 1)
        #
        self.ch8_qrcode = QtWidgets.QPushButton(self.widget1)
        self.ch8_qrcode.setObjectName("ch8_qrcode")
        self.gridLayout.addWidget(self.ch8_qrcode, 8, 1, 1, 1)
        #
        self.ch6_qrcode = QtWidgets.QPushButton(self.widget1)
        self.ch6_qrcode.setObjectName("ch6_qrcode")
        self.gridLayout.addWidget(self.ch6_qrcode, 6, 1, 1, 1)
        #
        self.ch5_qrcode = QtWidgets.QPushButton(self.widget1)
        self.ch5_qrcode.setObjectName("ch5_qrcode")
        self.gridLayout.addWidget(self.ch5_qrcode, 5, 1, 1, 1)
        #
        self.ch3_qrcode = QtWidgets.QPushButton(self.widget1)
        self.ch3_qrcode.setObjectName("ch3_qrcode")
        self.gridLayout.addWidget(self.ch3_qrcode, 3, 1, 1, 1)
        #
        self.ch4_qrcode = QtWidgets.QPushButton(self.widget1)
        self.ch4_qrcode.setObjectName("ch4_qrcode")
        self.gridLayout.addWidget(self.ch4_qrcode, 4, 1, 1, 1)
        #
        self.ch3_T_Off = QtWidgets.QLineEdit(self.widget1)
        self.ch3_T_Off.setObjectName("ch3_T_Off")
        self.gridLayout.addWidget(self.ch3_T_Off, 3, 4, 1, 1)
        #
        self.ch5_T_Off = QtWidgets.QLineEdit(self.widget1)
        self.ch5_T_Off.setObjectName("ch5_T_Off")
        self.gridLayout.addWidget(self.ch5_T_Off, 5, 4, 1, 1)
        #
        self.ch8_T_Off = QtWidgets.QLineEdit(self.widget1)
        self.ch8_T_Off.setObjectName("ch8_T_Off")
        self.gridLayout.addWidget(self.ch8_T_Off, 8, 4, 1, 1)
        #
        self.ch2_T_On = QtWidgets.QLineEdit(self.widget1)
        self.ch2_T_On.setObjectName("ch2_T_On")
        self.gridLayout.addWidget(self.ch2_T_On, 2, 3, 1, 1)
        #
        self.label_T_On = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_T_On.setFont(font)
        
        self.label_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T_On.setObjectName("label_T_On")
        self.gridLayout.addWidget(self.label_T_On, 0, 3, 1, 1)
        self.ch6_PF = QtWidgets.QLineEdit(self.widget1)
        self.ch6_PF.setObjectName("ch6_PF")
        self.gridLayout.addWidget(self.ch6_PF, 6, 5, 1, 1)
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

        # ch_T_Off
        self.ch1_T_Off.setObjectName("ch1_T_Off")
        self.ch2_T_Off.setObjectName("ch2_T_Off")
        self.ch3_T_Off.setObjectName("ch3_T_Off")
        self.ch4_T_Off.setObjectName("ch4_T_Off")
        self.ch5_T_Off.setObjectName("ch5_T_Off")
        self.ch6_T_Off.setObjectName("ch6_T_Off")
        self.ch7_T_Off.setObjectName("ch7_T_Off")
        self.ch8_T_Off.setObjectName("ch8_T_Off")

        # ch_T_On
        self.ch1_T_On.setObjectName("ch1_T_On")
        self.ch2_T_On.setObjectName("ch2_T_On")
        self.ch3_T_On.setObjectName("ch3_T_On")
        self.ch4_T_On.setObjectName("ch4_T_On")
        self.ch5_T_On.setObjectName("ch5_T_On")
        self.ch6_T_On.setObjectName("ch6_T_On")
        self.ch7_T_On.setObjectName("ch7_T_On")
        self.ch8_T_On.setObjectName("ch8_T_On")


        # label_ch
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



        self.retranslateUi(MainWindow)
        self.btn_clean.clicked.connect(self.clean_log)
        self.btn_opentxt.clicked.connect(self.browsefile)
        self.btn_save.clicked.connect(self.save_log)
        self.ch1_qrcode.clicked.connect(self.qrcode1)
        self.ch2_qrcode.clicked.connect(self.qrcode2)
        self.ch3_qrcode.clicked.connect(self.qrcode3)
        self.ch4_qrcode.clicked.connect(self.qrcode4)
        self.ch5_qrcode.clicked.connect(self.qrcode5)
        self.ch6_qrcode.clicked.connect(self.qrcode6)
        self.ch7_qrcode.clicked.connect(self.qrcode7)
        self.ch8_qrcode.clicked.connect(self.qrcode8)
        # self.output_datetime.setText(self.showtime)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # 文字檔設置
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "溫度監控程式"))
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

        #-------------------------Result區-----------------------------------
        self.Result_box.setTitle(_translate("MainWindow", "Result"))
        # Result區 項目欄的文字
        self.label_qrcode.setText(_translate("MainWindow", "QRCODE"))
        self.label_qrcode0.setText(_translate("MainWindow", "READ"))
        self.label_T_Off.setText(_translate("MainWindow", "T_Off"))
        self.label_T_On.setText(_translate("MainWindow", "T_On"))
        self.label_T_On_14.setText(_translate("MainWindow", "PASS/FAIL"))
        # Result區 各個Channel的文字
        self.label_ch1.setText(_translate("MainWindow", "CH1"))
        self.label_ch2.setText(_translate("MainWindow", "CH2"))
        self.label_ch3.setText(_translate("MainWindow", "CH3"))
        self.label_ch4.setText(_translate("MainWindow", "CH4"))
        self.label_ch5.setText(_translate("MainWindow", "CH5"))
        self.label_ch6.setText(_translate("MainWindow", "CH6"))
        self.label_ch7.setText(_translate("MainWindow", "CH7"))
        self.label_ch8.setText(_translate("MainWindow", "CH8"))

        
        #Result區 各個Channel回讀PASS或FAIL
        self.label1.setText(_translate("MainWindow", ""))
        self.label2.setText(_translate("MainWindow", ""))
        self.label3.setText(_translate("MainWindow", ""))
        self.label4.setText(_translate("MainWindow", ""))
        self.label5.setText(_translate("MainWindow", ""))
        self.label6.setText(_translate("MainWindow", ""))
        self.label7.setText(_translate("MainWindow", ""))
        self.label8.setText(_translate("MainWindow", ""))


        self.ch1_qrcode.setText(_translate("MainWindow", "檢測ch1"))
        self.ch2_qrcode.setText(_translate("MainWindow", "檢測ch2"))
        self.ch3_qrcode.setText(_translate("MainWindow", "檢測ch3"))
        self.ch4_qrcode.setText(_translate("MainWindow", "檢測ch4"))
        self.ch5_qrcode.setText(_translate("MainWindow", "檢測ch5"))
        self.ch6_qrcode.setText(_translate("MainWindow", "檢測ch6"))
        self.ch7_qrcode.setText(_translate("MainWindow", "檢測ch7"))
        self.ch8_qrcode.setText(_translate("MainWindow", "檢測ch8"))


        self.groupBox.setTitle(_translate("MainWindow", "Output"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
