# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.label_url = QtWidgets.QLabel(self.central_widget)
        self.label_url.setGeometry(QtCore.QRect(10, 20, 31, 31))
        self.label_url.setObjectName("label_url")
        self.text_edit_urls = QtWidgets.QTextEdit(self.central_widget)
        self.text_edit_urls.setGeometry(QtCore.QRect(50, 20, 291, 41))
        self.text_edit_urls.setObjectName("text_edit_urls")
        self.settingsBox = QtWidgets.QGroupBox(self.central_widget)
        self.settingsBox.setGeometry(QtCore.QRect(0, 120, 351, 351))
        self.settingsBox.setTitle("")
        self.settingsBox.setObjectName("settingsBox")
        self.proxy_checkBox = QtWidgets.QCheckBox(self.settingsBox)
        self.proxy_checkBox.setGeometry(QtCore.QRect(10, 150, 151, 31))
        self.proxy_checkBox.setObjectName("proxy_checkBox")
        self.file_path_label = QtWidgets.QLabel(self.settingsBox)
        self.file_path_label.setGeometry(QtCore.QRect(10, 50, 331, 21))
        self.file_path_label.setObjectName("file_path_label")
        self.set_path_button = QtWidgets.QPushButton(self.settingsBox)
        self.set_path_button.setGeometry(QtCore.QRect(10, 80, 331, 31))
        self.set_path_button.setObjectName("set_path_button")
        self.set_proxy_button = QtWidgets.QPushButton(self.settingsBox)
        self.set_proxy_button.setGeometry(QtCore.QRect(10, 190, 331, 31))
        self.set_proxy_button.setObjectName("set_proxy_button")
        self.check_update_button = QtWidgets.QPushButton(self.settingsBox)
        self.check_update_button.setGeometry(QtCore.QRect(10, 260, 151, 61))
        self.check_update_button.setObjectName("check_update_button")
        self.about_button = QtWidgets.QPushButton(self.settingsBox)
        self.about_button.setGeometry(QtCore.QRect(180, 260, 161, 61))
        self.about_button.setObjectName("about_button")
        self.label = QtWidgets.QLabel(self.settingsBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 321, 25))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.settingsBox)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 231, 25))
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(self.settingsBox)
        self.line_2.setGeometry(QtCore.QRect(-10, 230, 361, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.settingsBox)
        self.line_3.setGeometry(QtCore.QRect(-10, 120, 361, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.button_download = QtWidgets.QPushButton(self.central_widget)
        self.button_download.setGeometry(QtCore.QRect(10, 80, 331, 41))
        self.button_download.setObjectName("button_download")
        self.line = QtWidgets.QFrame(self.central_widget)
        self.line.setGeometry(QtCore.QRect(0, 130, 351, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.central_widget)
        self.menu_bar = QtWidgets.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 350, 31))
        self.menu_bar.setObjectName("menu_bar")
        self.menu_settings = QtWidgets.QMenu(self.menu_bar)
        self.menu_settings.setObjectName("menu_settings")
        self.menu_help = QtWidgets.QMenu(self.menu_bar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menu_bar)
        self.action_file_path = QtWidgets.QAction(MainWindow)
        self.action_file_path.setObjectName("action_file_path")
        self.action_report_bugs = QtWidgets.QAction(MainWindow)
        self.action_report_bugs.setObjectName("action_report_bugs")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_check_for_updates = QtWidgets.QAction(MainWindow)
        self.action_check_for_updates.setObjectName("action_check_for_updates")
        self.action_supported_sites = QtWidgets.QAction(MainWindow)
        self.action_supported_sites.setObjectName("action_supported_sites")
        self.menu_settings.addAction(self.action_file_path)
        self.menu_help.addAction(self.action_check_for_updates)
        self.menu_help.addAction(self.action_supported_sites)
        self.menu_help.addAction(self.action_report_bugs)
        self.menu_help.addAction(self.action_about)
        self.menu_bar.addAction(self.menu_settings.menuAction())
        self.menu_bar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouGet"))
        self.label_url.setText(_translate("MainWindow", "Url"))
        self.proxy_checkBox.setText(_translate("MainWindow", "Enable the proxy"))
        self.file_path_label.setText(_translate("MainWindow", "Path"))
        self.set_path_button.setText(_translate("MainWindow", "Set Path"))
        self.set_proxy_button.setText(_translate("MainWindow", "Set Proxy"))
        self.check_update_button.setText(_translate("MainWindow", "Check for Updates"))
        self.about_button.setText(_translate("MainWindow", "About"))
        self.label.setText(_translate("MainWindow", "Storage path:"))
        self.label_2.setText(_translate("MainWindow", "Proxy:"))
        self.button_download.setText(_translate("MainWindow", "Download"))
        self.menu_settings.setTitle(_translate("MainWindow", "Settings"))
        self.menu_help.setTitle(_translate("MainWindow", "Help"))
        self.action_file_path.setText(_translate("MainWindow", "File path"))
        self.action_report_bugs.setText(_translate("MainWindow", "Report bugs"))
        self.action_about.setText(_translate("MainWindow", "About"))
        self.action_check_for_updates.setText(_translate("MainWindow", "Check for updates"))
        self.action_supported_sites.setText(_translate("MainWindow", "Supported Sites"))

