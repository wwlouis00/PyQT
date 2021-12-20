from PyQt5.QtWidgets import QDialog,QApplication,QFileDialog
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import matplotlib.pyplot as plt
import time
import datetime
from datetime import datetime, timedelta
from pyzbar import pyzbar
import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsPixmapItem
from PyQt5 import QtCore, QtGui, QtWidgets
now_output_time = str(datetime.now().strftime('%Y-%m-%d %H-%M-%S'))

class Ui_MainWindow(QtWidgets.QWidget):
    def browsefile(self):
        self.fname = QFileDialog.getOpenFileName(self, '開啟csv檔案', 'C:\Program Files (x86)', 'csv files (*.csv)')
        self.Input_file.setText(self.fname[0])
        # global self.df_raw, df_ifc, df_normalization
        self.df_raw = pd.read_csv(self.fname[0])
        self.df_ifc = pd.read_csv("cali_factor.csv")
        self.df_normalization = self.df_raw.copy()
        self.get_accumulation_time()
        self.normalize()
        threshold_value = self.get_ct_threshold()
        Ct_value = self.get_ct_value(threshold_value)
        # self.save_excel = pd.DataFrame({"well_1": [Ct_value[0]], "well_2": [Ct_value[1]], "well_3": [Ct_value[2]],
        #                            "well_4": [Ct_value[3]],
        #                            "well_5": [Ct_value[4]], "well_6": [Ct_value[5]], "well_7": [Ct_value[6]],
        #                            "well_8": [Ct_value[7]],
        #                            "well_9": [Ct_value[8]], "well_10": [Ct_value[9]], "well_11": [Ct_value[10]],
        #                            "well_4": [Ct_value[11]],
        #                            "well_13": [Ct_value[12]], "well_14": [Ct_value[13]], "well_15": [Ct_value[14]],
        #                            "well_16": [Ct_value[15]]}


    # def get_accumulation_time(self):
    #     df_time = self.df_normalization['time']
    #     time_ori = datetime.strptime(df_time[0], "%H:%M:%S")
    #     time_delta = []
    #     for time in df_time:
    #         time_now = datetime.strptime(time, "%H:%M:%S")
    #         time_delta.append((time_now - time_ori).seconds / 60)
    #     self.df_normalization.insert(1, column="accumulation", value=time_delta)
    #
    # def get_StdDev_and_Avg(self):
    #     StdDev = []
    #     Avg = []
    #     for i in range(0, 16):
    #         df_current_well = self.df_normalization[f'well_{i + 1}']
    #         StdDev.append(df_current_well[8:30].std())
    #         Avg.append(df_current_well[8:30].mean())
    #     return StdDev, Avg
    #
    # def normalize(self):
    #     for i in range(0, 16):
    #         df_current_well = self.df_raw[f'well_{i + 1}']
    #         df_current_ifc = self.df_ifc[f'well{i + 1}']
    #         baseline = df_current_well[8:30].mean()
    #         self.df_normalization[f'well{i + 1}'] = (self.df_raw[f'well_{i + 1}'] - baseline) / df_current_ifc[0]  # normalized = (IF(t)-IF(b))/IFc
    #
    #
    # def get_ct_threshold(self):
    #     threshold_value = []
    #     StdDev, Avg = self.get_StdDev_and_Avg()
    #     for i in range(0, 16):
    #         threshold_value.append(10 * StdDev[i] + Avg[i])
    #         print(f"Well {i + 1}: StdDev is {StdDev[i]}, Avg is {Avg[i]}")
    #     return threshold_value

    # def get_ct_value(self,threshold_value):
    #     Ct_value = []
    #     for i in range(0, 16):
    #         df_current_well = self.df_normalization[f'well_{i + 1}']
    #         df_accumulation = self.df_normalization['accumulation']
    #         print("\n")
    #         print(df_current_well)
    #         print(f"Threshold value: {threshold_value[i]}")
    #         try:
    #             for j, row in enumerate(df_current_well):
    #                 if row >= threshold_value[i]:
    #                     print(f"row: {row}")
    #                     thres_lower = df_current_well[j - 1]
    #                     thres_upper = df_current_well[j]
    #                     acc_time_lower = df_accumulation[j - 1]
    #                     acc_time_upper = df_accumulation[j + 1]
    #
    #                     # linear regression
    #                     x2 = acc_time_upper
    #                     y2 = thres_upper
    #                     x1 = acc_time_lower
    #                     y1 = thres_lower
    #                     y = threshold_value[i]
    #                     x = (x2 - x1) * (y - y1) / (y2 - y1) + x1
    #
    #                     Ct_value.append(round(x, 2))
    #                     print(f"Ct of well_{i + 1} is {round(x, 2)}")
    #                     break
    #
    #                 # if there is no Ct_value availible
    #                 elif j == len(df_current_well) - 1:
    #                     Ct_value.append(99.99)
    #                     print("Ct value is not available")
    #         except Exception as e:
    #             print(e)
    #             Ct_value.append(99.99)
    #             print("Ct value is not available")
    #
    #     return Ct_value


    def save_file(self):
        print("good")
        self.df_raw.to_excel('./result/CT_Chart' + now_output_time+"output.xlsx", encoding="utf_8_sig")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 473)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Input_file = QtWidgets.QLineEdit(self.centralwidget)
        self.Input_file.setGeometry(QtCore.QRect(10, 18, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Input_file.setFont(font)
        self.Input_file.setObjectName("Input_file")
        self.openfile = QtWidgets.QPushButton(self.centralwidget)
        self.openfile.setGeometry(QtCore.QRect(660, 18, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.openfile.setFont(font)
        self.openfile.setObjectName("openfile")
        self.CT_chart = QtWidgets.QGraphicsView(self.centralwidget)
        self.CT_chart.setGeometry(QtCore.QRect(10, 66, 631, 373))
        self.CT_chart.setObjectName("CT_chart")
        self.savefile = QtWidgets.QPushButton(self.centralwidget)
        self.savefile.setGeometry(QtCore.QRect(660, 54, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.savefile.setFont(font)
        self.savefile.setObjectName("savefile")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(660, 132, 113, 22))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(660, 192, 113, 22))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660, 108, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(660, 168, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.openfile.clicked.connect(self.browsefile)
        self.savefile.clicked.connect(self.save_file)
        # self.df_normalization = self.df_raw.copy()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CT_Display"))
        self.openfile.setText(_translate("MainWindow", "開啟檔案"))
        self.savefile.setText(_translate("MainWindow", "儲存檔案"))
        self.label.setText(_translate("MainWindow", "開始時間"))
        self.label_2.setText(_translate("MainWindow", "結束時間"))
