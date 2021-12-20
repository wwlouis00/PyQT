# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CT_Display.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1011, 539)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Input_file = QtWidgets.QLineEdit(self.centralwidget)
        self.Input_file.setGeometry(QtCore.QRect(10, 18, 641, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Input_file.setFont(font)
        self.Input_file.setObjectName("Input_file")
        self.CT_chart = QtWidgets.QGraphicsView(self.centralwidget)
        self.CT_chart.setGeometry(QtCore.QRect(10, 66, 641, 463))
        self.CT_chart.setObjectName("CT_chart")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 462, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(660, 72, 341, 69))
        self.widget.setObjectName("widget")
        self.Input_Time = QtWidgets.QGridLayout(self.widget)
        self.Input_Time.setContentsMargins(0, 0, 0, 0)
        self.Input_Time.setObjectName("Input_Time")
        self.label_Timeofbackground = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_Timeofbackground.setFont(font)
        self.label_Timeofbackground.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Timeofbackground.setObjectName("label_Timeofbackground")
        self.Input_Time.addWidget(self.label_Timeofbackground, 0, 0, 1, 3)
        self.Start_time = QtWidgets.QLineEdit(self.widget)
        self.Start_time.setAlignment(QtCore.Qt.AlignCenter)
        self.Start_time.setObjectName("Start_time")
        self.Input_Time.addWidget(self.Start_time, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.Input_Time.addWidget(self.label_7, 1, 1, 1, 1)
        self.End_time = QtWidgets.QLineEdit(self.widget)
        self.End_time.setAlignment(QtCore.Qt.AlignCenter)
        self.End_time.setObjectName("End_time")
        self.Input_Time.addWidget(self.End_time, 1, 2, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(660, 144, 341, 69))
        self.widget1.setObjectName("widget1")
        self.ThresholdBlock = QtWidgets.QGridLayout(self.widget1)
        self.ThresholdBlock.setContentsMargins(0, 0, 0, 0)
        self.ThresholdBlock.setObjectName("ThresholdBlock")
        self.label_N = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_N.setFont(font)
        self.label_N.setAlignment(QtCore.Qt.AlignCenter)
        self.label_N.setObjectName("label_N")
        self.ThresholdBlock.addWidget(self.label_N, 1, 0, 1, 1)
        self.Input_N = QtWidgets.QLineEdit(self.widget1)
        self.Input_N.setAlignment(QtCore.Qt.AlignCenter)
        self.Input_N.setObjectName("Input_N")
        self.ThresholdBlock.addWidget(self.Input_N, 1, 1, 1, 1)
        self.label_Threshold = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_Threshold.setFont(font)
        self.label_Threshold.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Threshold.setObjectName("label_Threshold")
        self.ThresholdBlock.addWidget(self.label_Threshold, 0, 0, 1, 2)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(660, 0, 341, 67))
        self.widget2.setObjectName("widget2")
        self.ButtonBlcok = QtWidgets.QGridLayout(self.widget2)
        self.ButtonBlcok.setContentsMargins(0, 0, 0, 0)
        self.ButtonBlcok.setObjectName("ButtonBlcok")
        self.btn_openfile = QtWidgets.QPushButton(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_openfile.setFont(font)
        self.btn_openfile.setObjectName("btn_openfile")
        self.ButtonBlcok.addWidget(self.btn_openfile, 0, 0, 1, 1)
        self.btn_savefile = QtWidgets.QPushButton(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_savefile.setFont(font)
        self.btn_savefile.setObjectName("btn_savefile")
        self.ButtonBlcok.addWidget(self.btn_savefile, 0, 1, 1, 1)
        self.btn_clean = QtWidgets.QPushButton(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clean.setFont(font)
        self.btn_clean.setObjectName("btn_clean")
        self.ButtonBlcok.addWidget(self.btn_clean, 0, 2, 1, 1)
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(660, 246, 341, 283))
        self.widget3.setObjectName("widget3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_well_11 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_well_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_well_11.setObjectName("lineEdit_well_11")
        self.gridLayout.addWidget(self.lineEdit_well_11, 2, 3, 1, 1)
        self.lineEdit_well_15 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_well_15.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_well_15.setObjectName("lineEdit_well_15")
        self.gridLayout.addWidget(self.lineEdit_well_15, 6, 3, 1, 1)
        self.label_well2 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_well2.setFont(font)
        self.label_well2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_well2.setObjectName("label_well2")
        self.gridLayout.addWidget(self.label_well2, 1, 0, 1, 1)
        self.lineEdit_well_10 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_well_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_well_10.setObjectName("lineEdit_well_10")
        self.gridLayout.addWidget(self.lineEdit_well_10, 1, 3, 1, 1)
        self.lineEdit_well_5 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_well_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_well_5.setObjectName("lineEdit_well_5")
        self.gridLayout.addWidget(self.lineEdit_well_5, 4, 1, 1, 1)
        self.lineEdit_well_3 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_well_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_well_3.setObjectName("lineEdit_well_3")
        self.gridLayout.addWidget(self.lineEdit_well_3, 2, 1, 1, 1)
        self.lineEdit_well_12 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_well_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_well_12.setObjectName("lineEdit_well_12")
        self.gridLayout.addWidget(self.lineEdit_well_12, 3, 3, 1, 1)
        self.lineEdit_well_4 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_well_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_well_4.setObjectName("lineEdit_well_4")
        self.gridLayout.addWidget(self.lineEdit_well_4, 3, 1, 1, 1)
        self.lineEdit_well_2 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_well_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_well_2.setObjectName("lineEdit_well_2")
        self.gridLayout.addWidget(self.lineEdit_well_2, 1, 1, 1, 1)
        self.lineEdit_well_6 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_well_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_well_6.setObjectName("lineEdit_well_6")
        self.gridLayout.addWidget(self.lineEdit_well_6, 5, 1, 1, 1)
        self.lineEdit_well_8 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_well_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_well_8.setObjectName("lineEdit_well_8")
        self.gridLayout.addWidget(self.lineEdit_well_8, 7, 1, 1, 1)
        self.label_well12 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_well12.setFont(font)
        self.label_well12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_well12.setObjectName("label_well12")
        self.gridLayout.addWidget(self.label_well12, 3, 2, 1, 1)
        self.label_well3 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_well3.setFont(font)
        self.label_well3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_well3.setObjectName("label_well3")
        self.gridLayout.addWidget(self.label_well3, 2, 0, 1, 1)
        self.label_well11 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_well11.setFont(font)
        self.label_well11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_well11.setObjectName("label_well11")
        self.gridLayout.addWidget(self.label_well11, 2, 2, 1, 1)
        self.lineEdit_well_16 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_well_16.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_well_16.setObjectName("lineEdit_well_16")
        self.gridLayout.addWidget(self.lineEdit_well_16, 7, 3, 1, 1)
        self.label_well4 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_well4.setFont(font)
        self.label_well4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_well4.setObjectName("label_well4")
        self.gridLayout.addWidget(self.label_well4, 3, 0, 1, 1)
        self.lineEdit_well_1 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_well_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_well_1.setObjectName("lineEdit_well_1")
        self.gridLayout.addWidget(self.lineEdit_well_1, 0, 1, 1, 1)
        self.lineEdit_well_9 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_well_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_well_9.setObjectName("lineEdit_well_9")
        self.gridLayout.addWidget(self.lineEdit_well_9, 0, 3, 1, 1)
        self.lineEdit_well_13 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_well_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_well_13.setObjectName("lineEdit_well_13")
        self.gridLayout.addWidget(self.lineEdit_well_13, 4, 3, 1, 1)
        self.label_well9 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_well9.setFont(font)
        self.label_well9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_well9.setObjectName("label_well9")
        self.gridLayout.addWidget(self.label_well9, 0, 2, 1, 1)
        self.label_well5 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_well5.setFont(font)
        self.label_well5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_well5.setObjectName("label_well5")
        self.gridLayout.addWidget(self.label_well5, 4, 0, 1, 1)
        self.label_well1 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_well1.setFont(font)
        self.label_well1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_well1.setObjectName("label_well1")
        self.gridLayout.addWidget(self.label_well1, 0, 0, 1, 1)
        self.lineEdit_well_14 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_well_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_well_14.setObjectName("lineEdit_well_14")
        self.gridLayout.addWidget(self.lineEdit_well_14, 5, 3, 1, 1)
        self.label_well10 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_well10.setFont(font)
        self.label_well10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_well10.setObjectName("label_well10")
        self.gridLayout.addWidget(self.label_well10, 1, 2, 1, 1)
        self.label_well6 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_well6.setFont(font)
        self.label_well6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_well6.setObjectName("label_well6")
        self.gridLayout.addWidget(self.label_well6, 5, 0, 1, 1)
        self.lineEdit_well_7 = QtWidgets.QLineEdit(self.widget3)
        self.lineEdit_well_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_well_7.setObjectName("lineEdit_well_7")
        self.gridLayout.addWidget(self.lineEdit_well_7, 6, 1, 1, 1)
        self.label_well7 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_well7.setFont(font)
        self.label_well7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_well7.setObjectName("label_well7")
        self.gridLayout.addWidget(self.label_well7, 6, 0, 1, 1)
        self.label_well8 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_well8.setFont(font)
        self.label_well8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_well8.setObjectName("label_well8")
        self.gridLayout.addWidget(self.label_well8, 7, 0, 1, 1)
        self.label_well13 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_well13.setFont(font)
        self.label_well13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_well13.setObjectName("label_well13")
        self.gridLayout.addWidget(self.label_well13, 4, 2, 1, 1)
        self.label_well14 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_well14.setFont(font)
        self.label_well14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_well14.setObjectName("label_well14")
        self.gridLayout.addWidget(self.label_well14, 5, 2, 1, 1)
        self.label_well15 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_well15.setFont(font)
        self.label_well15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_well15.setObjectName("label_well15")
        self.gridLayout.addWidget(self.label_well15, 6, 2, 1, 1)
        self.label_well16 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_well16.setFont(font)
        self.label_well16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_well16.setObjectName("label_well16")
        self.gridLayout.addWidget(self.label_well16, 7, 2, 1, 1)
        self.widget4 = QtWidgets.QWidget(self.centralwidget)
        self.widget4.setGeometry(QtCore.QRect(660, 216, 341, 32))
        self.widget4.setObjectName("widget4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget4)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_Threshold_2 = QtWidgets.QLabel(self.widget4)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_Threshold_2.setFont(font)
        self.label_Threshold_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Threshold_2.setObjectName("label_Threshold_2")
        self.gridLayout_2.addWidget(self.label_Threshold_2, 0, 0, 1, 1)
        self.label_Threshold_3 = QtWidgets.QLabel(self.widget4)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_Threshold_3.setFont(font)
        self.label_Threshold_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Threshold_3.setObjectName("label_Threshold_3")
        self.gridLayout_2.addWidget(self.label_Threshold_3, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CT_Display"))
        self.label_Timeofbackground.setText(_translate("MainWindow", "Time of background"))
        self.label_7.setText(_translate("MainWindow", "~"))
        self.label_N.setText(_translate("MainWindow", "N :"))
        self.label_Threshold.setText(_translate("MainWindow", "Threshold: N  * Std"))
        self.btn_openfile.setText(_translate("MainWindow", "開啟檔案"))
        self.btn_savefile.setText(_translate("MainWindow", "儲存檔案"))
        self.btn_clean.setText(_translate("MainWindow", "清除"))
        self.label_well2.setText(_translate("MainWindow", "well2"))
        self.label_well12.setText(_translate("MainWindow", "well12"))
        self.label_well3.setText(_translate("MainWindow", "well3"))
        self.label_well11.setText(_translate("MainWindow", "well11"))
        self.label_well4.setText(_translate("MainWindow", "well4"))
        self.label_well9.setText(_translate("MainWindow", "well9"))
        self.label_well5.setText(_translate("MainWindow", "well5"))
        self.label_well1.setText(_translate("MainWindow", "well1"))
        self.label_well10.setText(_translate("MainWindow", "well10"))
        self.label_well6.setText(_translate("MainWindow", "well6"))
        self.label_well7.setText(_translate("MainWindow", "well7"))
        self.label_well8.setText(_translate("MainWindow", "well8"))
        self.label_well13.setText(_translate("MainWindow", "well13"))
        self.label_well14.setText(_translate("MainWindow", "well14"))
        self.label_well15.setText(_translate("MainWindow", "well15"))
        self.label_well16.setText(_translate("MainWindow", "well16"))
        self.label_Threshold_2.setText(_translate("MainWindow", "CT_Value"))
        self.label_Threshold_3.setText(_translate("MainWindow", "CT_Value"))
