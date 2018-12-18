# -*- coding: utf-8 -*-

from function import run  #导入生成词云函数
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(671, 826)
        self.imgEdit = QtWidgets.QLineEdit(Dialog)
        self.imgEdit.setGeometry(QtCore.QRect(140, 20, 311, 31))
        self.imgEdit.setObjectName("imgEdit")
        self.txtEdit = QtWidgets.QLineEdit(Dialog)
        self.txtEdit.setGeometry(QtCore.QRect(140, 80, 311, 31))
        self.txtEdit.setObjectName("txtEdit")
        self.imglabel = QtWidgets.QLabel(Dialog)
        self.imglabel.setGeometry(QtCore.QRect(40, 20, 71, 31))
        self.imglabel.setObjectName("imglabel")
        self.txtlabel = QtWidgets.QLabel(Dialog)
        self.txtlabel.setGeometry(QtCore.QRect(40, 80, 71, 31))
        self.txtlabel.setObjectName("txtlabel")
        self.run_pushButton = QtWidgets.QPushButton(Dialog)
        self.run_pushButton.setGeometry(QtCore.QRect(580, 20, 81, 31))
        self.run_pushButton.setObjectName("run_pushButton")
        self.run_pushButton.clicked.connect(self.achieve)     #定义按钮连接，调用achieve函数
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(150, 120, 321, 21))
        self.label.setObjectName("label")
        self.resultlabel = QtWidgets.QLabel(Dialog)
        self.resultlabel.setGeometry(QtCore.QRect(20, 240, 621, 561))
        self.resultlabel.setText("")
        self.resultlabel.setObjectName("resultlabel")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "中文词云生成器"))
        Dialog.setWindowIcon(QtGui.QIcon('imgs/icon.png'))
        self.imglabel.setText(_translate("Dialog", "图片绝对路径"))
        self.txtlabel.setText(_translate("Dialog", "文本绝对路径"))
        self.run_pushButton.setText(_translate("Dialog", "生成词云"))
        self.label.setText(_translate("Dialog", "输入路径时，请用正斜杠，例：C:/pc/imgs/apple.png"))

    def achieve(self):
        global imgpath
        imgpath = self.imgEdit.text()  #获取图片路径
        global txtpath 
        txtpath = self.txtEdit.text()  #获取文本路径
        run(imgpath,txtpath)           #调用函数生成词云

        self.resultlabel.setPixmap(QtGui.QPixmap('result.png'))  #显示结果图片
        self.resultlabel.setScaledContents(True)                 #让图片适应label大小

if __name__== "__main__":
    app=QtWidgets.QApplication(sys.argv)
    widget =QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec())