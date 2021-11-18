# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windows_tab_cam.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1076, 686)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(38)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 12, 1001, 133))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 33, 531, 67))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 0, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(550, 36, 121, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 150, 601, 355))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_8.setGeometry(QtCore.QRect(460, 282, 121, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox_2)
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
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 30, 561, 181))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_69 = QtWidgets.QWidget(self.layoutWidget1)
        self.widget_69.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.widget_69.setObjectName("widget_69")
        self.gridLayout_3.addWidget(self.widget_69, 0, 2, 1, 1)
        self.widget_86 = QtWidgets.QWidget(self.layoutWidget1)
        self.widget_86.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.widget_86.setObjectName("widget_86")
        self.gridLayout_3.addWidget(self.widget_86, 2, 2, 1, 1)
        self.widget_84 = QtWidgets.QWidget(self.layoutWidget1)
        self.widget_84.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.widget_84.setObjectName("widget_84")
        self.gridLayout_3.addWidget(self.widget_84, 2, 1, 1, 1)
        self.widget_64 = QtWidgets.QWidget(self.layoutWidget1)
        self.widget_64.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.widget_64.setObjectName("widget_64")
        self.gridLayout_3.addWidget(self.widget_64, 0, 0, 1, 1)
        self.widget_85 = QtWidgets.QWidget(self.layoutWidget1)
        self.widget_85.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.widget_85.setObjectName("widget_85")
        self.gridLayout_3.addWidget(self.widget_85, 2, 3, 1, 1)
        self.widget_68 = QtWidgets.QWidget(self.layoutWidget1)
        self.widget_68.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.widget_68.setObjectName("widget_68")
        self.gridLayout_3.addWidget(self.widget_68, 0, 3, 1, 1)
        self.widget_87 = QtWidgets.QWidget(self.layoutWidget1)
        self.widget_87.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.widget_87.setObjectName("widget_87")
        self.gridLayout_3.addWidget(self.widget_87, 2, 0, 1, 1)
        self.widget_67 = QtWidgets.QWidget(self.layoutWidget1)
        self.widget_67.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.widget_67.setObjectName("widget_67")
        self.gridLayout_3.addWidget(self.widget_67, 0, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_9.setGeometry(QtCore.QRect(330, 282, 121, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(620, 150, 391, 355))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 30, 352, 314))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setStyleSheet("color: rgb(67, 200, 98);")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_7.addWidget(self.lineEdit_15, 1, 3, 1, 1)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.gridLayout_7.addWidget(self.lineEdit_27, 4, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_7.addWidget(self.label_25, 3, 0, 1, 1)
        self.lineEdit_38 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.gridLayout_7.addWidget(self.lineEdit_38, 8, 3, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_7.addWidget(self.label_35, 7, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout_7.addWidget(self.label_34, 8, 0, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_7.addWidget(self.lineEdit_16, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_7.addWidget(self.label_10, 0, 0, 1, 1)
        self.lineEdit_41 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.gridLayout_7.addWidget(self.lineEdit_41, 5, 3, 1, 1)
        self.lineEdit_39 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.gridLayout_7.addWidget(self.lineEdit_39, 5, 1, 1, 1)
        self.lineEdit_34 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.gridLayout_7.addWidget(self.lineEdit_34, 6, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_7.addWidget(self.label_15, 0, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_7.addWidget(self.label_24, 2, 0, 1, 1)
        self.lineEdit_31 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.gridLayout_7.addWidget(self.lineEdit_31, 7, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout_7.addWidget(self.label_26, 4, 0, 1, 1)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.gridLayout_7.addWidget(self.lineEdit_26, 3, 3, 1, 1)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.gridLayout_7.addWidget(self.lineEdit_33, 6, 1, 1, 1)
        self.lineEdit_28 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.gridLayout_7.addWidget(self.lineEdit_28, 4, 2, 1, 1)
        self.lineEdit_29 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.gridLayout_7.addWidget(self.lineEdit_29, 4, 3, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_7.addWidget(self.lineEdit_7, 1, 2, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_7.addWidget(self.lineEdit_17, 2, 2, 1, 1)
        self.lineEdit_35 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.gridLayout_7.addWidget(self.lineEdit_35, 6, 3, 1, 1)
        self.lineEdit_32 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.gridLayout_7.addWidget(self.lineEdit_32, 7, 3, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout_7.addWidget(self.label_36, 6, 0, 1, 1)
        self.lineEdit_37 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.gridLayout_7.addWidget(self.lineEdit_37, 8, 2, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout_7.addWidget(self.label_37, 0, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.gridLayout_7.addWidget(self.label_20, 0, 2, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_7.addWidget(self.lineEdit_6, 1, 1, 1, 1)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.gridLayout_7.addWidget(self.lineEdit_24, 3, 1, 1, 1)
        self.lineEdit_36 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.gridLayout_7.addWidget(self.lineEdit_36, 8, 1, 1, 1)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.gridLayout_7.addWidget(self.lineEdit_25, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_30 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.gridLayout_7.addWidget(self.lineEdit_30, 7, 1, 1, 1)
        self.lineEdit_40 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.gridLayout_7.addWidget(self.lineEdit_40, 5, 2, 1, 1)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_23.setStyleSheet("color: rgb(255, 0, 0);")
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.gridLayout_7.addWidget(self.lineEdit_23, 2, 3, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.gridLayout_7.addWidget(self.label_51, 5, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 18, 101, 43))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 126, 101, 43))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 210, 101, 43))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 264, 101, 43))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 312, 101, 43))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 366, 101, 43))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.frame = QtWidgets.QFrame(self.tab_2)
        self.frame.setGeometry(QtCore.QRect(140, 18, 621, 391))
        self.frame.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhMultiLine|QtCore.Qt.ImhNoEditMenu|QtCore.Qt.ImhNoTextHandles|QtCore.Qt.ImhPreferLatin|QtCore.Qt.ImhUppercaseOnly)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QtDesigner測試"))
        self.label.setText(_translate("MainWindow", "EGGI 產測"))
        self.groupBox.setTitle(_translate("MainWindow", "Input"))
        self.label_3.setText(_translate("MainWindow", "日期"))
        self.label_2.setText(_translate("MainWindow", "操作人員"))
        self.label_5.setText(_translate("MainWindow", "TXT檔案"))
        self.pushButton.setText(_translate("MainWindow", "打開"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Picture"))
        self.pushButton_8.setText(_translate("MainWindow", "清除"))
        self.pushButton_9.setText(_translate("MainWindow", "儲存"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Result"))
        self.lineEdit_15.setText(_translate("MainWindow", "PASS"))
        self.label_25.setText(_translate("MainWindow", "CH3"))
        self.label_35.setText(_translate("MainWindow", "CH7"))
        self.label_34.setText(_translate("MainWindow", "CH8"))
        self.label_10.setText(_translate("MainWindow", "CH"))
        self.label_15.setText(_translate("MainWindow", "T_On"))
        self.label_24.setText(_translate("MainWindow", "CH2"))
        self.label_26.setText(_translate("MainWindow", "CH4"))
        self.label_36.setText(_translate("MainWindow", "CH6"))
        self.label_37.setText(_translate("MainWindow", "PASS/FAIL"))
        self.label_20.setText(_translate("MainWindow", "T_Off"))
        self.label_4.setText(_translate("MainWindow", "CH1"))
        self.lineEdit_23.setText(_translate("MainWindow", "FAIL"))
        self.label_51.setText(_translate("MainWindow", "CH5"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "溫度監控"))
        self.pushButton_2.setText(_translate("MainWindow", "開啟相機"))
        self.pushButton_3.setText(_translate("MainWindow", "焦距檢測:"))
        self.pushButton_4.setText(_translate("MainWindow", "焦距檢測:"))
        self.pushButton_5.setText(_translate("MainWindow", "讀取QRcode"))
        self.pushButton_6.setText(_translate("MainWindow", "儲存到資料ˋ庫"))
        self.pushButton_7.setText(_translate("MainWindow", "退出"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "相機"))