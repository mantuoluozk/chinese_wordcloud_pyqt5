# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ciyun.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from function import run  #导入生成词云函数
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(661, 826)
        self.imgEdit = QtWidgets.QLineEdit(Dialog)
        self.imgEdit.setGeometry(QtCore.QRect(140, 20, 331, 31))
        self.imgEdit.setObjectName("imgEdit")
        self.txtEdit = QtWidgets.QLineEdit(Dialog)
        self.txtEdit.setGeometry(QtCore.QRect(140, 80, 331, 31))
        self.txtEdit.setObjectName("txtEdit")
        self.imglabel = QtWidgets.QLabel(Dialog)
        self.imglabel.setGeometry(QtCore.QRect(40, 20, 71, 31))
        self.imglabel.setObjectName("imglabel")
        self.txtlabel = QtWidgets.QLabel(Dialog)
        self.txtlabel.setGeometry(QtCore.QRect(40, 80, 71, 31))
        self.txtlabel.setObjectName("txtlabel")
        self.run_pushButton = QtWidgets.QPushButton(Dialog)
        self.run_pushButton.setGeometry(QtCore.QRect(200, 150, 81, 31))
        self.run_pushButton.setObjectName("run_pushButton")
        self.run_pushButton.clicked.connect(self.achieve)      #定义生成词云按钮连接，调用achieve函数
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 120, 321, 21))
        self.label.setObjectName("label")
        self.resultlabel = QtWidgets.QLabel(Dialog)
        self.resultlabel.setGeometry(QtCore.QRect(20, 240, 621, 561))
        self.resultlabel.setText("")
        self.resultlabel.setObjectName("resultlabel")
        self.quit_pushButton = QtWidgets.QPushButton(Dialog)    
        self.quit_pushButton.setGeometry(QtCore.QRect(330, 150, 81, 31))
        self.quit_pushButton.setObjectName("quit_pushButton")
        self.quit_pushButton.clicked.connect(quit)             #退出按钮
        self.radioButton_1 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_1.setGeometry(QtCore.QRect(40, 140, 121, 21))
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_1.setChecked(True)                    #默认根据图片颜色生成
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(40, 170, 101, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton_img = QtWidgets.QPushButton(Dialog)
        self.pushButton_img.setGeometry(QtCore.QRect(470, 20, 71, 31))
        self.pushButton_img.setObjectName("pushButton_img")
        self.pushButton_img.clicked.connect(self.open_img)     #定义按钮连接，调用open_img函数
        self.pushButton_txt = QtWidgets.QPushButton(Dialog)
        self.pushButton_txt.setGeometry(QtCore.QRect(470, 80, 71, 31))
        self.pushButton_txt.setObjectName("pushButton_txt")
        self.pushButton_txt.clicked.connect(self.open_txt)     #定义按钮连接，调用open_txt函数

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "中文词云生成器"))
        Dialog.setWindowIcon(QtGui.QIcon('resource/icon.png'))
        self.imglabel.setText(_translate("Dialog", "图片路径(jpg,png)"))
        self.txtlabel.setText(_translate("Dialog", "文本路径(txt)"))
        self.run_pushButton.setText(_translate("Dialog", "生成词云"))
        self.label.setText(_translate("Dialog", "输入路径时，请用正斜杠，例：C:/pc/imgs/apple.png"))
        self.quit_pushButton.setText(_translate("Dialog", "退出程序"))
        self.radioButton_1.setText(_translate("Dialog", "根据图片颜色生成"))
        self.radioButton_2.setText(_translate("Dialog", "随机颜色"))
        self.pushButton_img.setText(_translate("Dialog", "打开文件"))
        self.pushButton_txt.setText(_translate("Dialog", "打开文件"))


    def open_img(self):
        # img_path = QtWidgets.QFileDialog.getExistingDirectory(None,"打开图片目录","C:/") #第一个参数设为self会报错
        fileName1 ,fileType1= QtWidgets.QFileDialog.getOpenFileNames(None,
                                "选取图片文件",
                                "C:/",
                                "All Files (*);;Text Files (*.txt)")   #设置文件扩展名过滤,注意用双分号间隔
        fileName1 = str(fileName1)
        fileName1 = fileName1[2:len(fileName1)-2]
        self.imgEdit.setText(fileName1)
        print(fileName1,fileType1)

    def open_txt(self):
        # txt_path = QtWidgets.QFileDialog.getExistingDirectory(None,"打开文本目录","C:/")
        fileName2 ,fileType2= QtWidgets.QFileDialog.getOpenFileNames(None,
                                "选取文本文件",
                                "C:/",
                                "All Files (*);;Text Files (*.txt)")   #设置文件扩展名过滤,注意用双分号间隔
        fileName2 = str(fileName2)
        fileName2 = fileName2[2:len(fileName2)-2]
        self.txtEdit.setText(fileName2)
        print(fileName2,fileType2)

    def achieve(self):
        if self.radioButton_1.isChecked():      #判断要生成那种颜色的词云
            color=1
        if self.radioButton_2.isChecked():
            color=0
        imgpath = self.imgEdit.text()           #获取图片路径
        txtpath = self.txtEdit.text()           #获取文本路径
        run(imgpath,txtpath,color)              #调用函数生成词云

        self.resultlabel.setPixmap(QtGui.QPixmap('result.png'))  #显示结果图片
        self.resultlabel.setScaledContents(True)                 #让图片适应label大小

if __name__== "__main__":
    app=QtWidgets.QApplication(sys.argv)
    widget =QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec())