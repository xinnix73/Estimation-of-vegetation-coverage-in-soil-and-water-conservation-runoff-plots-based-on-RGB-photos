#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np                            
import os   
import pandas as pd
import sys
import openpyxl



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1117, 728)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 531, 571))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 80, 561, 571))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 20, 131, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(590, 10, 131, 51))
        self.label_3.setStyleSheet("font: 16pt \"黑体\";")
        self.label_3.setObjectName("label_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(880, 20, 101, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 650, 101, 41))
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(730, 10, 141, 51))
        self.label_5.setStyleSheet("font: 14pt \"黑体\";")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1011, 650, 101, 41))
        self.label_6.setObjectName("label_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(1000, 20, 101, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 20, 431, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_5.clicked.connect(self.bt5)
        
        self.pushButton.clicked.connect(self.bt1)
        
        self.pushButton_3.clicked.connect(self.bt3)
        
        self.pushButton_2.clicked.connect(self.bt2)
        
        self.pushButton_4.clicked.connect(self.bt4)
        
        self.pushButton_6.clicked.connect(self.bt6)
        
        self.pushButton_7.clicked.connect(self.bt7)
        
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
    np.seterr(invalid='ignore')    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "径流小区植被覆盖度估算软件(吉林农业大学资源与环境学院）"))
        self.pushButton_5.setText(_translate("MainWindow", "选择文件"))
        self.label_3.setText(_translate("MainWindow", "计算结果:   "))
        self.pushButton_6.setText(_translate("MainWindow", "批量选择"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">源文件</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">二值图</span></p></body></html>"))
        self.pushButton_7.setText(_translate("MainWindow", "导出"))
        self.pushButton.setText(_translate("MainWindow", "EXG"))
        self.pushButton_3.setText(_translate("MainWindow", "GLI"))
        self.pushButton_2.setText(_translate("MainWindow", "EXG-EXR"))
        self.pushButton_4.setText(_translate("MainWindow", "RVBVI"))
    
    def bt5(self):
        global fname
        fname,_=QtWidgets.QFileDialog.getOpenFileName(self, '打开文件')
        self.label.setPixmap(QtGui.QPixmap(fname))
        self.label.setScaledContents (True)
    
    def bt1(self):
        image=cv2.imread(fname)
        a = np.array(image, dtype=np.float32) 
        (b, g, r) = cv2.split(a)
        EXG=2*g-r-b
        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(EXG)
        EXG_u8 = np.array((EXG - minVal) / (maxVal - minVal)* 255, dtype=np.uint8)
        (thresh, otus) = cv2.threshold(EXG_u8, 0, 255, cv2.THRESH_OTSU)
        b, c = cv2.findContours(otus, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#cv2.RETR_TREE
        # 这段是将转ndarray数组换成可以先是在label上的Qimage 
        #img=cv2.resize(src=otus,dsize=None,fx=0.2,fy=0.2)
        img=cv2.resize(src=otus, dsize=None, fx=0.2, fy=0.2)
        img2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.final_image = QtGui.QImage(img2[:],img2.shape[1], img2.shape[0],img2.shape[1] * 3, QtGui.QImage.Format_RGB888)                      
        #
        self.label_2.setPixmap(QtGui.QPixmap(self.final_image))
        self.label_2.setScaledContents (True)
        area = 0
        a1 = image.shape
        for i in range(0, len(b)):
            cnt = b[i]
            area += cv2.contourArea(cnt)
        v = area/(a1[0]*a1[1])
        v = round(v, 5)
        self.label_5.setText(str(v))
    
    def bt3(self):
        image = cv2.imread(fname)
        i = np.array(image, dtype=np.float32)
        (b, g, r) = cv2.split(i)
        GLI = (2*g-r-b)/(2*g+r+b)
        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(GLI)
        GLI_u8 = np.array((GLI- minVal) / (maxVal - minVal)*255, dtype=np.uint8)
        (thresh, otus) = cv2.threshold(GLI_u8, 0, 255, cv2.THRESH_OTSU)
        b, c = cv2.findContours(otus, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#cv2.RETR_TREE
        img=cv2.resize(src=otus,dsize=None,fx=0.2,fy=0.2)
        img2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.final_image = QtGui.QImage(img2[:],img2.shape[1], img2.shape[0],img2.shape[1] * 3, QtGui.QImage.Format_RGB888)
        self.label_2.setPixmap(QtGui.QPixmap(self.final_image))
        self.label_2.setScaledContents (True)
        z = GLI.shape
        area = 0
        for i in range(0, len(b)):
            cnt = b[i]
            area += cv2.contourArea(cnt)
        v = area/(z[0]*z[1])
        self.label_5.setText(str(v))
        
    def bt2(self):
        image = cv2.imread(fname)
        i = np.array(image, dtype=np.float32)#
        (b, g, r) = cv2.split(i)
        EXG_EXR = 3*g-2.4*r-b
        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(EXG_EXR)
        EXG_EXR_u8 = np.array((EXG_EXR - minVal) / (maxVal - minVal)* 255, dtype=np.uint8)
        (thresh, otus) = cv2.threshold(EXG_EXR_u8, 0, 255, cv2.THRESH_OTSU)
        b, c = cv2.findContours(otus, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#cv2.RETR_TREE
        img=cv2.resize(src=otus,dsize=None,fx=0.2,fy=0.2)
        img2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.final_image = QtGui.QImage(img2[:],img2.shape[1], img2.shape[0],img2.shape[1] * 3, QtGui.QImage.Format_RGB888)
        self.label_2.setPixmap(QtGui.QPixmap(self.final_image))
        self.label_2.setScaledContents (True)
        z = image.shape
        area = 0
        for i in range(0, len(b)):
            cnt = b[i]
            area += cv2.contourArea(cnt)
        a1 = image.shape
        v = area/(z[0]*z[1])
        self.label_5.setText(str(v))
        
    def bt4(self):
        image = cv2.imread(fname)
        i = np.array(image, dtype=np.float32)
        (b, g, r) = cv2.split(i)
        cha = (2*g-r-b)/(2*g+r+b)
        lv = 3*g-2.4*r-b
        xin = (cha*lv)**0.5
        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(xin)
        xinf = np.array((xin- minVal) / (maxVal - minVal)*255, dtype=np.uint8)
        (thresh, otus) = cv2.threshold(xinf, -255, 255, cv2.THRESH_OTSU)
        b, c = cv2.findContours(otus, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #cv2.RETR_TREE
        img=cv2.resize(src=otus,dsize=None,fx=0.2,fy=0.2)
        img2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.final_image = QtGui.QImage(img2[:],img2.shape[1], img2.shape[0],img2.shape[1] * 3, QtGui.QImage.Format_RGB888)
        self.label_2.setPixmap(QtGui.QPixmap(self.final_image))
        self.label_2.setScaledContents (True)
        z = image.shape
        area = 0
        for i in range(0, len(b)):
            cnt = b[i]
            area += cv2.contourArea(cnt)
        v = area/(z[0]*z[1])
        self.label_5.setText(str(v))
        
    def bt6(self):
        global final_data
        def EXG(lujing):
            image=cv2.imread(lujing)
            a = np.array(image, dtype=np.float32) 
            (b, g, r) = cv2.split(a)
            EXG=2*g-r-b
            (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(EXG)
            EXG_u8 = np.array((EXG - minVal) / (maxVal - minVal)* 255, dtype=np.uint8)
            (thresh, otus) = cv2.threshold(EXG_u8, 0, 255, cv2.THRESH_OTSU)
            b, c = cv2.findContours(otus, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            area = 0
            a1 = image.shape
            for i in range(0, len(b)):
                cnt = b[i]
                area += cv2.contourArea(cnt)
            v1 = area/(a1[0]*a1[1])
            return v1
        def GLI(lujing): 
            image = cv2.imread(lujing)
            i = np.array(image, dtype=np.float32)
            (b, g, r) = cv2.split(i)
            GLI = (2*g-r-b)/(2*g+r+b)
            (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(GLI)
            GLI_u8 = np.array((GLI- minVal) / (maxVal - minVal)*255, dtype=np.uint8)
            (thresh, otus) = cv2.threshold(GLI_u8, 0, 255, cv2.THRESH_OTSU)
            b, c = cv2.findContours(otus, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            z = image.shape
            area = 0
            for i in range(0, len(b)):
                cnt = b[i]
                area += cv2.contourArea(cnt)
            v2 = area/(z[0]*z[1])
            return v2 
        def EXG_EXR(lujing):
            image = cv2.imread(lujing)
            i = np.array(image, dtype=np.float32)#
            (b, g, r) = cv2.split(i)
            EXG_EXR = 3*g-2.4*r-b
            (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(EXG_EXR)
            EXG_EXR_u8 = np.array((EXG_EXR - minVal) / (maxVal - minVal)* 255, dtype=np.uint8)
            (thresh, otus) = cv2.threshold(EXG_EXR_u8, 0, 255, cv2.THRESH_OTSU)
            b, c = cv2.findContours(otus, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#cv2.RETR_TREE
            z = image.shape
            area = 0
            for i in range(0, len(b)):
                cnt = b[i]
                area += cv2.contourArea(cnt)
            a1 = image.shape
            v3 = area/(z[0]*z[1])
            return v3
        def RVBVI(lujing):
            image = cv2.imread(lujing)
            i = np.array(image, dtype=np.float32)
            (b, g, r) = cv2.split(i)
            cha = (2*g-r-b)/(2*g+r+b)
            lv = 3*g-2.4*r-b
            xin = (cha*lv)**0.5
            (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(xin)
            xinf = np.array((xin- minVal) / (maxVal - minVal)*255, dtype=np.uint8)
            (thresh, otus) = cv2.threshold(xinf, -255, 255, cv2.THRESH_OTSU)
            b, c = cv2.findContours(otus, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            z = image.shape
            area = 0
            for i in range(0, len(b)):
                cnt = b[i]
                area += cv2.contourArea(cnt)
            v4 = area/(z[0]*z[1])
            return v4        
        path,p = QtWidgets.QFileDialog.getOpenFileNames()  
        data1, data2, data3, data4, data5, final_index=[], [], [], [], [],[]
        for x in path:
            d1=EXG(x)
            data1.append(d1)
            d2=GLI(x)
            data2.append(d2)
            d3=EXG_EXR(x)
            data3.append(d3)
            d4=RVBVI(x)
            data4.append(d4)
            d5=(d1+d2+d3+d4)/4
            data5.append(d5)
            tempfilename=os.path.basename(x)
            (index, extension) = os.path.splitext(tempfilename)
            final_index.append(index)
        data={'EXG':data1
             ,'GLI':data2
             ,'EXG_EXR':data3
             ,'RVBVI':data4
             ,'均值':data5}
        final_data=pd.DataFrame(data, index=final_index)      
    def bt7(self):
        filesave, ok2 = QtWidgets.QFileDialog.getSaveFileName(self)
        filesave = filesave + '.xlsx'
        writer = pd.ExcelWriter(filesave)
        final_data.to_excel(writer)
        writer.save()
        
        writer.close()
            
class CoperQt(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = CoperQt()
    window.show()
    sys.exit(app.exec_())            


# In[ ]:





# In[ ]:




