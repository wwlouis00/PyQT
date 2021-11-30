# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sulink_Temperature_20211130.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
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
        self.ch2_char = QtWidgets.QGraphicsView(self.layoutWidget_2)
        self.ch2_char.setObjectName("ch2_char")
        self.gridLayout_3.addWidget(self.ch2_char, 0, 1, 1, 1)
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
        self.Result_box.setGeometry(QtCore.QRect(780, 90, 631, 673))
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
        self.ch5_PF = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch5_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.ch5_PF.setObjectName("ch5_PF")
        self.gridLayout.addWidget(self.ch5_PF, 5, 5, 1, 1)
        self.ch2_T_On = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch2_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch2_T_On.setObjectName("ch2_T_On")
        self.gridLayout.addWidget(self.ch2_T_On, 2, 3, 1, 1)
        self.label_qrcode = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_qrcode.setFont(font)
        self.label_qrcode.setAlignment(QtCore.Qt.AlignCenter)
        self.label_qrcode.setObjectName("label_qrcode")
        self.gridLayout.addWidget(self.label_qrcode, 0, 2, 1, 1)
        self.ch3_T_Off = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch3_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch3_T_Off.setObjectName("ch3_T_Off")
        self.gridLayout.addWidget(self.ch3_T_Off, 3, 4, 1, 1)
        self.ch6_T_Off = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch6_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch6_T_Off.setObjectName("ch6_T_Off")
        self.gridLayout.addWidget(self.ch6_T_Off, 6, 4, 1, 1)
        self.ch7_T_On = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch7_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch7_T_On.setObjectName("ch7_T_On")
        self.gridLayout.addWidget(self.ch7_T_On, 7, 3, 1, 1)
        self.label_T_Off = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_T_Off.setFont(font)
        self.label_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T_Off.setObjectName("label_T_Off")
        self.gridLayout.addWidget(self.label_T_Off, 0, 4, 1, 1)
        self.label_ch7 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch7.setFont(font)
        self.label_ch7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch7.setObjectName("label_ch7")
        self.gridLayout.addWidget(self.label_ch7, 7, 0, 1, 1)
        self.ch4_T_On = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch4_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch4_T_On.setObjectName("ch4_T_On")
        self.gridLayout.addWidget(self.ch4_T_On, 4, 3, 1, 1)
        self.ch8_T_On = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch8_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch8_T_On.setObjectName("ch8_T_On")
        self.gridLayout.addWidget(self.ch8_T_On, 8, 3, 1, 1)
        self.ch7_PF = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch7_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.ch7_PF.setObjectName("ch7_PF")
        self.gridLayout.addWidget(self.ch7_PF, 7, 5, 1, 1)
        self.label_ch1 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch1.setFont(font)
        self.label_ch1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch1.setObjectName("label_ch1")
        self.gridLayout.addWidget(self.label_ch1, 1, 0, 1, 1)
        self.ch3_T_On = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch3_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch3_T_On.setObjectName("ch3_T_On")
        self.gridLayout.addWidget(self.ch3_T_On, 3, 3, 1, 1)
        self.ch1_T_On = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch1_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_T_On.setObjectName("ch1_T_On")
        self.gridLayout.addWidget(self.ch1_T_On, 1, 3, 1, 1)
        self.label_ch3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch3.setFont(font)
        self.label_ch3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch3.setObjectName("label_ch3")
        self.gridLayout.addWidget(self.label_ch3, 3, 0, 1, 1)
        self.ch6_PF = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch6_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.ch6_PF.setObjectName("ch6_PF")
        self.gridLayout.addWidget(self.ch6_PF, 6, 5, 1, 1)
        self.ch7_T_Off = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch7_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch7_T_Off.setObjectName("ch7_T_Off")
        self.gridLayout.addWidget(self.ch7_T_Off, 7, 4, 1, 1)
        self.ch5_T_Off = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch5_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch5_T_Off.setObjectName("ch5_T_Off")
        self.gridLayout.addWidget(self.ch5_T_Off, 5, 4, 1, 1)
        self.ch8_PF = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch8_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.ch8_PF.setObjectName("ch8_PF")
        self.gridLayout.addWidget(self.ch8_PF, 8, 5, 1, 1)
        self.ch8_T_Off = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch8_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch8_T_Off.setObjectName("ch8_T_Off")
        self.gridLayout.addWidget(self.ch8_T_Off, 8, 4, 1, 1)
        self.label_ch8 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch8.setFont(font)
        self.label_ch8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch8.setObjectName("label_ch8")
        self.gridLayout.addWidget(self.label_ch8, 8, 0, 1, 1)
        self.ch1_PF = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch1_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_PF.setObjectName("ch1_PF")
        self.gridLayout.addWidget(self.ch1_PF, 1, 5, 1, 1)
        self.label_T_On_14 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_T_On_14.setFont(font)
        self.label_T_On_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T_On_14.setObjectName("label_T_On_14")
        self.gridLayout.addWidget(self.label_T_On_14, 0, 5, 1, 1)
        self.ch1_T_Off = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch1_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch1_T_Off.setObjectName("ch1_T_Off")
        self.gridLayout.addWidget(self.ch1_T_Off, 1, 4, 1, 1)
        self.label_ch5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch5.setFont(font)
        self.label_ch5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch5.setObjectName("label_ch5")
        self.gridLayout.addWidget(self.label_ch5, 5, 0, 1, 1)
        self.ch3_PF = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch3_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.ch3_PF.setObjectName("ch3_PF")
        self.gridLayout.addWidget(self.ch3_PF, 3, 5, 1, 1)
        self.label_ch4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch4.setFont(font)
        self.label_ch4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch4.setObjectName("label_ch4")
        self.gridLayout.addWidget(self.label_ch4, 4, 0, 1, 1)
        self.ch6_T_On = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch6_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch6_T_On.setObjectName("ch6_T_On")
        self.gridLayout.addWidget(self.ch6_T_On, 6, 3, 1, 1)
        self.ch2_T_Off = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch2_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch2_T_Off.setObjectName("ch2_T_Off")
        self.gridLayout.addWidget(self.ch2_T_Off, 2, 4, 1, 1)
        self.ch2_PF = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch2_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.ch2_PF.setObjectName("ch2_PF")
        self.gridLayout.addWidget(self.ch2_PF, 2, 5, 1, 1)
        self.ch4_T_Off = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch4_T_Off.setAlignment(QtCore.Qt.AlignCenter)
        self.ch4_T_Off.setObjectName("ch4_T_Off")
        self.gridLayout.addWidget(self.ch4_T_Off, 4, 4, 1, 1)
        self.label_T_On = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_T_On.setFont(font)
        self.label_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.label_T_On.setObjectName("label_T_On")
        self.gridLayout.addWidget(self.label_T_On, 0, 3, 1, 1)
        self.label_ch2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch2.setFont(font)
        self.label_ch2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch2.setObjectName("label_ch2")
        self.gridLayout.addWidget(self.label_ch2, 2, 0, 1, 1)
        self.ch4_PF = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch4_PF.setAlignment(QtCore.Qt.AlignCenter)
        self.ch4_PF.setObjectName("ch4_PF")
        self.gridLayout.addWidget(self.ch4_PF, 4, 5, 1, 1)
        self.ch5_T_On = QtWidgets.QLineEdit(self.layoutWidget1)
        self.ch5_T_On.setAlignment(QtCore.Qt.AlignCenter)
        self.ch5_T_On.setObjectName("ch5_T_On")
        self.gridLayout.addWidget(self.ch5_T_On, 5, 3, 1, 1)
        self.label_ch6 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_ch6.setFont(font)
        self.label_ch6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ch6.setObjectName("label_ch6")
        self.gridLayout.addWidget(self.label_ch6, 6, 0, 1, 1)
        self.label_qrcode_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_qrcode_2.setFont(font)
        self.label_qrcode_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_qrcode_2.setObjectName("label_qrcode_2")
        self.gridLayout.addWidget(self.label_qrcode_2, 0, 1, 1, 1)
        self.ch1_qrcode = QtWidgets.QPushButton(self.layoutWidget1)
        self.ch1_qrcode.setObjectName("ch1_qrcode")
        self.gridLayout.addWidget(self.ch1_qrcode, 1, 1, 1, 1)
        self.ch2_qrcode = QtWidgets.QPushButton(self.layoutWidget1)
        self.ch2_qrcode.setObjectName("ch2_qrcode")
        self.gridLayout.addWidget(self.ch2_qrcode, 2, 1, 1, 1)
        self.ch3_qrcode = QtWidgets.QPushButton(self.layoutWidget1)
        self.ch3_qrcode.setObjectName("ch3_qrcode")
        self.gridLayout.addWidget(self.ch3_qrcode, 3, 1, 1, 1)
        self.ch4_qrcode = QtWidgets.QPushButton(self.layoutWidget1)
        self.ch4_qrcode.setObjectName("ch4_qrcode")
        self.gridLayout.addWidget(self.ch4_qrcode, 4, 1, 1, 1)
        self.ch5_qrcode = QtWidgets.QPushButton(self.layoutWidget1)
        self.ch5_qrcode.setObjectName("ch5_qrcode")
        self.gridLayout.addWidget(self.ch5_qrcode, 5, 1, 1, 1)
        self.ch6_qrcode = QtWidgets.QPushButton(self.layoutWidget1)
        self.ch6_qrcode.setObjectName("ch6_qrcode")
        self.gridLayout.addWidget(self.ch6_qrcode, 6, 1, 1, 1)
        self.ch7_qrcode = QtWidgets.QPushButton(self.layoutWidget1)
        self.ch7_qrcode.setObjectName("ch7_qrcode")
        self.gridLayout.addWidget(self.ch7_qrcode, 7, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 8, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 2, 1, 1)
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

        self.retranslateUi(MainWindow)
        self.btn_opentxt.clicked.connect(self.btn_opentxt.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        self.label_qrcode.setText(_translate("MainWindow", "QRCODE"))
        self.label_T_Off.setText(_translate("MainWindow", "T_Off"))
        self.label_ch7.setText(_translate("MainWindow", "CH7"))
        self.label_ch1.setText(_translate("MainWindow", "CH1"))
        self.label_ch3.setText(_translate("MainWindow", "CH3"))
        self.label_ch8.setText(_translate("MainWindow", "CH8"))
        self.label_T_On_14.setText(_translate("MainWindow", "PASS/FAIL"))
        self.label_ch5.setText(_translate("MainWindow", "CH5"))
        self.label_ch4.setText(_translate("MainWindow", "CH4"))
        self.label_T_On.setText(_translate("MainWindow", "T_On"))
        self.label_ch2.setText(_translate("MainWindow", "CH2"))
        self.label_ch6.setText(_translate("MainWindow", "CH6"))
        self.label_qrcode_2.setText(_translate("MainWindow", "READ"))
        self.ch1_qrcode.setText(_translate("MainWindow", "檢測CH1"))
        self.ch2_qrcode.setText(_translate("MainWindow", "檢測CH2"))
        self.ch3_qrcode.setText(_translate("MainWindow", "檢測CH3"))
        self.ch4_qrcode.setText(_translate("MainWindow", "檢測CH4"))
        self.ch5_qrcode.setText(_translate("MainWindow", "檢測CH5"))
        self.ch6_qrcode.setText(_translate("MainWindow", "檢測CH6"))
        self.ch7_qrcode.setText(_translate("MainWindow", "檢測CH7"))
        self.pushButton_8.setText(_translate("MainWindow", "檢測CH8"))
        self.groupBox.setTitle(_translate("MainWindow", "Output"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
