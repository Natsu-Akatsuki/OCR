# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OCR_gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 450)
        MainWindow.setMinimumSize(QtCore.QSize(660, 450))
        MainWindow.setMaximumSize(QtCore.QSize(660, 450))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.box1 = QtWidgets.QGroupBox(self.centralwidget)
        self.box1.setEnabled(True)
        self.box1.setGeometry(QtCore.QRect(20, 30, 291, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.box1.setFont(font)
        self.box1.setObjectName("box1")
        self.formLayoutWidget = QtWidgets.QWidget(self.box1)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 40, 261, 41))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.metadata_label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.metadata_label.setFont(font)
        self.metadata_label.setAlignment(QtCore.Qt.AlignCenter)
        self.metadata_label.setObjectName("metadata_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.metadata_label)
        self.src_text = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.src_text.setFont(font)
        self.src_text.setObjectName("src_text")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.src_text)
        self.type_btn = QtWidgets.QRadioButton(self.box1)
        self.type_btn.setGeometry(QtCore.QRect(80, 80, 211, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.type_btn.setFont(font)
        self.type_btn.setObjectName("type_btn")
        self.confirm_btn1 = QtWidgets.QPushButton(self.box1)
        self.confirm_btn1.setEnabled(True)
        self.confirm_btn1.setGeometry(QtCore.QRect(200, 110, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.confirm_btn1.setFont(font)
        self.confirm_btn1.setStyleSheet("QPushButton::enabled{ \n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.confirm_btn1.setCheckable(False)
        self.confirm_btn1.setDefault(False)
        self.confirm_btn1.setObjectName("confirm_btn1")
        self.box2 = QtWidgets.QGroupBox(self.centralwidget)
        self.box2.setEnabled(False)
        self.box2.setGeometry(QtCore.QRect(20, 200, 291, 211))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.box2.setFont(font)
        self.box2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.box2.setFlat(False)
        self.box2.setObjectName("box2")
        self.browser1 = QtWidgets.QTextBrowser(self.box2)
        self.browser1.setGeometry(QtCore.QRect(10, 40, 271, 111))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.browser1.setFont(font)
        self.browser1.setObjectName("browser1")
        self.import_file_btn = QtWidgets.QPushButton(self.box2)
        self.import_file_btn.setGeometry(QtCore.QRect(200, 160, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.import_file_btn.setFont(font)
        self.import_file_btn.setStyleSheet("QPushButton::enabled{ \n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.import_file_btn.setCheckable(False)
        self.import_file_btn.setObjectName("import_file_btn")
        self.box3 = QtWidgets.QGroupBox(self.centralwidget)
        self.box3.setEnabled(False)
        self.box3.setGeometry(QtCore.QRect(330, 30, 301, 381))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.box3.setFont(font)
        self.box3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.box3.setFlat(False)
        self.box3.setObjectName("box3")
        self.browser2 = QtWidgets.QTextBrowser(self.box3)
        self.browser2.setGeometry(QtCore.QRect(10, 40, 271, 221))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.browser2.setFont(font)
        self.browser2.setObjectName("browser2")
        self.boot_btn = QtWidgets.QPushButton(self.box3)
        self.boot_btn.setGeometry(QtCore.QRect(110, 270, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.boot_btn.setFont(font)
        self.boot_btn.setStyleSheet("QPushButton::enabled{ \n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.boot_btn.setCheckable(False)
        self.boot_btn.setObjectName("boot_btn")
        self.tip_label = QtWidgets.QLabel(self.box3)
        self.tip_label.setGeometry(QtCore.QRect(110, 350, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tip_label.setFont(font)
        self.tip_label.setObjectName("tip_label")
        self.reboot_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reboot_btn.setGeometry(QtCore.QRect(530, 300, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reboot_btn.setFont(font)
        self.reboot_btn.setStyleSheet("QPushButton::enabled{ \n"
"    background-color: white;\n"
"    color: black;\n"
"}")
        self.reboot_btn.setCheckable(False)
        self.reboot_btn.setObjectName("reboot_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OCR"))
        self.box1.setTitle(_translate("MainWindow", "入库单元数据"))
        self.metadata_label.setText(_translate("MainWindow", "经费来源"))
        self.src_text.setText(_translate("MainWindow", "1103-502190138"))
        self.type_btn.setText(_translate("MainWindow", "机打发票(on) / 增值税发票(off)"))
        self.confirm_btn1.setText(_translate("MainWindow", "确认"))
        self.box2.setTitle(_translate("MainWindow", "文件导入"))
        self.browser1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:32px; margin-bottom:14px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; background-color:#ffffff;\"><br /></p></body></html>"))
        self.import_file_btn.setText(_translate("MainWindow", "导入文件"))
        self.box3.setTitle(_translate("MainWindow", "OCR启动"))
        self.boot_btn.setText(_translate("MainWindow", "启动识别"))
        self.tip_label.setText(_translate("MainWindow", "当前OCR识别支持pdf文件与图像文件"))
        self.reboot_btn.setText(_translate("MainWindow", "重新识别"))
