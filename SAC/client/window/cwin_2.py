# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cwin_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Setings(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Settings")
        MainWindow.resize(550, 500)
        MainWindow.setStyleSheet("")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(26, 43, 511, 431))
        self.label.setStyleSheet("background-color: #4d4d4d;\n"
"border: 2px solid #2d2d2d;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.Chat_Window = QtWidgets.QPushButton(self.centralwidget)
        self.Chat_Window.setGeometry(QtCore.QRect(26, 20, 66, 23))
        self.Chat_Window.setStyleSheet("border: 2px solid #2d2d2d;\n"
"border-bottom: 0px solid #2d2d2d;")
        self.Chat_Window.setObjectName("Chat_Window")
        self.Settings_window = QtWidgets.QPushButton(self.centralwidget)
        self.Settings_window.setGeometry(QtCore.QRect(90, 20, 71, 23))
        self.Settings_window.setStyleSheet("border: 2px solid #2d2d2d;\n"
"border-bottom: 0px solid #2d2d2d;\n"
"border-top-right-radius: 10px;\n"
"background-color: #4d4d4d;")
        self.Settings_window.setObjectName("Settings_window")
        # self.label_2 = QtWidgets.QLabel(self.centralwidget)
        # self.label_2.setGeometry(QtCore.QRect(46, 243, 471, 211))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
#         self.label_2.setFont(font)
#         self.label_2.setStyleSheet("color: #909090;\n"
# "background-color: #3f3f3f;\n"
# "border: 2px solid #2d2d2d;\n"
# "color: #c4c4c4;\n"
# "border-radius: 5px;")
#         self.label_2.setText("")
#         self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 350, 400, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border: 2px solid #2d2d2d;\n"
"color: #c4c4c4;\n"
"border-radius: 5px;")
        self.pushButton.setObjectName("pushButton")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 130, 481, 150))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: #909090;\n"
"background-color: #3f3f3f;\n"
"border: 2px solid #2d2d2d;\n"
"border-radius: 5px;\n"
"font-size: 25px;")
        self.lineEdit.setObjectName("nicname")


        self.nicname = QtWidgets.QLineEdit(self.centralwidget)
        self.nicname.setGeometry(QtCore.QRect(40, 230, 481, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.nicname.setFont(font)
        self.nicname.setStyleSheet("color: #909090;\n"
                                    "background-color: #3f3f3f;\n"
                                    "border: 2px solid #2d2d2d;\n"
                                    "border-radius: 5px;\n"
                                    "font-size: 25px;")
        self.nicname.setObjectName("nicname")

        self.ID_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.ID_Edit.setGeometry(QtCore.QRect(40, 50, 481, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setItalic(True)


        self.ID_Edit.setFont(font)
        self.ID_Edit.setStyleSheet("color: #909090;\n"
"border: 2px solid #2d2d2d;\n"
"background-color: #3f3f3f;\n"
"border-radius: 5px;\n"
"font-size: 25px;")
        self.ID_Edit.setObjectName("ID_Edit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 561, 511))
        self.label_3.setStyleSheet("background-color: #3d3d3d;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.raise_()
        self.label.raise_()
        self.Chat_Window.raise_()
        # self.label_2.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.nicname.raise_()
        self.ID_Edit.raise_()
        self.Settings_window.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Chat_Window.setText(_translate("MainWindow", "Чат"))
        self.Settings_window.setText(_translate("MainWindow", "Настройки"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить"))
        self.lineEdit.setText(_translate("MainWindow", "Порт сервера..."))
        self.ID_Edit.setText(_translate("MainWindow", "Адрес сервера..."))
        self.nicname.setText(_translate("MainWindow", "Имя..."))
        # self.label_2.setText(_translate("MainWindow", " "))