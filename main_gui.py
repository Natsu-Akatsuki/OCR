#!/usr/bin/env python
import json
import math
import sys
import threading

from PyQt5.QtCore import (QRect, QRectF, QTimer, QObject, pyqtSlot,
                          pyqtSignal, QThread, QEventLoop)
from PyQt5.QtGui import (QColor, QFont, QImage, QPainter, QPainterPath,
                         QPixmap)
from PyQt5.QtWidgets import (QFileDialog, QMainWindow, QMessageBox, QMenu, QAction)
from PyQt5 import QtWidgets

from OCR_gui import Ui_MainWindow
from OCR_api import OCRAPI
from pathlib import Path
from word_dump import DocDump


class UI(QMainWindow, Ui_MainWindow):
    def __init__(self, OCR_api, doc_dump):
        super(UI, self).__init__()
        self.setupUi(self)
        self.connect_signal_slot()
        self.OCR_api = OCR_api
        self.doc_dump = doc_dump

        self.check_type = 0
        self.type_btn.toggled.connect(self.switch_invoice_type)

    def switch_invoice_type(self):
        self.type_btn = self.sender()
        if self.type_btn.isChecked():
            self.check_type = 0
            self.browser2.setText("已选择机打发票")
        else:
            self.check_type = 1
            self.browser2.setText("已选择增值税发票")

    def read_fund(self):
        # 记录经费来源
        self.fund_id = self.src_text.text()
        self.box1.setEnabled(False)
        self.box2.setEnabled(True)

    def reset(self):
        self.box1.setEnabled(True)
        self.box2.setEnabled(False)
        self.box3.setEnabled(False)

    def connect_signal_slot(self):
        self.confirm_btn1.clicked.connect(self.read_fund)
        self.import_file_btn.clicked.connect(self.import_file)
        self.boot_btn.clicked.connect(self.boot)
        self.reboot_btn.clicked.connect(self.reset)

    def import_file(self):
        self.ocr_file_names = QFileDialog.getOpenFileNames(self, '选择文件(可多选)', '',
                                                           'Files(*.pdf *.jpg *.gif *.png *jpeg)')[0]
        self.box3.setEnabled(True)
        browser1_text = "将导入如下文件进行识别\n"
        for file_id, file_name in enumerate(self.ocr_file_names):
            browser1_text += f"{file_id + 1}、" + file_name + "\n"

        self.browser1.setText(("%s" % browser1_text))

    def boot(self):
        result = self.OCR_api.gui_2_api(self.ocr_file_names, self.check_type)
        if isinstance(result, str):
            self.browser2.setTextColor(QColor(255, 0, 0))
            self.browser2.append("发票数据识别失败")
            self.browser2.append(result)
            return
        else:
            # self.browser2.setTextColor(QColor(0, 255, 0))
            browser2_text = f"经费来源为: {self.fund_id}\n出入库单将保存在本地目录\n"
            self.browser2.append(browser2_text)
            self.browser2.append("发票数据识别成功")
            self.doc_dump.run(result, self.fund_id)
            self.browser2.append("出入库单已生成")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    # 创建线程
    thread_OCR = QThread()
    thread_OCR.start()
    thread_DOC = QThread()
    thread_DOC.start()

    # 将QObject对象挪到该线程
    OCR_api = OCRAPI()
    OCR_api.moveToThread(thread_OCR)

    doc_dump = DocDump()
    doc_dump.moveToThread(thread_DOC)

    main_window = UI(OCR_api, doc_dump)
    main_window.show()

    app.exec_()
    sys.exit()
