# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'httptool.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QStringListModel
import re
import requests
from lxml import etree
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.count = 0
        Dialog.setObjectName("Dialog")
        Dialog.resize(947, 683)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 70, 921, 201))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.get_tab = QtWidgets.QWidget()
        self.get_tab.setObjectName("get_tab")
        self.get_url_input = QtWidgets.QTextEdit(self.get_tab)
        self.get_url_input.setGeometry(QtCore.QRect(90, 10, 821, 31))
        self.get_url_input.setObjectName("get_url_input")
        self.label_3 = QtWidgets.QLabel(self.get_tab)
        self.label_3.setGeometry(QtCore.QRect(30, 15, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.get_tab)
        self.label_5.setGeometry(QtCore.QRect(20, 55, 60, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.get_header = QtWidgets.QTextEdit(self.get_tab)
        self.get_header.setGeometry(QtCore.QRect(90, 50, 821, 31))
        self.get_header.setPlaceholderText("")
        self.get_header.setObjectName("get_header")
        self.get_button = QtWidgets.QPushButton(self.get_tab)
        self.get_button.setGeometry(QtCore.QRect(800, 130, 113, 41))
        self.get_button.setDefault(False)
        self.get_button.setFlat(False)
        self.get_button.setObjectName("get_button")
        self.tabWidget.addTab(self.get_tab, "")
        self.post_tab = QtWidgets.QWidget()
        self.post_tab.setObjectName("post_tab")
        self.post_url_input = QtWidgets.QTextEdit(self.post_tab)
        self.post_url_input.setGeometry(QtCore.QRect(90, 10, 821, 31))
        self.post_url_input.setObjectName("post_url_input")
        self.label_4 = QtWidgets.QLabel(self.post_tab)
        self.label_4.setGeometry(QtCore.QRect(30, 15, 60, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.post_tab)
        self.label_6.setGeometry(QtCore.QRect(20, 55, 60, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.post_header = QtWidgets.QTextEdit(self.post_tab)
        self.post_header.setGeometry(QtCore.QRect(90, 50, 821, 31))
        self.post_header.setPlaceholderText("")
        self.post_header.setObjectName("post_header")
        self.label_10 = QtWidgets.QLabel(self.post_tab)
        self.label_10.setGeometry(QtCore.QRect(30, 90, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.post_data = QtWidgets.QTextEdit(self.post_tab)
        self.post_data.setGeometry(QtCore.QRect(90, 90, 821, 31))
        self.post_data.setObjectName("post_data")
        self.label_11 = QtWidgets.QLabel(self.post_tab)
        self.label_11.setGeometry(QtCore.QRect(90, 130, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.post_button = QtWidgets.QPushButton(self.post_tab)
        self.post_button.setGeometry(QtCore.QRect(800, 130, 113, 41))
        self.post_button.setObjectName("post_button")
        self.tabWidget.addTab(self.post_tab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(30, 90, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.patch_url_input = QtWidgets.QTextEdit(self.tab)
        self.patch_url_input.setGeometry(QtCore.QRect(90, 10, 821, 31))
        self.patch_url_input.setObjectName("patch_url_input")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(90, 130, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.patch_header = QtWidgets.QTextEdit(self.tab)
        self.patch_header.setGeometry(QtCore.QRect(90, 50, 821, 31))
        self.patch_header.setPlaceholderText("")
        self.patch_header.setObjectName("patch_header")
        self.patch_button = QtWidgets.QPushButton(self.tab)
        self.patch_button.setGeometry(QtCore.QRect(800, 130, 113, 41))
        self.patch_button.setObjectName("patch_button")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(30, 15, 60, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(20, 55, 60, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.patch_data = QtWidgets.QTextEdit(self.tab)
        self.patch_data.setGeometry(QtCore.QRect(90, 90, 821, 31))
        self.patch_data.setObjectName("patch_data")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_27 = QtWidgets.QLabel(self.tab_2)
        self.label_27.setGeometry(QtCore.QRect(20, 55, 60, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.delete_button = QtWidgets.QPushButton(self.tab_2)
        self.delete_button.setGeometry(QtCore.QRect(800, 130, 113, 41))
        self.delete_button.setObjectName("delete_button")
        self.delete_header = QtWidgets.QTextEdit(self.tab_2)
        self.delete_header.setGeometry(QtCore.QRect(90, 50, 821, 31))
        self.delete_header.setPlaceholderText("")
        self.delete_header.setObjectName("delete_header")
        self.label_28 = QtWidgets.QLabel(self.tab_2)
        self.label_28.setGeometry(QtCore.QRect(30, 15, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.delete_url_input = QtWidgets.QTextEdit(self.tab_2)
        self.delete_url_input.setGeometry(QtCore.QRect(90, 10, 821, 31))
        self.delete_url_input.setObjectName("delete_url_input")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(40, 19, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.re_input = QtWidgets.QTextEdit(self.tab_3)
        self.re_input.setGeometry(QtCore.QRect(140, 14, 651, 31))
        self.re_input.setObjectName("re_input")
        self.re_button = QtWidgets.QPushButton(self.tab_3)
        self.re_button.setGeometry(QtCore.QRect(800, 10, 91, 41))
        self.re_button.setObjectName("re_button")
        self.re_results = QtWidgets.QPlainTextEdit(self.tab_3)
        self.re_results.setGeometry(QtCore.QRect(140, 50, 651, 111))
        self.re_results.setObjectName("re_results")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.xpath_input = QtWidgets.QTextEdit(self.tab_4)
        self.xpath_input.setGeometry(QtCore.QRect(130, 13, 651, 31))
        self.xpath_input.setObjectName("xpath_input")
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setGeometry(QtCore.QRect(50, 13, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.xpath_button = QtWidgets.QPushButton(self.tab_4)
        self.xpath_button.setGeometry(QtCore.QRect(790, 10, 91, 41))
        self.xpath_button.setObjectName("xpath_button")
        self.xpath_results = QtWidgets.QPlainTextEdit(self.tab_4)
        self.xpath_results.setGeometry(QtCore.QRect(130, 53, 651, 111))
        self.xpath_results.setObjectName("xpath_results")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.css_input = QtWidgets.QTextEdit(self.tab_9)
        self.css_input.setGeometry(QtCore.QRect(150, 13, 651, 31))
        self.css_input.setObjectName("css_input")
        self.label_30 = QtWidgets.QLabel(self.tab_9)
        self.label_30.setGeometry(QtCore.QRect(50, 13, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.css_button = QtWidgets.QPushButton(self.tab_9)
        self.css_button.setGeometry(QtCore.QRect(810, 10, 81, 41))
        self.css_button.setObjectName("css_button")
        self.css_results = QtWidgets.QPlainTextEdit(self.tab_9)
        self.css_results.setGeometry(QtCore.QRect(150, 53, 651, 111))
        self.css_results.setObjectName("css_results")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_31 = QtWidgets.QLabel(self.tab_5)
        self.label_31.setGeometry(QtCore.QRect(310, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.tab_5)
        self.label_32.setGeometry(QtCore.QRect(310, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.ip_input = QtWidgets.QTextEdit(self.tab_5)
        self.ip_input.setGeometry(QtCore.QRect(390, 20, 191, 31))
        self.ip_input.setPlaceholderText("")
        self.ip_input.setObjectName("ip_input")
        self.port_input = QtWidgets.QTextEdit(self.tab_5)
        self.port_input.setGeometry(QtCore.QRect(390, 60, 191, 31))
        self.port_input.setPlaceholderText("")
        self.port_input.setObjectName("port_input")
        self.ip_button = QtWidgets.QPushButton(self.tab_5)
        self.ip_button.setGeometry(QtCore.QRect(420, 110, 121, 41))
        self.ip_button.setObjectName("ip_button")
        self.tabWidget.addTab(self.tab_5, "")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(270, 0, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 280, 921, 301))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setLineWidth(2)
        self.plainTextEdit.setDocumentTitle("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(10, 590, 921, 85))
        self.listView.setObjectName("listView")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 10, 71, 41))
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.get_url_input.setText('193.112.41.211:8000')
        self.post_url_input.setText('193.112.41.211:8000')
        self.patch_url_input.setText('193.112.41.211:8000')
        self.post_data.setText('username:234234----pass:234jkl')

        self.get_button.clicked.connect(self.get_request)
        self.post_button.clicked.connect(self.post_request)
        self.patch_button.clicked.connect(self.patch_request)
        self.delete_button.clicked.connect(self.delete_request)

        self.re_button.clicked.connect(self.re_match)
        self.xpath_button.clicked.connect(self.xpath_match)
        self.css_button.clicked.connect(self.css_match)

        self.qlist = []

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.get_url_input.setPlaceholderText(_translate("Dialog", "http://"))
        self.label_3.setText(_translate("Dialog", "URL"))
        self.label_5.setText(_translate("Dialog", "请求头"))
        self.get_header.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:64.0) Gecko/20100101 Firefox/64.0</p></body></html>"))
        self.get_button.setText(_translate("Dialog", "发送请求"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.get_tab), _translate("Dialog", "GET"))
        self.post_url_input.setPlaceholderText(_translate("Dialog", "http://"))
        self.label_4.setText(_translate("Dialog", "URL"))
        self.label_6.setText(_translate("Dialog", "请求头"))
        self.post_header.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:64.0) Gecko/20100101 Firefox/64.0</p></body></html>"))
        self.label_10.setText(_translate("Dialog", "数据"))
        self.post_data.setPlaceholderText(_translate("Dialog", "username:xxxxxx----password:xxxxxx"))
        self.label_11.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; color:#0000ff;\">请注意：post 表单数据请按照key1:value1----key2:value2的格式填写</span></p></body></html>"))
        self.post_button.setText(_translate("Dialog", "发送请求"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.post_tab), _translate("Dialog", "POST"))
        self.label_12.setText(_translate("Dialog", "数据"))
        self.patch_url_input.setPlaceholderText(_translate("Dialog", "http://"))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; color:#0000ff;\">请注意：PATCH方法的表单数据请按照key1:value1----key2:value2的格式填写</span></p></body></html>"))
        self.patch_header.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:64.0) Gecko/20100101 Firefox/64.0</p></body></html>"))
        self.patch_button.setText(_translate("Dialog", "发送请求"))
        self.label_9.setText(_translate("Dialog", "URL"))
        self.label_14.setText(_translate("Dialog", "请求头"))
        self.patch_data.setPlaceholderText(_translate("Dialog", "username:xxxxxx----password:xxxxxx"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "PATCH"))
        self.label_27.setText(_translate("Dialog", "请求头"))
        self.delete_button.setText(_translate("Dialog", "发送请求"))
        self.delete_header.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:64.0) Gecko/20100101 Firefox/64.0</p></body></html>"))
        self.label_28.setText(_translate("Dialog", "URL"))
        self.delete_url_input.setPlaceholderText(_translate("Dialog", "http://"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "DELETE"))
        self.label_7.setText(_translate("Dialog", "正则表达式"))
        self.re_input.setPlaceholderText(_translate("Dialog", "请输入正则表达式"))
        self.re_button.setText(_translate("Dialog", "全文匹配"))
        self.re_results.setPlaceholderText(_translate("Dialog", "匹配结果"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "正则表达式"))
        self.xpath_input.setPlaceholderText(_translate("Dialog", "请输入XPATH表达式"))
        self.label_8.setText(_translate("Dialog", "XPATH"))
        self.xpath_button.setText(_translate("Dialog", "全文匹配"))
        self.xpath_results.setPlaceholderText(_translate("Dialog", "匹配结果"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "XPATH"))
        self.css_input.setPlaceholderText(_translate("Dialog", "请输入CSS选择器表达式"))
        self.label_30.setText(_translate("Dialog", "CSS选择器"))
        self.css_button.setText(_translate("Dialog", "全文匹配"))
        self.css_results.setPlaceholderText(_translate("Dialog", "匹配结果"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("Dialog", "CSS选择器"))
        self.label_31.setText(_translate("Dialog", "代理IP"))
        self.label_32.setText(_translate("Dialog", "端口号"))
        self.ip_button.setText(_translate("Dialog", "确认"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "代理IP"))
        self.label_2.setText(_translate("Dialog", "KK HTTP测试工具 Mac版"))
        self.plainTextEdit.setPlaceholderText(_translate("Dialog", "运行结果"))

    def get_request(self):
        self.plainTextEdit.clear()
        url = self.get_url_input.toPlainText()

        if 'http://' not in url:
            url = 'http://' + url

        if 'https://' in url:
            url = url.replace('https://','')

        header = self.get_header.toPlainText()
        if not header:
            print('无请求头')
        headers = {'User-Agent': header}
        try:
            data = requests.get(url,headers=headers)
        except requests.exceptions.InvalidURL:
            self.plainTextEdit.appendPlainText('URL错误！')
        else:

            self.count += 1
            self.qlist.append(str(self.count) +':  GET  '+ url + '  状态码: ' + str(data.status_code))
            slm = QStringListModel()
            slm.setStringList(self.qlist)
            self.listView.setModel(slm)
            self.lcdNumber.setProperty("intValue", self.count)
            self.plainTextEdit.appendPlainText(data.text)


    def delete_request(self):
        self.plainTextEdit.clear()
        url = self.delete_url_input.toPlainText()
        header = self.delete_header.toPlainText()
        if 'http://' not in url:
            url = 'http://' + url
        if 'https://' in url:
            url = url.replace('https://','')

        if not header:
            print('无请求头')
        headers = {'User-Agent': header}
        try:
            data = requests.delete(url,headers=headers)
        except requests.exceptions.InvalidURL:
            self.plainTextEdit.clear()
            self.plainTextEdit.appendPlainText('URL错误！')
        else:
            self.count += 1
            self.qlist.append(str(self.count) + ':  DELETE  ' + url + '  状态码: ' + str(data.status_code))
            slm = QStringListModel()
            slm.setStringList(self.qlist)
            self.listView.setModel(slm)
            self.lcdNumber.setProperty("intValue", self.count)
            self.plainTextEdit.appendPlainText(data.text)


    def post_request(self):
        self.plainTextEdit.clear()
        url = self.post_url_input.toPlainText()
        header = self.post_header.toPlainText()
        postdata = self.post_data.toPlainText()
        if not url:
            print('请输入url')

        else:
            if 'http://' not in url:
                url = 'http://' + url
            if 'https://' in url:
                url = url.replace('https://', '')
            if not header:
                print('无请求头')
            headers = {'User-Agent': header}
            if not postdata:
                try:
                    data = requests.post(url,headers=headers)
                except requests.exceptions.InvalidURL:
                    self.plainTextEdit.clear()
                    self.plainTextEdit.appendPlainText('URL错误！')
                else:
                    self.count += 1
                    self.qlist.append(str(self.count) + ':  POST  ' + url + '  状态码: ' + str(data.status_code) + '  with no post data ')
                    slm = QStringListModel()
                    slm.setStringList(self.qlist)
                    self.listView.setModel(slm)
                    self.lcdNumber.setProperty("intValue", self.count)
                    self.plainTextEdit.appendPlainText(data.text)
                    print('POST ' + url + ' ' + str(data.status_code) +'  无POST表单数据 ')

            else:
                postdata = postdata.split('----')
                keylist = []
                valuelist = []
                try:
                    for item in postdata:
                        keylist.append(item.split(':')[0])
                        valuelist.append(item.split(':')[1])
                except IndexError:
                    print('数据格式错误了！！')

                postdata = dict(zip(keylist, valuelist))

                try:
                    data = requests.post(url,data=postdata,headers=headers)
                except requests.exceptions.InvalidURL:
                    self.plainTextEdit.clear()
                    self.plainTextEdit.appendPlainText('URL错误！')
                else:
                    self.count += 1
                    self.qlist.append(
                        str(self.count) + ':  POST  ' + url + '  状态码: ' + str(data.status_code) +'  表单数据： '+ str(postdata))
                    slm = QStringListModel()
                    slm.setStringList(self.qlist)
                    self.listView.setModel(slm)
                    self.lcdNumber.setProperty("intValue", self.count)

                    self.plainTextEdit.appendPlainText(data.text)
                    print('POST ' + url + ' ' + str(data.status_code) + ' 表单数据： ' + str(postdata))

    def patch_request(self):
        self.plainTextEdit.clear()
        url = self.patch_url_input.toPlainText()
        header = self.patch_header.toPlainText()
        patchdata = self.patch_data.toPlainText()
        if not url:
            print('请输入url')
            self.plainTextEdit.clear()
            self.plainTextEdit.appendPlainText('请输入URL！')
        else:
            if 'http://' not in url:
                url = 'http://' + url
            if 'https://' in url:
                url = url.replace('https://', '')
            if not header:
                print('无请求头')
            headers = {'User-Agent': header}
            if not patchdata:
                try:
                    data = requests.patch(url,headers=headers)
                except requests.exceptions.InvalidURL:
                    self.plainTextEdit.clear()
                    self.plainTextEdit.appendPlainText('URL错误！')
                else:
                    self.count += 1
                    self.qlist.append(str(self.count) + ':  PATCH  ' + url + '  状态码: ' + str(data.status_code) + '  未提交表单数据 ')
                    slm = QStringListModel()
                    slm.setStringList(self.qlist)
                    self.listView.setModel(slm)
                    self.lcdNumber.setProperty("intValue", self.count)
                    self.plainTextEdit.appendPlainText(data.text)
                    print('PATCH ' + url + ' ' + str(data.status_code) +'  无PATCH表单数据 ')

            else:
                patchdata = patchdata.split('----')
                keylist = []
                valuelist = []
                try:
                    for item in patchdata:
                        keylist.append(item.split(':')[0])
                        valuelist.append(item.split(':')[1])
                except IndexError:
                    self.plainTextEdit.clear()
                    self.plainTextEdit.appendPlainText('表单数据格式错误！')
                except requests.exceptions.ConnectionError:
                    self.plainTextEdit.clear()
                    self.plainTextEdit.appendPlainText('连接失败！')

                patchdata = dict(zip(keylist, valuelist))

                try:
                    data = requests.patch(url,data=patchdata,headers=headers)
                except requests.exceptions.InvalidURL:
                    self.plainTextEdit.clear()
                    self.plainTextEdit.appendPlainText('URL错误！')
                except requests.exceptions.ConnectionError:
                    self.plainTextEdit.clear()
                    self.plainTextEdit.appendPlainText('连接失败！')
                else:
                    self.count += 1
                    self.qlist.append(
                        str(self.count) + ':  PATCH  ' + url + '  状态码: ' + str(data.status_code) +'  表单数据： '+ str(patchdata))
                    slm = QStringListModel()
                    slm.setStringList(self.qlist)
                    self.listView.setModel(slm)
                    self.lcdNumber.setProperty("intValue", self.count)

                    self.plainTextEdit.appendPlainText(data.text)
                    print('PATCH ' + url + ' ' + str(data.status_code) + ' 表单数据： ' + str(patchdata))


    def re_match(self):
        origindata = self.plainTextEdit.toPlainText()
        exp = self.re_input.toPlainText()

        self.re_results.clear()
        results = re.compile(exp).findall(origindata)
        if len(results):
            self.re_results.appendPlainText('正则表达式匹配结果：'+str(len(results)))
            for result in results:
                self.re_results.appendPlainText(result)
        else:
            self.re_results.appendPlainText('没有匹配结果')

    def xpath_match(self):
        origindata = self.plainTextEdit.toPlainText()
        exp = self.xpath_input.toPlainText()

        self.xpath_results.clear()
        try:
            results = etree.HTML(origindata).xpath(exp)
        except etree.XPathEvalError:
            self.xpath_results.appendPlainText('XPATH表达式错误！！')
        else:

            self.xpath_results.appendPlainText('XPATH匹配结果：'+str(len(results))+'\n')
            for result in results:
                self.xpath_results.appendPlainText(result)


    def css_match(self):
        pass
