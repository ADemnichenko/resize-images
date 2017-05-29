# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Demnichenko\Programming\resize_image\resize_image\UI\resize.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(238, 200)
        MainWindow.setMinimumSize(QtCore.QSize(238, 200))
        MainWindow.setMaximumSize(QtCore.QSize(238, 200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.resize = QtWidgets.QLineEdit(self.centralwidget)
        self.resize.setGeometry(QtCore.QRect(110, 10, 81, 20))
        self.resize.setObjectName("resize")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label.setObjectName("label")
        self.out_dir_field = QtWidgets.QLineEdit(self.centralwidget)
        self.out_dir_field.setGeometry(QtCore.QRect(110, 40, 81, 20))
        self.out_dir_field.setObjectName("out_dir_field")
        self.save_dir_field = QtWidgets.QLineEdit(self.centralwidget)
        self.save_dir_field.setGeometry(QtCore.QRect(110, 70, 81, 20))
        self.save_dir_field.setObjectName("save_dir_field")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 111, 16))
        self.label_3.setObjectName("label_3")
        self.out_dir = QtWidgets.QToolButton(self.centralwidget)
        self.out_dir.setGeometry(QtCore.QRect(200, 40, 25, 19))
        self.out_dir.setObjectName("out_dir")
        self.save_dir = QtWidgets.QToolButton(self.centralwidget)
        self.save_dir.setGeometry(QtCore.QRect(200, 70, 25, 19))
        self.save_dir.setObjectName("save_dir")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 140, 219, 23))
        self.pushButton.setMinimumSize(QtCore.QSize(219, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(219, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(110, 100, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 71, 16))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter % for resize"))
        self.label_2.setText(_translate("MainWindow", "Select out dir"))
        self.label_3.setText(_translate("MainWindow", "Select save dir"))
        self.out_dir.setText(_translate("MainWindow", "..."))
        self.save_dir.setText(_translate("MainWindow", "..."))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.label_4.setText(_translate("MainWindow", "Select method"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

