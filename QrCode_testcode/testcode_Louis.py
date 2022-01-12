#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import sys
import cv2
import xlwt
import xlrd
from xlutils.copy import copy
from pyzbar import pyzbar
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QPalette, QBrush, QPixmap
import os

global number1
number1 = 1
xtime1=time.localtime()
fn= str(xtime1[0]) +"-" + str(xtime1[1]) +"-"+ str(xtime1[2]) + "-" + str(xtime1[3])+ ":" + str(xtime1[4])+'.xls'
def scan_qrcode(qrcode):
    data = pyzbar.decode(qrcode)
    return data[0].data.decode('utf-8')

class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)

        # self.face_recong = face.Recognition()
        self.timer_camera = QtCore.QTimer()
        self.cap = cv2.VideoCapture()
        self.CAM_NUM = 0
        self.set_ui()
        self.slot_init()
        self.__flag_work = 0
        self.x =0
        self.count = 0

    def set_ui(self):

        self.__layout_main = QtWidgets.QHBoxLayout()
        self.__layout_fun_button = QtWidgets.QVBoxLayout()
        self.__layout_data_show = QtWidgets.QVBoxLayout()



        self.button_open_camera = QtWidgets.QPushButton(u'開啟相機')
        self.label = QtWidgets.QLabel('以下為灰階圖片方差')
        self.label1 = QtWidgets.QLabel('機台編號:')
        self.button_close = QtWidgets.QPushButton(u'退出')
        self.button_test = QtWidgets.QPushButton(u'焦距檢測:')
        #self.button_sql = QtWidgets.QPushButton(u'開啟資料庫')
        self.button_sql1 = QtWidgets.QPushButton(u'儲存到資料庫')
        self.button_qrcode = QtWidgets.QPushButton(u'讀取QRcode')
        #self.button_test1 = QtWidgets.QPushButton(u'機台編號')
        #self.label1 =QtWidgets.QLabel('灰階圖片方差')
        self.number =QtWidgets.QLCDNumber(5)

        #Button 的顏色修改
        button_color = [self.button_open_camera, self.button_close]
        for i in range(2):
            button_color[i].setStyleSheet("QPushButton{color:black}"
                                          "QPushButton:hover{color:red}"
                                          "QPushButton{background-color:rgb(78,255,255)}"
                                          "QPushButton{border:2px}"
                                          "QPushButton{border-radius:10px}"
                                          "QPushButton{padding:2px 4px}")


        self.button_open_camera.setMinimumHeight(50)
        self.button_close.setMinimumHeight(50)
        self.button_test.setMinimumHeight(50)
        #self.button_sql.setMinimumHeight(50)
        self.button_sql1.setMinimumHeight(50)
        self.button_qrcode.setMinimumHeight(50)
        #self.button_test1.setMinimumHeight(50)
        self.label.setMinimumHeight(10)
        self.label1.setMinimumHeight(10)
        #self.label1.setMinimumHeight(50)
        self.number.setMinimumHeight(10)
        # self.button_close.move(300,300)
        # move()方法移動視窗在螢幕上的位置到x = 300，y = 300座標。
        self.move(300, 300)

        # 資訊顯示
        self.label_show_camera = QtWidgets.QLabel()
        self.label_move = QtWidgets.QLabel()
        self.label_move.setFixedSize(10, 10)

        self.label_show_camera.setFixedSize(641, 481)
        self.label_show_camera.setAutoFillBackground(False)

        self.__layout_fun_button.addWidget(self.label1)
        self.__layout_fun_button.addWidget(self.button_open_camera)
        self.__layout_fun_button.addWidget(self.label)
        #self.__layout_fun_button.addWidget(self.label1)
        #self.__layout_fun_button.addWidget(self.button_test1)
        self.__layout_fun_button.addWidget(self.number)
        self.__layout_fun_button.addWidget(self.button_test)
        self.__layout_fun_button.addWidget(self.button_qrcode)
        self.__layout_fun_button.addWidget(self.button_sql1)
        #self.__layout_fun_button.addWidget(self.button_sql)        
        self.__layout_fun_button.addWidget(self.button_close)
        self.__layout_fun_button.addWidget(self.label_move)

        self.__layout_main.addLayout(self.__layout_fun_button)
        self.__layout_main.addWidget(self.label_show_camera)

        self.setLayout(self.__layout_main)
        self.label_move.raise_()
        self.setWindowTitle(u'焦距檢測')

        '''
        # 設定背景圖片
        palette1 = QPalette()
        palette1.setBrush(self.backgroundRole(), QBrush(QPixmap('background.jpg')))
        self.setPalette(palette1)
        '''
        

    def slot_init(self):
        self.button_open_camera.clicked.connect(self.button_open_camera_click)
        self.timer_camera.timeout.connect(self.show_camera)
        self.button_close.clicked.connect(self.close)
        self.button_sql1.clicked.connect(self.button_sql1_click)
        #self.button_sql.clicked.connect(self.button_sql_click)
        self.button_qrcode.clicked.connect(self.button_qrcode_click)

    def button_open_camera_click(self):
        if self.timer_camera.isActive() == False:
            flag = self.cap.open(self.CAM_NUM)
            if flag == False:
                msg = QtWidgets.QMessageBox.warning(self, u"Warning", u"請檢測相機與電腦是否連線正確", buttons=QtWidgets.QMessageBox.Ok,
                                                defaultButton=QtWidgets.QMessageBox.Ok)
            # if msg==QtGui.QMessageBox.Cancel:
            #                     pass
            else:
                self.timer_camera.start(30)

                self.button_open_camera.setText(u'關閉相機')
        else:
            self.timer_camera.stop()
            self.cap.release()
            self.label_show_camera.clear()
            self.button_open_camera.setText(u'開啟相機')



    def show_camera(self):
        flag, self.image = self.cap.read()
        # face = self.face_detect.align(self.image)
        # if face:
        #     pass
        global show
        show = cv2.resize(self.image, (640, 480))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        
        
        gray = cv2.cvtColor(show, cv2.COLOR_BGR2GRAY)
        global fm
        fm = cv2 . Laplacian ( gray , cv2.CV_64F ) . var ( )
        fm =int(fm)
        self.number.display(fm)
        global fm1
        if(fm>100 and fm<200):
            self.button_test.setText(u'焦距檢測:自動儲存')
            self.button_test.setStyleSheet("QPushButton{color:green}")
            fm1 = "AutoSave"
        elif(fm>200):
            self.button_test.setText(u'焦距檢測:對焦成功')
            self.button_test.setStyleSheet("QPushButton{color:green}")
            fm1 = "Pass"
        else:
            self.button_test.setText(u'焦距檢測:對焦失敗')
            self.button_test.setStyleSheet("QPushButton{color:red}")
            fm1 = "Fail"
        
        '''
        text = None
        try:
            text = scan_qrcode(show)
        except Exception as e:
            pass
        if text:
            print(text)
        '''   
        

        # print(show.shape[1], show.shape[0])
        #show.shape[1] = 640, show.shape[0] = 480
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))
        # self.x += 1
        # self.label_move.move(self.x,100)

        # if self.x ==320:
        #     self.label_show_camera.raise_()


    def closeEvent(self, event):
        ok = QtWidgets.QPushButton()
        cacel = QtWidgets.QPushButton()

        msg = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, u"關閉", u"是否關閉！")

        msg.addButton(ok,QtWidgets.QMessageBox.ActionRole)
        msg.addButton(cacel, QtWidgets.QMessageBox.RejectRole)
        ok.setText(u'確定')
        cacel.setText(u'取消')
        # msg.setDetailedText('sdfsdff')
        if msg.exec_() == QtWidgets.QMessageBox.RejectRole:
            event.ignore()
        else:
            #self.socket_client.send_command(self.socket_client.current_user_command)
            if self.cap.isOpened():
                self.cap.release()
            if self.timer_camera.isActive():
                self.timer_camera.stop()
            event.accept()
    
    
    def button_sql1_click(self):

        
        global number1
        
        xtime=time.localtime()
        time1 = str(xtime[0]) +"/" + str(xtime[1]) +"/"+ str(xtime[2]) + "-" + str(xtime[3]) + ":" + str(xtime[4]) 
        #fn= str(xtime[0]) +"-" + str(xtime[1]) +"-"+ str(xtime[2]) +'.xls'
        test10= str(xtime[0]) +"-" + str(xtime[1]) +"-"+ str(xtime[2]) + "-" + str(xtime[3]) + ":" + str(xtime[4]) + "-" + str(number1) +".png"
        cv2.imwrite(test10, show)

        if number1 == 1:
            datahead=[' ','日期','相機編號','灰階圖偏方差值','對焦結果(Pass/Fail)','相機存檔檔名']            
            wb = xlwt.Workbook()
            sh=wb.add_sheet('sheet1',cell_overwrite_ok=True)
            for i in range (len(datahead)):
                sh.write(0 , i , datahead[i])
            price=[number1,time1,qrcode,fm,fm1,test10]
            for j in range (len(price)):
                sh.write(number1 ,j,price[j])
            number1 = number1+1
            wb.save(fn)
        else:
            wb = xlrd.open_workbook(fn,formatting_info=True)
            '''
            sh = wb.sheets()[0]
            price=[cool,time1,qrcode,fm,fm1,' ']
            for j in range (len(price)):
                sh.write(cool ,j,price[j])
            cool = cool+1
            '''
            wt = copy(wb)
            sheets=wt.get_sheet(0)
            price=[number1,time1,qrcode,fm,fm1,test10]
            for j in range (len(price)):
                sheets.write(number1 ,j,price[j])
            number1 = number1+1
            wt.save(fn)
        
    def button_sql_click(self):
        fn = '2021-10-15.xls'
        wb = xlrd.open_workbook(fn)
        sh = wb.sheets()[0]
        rows = sh.nrows
        for row in range(rows):
            print(sh.row_values(row))
    
    def button_qrcode_click(self):
        text = None 
        global  qrcode      
        try:
            text = scan_qrcode(show)
        except Exception as e:
            pass
        if text:
            qrcode=text
            text1="機台編號:"+text
            self.label1.setText(text1)
            print(qrcode)
    
        
if __name__ == "__main__":
    App = QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(App.exec_())
