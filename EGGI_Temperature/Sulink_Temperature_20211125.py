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
import numpy
import os
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


# CH_total = [i for i in range(1,sh.max_row + 1,1)]




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



        self.fname = QFileDialog.getOpenFileName(self, '開啟txt檔案', 'C:\Program Files (x86)', 'txt files (*.txt)')
        # " C:\python\Learn_Python\Temperature" 是自己的電腦位置路徑
        self.input_file.setText(self.fname[0])
        print(self.fname[0])
        self.df = pd.read_csv(self.fname[0],delimiter='\t')
        self.df.columns = ['time', 'index', 'CH1', 'CH2', 'CH3', 'CH4', 'CH5', 'CH6', 'CH7', 'CH8']
        print(self.df)
        print(len(self.df.index))
        # print(df)
        for ch in range(1, 9, 1):
            if ch == 1:
                self.CH_data = [[self.df.loc[i, 'CH' + str(ch)] for i in range(len(self.df.index))]]
            else:
                self.CH_data.append([self.df.loc[i, 'CH' + str(ch)] for i in range(len(self.df.index))])
            print("Channel now is:" + str(ch))
        print(self.CH_data[0][0])
        #存取每個Channel的值到陣列








        self.ch1_T_On.setText(str(self.CH_data[0][1]))
        self.ch1_T_Off.setText(str(self.CH_data[0][1]))
        self.ch2_T_On.setText(str(self.CH_data[1][1]))
        self.ch2_T_Off.setText(str(self.CH_data[1][1]))
        self.ch3_T_On.setText(str(self.CH_data[2][1]))
        self.ch3_T_Off.setText(str(self.CH_data[2][1]))
        self.ch4_T_On.setText(str(self.CH_data[3][1]))
        self.ch4_T_Off.setText(str(self.CH_data[4][1]))
        self.ch5_T_On.setText(str(self.CH_data[4][1]))
        self.ch5_T_Off.setText(str(self.CH_data[4][1]))
        self.ch6_T_On.setText(str(self.CH_data[5][1]))
        self.ch6_T_Off.setText(str(self.CH_data[5][1]))
        self.ch7_T_On.setText(str(self.CH_data[5][1]))
        self.ch7_T_Off.setText(str(self.CH_data[6][1]))
        self.ch8_T_On.setText(str(self.CH_data[7][1]))
        self.ch8_T_Off.setText(str(self.CH_data[7][1]))
        # for pf in range(0,8,1):
        #     if (self.CH_data[pf][0]) == -204.8:

        T = "PASS"
        F = "FAIL"
        self.TF_array = []
        #CH1PF
        if self.CH_data[0][0] == -204.8:
            self.ch1_PF.setText(F)
            self.TF_array.append(F)
        else:
            self.ch1_PF.setText(T)
            self.TF_array.append(T)
        #CH2PF
        if self.CH_data[1][0] == -204.8:
            self.ch2_PF.setText(F)
            self.TF_array.append(F)
        else:
            self.ch2_PF.setText(T)
        #CH3PF
        if self.CH_data[2][0] == -204.8:
            self.ch3_PF.setText(F)
            self.TF_array.append(F)
        else:
            self.ch3_PF.setText(T)
        #CH4PF
        if self.CH_data[3][0] == -204.8:
            self.ch4_PF.setText(F)
            self.TF_array.append(F)
        else:
            self.ch4_PF.setText(T)
            self.TF_array.append(T)
        #CH5PF
        if self.CH_data[4][0] == -204.8:
            self.ch5_PF.setText(F)
            self.TF_array.append(F)
        else:
            self.ch5_PF.setText(T)
            self.TF_array.append(T)
        #CH6PF
        if self.CH_data[5][0] == -204.8:
            self.ch6_PF.setText(F)
            self.TF_array.append(F)
        else:
            self.ch6_PF.setText(T)
            self.TF_array.append(T)
        #CH7PF
        if self.CH_data[6][0] == -204.8:
            self.ch7_PF.setText(F)
            self.TF_array.append(F)
        else:
            self.ch7_PF.setText(T)
            self.TF_array.append(T)
        #CH8PF
        if self.CH_data[7][0] == -204.8:
            self.ch8_PF.setText(F)
            self.TF_array.append(F)
        else:
            self.ch8_PF.setText(T)
            self.TF_array.append(T)
        print(self.TF_array)

    def save_log(self):
        QtWidgets.QMessageBox.warning(self, u"存取消息", u"成功存取消息", buttons=QtWidgets.QMessageBox.Ok,
                                      defaultButton=QtWidgets.QMessageBox.Ok)

        self.save_excel = pd.DataFrame({"qrcode":["1","1","1","1","1","1","1","1"],
                                        "T_On":[self.CH_data[0][0], "1", "1", "1", "1", "1", "1", "1"],
                                        "T_Off": ["1", "1", "1", "1", "1", "1", "1", "1"],
                                        "檢測結果": [self.TF_array[0], self.TF_array[1], self.TF_array[2],self.TF_array[3],self.TF_array[4], self.TF_array[5], self.TF_array[6], self.TF_array[7]]
                                       },index=['ch1', 'ch2', 'ch3', 'ch4', 'ch5', 'ch6', 'ch7', 'ch8'])
        self.save_excel.to_excel('./'+'history'+now_output_time,encoding="utf_8_sig")

    #清除介面上所有數據
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
        self.ch3_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch3_chart.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.ch3_chart.setObjectName("ch3_chart")
        self.gridLayout_3.addWidget(self.ch3_chart, 0, 2, 1, 1)
        self.ch7_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch7_chart.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.ch7_chart.setObjectName("ch7_chart")
        self.gridLayout_3.addWidget(self.ch7_chart, 2, 2, 1, 1)
        self.ch6_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch6_chart.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.ch6_chart.setObjectName("ch6_chart")
        self.gridLayout_3.addWidget(self.ch6_chart, 2, 1, 1, 1)
        self.ch1_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch1_chart.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.ch1_chart.setObjectName("ch1_chart")
        self.gridLayout_3.addWidget(self.ch1_chart, 0, 0, 1, 1)
        self.ch8_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch8_chart.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.ch8_chart.setObjectName("ch8_chart")
        self.gridLayout_3.addWidget(self.ch8_chart, 2, 3, 1, 1)
        self.ch4_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch4_chart.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.ch4_chart.setObjectName("ch4_chart")
        self.gridLayout_3.addWidget(self.ch4_chart, 0, 3, 1, 1)
        self.ch5_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch5_chart.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.ch5_chart.setObjectName("ch5_chart")
        self.gridLayout_3.addWidget(self.ch5_chart, 2, 0, 1, 1)
        self.ch2_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch2_chart.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.ch2_chart.setObjectName("ch2_chart")
        self.gridLayout_3.addWidget(self.ch2_chart, 0, 1, 1, 1)
        self.Result_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Result_box.setGeometry(QtCore.QRect(800, 90, 561, 697))
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
        self.ch6_T_Off = QtWidgets.QLineEdit(self.widget1)
        self.ch6_T_Off.setObjectName("ch6_T_Off")
        self.gridLayout.addWidget(self.ch6_T_Off, 6, 3, 1, 1)
        self.ch7_T_Off = QtWidgets.QLineEdit(self.widget1)
        self.ch7_T_Off.setObjectName("ch7_T_Off")
        self.gridLayout.addWidget(self.ch7_T_Off, 7, 3, 1, 1)
        self.ch8_T_On = QtWidgets.QLineEdit(self.widget1)
        self.ch8_T_On.setObjectName("ch8_T_On")
        self.gridLayout.addWidget(self.ch8_T_On, 8, 2, 1, 1)
        self.label_ch7 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch7.setFont(font)
        self.label_ch7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch7.setObjectName("label_ch7")
        self.gridLayout.addWidget(self.label_ch7, 7, 0, 1, 1)
        self.ch2_T_Off = QtWidgets.QLineEdit(self.widget1)
        self.ch2_T_Off.setObjectName("ch2_T_Off")
        self.gridLayout.addWidget(self.ch2_T_Off, 2, 3, 1, 1)
        self.label_qrcode = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_qrcode.setFont(font)
        self.label_qrcode.setAlignment(QtCore.Qt.AlignCenter)
        self.label_qrcode.setObjectName("label_qrcode")
        self.gridLayout.addWidget(self.label_qrcode, 0, 1, 1, 1)
        self.label_ch3 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch3.setFont(font)
        self.label_ch3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch3.setObjectName("label_ch3")
        self.gridLayout.addWidget(self.label_ch3, 3, 0, 1, 1)
        self.ch5_PF = QtWidgets.QLineEdit(self.widget1)
        self.ch5_PF.setObjectName("ch5_PF")
        self.gridLayout.addWidget(self.ch5_PF, 5, 4, 1, 1)
        self.label_ch2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch2.setFont(font)
        self.label_ch2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch2.setObjectName("label_ch2")
        self.gridLayout.addWidget(self.label_ch2, 2, 0, 1, 1)
        self.label_ch6 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch6.setFont(font)
        self.label_ch6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch6.setObjectName("label_ch6")
        self.gridLayout.addWidget(self.label_ch6, 6, 0, 1, 1)
        self.ch5_T_On = QtWidgets.QLineEdit(self.widget1)
        self.ch5_T_On.setObjectName("ch5_T_On")
        self.gridLayout.addWidget(self.ch5_T_On, 5, 2, 1, 1)
        self.ch2_PF = QtWidgets.QLineEdit(self.widget1)

        self.gridLayout.addWidget(self.ch2_PF, 2, 4, 1, 1)
        self.ch1_T_Off = QtWidgets.QLineEdit(self.widget1)
        self.ch1_T_Off.setObjectName("ch1_T_Off")
        self.gridLayout.addWidget(self.ch1_T_Off, 1, 3, 1, 1)
        self.ch3_PF = QtWidgets.QLineEdit(self.widget1)
        self.ch3_PF.setObjectName("ch3_PF")
        self.gridLayout.addWidget(self.ch3_PF, 3, 4, 1, 1)
        self.ch4_PF = QtWidgets.QLineEdit(self.widget1)

        self.gridLayout.addWidget(self.ch4_PF, 4, 4, 1, 1)
        self.ch8_PF = QtWidgets.QLineEdit(self.widget1)
        self.ch8_PF.setObjectName("ch8_PF")
        self.gridLayout.addWidget(self.ch8_PF, 8, 4, 1, 1)
        self.ch1_PF = QtWidgets.QLineEdit(self.widget1)

        self.gridLayout.addWidget(self.ch1_PF, 1, 4, 1, 1)
        self.ch6_T_On = QtWidgets.QLineEdit(self.widget1)
        self.ch6_T_On.setObjectName("ch6_T_On")
        self.gridLayout.addWidget(self.ch6_T_On, 6, 2, 1, 1)
        self.ch4_T_On = QtWidgets.QLineEdit(self.widget1)
        self.ch4_T_On.setObjectName("ch4_T_On")
        self.gridLayout.addWidget(self.ch4_T_On, 4, 2, 1, 1)
        self.ch4_T_Off = QtWidgets.QLineEdit(self.widget1)
        self.ch4_T_Off.setObjectName("ch4_T_Off")
        self.gridLayout.addWidget(self.ch4_T_Off, 4, 3, 1, 1)
        self.ch7_T_On = QtWidgets.QLineEdit(self.widget1)
        self.ch7_T_On.setObjectName("ch7_T_On")
        self.gridLayout.addWidget(self.ch7_T_On, 7, 2, 1, 1)
        self.label_ch5 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch5.setFont(font)
        self.label_ch5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch5.setObjectName("label_ch5")
        self.gridLayout.addWidget(self.label_ch5, 5, 0, 1, 1)
        self.label_ch8 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch8.setFont(font)
        self.label_ch8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch8.setObjectName("label_ch8")
        self.gridLayout.addWidget(self.label_ch8, 8, 0, 1, 1)
        self.label_ch1 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch1.setFont(font)
        self.label_ch1.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_ch1, 1, 0, 1, 1)
        self.label_T_Off = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_T_Off.setFont(font)
        self.label_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T_Off.setObjectName("label_T_Off")
        self.gridLayout.addWidget(self.label_T_Off, 0, 3, 1, 1)
        self.label_T_On_14 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_T_On_14.setFont(font)
        self.label_T_On_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T_On_14.setObjectName("label_T_On_14")
        self.gridLayout.addWidget(self.label_T_On_14, 0, 4, 1, 1)
        self.ch3_T_On = QtWidgets.QLineEdit(self.widget1)
        self.ch3_T_On.setObjectName("ch3_T_On")
        self.gridLayout.addWidget(self.ch3_T_On, 3, 2, 1, 1)
        self.ch2_qrcode = QtWidgets.QGraphicsView(self.widget1)
        self.ch2_qrcode.setObjectName("ch2_qrcode")
        self.gridLayout.addWidget(self.ch2_qrcode, 2, 1, 1, 1)
        self.ch1_qrcode = QtWidgets.QGraphicsView(self.widget1)
        self.ch1_qrcode.setObjectName("ch1_qrcode")
        self.gridLayout.addWidget(self.ch1_qrcode, 1, 1, 1, 1)
        self.ch7_PF = QtWidgets.QLineEdit(self.widget1)
        self.ch7_PF.setObjectName("ch7_PF")
        self.gridLayout.addWidget(self.ch7_PF, 7, 4, 1, 1)
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.widget1)
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.gridLayout.addWidget(self.graphicsView_8, 8, 1, 1, 1)
        self.label_ch4 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch4.setFont(font)
        self.label_ch4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch4.setObjectName("label_ch4")
        self.gridLayout.addWidget(self.label_ch4, 4, 0, 1, 1)
        self.ch1_T_On = QtWidgets.QLineEdit(self.widget1)
        self.ch1_T_On.setObjectName("ch1_T_On")
        self.gridLayout.addWidget(self.ch1_T_On, 1, 2, 1, 1)
        self.ch7_qrcode = QtWidgets.QGraphicsView(self.widget1)
        self.ch7_qrcode.setObjectName("ch7_qrcode")
        self.gridLayout.addWidget(self.ch7_qrcode, 7, 1, 1, 1)
        self.ch6_qrcode = QtWidgets.QGraphicsView(self.widget1)
        self.ch6_qrcode.setObjectName("ch6_qrcode")
        self.gridLayout.addWidget(self.ch6_qrcode, 6, 1, 1, 1)
        self.ch5_qrcode = QtWidgets.QGraphicsView(self.widget1)
        self.ch5_qrcode.setObjectName("ch5_qrcode")
        self.gridLayout.addWidget(self.ch5_qrcode, 5, 1, 1, 1)
        self.ch3_qrcode = QtWidgets.QGraphicsView(self.widget1)
        self.ch3_qrcode.setObjectName("ch3_qrcode")
        self.gridLayout.addWidget(self.ch3_qrcode, 3, 1, 1, 1)
        self.ch4_qrcode = QtWidgets.QGraphicsView(self.widget1)
        self.ch4_qrcode.setObjectName("ch4_qrcode")
        self.gridLayout.addWidget(self.ch4_qrcode, 4, 1, 1, 1)
        self.ch3_T_Off = QtWidgets.QLineEdit(self.widget1)
        self.ch3_T_Off.setObjectName("ch3_T_Off")
        self.gridLayout.addWidget(self.ch3_T_Off, 3, 3, 1, 1)
        self.ch5_T_Off = QtWidgets.QLineEdit(self.widget1)
        self.ch5_T_Off.setObjectName("ch5_T_Off")
        self.gridLayout.addWidget(self.ch5_T_Off, 5, 3, 1, 1)
        self.ch8_T_Off = QtWidgets.QLineEdit(self.widget1)
        self.ch8_T_Off.setObjectName("ch8_T_Off")
        self.gridLayout.addWidget(self.ch8_T_Off, 8, 3, 1, 1)
        self.ch2_T_On = QtWidgets.QLineEdit(self.widget1)
        self.ch2_T_On.setObjectName("ch2_T_On")
        self.gridLayout.addWidget(self.ch2_T_On, 2, 2, 1, 1)
        self.label_T_On = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_T_On.setFont(font)
        self.label_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T_On.setObjectName("label_T_On")
        self.gridLayout.addWidget(self.label_T_On, 0, 2, 1, 1)
        self.ch6_PF = QtWidgets.QLineEdit(self.widget1)
        self.ch6_PF.setObjectName("ch6_PF")
        self.gridLayout.addWidget(self.ch6_PF, 6, 4, 1, 1)
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
        # self.btn_save.clicked.connect(self.warning)
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




        self.groupBox.setTitle(_translate("MainWindow", "Output"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
