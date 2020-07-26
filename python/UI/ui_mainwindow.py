# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(555, 430)
        self.actionConnect = QAction(MainWindow)
        self.actionConnect.setObjectName(u"actionConnect")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 520, 360))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 520, 330))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayoutWidget_2 = QWidget(self.tab_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 520, 330))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget_3 = QWidget(self.tab_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 520, 330))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_5, 3, 0, 1, 3)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy2.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.pushButton_4, 2, 0, 1, 3)

        self.label_2 = QLabel(self.gridLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.timeEdit_2 = QTimeEdit(self.gridLayoutWidget_3)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 1)))
        self.timeEdit_2.setMaximumDateTime(QDateTime(QDate(2000, 1, 1), QTime(23, 0, 1)))
        self.timeEdit_2.setMinimumDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 1)))
        self.timeEdit_2.setMaximumTime(QTime(23, 0, 1))
        self.timeEdit_2.setMinimumTime(QTime(0, 0, 1))
        self.timeEdit_2.setCurrentSection(QDateTimeEdit.HourSection)

        self.gridLayout_3.addWidget(self.timeEdit_2, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayoutWidget_4 = QWidget(self.tab_4)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 0, 520, 330))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.spinBox_3 = QSpinBox(self.gridLayoutWidget_4)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(99999)

        self.gridLayout_4.addWidget(self.spinBox_3, 2, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy2.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.pushButton_7, 4, 0, 1, 3)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy2.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.pushButton_6, 3, 0, 1, 3)

        self.label_4 = QLabel(self.gridLayoutWidget_4)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.timeEdit_5 = QTimeEdit(self.gridLayoutWidget_4)
        self.timeEdit_5.setObjectName(u"timeEdit_5")
        self.timeEdit_5.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 1)))
        self.timeEdit_5.setMaximumDateTime(QDateTime(QDate(2000, 1, 1), QTime(23, 0, 1)))
        self.timeEdit_5.setMinimumDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 1)))
        self.timeEdit_5.setMaximumTime(QTime(23, 0, 1))
        self.timeEdit_5.setMinimumTime(QTime(0, 0, 1))
        self.timeEdit_5.setCurrentSection(QDateTimeEdit.HourSection)

        self.gridLayout_4.addWidget(self.timeEdit_5, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayoutWidget_5 = QWidget(self.tab_5)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(0, 0, 520, 330))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.gridLayoutWidget_5)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 2, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.gridLayoutWidget_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy2.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.pushButton_8, 3, 0, 1, 3)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget_5)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy2.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.pushButton_9, 4, 0, 1, 3)

        self.timeEdit_4 = QTimeEdit(self.gridLayoutWidget_5)
        self.timeEdit_4.setObjectName(u"timeEdit_4")
        self.timeEdit_4.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 1)))
        self.timeEdit_4.setMaximumDateTime(QDateTime(QDate(2000, 1, 1), QTime(23, 0, 1)))
        self.timeEdit_4.setMinimumDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 1)))
        self.timeEdit_4.setMaximumTime(QTime(23, 0, 1))
        self.timeEdit_4.setMinimumTime(QTime(0, 0, 1))
        self.timeEdit_4.setCurrentSection(QDateTimeEdit.HourSection)

        self.gridLayout_5.addWidget(self.timeEdit_4, 0, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_5)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1)

        self.spinBox_4 = QSpinBox(self.gridLayoutWidget_5)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(99999)

        self.gridLayout_5.addWidget(self.spinBox_4, 1, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_5)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 0, 0, 1, 1)

        self.timeEdit_3 = QTimeEdit(self.gridLayoutWidget_5)
        self.timeEdit_3.setObjectName(u"timeEdit_3")
        self.timeEdit_3.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 1)))
        self.timeEdit_3.setMaximumDateTime(QDateTime(QDate(2000, 1, 1), QTime(23, 0, 1)))
        self.timeEdit_3.setMinimumDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 1)))
        self.timeEdit_3.setMaximumTime(QTime(23, 0, 1))
        self.timeEdit_3.setMinimumTime(QTime(0, 0, 1))
        self.timeEdit_3.setCurrentSection(QDateTimeEdit.HourSection)

        self.gridLayout_5.addWidget(self.timeEdit_3, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 555, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionConnect)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Intervallometer", None))
        self.actionConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
#if QT_CONFIG(shortcut)
        self.actionConnect.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Single Shot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Single Shot", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Bulb ON", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Bulb OFF", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Manual BULB", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Bulb ON time", None))
        self.timeEdit_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm:ss", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Timed BULB", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Shots", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Delay", None))
        self.timeEdit_5.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm:ss", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Intervallometer", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Shutter open for", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.timeEdit_4.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm:ss", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Shots", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Delay", None))
        self.timeEdit_3.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm:ss", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"BULB Intervallometer", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

