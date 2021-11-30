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
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import os
import time
import datetime
from datetime import datetime, timedelta
import statistics
import numpy as np
from heapq import nsmallest
from pandas.core.indexes.base import Index
from pandas.core.series import Series
from pyzbar import pyzbar
import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsPixmapItem

now_output_time = str(datetime.now().strftime('%Y-%m-%d %H-%M-%S'))+"output.xlsx"

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
        self.qrcode_result =[]


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
                self.ch1_qrcodelable.setText(text)
                self.qrcode_result.append(text)
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
                self.ch2_qrcodelable.setText(text)
                self.qrcode_result.append(text)
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
                self.ch3_qrcodelable.setText(text)
                self.qrcode_result.append(text)
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
                self.ch4_qrcodelable.setText(text)
                self.qrcode_result.append(text)
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
                self.ch5_qrcodelable.setText(text)
                self.qrcode_result.append(text)
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
                self.ch6_qrcodelable.setText(text)
                self.qrcode_result.append(text)
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
                self.ch7_qrcodelable.setText(text)
                self.qrcode_result.append(text)
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
                self.ch8_qrcodelable.setText(text)
                self.qrcode_result.append(text)
                break
            key = cv2.waitKey(10)
            if key == ord('q'):
                break
        cv2.destroyAllWindows()

    def browsefile(self):
        self.CH1_data = []
        self.CH2_data = []
        self.CH3_data = []
        self.CH4_data = []
        self.CH5_data = []
        self.CH6_data = []
        self.CH7_data = []
        self.CH8_data = []
        self.CH_T_On = []
        self.CH_T_Off = []



        self.fname = QFileDialog.getOpenFileName(self, '開啟txt檔案', 'C:\Program Files (x86)', 'txt files (*.txt)')
        # " C:\python\Learn_Python\Temperature" 是自己的電腦位置路徑
        self.input_file.setText(self.fname[0])
        self.df = pd.read_csv(self.fname[0],delimiter='\t')
        self.df.columns = ['time', 'index', 'CH1', 'CH2', 'CH3', 'CH4', 'CH5', 'CH6', 'CH7', 'CH8']#在開啟檔案上面新增一行

        for ch in range(1, 9, 1):
            if ch == 1:
                self.CH_data = [[self.df.loc[i, 'CH' + str(ch)] for i in range(len(self.df.index))]]
            else:
                self.CH_data.append([self.df.loc[i, 'CH' + str(ch)] for i in range(len(self.df.index))])

        # 存取每個Channel的值到陣列
        for i in range(0, 8, 1):
            self.T_On_array = []
            self.T_Off_array = []
            # 對一個Channel進行資料搜尋
            for ch in range(0, len(self.df.index) - 1, 1):
                a = self.CH_data[i][ch + 1] - self.CH_data[i][ch]
                # 達成T_On條件把資料存進self.T_On_array陣列
                if a < 0 and self.CH_data[i][ch] > 109:
                    self.T_On_array.append(self.CH_data[i][ch])
                # 達成T_Off條件把資料存進self.T_Off_array陣列
                elif a > 0 and 73 < self.CH_data[i][ch] < 74:
                    self.T_Off_array.append(self.CH_data[i][ch])
            # 溫度資料發生其他狀況
            if self.CH_data[i][0] == -204.8 or self.CH_data[i][2] == self.CH_data[i][3]:
                # 如果溫度未加熱保持恆溫
                if self.CH_data[i][2] != -204.8:
                    for j in range(1, 9, 1):
                        self.T_On_array.append("恆溫")
                        self.T_Off_array.append("恆溫")
                # 如果沒有連接上
                for k in range(1, 9, 1):
                    self.T_On_array.append("None")
                    self.T_Off_array.append("None")
            self.CH_T_On.append(self.T_On_array[0])
            self.CH_T_Off.append(self.T_Off_array[0])

        # 將On跟Off陣列存取的資料對應至各個位置上
        self.ch1_T_On.setText(str(self.CH_T_On[0]))
        self.ch1_T_Off.setText(str(self.CH_T_Off[0]))
        self.ch2_T_On.setText(str(self.CH_T_On[1]))
        self.ch2_T_Off.setText(str(self.CH_T_Off[1]))
        self.ch3_T_On.setText(str(self.CH_T_On[2]))
        self.ch3_T_Off.setText(str(self.CH_T_Off[2]))
        self.ch4_T_On.setText(str(self.CH_T_On[3]))
        self.ch4_T_Off.setText(str(self.CH_T_Off[3]))
        self.ch5_T_On.setText(str(self.CH_T_On[4]))
        self.ch5_T_Off.setText(str(self.CH_T_Off[4]))
        self.ch6_T_On.setText(str(self.CH_T_On[5]))
        self.ch6_T_Off.setText(str(self.CH_T_Off[5]))
        self.ch7_T_On.setText(str(self.CH_T_On[6]))
        self.ch7_T_Off.setText(str(self.CH_T_Off[6]))
        self.ch8_T_On.setText(str(self.CH_T_On[7]))
        self.ch8_T_Off.setText(str(self.CH_T_Off[7]))
        #
        #####每個channel結果Pass或Fail
        # 資料對應
        P = "Pass"
        F = "Fail"
        N = "未連接"
        W = "未加熱"
        # 對應顏色
        T_color = "color: green;"
        F_color = "color: gray;"
        constant_color = "color: orange;"
        # 儲存結果
        self.TF_array = []
        # CH1PF
        if self.CH_T_On[0] == "None":
            self.ch1_PF.setText(N)
            self.ch1_PF.setStyleSheet(F_color)
            self.TF_array.append(N)
        else:
            self.ch1_PF.setText(P)
            self.ch1_PF.setStyleSheet(T_color)
            self.TF_array.append(P)
        # CH2PF
        if self.CH_T_On[1] == "None":
            self.ch2_PF.setText(N)
            self.ch2_PF.setStyleSheet(F_color)
            self.TF_array.append(N)
        else:
            self.ch2_PF.setText(P)
            self.ch2_PF.setStyleSheet(T_color)
            self.TF_array.append(P)
        # CH3PF
        if self.CH_T_On[2] == "None":
            self.ch3_PF.setText(N)
            self.ch3_PF.setStyleSheet(F_color)
            self.TF_array.append(N)
        else:
            self.ch3_PF.setText(P)
            self.ch3_PF.setStyleSheet(T_color)
            self.TF_array.append(P)
        # CH4PF
        if self.CH_T_On[3] == "None":
            self.ch4_PF.setText(N)
            self.ch4_PF.setStyleSheet(F_color)
            self.TF_array.append(N)
        else:
            self.ch4_PF.setText(P)
            self.ch4_PF.setStyleSheet(T_color)
            self.TF_array.append(P)
        # CH5PF
        if self.CH_T_On[4] == "None":
            self.ch5_PF.setText(N)
            self.ch5_PF.setStyleSheet(F_color)
            self.TF_array.append(N)
        else:
            self.ch5_PF.setText(P)
            self.ch5_PF.setStyleSheet(T_color)
            self.TF_array.append(P)
        # CH6PF
        if self.CH_T_On[5] == "None":
            self.ch6_PF.setText(N)
            self.ch6_PF.setStyleSheet(F_color)
            self.TF_array.append(N)
        elif self.CH_T_On[5] == "恆溫":
            self.ch6_PF.setText(W)
            self.ch6_PF.setStyleSheet(constant_color)
            self.TF_array.append(W)
        else:
            self.ch6_PF.setText(P)
            self.ch6_PF.setStyleSheet(T_color)
            self.TF_array.append(P)
        # CH7PF
        if self.CH_T_On[6] == "None":
            self.ch7_PF.setText(N)
            self.ch7_PF.setStyleSheet(F_color)
            self.TF_array.append(N)
        else:
            self.ch7_PF.setText(P)
            self.ch7_PF.setStyleSheet(T_color)
            self.TF_array.append(P)
        # CH8PF
        if self.CH_T_On[7] == "None":
            self.ch8_PF.setText(N)
            self.ch8_PF.setStyleSheet(F_color)
            self.TF_array.append(N)
        else:
            self.ch8_PF.setText(P)
            self.ch8_PF.setStyleSheet(T_color)
            self.TF_array.append(P)
        self.take_picture()
        img = cv2.imread("good.jpg")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        x = img.shape[0]
        y = img.shape[0]
        frame = QImage(img, x, y, x * 3, QImage.Format_RGB888)
        pix = QPixmap.fromImage(frame)

        self.item = QGraphicsPixmapItem(pix)
        self.scene = QGraphicsScene()
        self.scene.addItem(self.item)
        self.ch1_chart.setScene(self.scene)
        self.ch2_chart.setScene(self.scene)
        self.ch3_chart.setScene(self.scene)
        self.ch4_chart.setScene(self.scene)
        self.ch5_chart.setScene(self.scene)
        self.ch6_chart.setScene(self.scene)
        self.ch7_chart.setScene(self.scene)
        self.ch8_chart.setScene(self.scene)

    def take_picture(self):
        plt.figure(figsize=(4, 4), dpi=30, linewidth=0)
        plt.plot(len(self.df.index), self.CH_data[0][0], 'o-', color='red', label="CH1_data")  # 紅
        # plt.plot(len(self.df.index), self.CH_data[1][1], 'o-', color='orange', label="CH2_data")  # 澄
        # plt.plot(len(self.df.index), self.CH_data[2][1], 'o-', color='yellow', label="CH3_data")  # 黃
        # plt.plot(len(self.df.index), self.CH_data[3][1], 'o-', color='green', label="CH4_data")  # 綠
        # plt.plot(len(self.df.index), self.CH_data[4][1], 'o-', color='#6F00FF', label="CH5_data")  # 藍
        # plt.plot(len(self.df.index), self.CH_data[5][1], 'o-', color='m', label="CH6_data")  # 靛
        # plt.plot(len(self.df.index), self.CH_data[6][1], 'o-', color='purple', label="CH7_data")  # 紫
        # plt.plot(len(self.df.index), self.CH_data[7][1], 'o-', color='k', label="CH8_data")  # 黑
        # 設定圖範圍
        plt.xlim(0, len(self.df.index))
        plt.ylim(0, 130)
        plt.grid(True)
        plt.savefig('good.jpg')

    #儲存結果
    def save_log(self):
        QtWidgets.QMessageBox.warning(self, u"存取消息", u"成功存取消息", buttons=QtWidgets.QMessageBox.Ok,
                                      defaultButton=QtWidgets.QMessageBox.Ok)

        self.save_excel = pd.DataFrame({"qrcode": [self.qrcode_result[0], self.qrcode_result[0], self.qrcode_result[0], self.qrcode_result[0], self.qrcode_result[0], self.qrcode_result[0], "1", "1"],
                                        "T_On": [self.CH_T_On[0], self.CH_T_On[1], self.CH_T_On[2], self.CH_T_On[3],
                                                 self.CH_T_On[4], self.CH_T_On[5], self.CH_T_On[6], self.CH_T_On[7]],
                                        "T_Off": [self.CH_T_Off[0], self.CH_T_Off[1], self.CH_T_Off[2],
                                                  self.CH_T_Off[3], self.CH_T_Off[4], self.CH_T_Off[5],
                                                  self.CH_T_Off[6], self.CH_T_Off[7]],
                                        "檢測結果": [self.TF_array[0], self.TF_array[1], self.TF_array[2], self.TF_array[3],
                                                 self.TF_array[4], self.TF_array[5], self.TF_array[6], self.TF_array[7]]
                                        }, index=['Ch1', 'Ch2', 'Ch3', 'Ch4', 'Ch5', 'Ch6', 'Ch7', 'Ch8'])
        self.save_excel.to_excel('./' + 'history' + now_output_time, encoding="utf_8_sig")
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
        # #Chart
        # self.ch1_chart.setScene("")
        # self.ch2_chart.setScene("")
        # self.ch3_chart.setScene("")
        # self.ch4_chart.setScene("")
        # self.ch5_chart.setScene("")
        # self.ch6_chart.setScene("")
        # self.ch7_chart.setScene("")
        # self.ch8_chart.setScene("")


    # 顯示現在時間
    def showtime(self):
        self.time = QDateTime.currentDateTime()
        timedisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")  # 格式化一下時間
        self.time.setText(timedisplay)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1420, 788)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Input_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Input_box.setGeometry(QtCore.QRect(10, 96, 761, 175))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Input_box.setFont(font)
        self.Input_box.setStyleSheet("")
        self.Input_box.setObjectName("Input_box")
        self.btn_opentxt = QtWidgets.QPushButton(self.Input_box)
        self.btn_opentxt.setGeometry(QtCore.QRect(650, 36, 91, 43))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.btn_opentxt.setFont(font)
        self.btn_opentxt.setObjectName("btn_opentxt")
        self.btn_save = QtWidgets.QPushButton(self.Input_box)
        self.btn_save.setGeometry(QtCore.QRect(650, 78, 91, 43))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.btn_save.setFont(font)
        self.btn_save.setObjectName("btn_save")
        self.btn_clean = QtWidgets.QPushButton(self.Input_box)
        self.btn_clean.setGeometry(QtCore.QRect(650, 120, 91, 43))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.btn_clean.setFont(font)
        self.btn_clean.setObjectName("btn_clean")
        self.layoutWidget = QtWidgets.QWidget(self.Input_box)
        self.layoutWidget.setGeometry(QtCore.QRect(11, 39, 631, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_name = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_name.setFont(font)
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.gridLayout_2.addWidget(self.label_name, 0, 0, 1, 1)
        self.input_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_name.setObjectName("input_name")
        self.gridLayout_2.addWidget(self.input_name, 0, 1, 1, 1)
        self.label_datetime = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_datetime.setFont(font)
        self.label_datetime.setAlignment(QtCore.Qt.AlignCenter)
        self.label_datetime.setObjectName("label_datetime")
        self.gridLayout_2.addWidget(self.label_datetime, 0, 2, 1, 1)
        self.output_datetime = QtWidgets.QLineEdit(self.layoutWidget)
        self.output_datetime.setObjectName("output_datetime")
        self.gridLayout_2.addWidget(self.output_datetime, 0, 3, 1, 1)
        self.label_txt_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_txt_2.setFont(font)
        self.label_txt_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_txt_2.setObjectName("label_txt_2")
        self.gridLayout_2.addWidget(self.label_txt_2, 1, 0, 1, 1)
        self.input_file = QtWidgets.QLineEdit(self.layoutWidget)
        self.input_file.setObjectName("input_file")
        self.gridLayout_2.addWidget(self.input_file, 1, 1, 1, 3)
        self.EGGI_Title = QtWidgets.QLabel(self.centralwidget)
        self.EGGI_Title.setGeometry(QtCore.QRect(10, 6, 1401, 79))
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
        self.Chart_box.setGeometry(QtCore.QRect(10, 276, 761, 337))
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
        self.ch1_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch1_chart.setObjectName("ch1_chart")
        self.gridLayout_3.addWidget(self.ch1_chart, 0, 0, 1, 1)
        self.ch5_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch5_chart.setObjectName("ch5_chart")
        self.gridLayout_3.addWidget(self.ch5_chart, 1, 0, 1, 1)
        self.ch4_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch4_chart.setObjectName("ch4_chart")
        self.gridLayout_3.addWidget(self.ch4_chart, 0, 3, 1, 1)
        self.ch2_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch2_chart.setObjectName("ch2_chart")
        self.gridLayout_3.addWidget(self.ch2_chart, 0, 1, 1, 1)
        self.ch3_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch3_chart.setObjectName("ch3_chart")
        self.gridLayout_3.addWidget(self.ch3_chart, 0, 2, 1, 1)
        self.ch6_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch6_chart.setObjectName("ch6_chart")
        self.gridLayout_3.addWidget(self.ch6_chart, 1, 1, 1, 1)
        self.ch7_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch7_chart.setObjectName("ch7_chart")
        self.gridLayout_3.addWidget(self.ch7_chart, 1, 2, 1, 1)
        self.ch8_chart = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch8_chart.setObjectName("ch8_chart")
        self.gridLayout_3.addWidget(self.ch8_chart, 1, 3, 1, 1)
        self.Result_box = QtWidgets.QGroupBox(self.centralwidget)
        self.Result_box.setGeometry(QtCore.QRect(780, 90, 621, 673))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Result_box.setFont(font)
        self.Result_box.setObjectName("Result_box")
        self.layoutWidget1 = QtWidgets.QWidget(self.Result_box)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 36, 578, 355))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_T_Off = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_T_Off.setFont(font)
        self.label_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T_Off.setObjectName("label_T_Off")
        self.gridLayout.addWidget(self.label_T_Off, 0, 4, 1, 1)
        self.label_ch5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch5.setFont(font)
        self.label_ch5.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_ch5, 5, 0, 1, 1)
        self.ch2_T_Off = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch2_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch2_T_Off.setObjectName("ch2_T_Off")
        self.gridLayout.addWidget(self.ch2_T_Off, 2, 4, 1, 1)
        self.ch7_qrcode = QtWidgets.QPushButton(self.layoutWidget1)
        self.ch7_qrcode.setObjectName("ch7_qrcode")
        self.gridLayout.addWidget(self.ch7_qrcode, 7, 1, 1, 1)
        self.ch6_qrcode = QtWidgets.QPushButton(self.layoutWidget1)
        self.ch6_qrcode.setObjectName("ch6_qrcode")
        self.gridLayout.addWidget(self.ch6_qrcode, 6, 1, 1, 1)
        self.label_ch8 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch8.setFont(font)
        self.label_ch8.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_ch8, 8, 0, 1, 1)
        self.ch7_T_Off = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch7_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch7_T_Off.setObjectName("ch7_T_Off")
        self.gridLayout.addWidget(self.ch7_T_Off, 7, 4, 1, 1)
        self.label_ch3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch3.setFont(font)
        self.label_ch3.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_ch3, 3, 0, 1, 1)
        self.ch3_PF = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch3_PF.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout.addWidget(self.ch3_PF, 3, 5, 1, 1)
        self.ch2_qrcode = QtWidgets.QPushButton(self.layoutWidget1)
        self.ch2_qrcode.setObjectName("ch2_qrcode")
        self.gridLayout.addWidget(self.ch2_qrcode, 2, 1, 1, 1)
        self.ch5_PF = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch5_PF.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout.addWidget(self.ch5_PF, 5, 5, 1, 1)
        self.ch1_T_Off = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch1_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_T_Off.setObjectName("ch1_T_Off")
        self.gridLayout.addWidget(self.ch1_T_Off, 1, 4, 1, 1)
        #
        self.label_qrcode_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_qrcode_2.setFont(font)
        self.label_qrcode_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_qrcode_2.setObjectName("label_qrcode_2")
        self.gridLayout.addWidget(self.label_qrcode_2, 0, 1, 1, 1)
        self.ch8_PF = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch8_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.ch8_PF, 8, 5, 1, 1)
        #
        self.ch3_T_On = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch3_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch3_T_On.setObjectName("ch3_T_On")
        self.gridLayout.addWidget(self.ch3_T_On, 3, 3, 1, 1)
        #
        self.ch4_PF = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch4_PF.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout.addWidget(self.ch4_PF, 4, 5, 1, 1)
        self.label_ch4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch4.setFont(font)
        self.label_ch4.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.label_ch4, 4, 0, 1, 1)
        self.label_ch1 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch1.setFont(font)
        self.label_ch1.setAlignment(QtCore.Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_ch1, 1, 0, 1, 1)
        self.ch1_PF = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch1_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.ch1_PF, 1, 5, 1, 1)
        #
        self.ch3_qrcode = QtWidgets.QPushButton(self.layoutWidget1)
        self.ch3_qrcode.setObjectName("ch3_qrcode")
        self.gridLayout.addWidget(self.ch3_qrcode, 3, 1, 1, 1)
        #
        self.label_ch2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch2.setFont(font)
        self.label_ch2.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.label_ch2, 2, 0, 1, 1)
        #
        self.ch8_T_Off = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch8_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch8_T_Off.setObjectName("ch8_T_Off")
        self.gridLayout.addWidget(self.ch8_T_Off, 8, 4, 1, 1)
        #
        self.ch7_T_On = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch7_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch7_T_On.setObjectName("ch7_T_On")
        self.gridLayout.addWidget(self.ch7_T_On, 7, 3, 1, 1)
        #
        self.ch5_qrcode = QtWidgets.QPushButton(self.layoutWidget1)
        self.ch5_qrcode.setObjectName("ch5_qrcode")
        self.gridLayout.addWidget(self.ch5_qrcode, 5, 1, 1, 1)
        #
        self.ch4_qrcode = QtWidgets.QPushButton(self.layoutWidget1)
        self.ch4_qrcode.setObjectName("ch4_qrcode")
        self.gridLayout.addWidget(self.ch4_qrcode, 4, 1, 1, 1)
        #
        self.ch4_T_Off = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch4_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch4_T_Off.setObjectName("ch4_T_Off")
        self.gridLayout.addWidget(self.ch4_T_Off, 4, 4, 1, 1)
        #
        self.ch2_PF = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch2_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.ch2_PF, 2, 5, 1, 1)
        #
        self.ch1_qrcode = QtWidgets.QPushButton(self.layoutWidget1)
        self.ch1_qrcode.setObjectName("ch1_qrcode")
        self.gridLayout.addWidget(self.ch1_qrcode, 1, 1, 1, 1)
        #
        self.ch3_T_Off = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch3_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch3_T_Off.setObjectName("ch3_T_Off")
        self.gridLayout.addWidget(self.ch3_T_Off, 3, 4, 1, 1)
        #
        self.ch6_T_Off = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch6_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch6_T_Off.setObjectName("ch6_T_Off")
        self.gridLayout.addWidget(self.ch6_T_Off, 6, 4, 1, 1)
        #
        self.ch6_PF = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch6_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.ch6_PF, 6, 5, 1, 1)
        self.ch5_T_Off = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch5_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch5_T_Off.setObjectName("ch5_T_Off")
        self.gridLayout.addWidget(self.ch5_T_Off, 5, 4, 1, 1)
        #
        self.label_qrcode = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_qrcode.setFont(font)
        self.label_qrcode.setAlignment(QtCore.Qt.AlignCenter)
        self.label_qrcode.setObjectName("label_qrcode")
        self.gridLayout.addWidget(self.label_qrcode, 0, 2, 1, 1)
        self.ch1_qrcodelable = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch1_qrcodelable.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_qrcodelable.setObjectName("ch1_qrcodelable")
        self.gridLayout.addWidget(self.ch1_qrcodelable, 1, 2, 1, 1)
        self.label_ch7 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch7.setFont(font)
        self.label_ch7.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.label_ch7, 7, 0, 1, 1)
        #
        self.label_ch6 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch6.setFont(font)
        self.label_ch6.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.label_ch6, 6, 0, 1, 1)
        #
        self.ch4_T_On = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch4_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch4_T_On.setObjectName("ch4_T_On")
        self.gridLayout.addWidget(self.ch4_T_On, 4, 3, 1, 1)
        #
        self.label_T_On = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_T_On.setFont(font)
        self.label_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T_On.setObjectName("label_T_On")
        self.gridLayout.addWidget(self.label_T_On, 0, 3, 1, 1)
        #
        self.ch7_PF = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch7_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.ch7_PF, 7, 5, 1, 1)
        #
        self.ch5_T_On = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch5_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch5_T_On.setObjectName("ch5_T_On")
        self.gridLayout.addWidget(self.ch5_T_On, 5, 3, 1, 1)
        #
        self.ch6_T_On = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch6_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch6_T_On.setObjectName("ch6_T_On")
        self.gridLayout.addWidget(self.ch6_T_On, 6, 3, 1, 1)
        #
        self.ch8_qrcode = QtWidgets.QPushButton(self.layoutWidget1)
        self.ch8_qrcode.setObjectName("ch8_qrcode")
        self.gridLayout.addWidget(self.ch8_qrcode, 8, 1, 1, 1)
        #
        self.label_T_On_14 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_T_On_14.setFont(font)
        self.label_T_On_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T_On_14.setObjectName("label_T_On_14")
        self.gridLayout.addWidget(self.label_T_On_14, 0, 5, 1, 1)
        #
        self.ch1_T_On = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch1_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_T_On.setObjectName("ch1_T_On")
        self.gridLayout.addWidget(self.ch1_T_On, 1, 3, 1, 1)
        #
        self.ch2_T_On = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch2_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch2_T_On.setObjectName("ch2_T_On")
        self.gridLayout.addWidget(self.ch2_T_On, 2, 3, 1, 1)
        #
        self.ch8_T_On = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch8_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch8_T_On.setObjectName("ch8_T_On")
        self.gridLayout.addWidget(self.ch8_T_On, 8, 3, 1, 1)
        self.ch2_qrcodelable = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch2_qrcodelable.setAlignment(QtCore.Qt.AlignCenter)
        self.ch2_qrcodelable.setObjectName("ch2_qrcodelable")
        self.gridLayout.addWidget(self.ch2_qrcodelable, 2, 2, 1, 1)
        self.ch3_qrcodelable = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch3_qrcodelable.setAlignment(QtCore.Qt.AlignCenter)
        self.ch3_qrcodelable.setObjectName("ch3_qrcodelable")
        self.gridLayout.addWidget(self.ch3_qrcodelable, 3, 2, 1, 1)
        self.ch4_qrcodelable = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch4_qrcodelable.setAlignment(QtCore.Qt.AlignCenter)
        self.ch4_qrcodelable.setObjectName("ch4_qrcodelable")
        self.gridLayout.addWidget(self.ch4_qrcodelable, 4, 2, 1, 1)
        self.ch6_qrcodelable = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch6_qrcodelable.setAlignment(QtCore.Qt.AlignCenter)
        self.ch6_qrcodelable.setObjectName("ch6_qrcodelable")
        self.gridLayout.addWidget(self.ch6_qrcodelable, 5, 2, 1, 1)
        self.ch6_qrcodelable_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch6_qrcodelable_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ch6_qrcodelable_2.setObjectName("ch6_qrcodelable_2")
        self.gridLayout.addWidget(self.ch6_qrcodelable_2, 6, 2, 1, 1)
        self.ch7_qrcodelable = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch7_qrcodelable.setAlignment(QtCore.Qt.AlignCenter)
        self.ch7_qrcodelable.setObjectName("ch7_qrcodelable")
        self.gridLayout.addWidget(self.ch7_qrcodelable, 7, 2, 1, 1)
        self.ch8_qrcodelable = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch8_qrcodelable.setAlignment(QtCore.Qt.AlignCenter)
        self.ch8_qrcodelable.setObjectName("ch8_qrcodelable")
        self.gridLayout.addWidget(self.ch8_qrcodelable, 8, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 612, 761, 151))
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

        # ch_PF
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
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.ch1_qrcode.clicked.connect(self.qrcode1)
        self.ch2_qrcode.clicked.connect(self.qrcode2)
        self.ch3_qrcode.clicked.connect(self.qrcode3)
        self.ch4_qrcode.clicked.connect(self.qrcode4)
        self.ch5_qrcode.clicked.connect(self.qrcode5)
        self.ch6_qrcode.clicked.connect(self.qrcode6)
        self.ch7_qrcode.clicked.connect(self.qrcode7)
        self.ch8_qrcode.clicked.connect(self.qrcode8)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # -------------------------Input區-----------------------------------
        MainWindow.setWindowTitle(_translate("MainWindow", "溫度監控程式"))
        self.Input_box.setTitle(_translate("MainWindow", "Input"))
        self.btn_opentxt.setText(_translate("MainWindow", "打開"))
        self.btn_save.setText(_translate("MainWindow", "儲存"))
        self.btn_clean.setText(_translate("MainWindow", "清除"))
        self.label_name.setText(_translate("MainWindow", "操作人員"))
        self.label_datetime.setText(_translate("MainWindow", "日期"))
        self.label_txt_2.setText(_translate("MainWindow", "TXT檔案"))
        self.EGGI_Title.setText(_translate("MainWindow", "EGGI 產測"))
        self.Chart_box.setTitle(_translate("MainWindow", "Chart"))

        # -------------------------Result區-----------------------------------
        self.Result_box.setTitle(_translate("MainWindow", "Result"))
        # Result區 項目欄的文字

        # Result區 各個Channel的文字
        self.label_ch1.setText(_translate("MainWindow", "CH1"))
        self.label_ch2.setText(_translate("MainWindow", "CH2"))
        self.label_ch3.setText(_translate("MainWindow", "CH3"))
        self.label_ch4.setText(_translate("MainWindow", "CH4"))
        self.label_ch5.setText(_translate("MainWindow", "CH5"))
        self.label_ch6.setText(_translate("MainWindow", "CH6"))
        self.label_ch7.setText(_translate("MainWindow", "CH7"))
        self.label_ch8.setText(_translate("MainWindow", "CH8"))
        # Result區 各個Channel回讀PASS或FAIL
        self.label_T_Off.setText(_translate("MainWindow", "T_Off"))
        # Result區 各個Channel檢測按鈕的文字
        self.ch1_qrcode.setText(_translate("MainWindow", "檢測CH1"))
        self.ch2_qrcode.setText(_translate("MainWindow", "檢測CH2"))
        self.ch3_qrcode.setText(_translate("MainWindow", "檢測CH3"))
        self.ch4_qrcode.setText(_translate("MainWindow", "檢測CH4"))
        self.ch5_qrcode.setText(_translate("MainWindow", "檢測CH5"))
        self.ch6_qrcode.setText(_translate("MainWindow", "檢測CH6"))
        self.ch7_qrcode.setText(_translate("MainWindow", "檢測CH7"))
        self.ch8_qrcode.setText(_translate("MainWindow", "檢測CH8"))




        self.label_qrcode_2.setText(_translate("MainWindow", "READ"))







        self.label_qrcode.setText(_translate("MainWindow", "QRCODE"))


        self.label_T_On.setText(_translate("MainWindow", "T_On"))

        self.label_T_On_14.setText(_translate("MainWindow", "PASS/FAIL"))
        self.groupBox.setTitle(_translate("MainWindow", "Output"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))