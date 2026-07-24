# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QStackedWidget,
    QToolButton, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setMinimumSize(QSize(1024, 600))
        MainWindow.setStyleSheet(u"background: #E8ECF0;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.widget.setMaximumSize(QSize(16777215, 60))
        self.widget.setStyleSheet(u"background: #F5F6F8;")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.lblDate = QLabel(self.widget)
        self.lblDate.setObjectName(u"lblDate")

        self.horizontalLayout_2.addWidget(self.lblDate)

        self.horizontalSpacer = QSpacerItem(584, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btnExit = QPushButton(self.widget)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setMinimumSize(QSize(85, 30))
        self.btnExit.setStyleSheet(u"QPushButton {\n"
"	background: #F0F2F5;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #D5DAE0;\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.btnExit)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainMenu = QWidget(self.widget_2)
        self.mainMenu.setObjectName(u"mainMenu")
        self.mainMenu.setMinimumSize(QSize(200, 0))
        self.mainMenu.setStyleSheet(u"QPushButton {\n"
"	padding-left: 15px;\n"
"	text-align: left;\n"
"	background-color: #F0F2F5;\n"
"	border-radius: none;\n"
"	height: 30px;\n"
"	border-top: 1px solid #B8C0CC;\n"
"	border-bottom: 1px solid #B8C0CC;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #D5DAE0;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #D5DAE0;\n"
"    border-left: 4px solid #4A8AB5;\n"
"    border-top: 1px solid #9AA3B3;\n"
"    border-bottom: 1px solid #9AA3B3;\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.mainMenu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnAutoMode = QPushButton(self.mainMenu)
        self.btnAutoMode.setObjectName(u"btnAutoMode")

        self.verticalLayout_2.addWidget(self.btnAutoMode)

        self.btnManualMode = QPushButton(self.mainMenu)
        self.btnManualMode.setObjectName(u"btnManualMode")

        self.verticalLayout_2.addWidget(self.btnManualMode)

        self.subMenu = QWidget(self.mainMenu)
        self.subMenu.setObjectName(u"subMenu")
        self.subMenu.setStyleSheet(u"QPushButton {\n"
"	height: 40px;\n"
"	margin-left: 10px;\n"
"	border-left: 1px solid #B8C0CC;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #D5DAE0;\n"
"    border-left: 4px solid #4A8AB5;\n"
"    border-bottom: 1px solid #B8C0CC;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.subMenu)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnLinear = QPushButton(self.subMenu)
        self.btnLinear.setObjectName(u"btnLinear")

        self.verticalLayout_3.addWidget(self.btnLinear)

        self.btnFixation = QPushButton(self.subMenu)
        self.btnFixation.setObjectName(u"btnFixation")

        self.verticalLayout_3.addWidget(self.btnFixation)

        self.btnPreCrimp = QPushButton(self.subMenu)
        self.btnPreCrimp.setObjectName(u"btnPreCrimp")

        self.verticalLayout_3.addWidget(self.btnPreCrimp)

        self.btnPostCrimp = QPushButton(self.subMenu)
        self.btnPostCrimp.setObjectName(u"btnPostCrimp")

        self.verticalLayout_3.addWidget(self.btnPostCrimp)


        self.verticalLayout_2.addWidget(self.subMenu)

        self.btnCalibration = QPushButton(self.mainMenu)
        self.btnCalibration.setObjectName(u"btnCalibration")

        self.verticalLayout_2.addWidget(self.btnCalibration)

        self.btnDebug = QPushButton(self.mainMenu)
        self.btnDebug.setObjectName(u"btnDebug")

        self.verticalLayout_2.addWidget(self.btnDebug)

        self.btnSettings = QPushButton(self.mainMenu)
        self.btnSettings.setObjectName(u"btnSettings")

        self.verticalLayout_2.addWidget(self.btnSettings)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.lblTemp = QLabel(self.mainMenu)
        self.lblTemp.setObjectName(u"lblTemp")
        self.lblTemp.setMinimumSize(QSize(0, 20))
        self.lblTemp.setMaximumSize(QSize(16777215, 36))
        font = QFont()
        font.setPointSize(9)
        self.lblTemp.setFont(font)
        self.lblTemp.setStyleSheet(u"padding-left: 10px;")

        self.verticalLayout_2.addWidget(self.lblTemp)


        self.horizontalLayout.addWidget(self.mainMenu)

        self.stackedWidget = QStackedWidget(self.widget_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: #dde0e7;")
        self.pageAutoMode = QWidget()
        self.pageAutoMode.setObjectName(u"pageAutoMode")
        self.verticalLayout_30 = QVBoxLayout(self.pageAutoMode)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label = QLabel(self.pageAutoMode)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_30.addWidget(self.label)

        self.stackedWidget.addWidget(self.pageAutoMode)
        self.pageManualMode = QWidget()
        self.pageManualMode.setObjectName(u"pageManualMode")
        self.verticalLayout_44 = QVBoxLayout(self.pageManualMode)
        self.verticalLayout_44.setSpacing(5)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(10, 10, 10, 10)
        self.widget_33 = QWidget(self.pageManualMode)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setMinimumSize(QSize(0, 200))
        self.horizontalLayout_26 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_26.setSpacing(5)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.widget_34 = QWidget(self.widget_33)
        self.widget_34.setObjectName(u"widget_34")
        self.widget_34.setMinimumSize(QSize(300, 0))
        self.widget_34.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_45 = QVBoxLayout(self.widget_34)
        self.verticalLayout_45.setSpacing(5)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.frameXPos_7 = QFrame(self.widget_34)
        self.frameXPos_7.setObjectName(u"frameXPos_7")
        self.frameXPos_7.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameXPos {\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.frameXPos_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameXPos_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frameXPos_7)
        self.verticalLayout_56.setSpacing(5)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(10, 10, 10, 10)
        self.label_42 = QLabel(self.frameXPos_7)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(0, 0))
        self.label_42.setMaximumSize(QSize(16777215, 25))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_42.setFont(font2)

        self.verticalLayout_56.addWidget(self.label_42)

        self.widget_42 = QWidget(self.frameXPos_7)
        self.widget_42.setObjectName(u"widget_42")
        self.verticalLayout_57 = QVBoxLayout(self.widget_42)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.widget_42)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setPointSize(10)
        self.label_43.setFont(font3)
        self.label_43.setWordWrap(True)

        self.verticalLayout_57.addWidget(self.label_43)

        self.lblLinPosMan = QLabel(self.widget_42)
        self.lblLinPosMan.setObjectName(u"lblLinPosMan")
        self.lblLinPosMan.setMaximumSize(QSize(16777215, 40))
        font4 = QFont()
        font4.setPointSize(21)
        font4.setBold(True)
        self.lblLinPosMan.setFont(font4)

        self.verticalLayout_57.addWidget(self.lblLinPosMan)


        self.verticalLayout_56.addWidget(self.widget_42)

        self.line_11 = QFrame(self.frameXPos_7)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setStyleSheet(u"Line {\n"
"	border: 1px solid #ced3d7;\n"
"}")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_56.addWidget(self.line_11)

        self.widget_41 = QWidget(self.frameXPos_7)
        self.widget_41.setObjectName(u"widget_41")
        self.verticalLayout_58 = QVBoxLayout(self.widget_41)
        self.verticalLayout_58.setSpacing(5)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.widget_43 = QWidget(self.widget_41)
        self.widget_43.setObjectName(u"widget_43")
        self.gridLayout = QGridLayout(self.widget_43)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btnLinForwardMan = QToolButton(self.widget_43)
        self.btnLinForwardMan.setObjectName(u"btnLinForwardMan")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLinForwardMan.sizePolicy().hasHeightForWidth())
        self.btnLinForwardMan.setSizePolicy(sizePolicy)
        self.btnLinForwardMan.setMinimumSize(QSize(0, 45))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.btnLinForwardMan.setFont(font5)
        self.btnLinForwardMan.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/left.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLinForwardMan.setIcon(icon)
        self.btnLinForwardMan.setIconSize(QSize(35, 35))
        self.btnLinForwardMan.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.gridLayout.addWidget(self.btnLinForwardMan, 0, 1, 1, 1)

        self.btnLinBackMan = QToolButton(self.widget_43)
        self.btnLinBackMan.setObjectName(u"btnLinBackMan")
        sizePolicy.setHeightForWidth(self.btnLinBackMan.sizePolicy().hasHeightForWidth())
        self.btnLinBackMan.setSizePolicy(sizePolicy)
        self.btnLinBackMan.setMinimumSize(QSize(0, 45))
        self.btnLinBackMan.setFont(font5)
        self.btnLinBackMan.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLinBackMan.setIcon(icon1)
        self.btnLinBackMan.setIconSize(QSize(35, 35))
        self.btnLinBackMan.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.gridLayout.addWidget(self.btnLinBackMan, 0, 0, 1, 1)

        self.btnGoLinPos1Man = QPushButton(self.widget_43)
        self.btnGoLinPos1Man.setObjectName(u"btnGoLinPos1Man")
        self.btnGoLinPos1Man.setMinimumSize(QSize(0, 45))
        self.btnGoLinPos1Man.setFont(font5)
        self.btnGoLinPos1Man.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btnGoLinPos1Man, 2, 0, 1, 1)

        self.btnGoLinPos2Man = QPushButton(self.widget_43)
        self.btnGoLinPos2Man.setObjectName(u"btnGoLinPos2Man")
        self.btnGoLinPos2Man.setMinimumSize(QSize(0, 45))
        self.btnGoLinPos2Man.setFont(font5)
        self.btnGoLinPos2Man.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btnGoLinPos2Man, 2, 1, 1, 1)


        self.verticalLayout_58.addWidget(self.widget_43)

        self.widget_32 = QWidget(self.widget_41)
        self.widget_32.setObjectName(u"widget_32")
        self.verticalLayout_46 = QVBoxLayout(self.widget_32)
        self.verticalLayout_46.setSpacing(5)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.btnLinHomeMan = QToolButton(self.widget_32)
        self.btnLinHomeMan.setObjectName(u"btnLinHomeMan")
        sizePolicy.setHeightForWidth(self.btnLinHomeMan.sizePolicy().hasHeightForWidth())
        self.btnLinHomeMan.setSizePolicy(sizePolicy)
        self.btnLinHomeMan.setMinimumSize(QSize(0, 45))
        self.btnLinHomeMan.setFont(font5)
        self.btnLinHomeMan.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLinHomeMan.setIcon(icon2)
        self.btnLinHomeMan.setIconSize(QSize(35, 35))
        self.btnLinHomeMan.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_46.addWidget(self.btnLinHomeMan)


        self.verticalLayout_58.addWidget(self.widget_32)


        self.verticalLayout_56.addWidget(self.widget_41)


        self.verticalLayout_45.addWidget(self.frameXPos_7)

        self.frameXPos_8 = QFrame(self.widget_34)
        self.frameXPos_8.setObjectName(u"frameXPos_8")
        self.frameXPos_8.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameXPos {\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.frameXPos_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameXPos_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frameXPos_8)
        self.verticalLayout_59.setSpacing(5)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(10, 10, 10, 10)
        self.label_45 = QLabel(self.frameXPos_8)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(0, 0))
        self.label_45.setMaximumSize(QSize(16777215, 25))
        self.label_45.setFont(font2)

        self.verticalLayout_59.addWidget(self.label_45)

        self.widget_45 = QWidget(self.frameXPos_8)
        self.widget_45.setObjectName(u"widget_45")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_45)
        self.horizontalLayout_27.setSpacing(5)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.widget_47 = QWidget(self.widget_45)
        self.widget_47.setObjectName(u"widget_47")
        self.verticalLayout_60 = QVBoxLayout(self.widget_47)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.widget_47)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(16777215, 30))
        font6 = QFont()
        font6.setPointSize(8)
        self.label_46.setFont(font6)
        self.label_46.setWordWrap(True)

        self.verticalLayout_60.addWidget(self.label_46)

        self.lblPrePosMan = QLabel(self.widget_47)
        self.lblPrePosMan.setObjectName(u"lblPrePosMan")
        self.lblPrePosMan.setMaximumSize(QSize(16777215, 40))
        font7 = QFont()
        font7.setPointSize(19)
        font7.setBold(True)
        self.lblPrePosMan.setFont(font7)

        self.verticalLayout_60.addWidget(self.lblPrePosMan)


        self.horizontalLayout_27.addWidget(self.widget_47)

        self.line_13 = QFrame(self.widget_45)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setStyleSheet(u"Line {\n"
"	border: 1px solid #ced3d7;\n"
"}")
        self.line_13.setFrameShape(QFrame.Shape.VLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_27.addWidget(self.line_13)

        self.widget_48 = QWidget(self.widget_45)
        self.widget_48.setObjectName(u"widget_48")
        self.verticalLayout_61 = QVBoxLayout(self.widget_48)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.widget_48)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(16777215, 30))
        self.label_48.setFont(font6)
        self.label_48.setWordWrap(True)

        self.verticalLayout_61.addWidget(self.label_48)

        self.label_49 = QLabel(self.widget_48)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMaximumSize(QSize(16777215, 40))
        self.label_49.setFont(font7)

        self.verticalLayout_61.addWidget(self.label_49)


        self.horizontalLayout_27.addWidget(self.widget_48)


        self.verticalLayout_59.addWidget(self.widget_45)

        self.line_14 = QFrame(self.frameXPos_8)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setStyleSheet(u"Line {\n"
"	border: 1px solid #ced3d7;\n"
"}")
        self.line_14.setFrameShape(QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_59.addWidget(self.line_14)

        self.widget_44 = QWidget(self.frameXPos_8)
        self.widget_44.setObjectName(u"widget_44")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_44)
        self.horizontalLayout_31.setSpacing(5)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.widget_46 = QWidget(self.widget_44)
        self.widget_46.setObjectName(u"widget_46")
        self.gridLayout_2 = QGridLayout(self.widget_46)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnPreUpMan = QToolButton(self.widget_46)
        self.btnPreUpMan.setObjectName(u"btnPreUpMan")
        sizePolicy.setHeightForWidth(self.btnPreUpMan.sizePolicy().hasHeightForWidth())
        self.btnPreUpMan.setSizePolicy(sizePolicy)
        self.btnPreUpMan.setMinimumSize(QSize(0, 45))
        self.btnPreUpMan.setFont(font5)
        self.btnPreUpMan.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/up.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPreUpMan.setIcon(icon3)
        self.btnPreUpMan.setIconSize(QSize(35, 35))
        self.btnPreUpMan.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.gridLayout_2.addWidget(self.btnPreUpMan, 0, 0, 1, 1)

        self.btnPreDownMan = QToolButton(self.widget_46)
        self.btnPreDownMan.setObjectName(u"btnPreDownMan")
        sizePolicy.setHeightForWidth(self.btnPreDownMan.sizePolicy().hasHeightForWidth())
        self.btnPreDownMan.setSizePolicy(sizePolicy)
        self.btnPreDownMan.setMinimumSize(QSize(0, 45))
        self.btnPreDownMan.setFont(font5)
        self.btnPreDownMan.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/down.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPreDownMan.setIcon(icon4)
        self.btnPreDownMan.setIconSize(QSize(35, 35))
        self.btnPreDownMan.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.gridLayout_2.addWidget(self.btnPreDownMan, 0, 1, 1, 1)

        self.btnPreDown11 = QToolButton(self.widget_46)
        self.btnPreDown11.setObjectName(u"btnPreDown11")
        sizePolicy.setHeightForWidth(self.btnPreDown11.sizePolicy().hasHeightForWidth())
        self.btnPreDown11.setSizePolicy(sizePolicy)
        self.btnPreDown11.setMinimumSize(QSize(0, 45))
        self.btnPreDown11.setFont(font5)
        self.btnPreDown11.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/press.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPreDown11.setIcon(icon5)
        self.btnPreDown11.setIconSize(QSize(35, 35))
        self.btnPreDown11.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.gridLayout_2.addWidget(self.btnPreDown11, 1, 0, 1, 1)

        self.btnPreHomeMan = QToolButton(self.widget_46)
        self.btnPreHomeMan.setObjectName(u"btnPreHomeMan")
        sizePolicy.setHeightForWidth(self.btnPreHomeMan.sizePolicy().hasHeightForWidth())
        self.btnPreHomeMan.setSizePolicy(sizePolicy)
        self.btnPreHomeMan.setMinimumSize(QSize(0, 45))
        self.btnPreHomeMan.setFont(font5)
        self.btnPreHomeMan.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.btnPreHomeMan.setIcon(icon2)
        self.btnPreHomeMan.setIconSize(QSize(35, 35))
        self.btnPreHomeMan.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.gridLayout_2.addWidget(self.btnPreHomeMan, 1, 1, 1, 1)


        self.horizontalLayout_31.addWidget(self.widget_46)


        self.verticalLayout_59.addWidget(self.widget_44)


        self.verticalLayout_45.addWidget(self.frameXPos_8)


        self.horizontalLayout_26.addWidget(self.widget_34)

        self.widget_35 = QWidget(self.widget_33)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setMinimumSize(QSize(300, 0))
        self.widget_35.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_47 = QVBoxLayout(self.widget_35)
        self.verticalLayout_47.setSpacing(5)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frameXPos_6 = QFrame(self.widget_35)
        self.frameXPos_6.setObjectName(u"frameXPos_6")
        self.frameXPos_6.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameXPos {\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.frameXPos_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameXPos_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frameXPos_6)
        self.verticalLayout_53.setSpacing(5)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(10, 10, 10, 10)
        self.label_39 = QLabel(self.frameXPos_6)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(0, 0))
        self.label_39.setMaximumSize(QSize(16777215, 25))
        self.label_39.setFont(font2)

        self.verticalLayout_53.addWidget(self.label_39)

        self.widget_39 = QWidget(self.frameXPos_6)
        self.widget_39.setObjectName(u"widget_39")
        self.verticalLayout_54 = QVBoxLayout(self.widget_39)
        self.verticalLayout_54.setSpacing(0)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.widget_39)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(16777215, 30))
        self.label_40.setFont(font3)
        self.label_40.setWordWrap(True)

        self.verticalLayout_54.addWidget(self.label_40)

        self.label_41 = QLabel(self.widget_39)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMaximumSize(QSize(16777215, 40))
        self.label_41.setFont(font4)

        self.verticalLayout_54.addWidget(self.label_41)


        self.verticalLayout_53.addWidget(self.widget_39)

        self.line_6 = QFrame(self.frameXPos_6)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"Line {\n"
"	border: 1px solid #ced3d7;\n"
"}")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_53.addWidget(self.line_6)

        self.widget_38 = QWidget(self.frameXPos_6)
        self.widget_38.setObjectName(u"widget_38")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_29.setSpacing(5)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.widget_49 = QWidget(self.widget_38)
        self.widget_49.setObjectName(u"widget_49")
        self.verticalLayout_48 = QVBoxLayout(self.widget_49)
        self.verticalLayout_48.setSpacing(5)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.btnFixBackMan = QToolButton(self.widget_49)
        self.btnFixBackMan.setObjectName(u"btnFixBackMan")
        sizePolicy.setHeightForWidth(self.btnFixBackMan.sizePolicy().hasHeightForWidth())
        self.btnFixBackMan.setSizePolicy(sizePolicy)
        self.btnFixBackMan.setMinimumSize(QSize(0, 45))
        self.btnFixBackMan.setFont(font5)
        self.btnFixBackMan.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/unfix.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnFixBackMan.setIcon(icon6)
        self.btnFixBackMan.setIconSize(QSize(35, 35))
        self.btnFixBackMan.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_48.addWidget(self.btnFixBackMan)

        self.btnFixForwardMan = QToolButton(self.widget_49)
        self.btnFixForwardMan.setObjectName(u"btnFixForwardMan")
        sizePolicy.setHeightForWidth(self.btnFixForwardMan.sizePolicy().hasHeightForWidth())
        self.btnFixForwardMan.setSizePolicy(sizePolicy)
        self.btnFixForwardMan.setMinimumSize(QSize(0, 45))
        self.btnFixForwardMan.setFont(font5)
        self.btnFixForwardMan.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/fix.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnFixForwardMan.setIcon(icon7)
        self.btnFixForwardMan.setIconSize(QSize(35, 35))
        self.btnFixForwardMan.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_48.addWidget(self.btnFixForwardMan)


        self.horizontalLayout_29.addWidget(self.widget_49)

        self.widget_40 = QWidget(self.widget_38)
        self.widget_40.setObjectName(u"widget_40")
        self.verticalLayout_55 = QVBoxLayout(self.widget_40)
        self.verticalLayout_55.setSpacing(5)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.toolButton_28 = QToolButton(self.widget_40)
        self.toolButton_28.setObjectName(u"toolButton_28")
        sizePolicy.setHeightForWidth(self.toolButton_28.sizePolicy().hasHeightForWidth())
        self.toolButton_28.setSizePolicy(sizePolicy)
        self.toolButton_28.setMinimumSize(QSize(0, 45))
        self.toolButton_28.setFont(font5)
        self.toolButton_28.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.toolButton_28.setIcon(icon6)
        self.toolButton_28.setIconSize(QSize(35, 35))
        self.toolButton_28.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_55.addWidget(self.toolButton_28)

        self.toolButton_29 = QToolButton(self.widget_40)
        self.toolButton_29.setObjectName(u"toolButton_29")
        sizePolicy.setHeightForWidth(self.toolButton_29.sizePolicy().hasHeightForWidth())
        self.toolButton_29.setSizePolicy(sizePolicy)
        self.toolButton_29.setMinimumSize(QSize(0, 45))
        self.toolButton_29.setFont(font5)
        self.toolButton_29.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.toolButton_29.setIcon(icon7)
        self.toolButton_29.setIconSize(QSize(35, 35))
        self.toolButton_29.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_55.addWidget(self.toolButton_29)


        self.horizontalLayout_29.addWidget(self.widget_40)


        self.verticalLayout_53.addWidget(self.widget_38)


        self.verticalLayout_47.addWidget(self.frameXPos_6)

        self.frameXPos_5 = QFrame(self.widget_35)
        self.frameXPos_5.setObjectName(u"frameXPos_5")
        self.frameXPos_5.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameXPos {\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.frameXPos_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameXPos_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frameXPos_5)
        self.verticalLayout_49.setSpacing(5)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(10, 10, 10, 10)
        self.label_36 = QLabel(self.frameXPos_5)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(0, 0))
        self.label_36.setMaximumSize(QSize(16777215, 25))
        self.label_36.setFont(font2)

        self.verticalLayout_49.addWidget(self.label_36)

        self.widget_36 = QWidget(self.frameXPos_5)
        self.widget_36.setObjectName(u"widget_36")
        self.verticalLayout_52 = QVBoxLayout(self.widget_36)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.widget_36)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(16777215, 30))
        self.label_37.setFont(font3)
        self.label_37.setWordWrap(True)

        self.verticalLayout_52.addWidget(self.label_37)

        self.label_38 = QLabel(self.widget_36)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(16777215, 40))
        self.label_38.setFont(font4)

        self.verticalLayout_52.addWidget(self.label_38)


        self.verticalLayout_49.addWidget(self.widget_36)

        self.line_10 = QFrame(self.frameXPos_5)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setStyleSheet(u"Line {\n"
"	border: 1px solid #ced3d7;\n"
"}")
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_49.addWidget(self.line_10)

        self.widget_37 = QWidget(self.frameXPos_5)
        self.widget_37.setObjectName(u"widget_37")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_37)
        self.horizontalLayout_28.setSpacing(5)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.widget_50 = QWidget(self.widget_37)
        self.widget_50.setObjectName(u"widget_50")
        self.verticalLayout_50 = QVBoxLayout(self.widget_50)
        self.verticalLayout_50.setSpacing(5)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.btnPostBackMan = QToolButton(self.widget_50)
        self.btnPostBackMan.setObjectName(u"btnPostBackMan")
        sizePolicy.setHeightForWidth(self.btnPostBackMan.sizePolicy().hasHeightForWidth())
        self.btnPostBackMan.setSizePolicy(sizePolicy)
        self.btnPostBackMan.setMinimumSize(QSize(0, 45))
        self.btnPostBackMan.setFont(font5)
        self.btnPostBackMan.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.btnPostBackMan.setIcon(icon6)
        self.btnPostBackMan.setIconSize(QSize(35, 35))
        self.btnPostBackMan.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_50.addWidget(self.btnPostBackMan)

        self.btnPostForwardMan = QToolButton(self.widget_50)
        self.btnPostForwardMan.setObjectName(u"btnPostForwardMan")
        sizePolicy.setHeightForWidth(self.btnPostForwardMan.sizePolicy().hasHeightForWidth())
        self.btnPostForwardMan.setSizePolicy(sizePolicy)
        self.btnPostForwardMan.setMinimumSize(QSize(0, 45))
        self.btnPostForwardMan.setFont(font5)
        self.btnPostForwardMan.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.btnPostForwardMan.setIcon(icon7)
        self.btnPostForwardMan.setIconSize(QSize(35, 35))
        self.btnPostForwardMan.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_50.addWidget(self.btnPostForwardMan)


        self.horizontalLayout_28.addWidget(self.widget_50)

        self.widget_31 = QWidget(self.widget_37)
        self.widget_31.setObjectName(u"widget_31")
        self.verticalLayout_51 = QVBoxLayout(self.widget_31)
        self.verticalLayout_51.setSpacing(5)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.toolButton_25 = QToolButton(self.widget_31)
        self.toolButton_25.setObjectName(u"toolButton_25")
        sizePolicy.setHeightForWidth(self.toolButton_25.sizePolicy().hasHeightForWidth())
        self.toolButton_25.setSizePolicy(sizePolicy)
        self.toolButton_25.setMinimumSize(QSize(0, 45))
        self.toolButton_25.setFont(font5)
        self.toolButton_25.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.toolButton_25.setIcon(icon6)
        self.toolButton_25.setIconSize(QSize(35, 35))
        self.toolButton_25.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_51.addWidget(self.toolButton_25)

        self.toolButton_26 = QToolButton(self.widget_31)
        self.toolButton_26.setObjectName(u"toolButton_26")
        sizePolicy.setHeightForWidth(self.toolButton_26.sizePolicy().hasHeightForWidth())
        self.toolButton_26.setSizePolicy(sizePolicy)
        self.toolButton_26.setMinimumSize(QSize(0, 45))
        self.toolButton_26.setFont(font5)
        self.toolButton_26.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.toolButton_26.setIcon(icon7)
        self.toolButton_26.setIconSize(QSize(35, 35))
        self.toolButton_26.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_51.addWidget(self.toolButton_26)


        self.horizontalLayout_28.addWidget(self.widget_31)


        self.verticalLayout_49.addWidget(self.widget_37)


        self.verticalLayout_47.addWidget(self.frameXPos_5)


        self.horizontalLayout_26.addWidget(self.widget_35)


        self.verticalLayout_44.addWidget(self.widget_33)

        self.stackedWidget.addWidget(self.pageManualMode)
        self.pageCalibration = QWidget()
        self.pageCalibration.setObjectName(u"pageCalibration")
        self.horizontalLayout_17 = QHBoxLayout(self.pageCalibration)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_2 = QLabel(self.pageCalibration)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.pageCalibration)
        self.pageDebug = QWidget()
        self.pageDebug.setObjectName(u"pageDebug")
        self.horizontalLayout_18 = QHBoxLayout(self.pageDebug)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_3 = QLabel(self.pageDebug)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.pageDebug)
        self.pageSettings = QWidget()
        self.pageSettings.setObjectName(u"pageSettings")
        self.verticalLayout_43 = QVBoxLayout(self.pageSettings)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.widget_51 = QWidget(self.pageSettings)
        self.widget_51.setObjectName(u"widget_51")
        self.widget_51.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_24 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_51)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setPixmap(QPixmap(u":/icons/fan.jpg"))

        self.horizontalLayout_24.addWidget(self.label_4)

        self.label_8 = QLabel(self.widget_51)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 40))
        font8 = QFont()
        font8.setPointSize(13)
        font8.setBold(True)
        self.label_8.setFont(font8)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_8)

        self.label_9 = QLabel(self.widget_51)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(40, 40))
        self.label_9.setPixmap(QPixmap(u":/icons/fan.jpg"))

        self.horizontalLayout_24.addWidget(self.label_9)


        self.verticalLayout_43.addWidget(self.widget_51)

        self.widget_52 = QWidget(self.pageSettings)
        self.widget_52.setObjectName(u"widget_52")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_52)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.widget_53 = QWidget(self.widget_52)
        self.widget_53.setObjectName(u"widget_53")
        self.verticalLayout_62 = QVBoxLayout(self.widget_53)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.groupBox_2 = QGroupBox(self.widget_53)
        self.groupBox_2.setObjectName(u"groupBox_2")
        font9 = QFont()
        font9.setPointSize(12)
        font9.setBold(True)
        self.groupBox_2.setFont(font9)
        self.verticalLayout_64 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_64.setSpacing(5)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(10, 10, 10, 10)
        self.radioButton = QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName(u"radioButton")
        font10 = QFont()
        font10.setBold(True)
        self.radioButton.setFont(font10)
        self.radioButton.setStyleSheet(u"QRadioButton {\n"
"    color: #2C3E50;\n"
"    font-size: 12px;\n"
"    padding: 5px;\n"
"    spacing: 8px;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 2px solid #B8C0CC;\n"
"    border-radius: 8px\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    border-color: #4A8AB5;\n"
"}")
        self.radioButton.setChecked(True)

        self.verticalLayout_64.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font10)
        self.radioButton_2.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.radioButton_2.setStyleSheet(u"QRadioButton {\n"
"    color: #2C3E50;\n"
"    font-size: 12px;\n"
"    padding: 5px;\n"
"    spacing: 8px;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 2px solid #B8C0CC;\n"
"    border-radius: 8px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    border-color: #4A8AB5;\n"
"}")
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setAutoRepeat(False)
        self.radioButton_2.setAutoExclusive(True)

        self.verticalLayout_64.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox_2)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font10)
        self.radioButton_3.setStyleSheet(u"QRadioButton {\n"
"\n"
"    color: #2C3E50;\n"
"    font-size: 12px;\n"
"    padding: 5px;\n"
"    spacing: 8px;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 2px solid #B8C0CC;\n"
"    border-radius: 8px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    border-color: #4A8AB5;\n"
"}")

        self.verticalLayout_64.addWidget(self.radioButton_3)


        self.verticalLayout_62.addWidget(self.groupBox_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_62.addItem(self.verticalSpacer_2)


        self.horizontalLayout_25.addWidget(self.widget_53)

        self.widget_54 = QWidget(self.widget_52)
        self.widget_54.setObjectName(u"widget_54")
        self.verticalLayout_63 = QVBoxLayout(self.widget_54)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.groupBox_3 = QGroupBox(self.widget_54)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font9)
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.label_32 = QLabel(self.groupBox_3)
        self.label_32.setObjectName(u"label_32")
        font11 = QFont()
        font11.setPointSize(10)
        font11.setBold(False)
        self.label_32.setFont(font11)

        self.gridLayout_3.addWidget(self.label_32, 0, 0, 1, 1)

        self.fanSpeed = QSlider(self.groupBox_3)
        self.fanSpeed.setObjectName(u"fanSpeed")
        self.fanSpeed.setMinimumSize(QSize(0, 40))
        self.fanSpeed.setFont(font)
        self.fanSpeed.setStyleSheet(u"/* \u0414\u043e\u0440\u043e\u0436\u043a\u0430 */\n"
"QSlider::groove:horizontal {\n"
"    height: 8px;\n"
"    background: #d5d8df;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u0437\u0443\u043d\u043e\u043a (\u043a\u0440\u0443\u0436\u043e\u043a) */\n"
"QSlider::handle:horizontal {\n"
"    background: #bdcfdd;\n"
"    border: 2px solid #a6b8c6;\n"
"    border-radius: 20px;      /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 = \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u0430 \u0448\u0438\u0440\u0438\u043d\u044b \u0434\u043b\u044f \u043a\u0440\u0443\u0433\u0430 */\n"
"    width: 40px;\n"
"    height: 40px;\n"
"    margin: -16px 0;          /* (40-8)/2 = 16 */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #cfddeb;\n"
"    border-color: #4A8AB5;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background: #4A8AB5;\n"
"    border-color: #2c6a8f;\n"
"}\n"
"\n"
"/* \u0417\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u0430\u044f \u0447\u0430\u0441"
                        "\u0442\u044c */\n"
"QSlider::sub-page:horizontal {\n"
"    background: #4A8AB5;\n"
"    border-radius: 4px;\n"
"}")
        self.fanSpeed.setMaximum(100)
        self.fanSpeed.setValue(50)
        self.fanSpeed.setOrientation(Qt.Orientation.Horizontal)
        self.fanSpeed.setInvertedAppearance(False)
        self.fanSpeed.setInvertedControls(False)

        self.gridLayout_3.addWidget(self.fanSpeed, 1, 0, 1, 1)

        self.lblFanSpeed = QLabel(self.groupBox_3)
        self.lblFanSpeed.setObjectName(u"lblFanSpeed")
        self.lblFanSpeed.setMinimumSize(QSize(40, 0))
        self.lblFanSpeed.setMaximumSize(QSize(30, 16777215))
        font12 = QFont()
        font12.setPointSize(9)
        font12.setBold(False)
        self.lblFanSpeed.setFont(font12)

        self.gridLayout_3.addWidget(self.lblFanSpeed, 1, 1, 1, 1)


        self.verticalLayout_63.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.widget_54)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font9)
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_34 = QLabel(self.groupBox_4)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font12)

        self.gridLayout_4.addWidget(self.label_34, 0, 0, 1, 1)

        self.tempMin = QSpinBox(self.groupBox_4)
        self.tempMin.setObjectName(u"tempMin")
        self.tempMin.setMinimumSize(QSize(0, 40))
        self.tempMin.setMaximumSize(QSize(110, 16777215))
        self.tempMin.setFont(font12)
        self.tempMin.setMinimum(20)
        self.tempMin.setMaximum(100)

        self.gridLayout_4.addWidget(self.tempMin, 0, 1, 1, 1)

        self.label_51 = QLabel(self.groupBox_4)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMaximumSize(QSize(30, 16777215))
        self.label_51.setFont(font12)

        self.gridLayout_4.addWidget(self.label_51, 0, 2, 1, 1)

        self.label_35 = QLabel(self.groupBox_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font12)

        self.gridLayout_4.addWidget(self.label_35, 1, 0, 1, 1)

        self.tempMax = QSpinBox(self.groupBox_4)
        self.tempMax.setObjectName(u"tempMax")
        self.tempMax.setMinimumSize(QSize(101, 40))
        self.tempMax.setMaximumSize(QSize(90, 16777215))
        self.tempMax.setFont(font12)
        self.tempMax.setMinimum(40)

        self.gridLayout_4.addWidget(self.tempMax, 1, 1, 1, 1)

        self.label_52 = QLabel(self.groupBox_4)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font12)

        self.gridLayout_4.addWidget(self.label_52, 1, 2, 1, 1)

        self.label_50 = QLabel(self.groupBox_4)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font12)

        self.gridLayout_4.addWidget(self.label_50, 2, 0, 1, 1)

        self.startSpeed = QSpinBox(self.groupBox_4)
        self.startSpeed.setObjectName(u"startSpeed")
        self.startSpeed.setMinimumSize(QSize(0, 40))
        self.startSpeed.setMaximumSize(QSize(110, 16777215))
        self.startSpeed.setFont(font12)
        self.startSpeed.setMinimum(5)
        self.startSpeed.setMaximum(40)

        self.gridLayout_4.addWidget(self.startSpeed, 2, 1, 1, 1)

        self.label_53 = QLabel(self.groupBox_4)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font12)

        self.gridLayout_4.addWidget(self.label_53, 2, 2, 1, 1)


        self.verticalLayout_63.addWidget(self.groupBox_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_63.addItem(self.verticalSpacer_3)


        self.horizontalLayout_25.addWidget(self.widget_54)


        self.verticalLayout_43.addWidget(self.widget_52)

        self.stackedWidget.addWidget(self.pageSettings)
        self.pageLinear = QWidget()
        self.pageLinear.setObjectName(u"pageLinear")
        self.verticalLayout_4 = QVBoxLayout(self.pageLinear)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_3 = QWidget(self.pageLinear)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 200))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.widget_5)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 50))
        self.label_6.setFont(font9)
        self.label_6.setStyleSheet(u"QLabel {\n"
"	padding-left: 10px;\n"
"}")
        self.label_6.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_6)

        self.frameLin = QFrame(self.widget_5)
        self.frameLin.setObjectName(u"frameLin")
        self.frameLin.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameLin {\n"
"	background: #e9ecf1;\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.frameLin.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLin.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frameLin)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.btnLinForward = QToolButton(self.frameLin)
        self.btnLinForward.setObjectName(u"btnLinForward")
        sizePolicy.setHeightForWidth(self.btnLinForward.sizePolicy().hasHeightForWidth())
        self.btnLinForward.setSizePolicy(sizePolicy)
        self.btnLinForward.setMinimumSize(QSize(0, 60))
        self.btnLinForward.setFont(font9)
        self.btnLinForward.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.btnLinForward.setIcon(icon)
        self.btnLinForward.setIconSize(QSize(50, 50))
        self.btnLinForward.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_10.addWidget(self.btnLinForward)

        self.btnLinBack = QToolButton(self.frameLin)
        self.btnLinBack.setObjectName(u"btnLinBack")
        sizePolicy.setHeightForWidth(self.btnLinBack.sizePolicy().hasHeightForWidth())
        self.btnLinBack.setSizePolicy(sizePolicy)
        self.btnLinBack.setMinimumSize(QSize(0, 60))
        self.btnLinBack.setFont(font9)
        self.btnLinBack.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.btnLinBack.setIcon(icon1)
        self.btnLinBack.setIconSize(QSize(50, 50))
        self.btnLinBack.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_10.addWidget(self.btnLinBack)

        self.lblLinSpeed = QLabel(self.frameLin)
        self.lblLinSpeed.setObjectName(u"lblLinSpeed")
        self.lblLinSpeed.setMaximumSize(QSize(16777215, 30))
        self.lblLinSpeed.setFont(font5)
        self.lblLinSpeed.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_10.addWidget(self.lblLinSpeed)

        self.linSpeed = QSlider(self.frameLin)
        self.linSpeed.setObjectName(u"linSpeed")
        self.linSpeed.setMinimumSize(QSize(0, 30))
        self.linSpeed.setStyleSheet(u"/* \u0414\u043e\u0440\u043e\u0436\u043a\u0430 */\n"
"QSlider::groove:horizontal {\n"
"    height: 8px;\n"
"    background: #d5d8df;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u0437\u0443\u043d\u043e\u043a (\u043a\u0440\u0443\u0436\u043e\u043a) */\n"
"QSlider::handle:horizontal {\n"
"    background: #bdcfdd;\n"
"    border: 2px solid #a6b8c6;\n"
"    border-radius: 10px;      /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 = \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u0430 \u0448\u0438\u0440\u0438\u043d\u044b \u0434\u043b\u044f \u043a\u0440\u0443\u0433\u0430 */\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    margin: -8px 0;          /* (40-8)/2 = 16 */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #cfddeb;\n"
"    border-color: #4A8AB5;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background: #4A8AB5;\n"
"    border-color: #2c6a8f;\n"
"}\n"
"\n"
"/* \u0417\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u0430\u044f \u0447\u0430\u0441"
                        "\u0442\u044c */\n"
"QSlider::sub-page:horizontal {\n"
"    background: #4A8AB5;\n"
"    border-radius: 4px;\n"
"}")
        self.linSpeed.setMinimum(1)
        self.linSpeed.setMaximum(100)
        self.linSpeed.setValue(30)
        self.linSpeed.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_10.addWidget(self.linSpeed)

        self.btnSetLinSpeed = QPushButton(self.frameLin)
        self.btnSetLinSpeed.setObjectName(u"btnSetLinSpeed")
        self.btnSetLinSpeed.setMinimumSize(QSize(0, 30))
        self.btnSetLinSpeed.setStyleSheet(u"QPushButton {\n"
"	background: #d5d8df;\n"
"	border: 2px solid #babec7;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_10.addWidget(self.btnSetLinSpeed)


        self.verticalLayout_8.addWidget(self.frameLin)


        self.horizontalLayout_3.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 0))
        self.widget_6.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.widget_6)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.framePos = QFrame(self.widget_6)
        self.framePos.setObjectName(u"framePos")
        self.framePos.setMinimumSize(QSize(0, 135))
        self.framePos.setMaximumSize(QSize(16777215, 135))
        self.framePos.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#framePos {\n"
"	\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.framePos.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePos.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.framePos)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 10, 10, 5)
        self.label_11 = QLabel(self.framePos)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 30))
        font13 = QFont()
        font13.setPointSize(11)
        self.label_11.setFont(font13)

        self.verticalLayout_9.addWidget(self.label_11)

        self.lblLinPos = QLabel(self.framePos)
        self.lblLinPos.setObjectName(u"lblLinPos")
        self.lblLinPos.setMaximumSize(QSize(16777215, 40))
        font14 = QFont()
        font14.setPointSize(30)
        font14.setBold(True)
        self.lblLinPos.setFont(font14)

        self.verticalLayout_9.addWidget(self.lblLinPos)

        self.line_2 = QFrame(self.framePos)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"Line {\n"
"	border: 1px solid #ced3d7;\n"
"}")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line_2)

        self.btnResLinPos = QPushButton(self.framePos)
        self.btnResLinPos.setObjectName(u"btnResLinPos")
        self.btnResLinPos.setMinimumSize(QSize(0, 25))
        self.btnResLinPos.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_9.addWidget(self.btnResLinPos)


        self.verticalLayout_7.addWidget(self.framePos)

        self.frameXPos = QFrame(self.widget_6)
        self.frameXPos.setObjectName(u"frameXPos")
        self.frameXPos.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameXPos {\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.frameXPos.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameXPos.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frameXPos)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_14 = QLabel(self.frameXPos)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 25))
        self.label_14.setFont(font2)

        self.verticalLayout_11.addWidget(self.label_14)

        self.widget_7 = QWidget(self.frameXPos)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btnBackLin5mm = QPushButton(self.widget_7)
        self.btnBackLin5mm.setObjectName(u"btnBackLin5mm")
        self.btnBackLin5mm.setMinimumSize(QSize(0, 40))
        self.btnBackLin5mm.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.horizontalLayout_5.addWidget(self.btnBackLin5mm)

        self.btnBackLin1mm = QPushButton(self.widget_7)
        self.btnBackLin1mm.setObjectName(u"btnBackLin1mm")
        self.btnBackLin1mm.setMinimumSize(QSize(0, 40))
        self.btnBackLin1mm.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.horizontalLayout_5.addWidget(self.btnBackLin1mm)

        self.btnForwardLin1mm = QPushButton(self.widget_7)
        self.btnForwardLin1mm.setObjectName(u"btnForwardLin1mm")
        self.btnForwardLin1mm.setMinimumSize(QSize(0, 40))
        self.btnForwardLin1mm.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.horizontalLayout_5.addWidget(self.btnForwardLin1mm)

        self.btnForwardLin5mm = QPushButton(self.widget_7)
        self.btnForwardLin5mm.setObjectName(u"btnForwardLin5mm")
        self.btnForwardLin5mm.setMinimumSize(QSize(0, 40))
        self.btnForwardLin5mm.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.horizontalLayout_5.addWidget(self.btnForwardLin5mm)


        self.verticalLayout_11.addWidget(self.widget_7)

        self.exLinPos = QSpinBox(self.frameXPos)
        self.exLinPos.setObjectName(u"exLinPos")
        self.exLinPos.setMinimumSize(QSize(0, 30))

        self.verticalLayout_11.addWidget(self.exLinPos)

        self.widget_8 = QWidget(self.frameXPos)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btnLinBackEx = QToolButton(self.widget_8)
        self.btnLinBackEx.setObjectName(u"btnLinBackEx")
        sizePolicy.setHeightForWidth(self.btnLinBackEx.sizePolicy().hasHeightForWidth())
        self.btnLinBackEx.setSizePolicy(sizePolicy)
        self.btnLinBackEx.setMinimumSize(QSize(0, 45))
        self.btnLinBackEx.setFont(font5)
        self.btnLinBackEx.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.btnLinBackEx.setIcon(icon1)
        self.btnLinBackEx.setIconSize(QSize(35, 35))
        self.btnLinBackEx.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_6.addWidget(self.btnLinBackEx)

        self.btnLinForwardEx = QToolButton(self.widget_8)
        self.btnLinForwardEx.setObjectName(u"btnLinForwardEx")
        sizePolicy.setHeightForWidth(self.btnLinForwardEx.sizePolicy().hasHeightForWidth())
        self.btnLinForwardEx.setSizePolicy(sizePolicy)
        self.btnLinForwardEx.setMinimumSize(QSize(0, 45))
        self.btnLinForwardEx.setFont(font5)
        self.btnLinForwardEx.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.btnLinForwardEx.setIcon(icon)
        self.btnLinForwardEx.setIconSize(QSize(35, 35))
        self.btnLinForwardEx.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_6.addWidget(self.btnLinForwardEx)


        self.verticalLayout_11.addWidget(self.widget_8)


        self.verticalLayout_7.addWidget(self.frameXPos)


        self.horizontalLayout_3.addWidget(self.widget_6)

        self.framePosAndHome = QFrame(self.widget_3)
        self.framePosAndHome.setObjectName(u"framePosAndHome")
        self.framePosAndHome.setMaximumSize(QSize(200, 16777215))
        self.framePosAndHome.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#framePosAndHome {\n"
"	\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.framePosAndHome.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePosAndHome.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.framePosAndHome)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btnLinHome = QToolButton(self.framePosAndHome)
        self.btnLinHome.setObjectName(u"btnLinHome")
        sizePolicy.setHeightForWidth(self.btnLinHome.sizePolicy().hasHeightForWidth())
        self.btnLinHome.setSizePolicy(sizePolicy)
        self.btnLinHome.setMinimumSize(QSize(0, 90))
        self.btnLinHome.setFont(font9)
        self.btnLinHome.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.btnLinHome.setIcon(icon2)
        self.btnLinHome.setIconSize(QSize(50, 50))
        self.btnLinHome.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_6.addWidget(self.btnLinHome)

        self.line = QFrame(self.framePosAndHome)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"Line {\n"
"	border: 1px solid #ced3d7;\n"
"}")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.btnSaveLinPos1 = QPushButton(self.framePosAndHome)
        self.btnSaveLinPos1.setObjectName(u"btnSaveLinPos1")
        self.btnSaveLinPos1.setMinimumSize(QSize(0, 40))
        self.btnSaveLinPos1.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_6.addWidget(self.btnSaveLinPos1)

        self.btnSaveLinPos2 = QPushButton(self.framePosAndHome)
        self.btnSaveLinPos2.setObjectName(u"btnSaveLinPos2")
        self.btnSaveLinPos2.setMinimumSize(QSize(0, 40))
        self.btnSaveLinPos2.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_6.addWidget(self.btnSaveLinPos2)

        self.btnGoLinPos1 = QPushButton(self.framePosAndHome)
        self.btnGoLinPos1.setObjectName(u"btnGoLinPos1")
        self.btnGoLinPos1.setMinimumSize(QSize(0, 40))
        self.btnGoLinPos1.setFont(font6)
        self.btnGoLinPos1.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_6.addWidget(self.btnGoLinPos1)

        self.btnGoLinPos2 = QPushButton(self.framePosAndHome)
        self.btnGoLinPos2.setObjectName(u"btnGoLinPos2")
        self.btnGoLinPos2.setMinimumSize(QSize(0, 40))
        self.btnGoLinPos2.setFont(font6)
        self.btnGoLinPos2.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_6.addWidget(self.btnGoLinPos2)


        self.horizontalLayout_3.addWidget(self.framePosAndHome)


        self.verticalLayout_4.addWidget(self.widget_3)

        self.frameLogs = QFrame(self.pageLinear)
        self.frameLogs.setObjectName(u"frameLogs")
        self.frameLogs.setMaximumSize(QSize(16777215, 190))
        self.frameLogs.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameLogs {\n"
"	\n"
"	border-radius: 7px;\n"
"	border: 1px solid #cdced2;\n"
"}")
        self.frameLogs.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLogs.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frameLogs)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 5, 10, 10)
        self.widget_4 = QWidget(self.frameLogs)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 5, 0, 5)
        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.horizontalSpacer_2 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addWidget(self.widget_4)

        self.plainLogLin = QPlainTextEdit(self.frameLogs)
        self.plainLogLin.setObjectName(u"plainLogLin")
        self.plainLogLin.setMaximumSize(QSize(16777215, 160))
        self.plainLogLin.setStyleSheet(u"QPlainTextEdit {\n"
"	padding: 5px;\n"
"	border: 1px solid #e0e1e6;\n"
"	background-color: #f3f4f6;\n"
"	border-radius: 7px;\n"
"}\n"
"")
        self.plainLogLin.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.plainLogLin.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.plainLogLin.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.plainLogLin.setTabChangesFocus(False)
        self.plainLogLin.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.plainLogLin.setReadOnly(True)
        self.plainLogLin.setOverwriteMode(False)
        self.plainLogLin.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_5.addWidget(self.plainLogLin)


        self.verticalLayout_4.addWidget(self.frameLogs)

        self.stackedWidget.addWidget(self.pageLinear)
        self.pageFixation = QWidget()
        self.pageFixation.setObjectName(u"pageFixation")
        self.verticalLayout_29 = QVBoxLayout(self.pageFixation)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.widget_16 = QWidget(self.pageFixation)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(0, 200))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_17 = QWidget(self.widget_16)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_21 = QVBoxLayout(self.widget_17)
        self.verticalLayout_21.setSpacing(10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.widget_17)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 50))
        self.label_20.setFont(font9)
        self.label_20.setStyleSheet(u"QLabel {\n"
"	padding-left: 10px;\n"
"}")
        self.label_20.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.label_20)

        self.frameLin_3 = QFrame(self.widget_17)
        self.frameLin_3.setObjectName(u"frameLin_3")
        self.frameLin_3.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameLin {\n"
"	background: #e9ecf1;\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.frameLin_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLin_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frameLin_3)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.btnFixForward = QToolButton(self.frameLin_3)
        self.btnFixForward.setObjectName(u"btnFixForward")
        sizePolicy.setHeightForWidth(self.btnFixForward.sizePolicy().hasHeightForWidth())
        self.btnFixForward.setSizePolicy(sizePolicy)
        self.btnFixForward.setMinimumSize(QSize(0, 60))
        self.btnFixForward.setFont(font9)
        self.btnFixForward.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.btnFixForward.setIcon(icon7)
        self.btnFixForward.setIconSize(QSize(50, 50))
        self.btnFixForward.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_22.addWidget(self.btnFixForward)

        self.btnFixBack = QToolButton(self.frameLin_3)
        self.btnFixBack.setObjectName(u"btnFixBack")
        sizePolicy.setHeightForWidth(self.btnFixBack.sizePolicy().hasHeightForWidth())
        self.btnFixBack.setSizePolicy(sizePolicy)
        self.btnFixBack.setMinimumSize(QSize(0, 60))
        self.btnFixBack.setFont(font9)
        self.btnFixBack.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.btnFixBack.setIcon(icon6)
        self.btnFixBack.setIconSize(QSize(50, 50))
        self.btnFixBack.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_22.addWidget(self.btnFixBack)

        self.lblFixSpeed = QLabel(self.frameLin_3)
        self.lblFixSpeed.setObjectName(u"lblFixSpeed")
        self.lblFixSpeed.setMaximumSize(QSize(16777215, 30))
        self.lblFixSpeed.setFont(font2)
        self.lblFixSpeed.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_22.addWidget(self.lblFixSpeed)

        self.fixSpeed = QSlider(self.frameLin_3)
        self.fixSpeed.setObjectName(u"fixSpeed")
        self.fixSpeed.setMinimumSize(QSize(0, 30))
        self.fixSpeed.setStyleSheet(u"/* \u0414\u043e\u0440\u043e\u0436\u043a\u0430 */\n"
"QSlider::groove:horizontal {\n"
"    height: 8px;\n"
"    background: #d5d8df;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u0437\u0443\u043d\u043e\u043a (\u043a\u0440\u0443\u0436\u043e\u043a) */\n"
"QSlider::handle:horizontal {\n"
"    background: #bdcfdd;\n"
"    border: 2px solid #a6b8c6;\n"
"    border-radius: 10px;      /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 = \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u0430 \u0448\u0438\u0440\u0438\u043d\u044b \u0434\u043b\u044f \u043a\u0440\u0443\u0433\u0430 */\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    margin: -8px 0;          /* (40-8)/2 = 16 */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #cfddeb;\n"
"    border-color: #4A8AB5;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background: #4A8AB5;\n"
"    border-color: #2c6a8f;\n"
"}\n"
"\n"
"/* \u0417\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u0430\u044f \u0447\u0430\u0441"
                        "\u0442\u044c */\n"
"QSlider::sub-page:horizontal {\n"
"    background: #4A8AB5;\n"
"    border-radius: 4px;\n"
"}")
        self.fixSpeed.setMinimum(1)
        self.fixSpeed.setMaximum(100)
        self.fixSpeed.setValue(30)
        self.fixSpeed.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_22.addWidget(self.fixSpeed)

        self.btnSetFixSpeed = QPushButton(self.frameLin_3)
        self.btnSetFixSpeed.setObjectName(u"btnSetFixSpeed")
        self.btnSetFixSpeed.setMinimumSize(QSize(0, 30))
        self.btnSetFixSpeed.setStyleSheet(u"QPushButton {\n"
"	background: #d5d8df;\n"
"	border: 2px solid #babec7;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_22.addWidget(self.btnSetFixSpeed)


        self.verticalLayout_21.addWidget(self.frameLin_3)


        self.horizontalLayout_12.addWidget(self.widget_17)

        self.widget_18 = QWidget(self.widget_16)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(0, 0))
        self.widget_18.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_23 = QVBoxLayout(self.widget_18)
        self.verticalLayout_23.setSpacing(10)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.framePos_3 = QFrame(self.widget_18)
        self.framePos_3.setObjectName(u"framePos_3")
        self.framePos_3.setMinimumSize(QSize(0, 135))
        self.framePos_3.setMaximumSize(QSize(16777215, 135))
        self.framePos_3.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#framePos {\n"
"	\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.framePos_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePos_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.framePos_3)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(10, 10, 10, 5)
        self.label_21 = QLabel(self.framePos_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 30))
        self.label_21.setFont(font13)

        self.verticalLayout_24.addWidget(self.label_21)

        self.label_22 = QLabel(self.framePos_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(16777215, 40))
        self.label_22.setFont(font14)

        self.verticalLayout_24.addWidget(self.label_22)


        self.verticalLayout_23.addWidget(self.framePos_3)

        self.frameXPos_3 = QFrame(self.widget_18)
        self.frameXPos_3.setObjectName(u"frameXPos_3")
        self.frameXPos_3.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameXPos {\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.frameXPos_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameXPos_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frameXPos_3)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_23 = QLabel(self.frameXPos_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 25))
        self.label_23.setFont(font2)

        self.verticalLayout_25.addWidget(self.label_23)

        self.widget_19 = QWidget(self.frameXPos_3)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.btnBackFix5grad = QPushButton(self.widget_19)
        self.btnBackFix5grad.setObjectName(u"btnBackFix5grad")
        self.btnBackFix5grad.setMinimumSize(QSize(0, 40))
        self.btnBackFix5grad.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.horizontalLayout_13.addWidget(self.btnBackFix5grad)

        self.btnBackFix1grad = QPushButton(self.widget_19)
        self.btnBackFix1grad.setObjectName(u"btnBackFix1grad")
        self.btnBackFix1grad.setMinimumSize(QSize(0, 40))
        self.btnBackFix1grad.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.horizontalLayout_13.addWidget(self.btnBackFix1grad)

        self.btnForwardFix1grad = QPushButton(self.widget_19)
        self.btnForwardFix1grad.setObjectName(u"btnForwardFix1grad")
        self.btnForwardFix1grad.setMinimumSize(QSize(0, 40))
        self.btnForwardFix1grad.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.horizontalLayout_13.addWidget(self.btnForwardFix1grad)

        self.btnForwardFix5grad = QPushButton(self.widget_19)
        self.btnForwardFix5grad.setObjectName(u"btnForwardFix5grad")
        self.btnForwardFix5grad.setMinimumSize(QSize(0, 40))
        self.btnForwardFix5grad.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.horizontalLayout_13.addWidget(self.btnForwardFix5grad)


        self.verticalLayout_25.addWidget(self.widget_19)

        self.exFixPos = QSpinBox(self.frameXPos_3)
        self.exFixPos.setObjectName(u"exFixPos")
        self.exFixPos.setMinimumSize(QSize(0, 30))
        self.exFixPos.setMinimum(1)
        self.exFixPos.setMaximum(360)

        self.verticalLayout_25.addWidget(self.exFixPos)

        self.widget_20 = QWidget(self.frameXPos_3)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.btnFixBackEx = QToolButton(self.widget_20)
        self.btnFixBackEx.setObjectName(u"btnFixBackEx")
        sizePolicy.setHeightForWidth(self.btnFixBackEx.sizePolicy().hasHeightForWidth())
        self.btnFixBackEx.setSizePolicy(sizePolicy)
        self.btnFixBackEx.setMinimumSize(QSize(0, 45))
        self.btnFixBackEx.setFont(font5)
        self.btnFixBackEx.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.btnFixBackEx.setIcon(icon6)
        self.btnFixBackEx.setIconSize(QSize(35, 35))
        self.btnFixBackEx.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_14.addWidget(self.btnFixBackEx)

        self.btnFixForwardEx = QToolButton(self.widget_20)
        self.btnFixForwardEx.setObjectName(u"btnFixForwardEx")
        sizePolicy.setHeightForWidth(self.btnFixForwardEx.sizePolicy().hasHeightForWidth())
        self.btnFixForwardEx.setSizePolicy(sizePolicy)
        self.btnFixForwardEx.setMinimumSize(QSize(0, 45))
        self.btnFixForwardEx.setFont(font5)
        self.btnFixForwardEx.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.btnFixForwardEx.setIcon(icon7)
        self.btnFixForwardEx.setIconSize(QSize(35, 35))
        self.btnFixForwardEx.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_14.addWidget(self.btnFixForwardEx)


        self.verticalLayout_25.addWidget(self.widget_20)


        self.verticalLayout_23.addWidget(self.frameXPos_3)


        self.horizontalLayout_12.addWidget(self.widget_18)

        self.framePosAndHome_3 = QFrame(self.widget_16)
        self.framePosAndHome_3.setObjectName(u"framePosAndHome_3")
        self.framePosAndHome_3.setMaximumSize(QSize(200, 16777215))
        self.framePosAndHome_3.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#framePosAndHome {\n"
"	\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.framePosAndHome_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePosAndHome_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.framePosAndHome_3)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.btnFixHome = QToolButton(self.framePosAndHome_3)
        self.btnFixHome.setObjectName(u"btnFixHome")
        sizePolicy.setHeightForWidth(self.btnFixHome.sizePolicy().hasHeightForWidth())
        self.btnFixHome.setSizePolicy(sizePolicy)
        self.btnFixHome.setMinimumSize(QSize(0, 120))
        self.btnFixHome.setFont(font9)
        self.btnFixHome.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.btnFixHome.setIcon(icon2)
        self.btnFixHome.setIconSize(QSize(80, 80))
        self.btnFixHome.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_26.addWidget(self.btnFixHome)

        self.line_7 = QFrame(self.framePosAndHome_3)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"Line {\n"
"	border: 1px solid #ced3d7;\n"
"}")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_26.addWidget(self.line_7)

        self.pushButton_26 = QPushButton(self.framePosAndHome_3)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(0, 40))
        self.pushButton_26.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_26.addWidget(self.pushButton_26)

        self.pushButton_27 = QPushButton(self.framePosAndHome_3)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setMinimumSize(QSize(0, 40))
        self.pushButton_27.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_26.addWidget(self.pushButton_27)

        self.pushButton_29 = QPushButton(self.framePosAndHome_3)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setMinimumSize(QSize(0, 40))
        self.pushButton_29.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_26.addWidget(self.pushButton_29)


        self.horizontalLayout_12.addWidget(self.framePosAndHome_3)


        self.verticalLayout_29.addWidget(self.widget_16)

        self.widget_21 = QWidget(self.pageFixation)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frameLogs_3 = QFrame(self.widget_21)
        self.frameLogs_3.setObjectName(u"frameLogs_3")
        self.frameLogs_3.setMaximumSize(QSize(16777215, 190))
        self.frameLogs_3.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameLogs {\n"
"	\n"
"	border-radius: 7px;\n"
"	border: 1px solid #cdced2;\n"
"}")
        self.frameLogs_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLogs_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frameLogs_3)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(10, 5, 10, 10)
        self.widget_22 = QWidget(self.frameLogs_3)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_16 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 5, 0, 5)
        self.label_26 = QLabel(self.widget_22)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_16.addWidget(self.label_26)

        self.horizontalSpacer_4 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_4)


        self.verticalLayout_27.addWidget(self.widget_22)

        self.plainLogFix = QPlainTextEdit(self.frameLogs_3)
        self.plainLogFix.setObjectName(u"plainLogFix")
        self.plainLogFix.setMaximumSize(QSize(16777215, 160))
        self.plainLogFix.setStyleSheet(u"QPlainTextEdit {\n"
"	padding: 5px;\n"
"	border: 1px solid #e0e1e6;\n"
"	background-color: #f3f4f6;\n"
"	border-radius: 7px;\n"
"}\n"
"")
        self.plainLogFix.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.plainLogFix.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.plainLogFix.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.plainLogFix.setTabChangesFocus(False)
        self.plainLogFix.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.plainLogFix.setReadOnly(True)
        self.plainLogFix.setOverwriteMode(False)
        self.plainLogFix.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_27.addWidget(self.plainLogFix)


        self.horizontalLayout_15.addWidget(self.frameLogs_3)

        self.framePreCrimpGraph_2 = QFrame(self.widget_21)
        self.framePreCrimpGraph_2.setObjectName(u"framePreCrimpGraph_2")
        self.framePreCrimpGraph_2.setMinimumSize(QSize(155, 155))
        self.framePreCrimpGraph_2.setMaximumSize(QSize(16777215, 155))
        self.framePreCrimpGraph_2.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#framePreCrimpGraph {\n"
"	\n"
"	border-radius: 7px;\n"
"	border: 1px solid #cdced2;\n"
"}")
        self.framePreCrimpGraph_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePreCrimpGraph_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.framePreCrimpGraph_2)
        self.verticalLayout_28.setSpacing(5)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(5, 5, 5, 5)
        self.pushButton_28 = QPushButton(self.framePreCrimpGraph_2)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setMinimumSize(QSize(0, 26))
        self.pushButton_28.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_28.addWidget(self.pushButton_28)

        self.graphPreCrimp_2 = QChartView(self.framePreCrimpGraph_2)
        self.graphPreCrimp_2.setObjectName(u"graphPreCrimp_2")

        self.verticalLayout_28.addWidget(self.graphPreCrimp_2)


        self.horizontalLayout_15.addWidget(self.framePreCrimpGraph_2)


        self.verticalLayout_29.addWidget(self.widget_21)

        self.stackedWidget.addWidget(self.pageFixation)
        self.pagePreCrimp = QWidget()
        self.pagePreCrimp.setObjectName(u"pagePreCrimp")
        self.verticalLayout_19 = QVBoxLayout(self.pagePreCrimp)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_9 = QWidget(self.pagePreCrimp)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 200))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_12 = QVBoxLayout(self.widget_10)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 50))
        self.label_7.setFont(font9)
        self.label_7.setStyleSheet(u"QLabel {\n"
"	padding-left: 10px;\n"
"}")
        self.label_7.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.label_7)

        self.frameLin_2 = QFrame(self.widget_10)
        self.frameLin_2.setObjectName(u"frameLin_2")
        self.frameLin_2.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameLin {\n"
"	background: #e9ecf1;\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.frameLin_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLin_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frameLin_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.btnPreUp = QToolButton(self.frameLin_2)
        self.btnPreUp.setObjectName(u"btnPreUp")
        sizePolicy.setHeightForWidth(self.btnPreUp.sizePolicy().hasHeightForWidth())
        self.btnPreUp.setSizePolicy(sizePolicy)
        self.btnPreUp.setMinimumSize(QSize(0, 60))
        self.btnPreUp.setFont(font9)
        self.btnPreUp.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.btnPreUp.setIcon(icon3)
        self.btnPreUp.setIconSize(QSize(50, 50))
        self.btnPreUp.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_13.addWidget(self.btnPreUp)

        self.btnDownBack = QToolButton(self.frameLin_2)
        self.btnDownBack.setObjectName(u"btnDownBack")
        sizePolicy.setHeightForWidth(self.btnDownBack.sizePolicy().hasHeightForWidth())
        self.btnDownBack.setSizePolicy(sizePolicy)
        self.btnDownBack.setMinimumSize(QSize(0, 60))
        self.btnDownBack.setFont(font9)
        self.btnDownBack.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.btnDownBack.setIcon(icon4)
        self.btnDownBack.setIconSize(QSize(50, 50))
        self.btnDownBack.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_13.addWidget(self.btnDownBack)

        self.lblPreSpeed = QLabel(self.frameLin_2)
        self.lblPreSpeed.setObjectName(u"lblPreSpeed")
        self.lblPreSpeed.setMaximumSize(QSize(16777215, 30))
        self.lblPreSpeed.setFont(font5)
        self.lblPreSpeed.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_13.addWidget(self.lblPreSpeed)

        self.preSpeed = QSlider(self.frameLin_2)
        self.preSpeed.setObjectName(u"preSpeed")
        self.preSpeed.setMinimumSize(QSize(0, 30))
        self.preSpeed.setStyleSheet(u"/* \u0414\u043e\u0440\u043e\u0436\u043a\u0430 */\n"
"QSlider::groove:horizontal {\n"
"    height: 8px;\n"
"    background: #d5d8df;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u0437\u0443\u043d\u043e\u043a (\u043a\u0440\u0443\u0436\u043e\u043a) */\n"
"QSlider::handle:horizontal {\n"
"    background: #bdcfdd;\n"
"    border: 2px solid #a6b8c6;\n"
"    border-radius: 10px;      /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 = \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u0430 \u0448\u0438\u0440\u0438\u043d\u044b \u0434\u043b\u044f \u043a\u0440\u0443\u0433\u0430 */\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    margin: -8px 0;          /* (40-8)/2 = 16 */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #cfddeb;\n"
"    border-color: #4A8AB5;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background: #4A8AB5;\n"
"    border-color: #2c6a8f;\n"
"}\n"
"\n"
"/* \u0417\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u0430\u044f \u0447\u0430\u0441"
                        "\u0442\u044c */\n"
"QSlider::sub-page:horizontal {\n"
"    background: #4A8AB5;\n"
"    border-radius: 4px;\n"
"}")
        self.preSpeed.setMinimum(1)
        self.preSpeed.setMaximum(100)
        self.preSpeed.setValue(30)
        self.preSpeed.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_13.addWidget(self.preSpeed)

        self.btnSetPreSpeed = QPushButton(self.frameLin_2)
        self.btnSetPreSpeed.setObjectName(u"btnSetPreSpeed")
        self.btnSetPreSpeed.setMinimumSize(QSize(0, 30))
        self.btnSetPreSpeed.setStyleSheet(u"QPushButton {\n"
"	background: #d5d8df;\n"
"	border: 2px solid #babec7;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_13.addWidget(self.btnSetPreSpeed)


        self.verticalLayout_12.addWidget(self.frameLin_2)


        self.horizontalLayout_7.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 0))
        self.widget_11.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_14 = QVBoxLayout(self.widget_11)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.framePos_2 = QFrame(self.widget_11)
        self.framePos_2.setObjectName(u"framePos_2")
        self.framePos_2.setMinimumSize(QSize(0, 135))
        self.framePos_2.setMaximumSize(QSize(16777215, 135))
        self.framePos_2.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#framePos {\n"
"	\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.framePos_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePos_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.framePos_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 5)
        self.label_13 = QLabel(self.framePos_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 30))
        self.label_13.setFont(font13)

        self.verticalLayout_15.addWidget(self.label_13)

        self.lblPrePos = QLabel(self.framePos_2)
        self.lblPrePos.setObjectName(u"lblPrePos")
        self.lblPrePos.setMaximumSize(QSize(16777215, 40))
        self.lblPrePos.setFont(font14)

        self.verticalLayout_15.addWidget(self.lblPrePos)

        self.line_3 = QFrame(self.framePos_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"Line {\n"
"	border: 1px solid #ced3d7;\n"
"}")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_15.addWidget(self.line_3)

        self.btnResPrePos = QPushButton(self.framePos_2)
        self.btnResPrePos.setObjectName(u"btnResPrePos")
        self.btnResPrePos.setMinimumSize(QSize(0, 25))
        self.btnResPrePos.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_15.addWidget(self.btnResPrePos)


        self.verticalLayout_14.addWidget(self.framePos_2)

        self.frameXPos_2 = QFrame(self.widget_11)
        self.frameXPos_2.setObjectName(u"frameXPos_2")
        self.frameXPos_2.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameXPos {\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.frameXPos_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameXPos_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frameXPos_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_16 = QLabel(self.frameXPos_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 25))
        self.label_16.setFont(font2)

        self.verticalLayout_16.addWidget(self.label_16)

        self.widget_12 = QWidget(self.frameXPos_2)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btnUpPre5mm = QPushButton(self.widget_12)
        self.btnUpPre5mm.setObjectName(u"btnUpPre5mm")
        self.btnUpPre5mm.setMinimumSize(QSize(0, 40))
        self.btnUpPre5mm.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.horizontalLayout_8.addWidget(self.btnUpPre5mm)

        self.btnUpPre1mm = QPushButton(self.widget_12)
        self.btnUpPre1mm.setObjectName(u"btnUpPre1mm")
        self.btnUpPre1mm.setMinimumSize(QSize(0, 40))
        self.btnUpPre1mm.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.horizontalLayout_8.addWidget(self.btnUpPre1mm)

        self.btnDownPre1mm = QPushButton(self.widget_12)
        self.btnDownPre1mm.setObjectName(u"btnDownPre1mm")
        self.btnDownPre1mm.setMinimumSize(QSize(0, 40))
        self.btnDownPre1mm.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.horizontalLayout_8.addWidget(self.btnDownPre1mm)

        self.btnDownPre5mm = QPushButton(self.widget_12)
        self.btnDownPre5mm.setObjectName(u"btnDownPre5mm")
        self.btnDownPre5mm.setMinimumSize(QSize(0, 40))
        self.btnDownPre5mm.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.horizontalLayout_8.addWidget(self.btnDownPre5mm)


        self.verticalLayout_16.addWidget(self.widget_12)

        self.exPrePos = QSpinBox(self.frameXPos_2)
        self.exPrePos.setObjectName(u"exPrePos")
        self.exPrePos.setMinimumSize(QSize(0, 30))

        self.verticalLayout_16.addWidget(self.exPrePos)

        self.widget_13 = QWidget(self.frameXPos_2)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btnPreUpEx = QToolButton(self.widget_13)
        self.btnPreUpEx.setObjectName(u"btnPreUpEx")
        sizePolicy.setHeightForWidth(self.btnPreUpEx.sizePolicy().hasHeightForWidth())
        self.btnPreUpEx.setSizePolicy(sizePolicy)
        self.btnPreUpEx.setMinimumSize(QSize(0, 45))
        self.btnPreUpEx.setFont(font5)
        self.btnPreUpEx.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.btnPreUpEx.setIcon(icon3)
        self.btnPreUpEx.setIconSize(QSize(35, 35))
        self.btnPreUpEx.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_9.addWidget(self.btnPreUpEx)

        self.btnPreDownEx = QToolButton(self.widget_13)
        self.btnPreDownEx.setObjectName(u"btnPreDownEx")
        sizePolicy.setHeightForWidth(self.btnPreDownEx.sizePolicy().hasHeightForWidth())
        self.btnPreDownEx.setSizePolicy(sizePolicy)
        self.btnPreDownEx.setMinimumSize(QSize(0, 45))
        self.btnPreDownEx.setFont(font5)
        self.btnPreDownEx.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.btnPreDownEx.setIcon(icon4)
        self.btnPreDownEx.setIconSize(QSize(35, 35))
        self.btnPreDownEx.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_9.addWidget(self.btnPreDownEx)


        self.verticalLayout_16.addWidget(self.widget_13)


        self.verticalLayout_14.addWidget(self.frameXPos_2)


        self.horizontalLayout_7.addWidget(self.widget_11)

        self.framePosAndHome_2 = QFrame(self.widget_9)
        self.framePosAndHome_2.setObjectName(u"framePosAndHome_2")
        self.framePosAndHome_2.setMaximumSize(QSize(200, 16777215))
        self.framePosAndHome_2.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#framePosAndHome {\n"
"	\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.framePosAndHome_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePosAndHome_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.framePosAndHome_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.btnPreHome = QToolButton(self.framePosAndHome_2)
        self.btnPreHome.setObjectName(u"btnPreHome")
        sizePolicy.setHeightForWidth(self.btnPreHome.sizePolicy().hasHeightForWidth())
        self.btnPreHome.setSizePolicy(sizePolicy)
        self.btnPreHome.setMinimumSize(QSize(0, 120))
        self.btnPreHome.setFont(font9)
        self.btnPreHome.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.btnPreHome.setIcon(icon2)
        self.btnPreHome.setIconSize(QSize(80, 80))
        self.btnPreHome.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_17.addWidget(self.btnPreHome)

        self.line_4 = QFrame(self.framePosAndHome_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"Line {\n"
"	border: 1px solid #ced3d7;\n"
"}")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_17.addWidget(self.line_4)

        self.pushButton_18 = QPushButton(self.framePosAndHome_2)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setMinimumSize(QSize(0, 40))
        self.pushButton_18.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_17.addWidget(self.pushButton_18)

        self.pushButton_20 = QPushButton(self.framePosAndHome_2)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setMinimumSize(QSize(0, 40))
        self.pushButton_20.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_17.addWidget(self.pushButton_20)

        self.line_5 = QFrame(self.framePosAndHome_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"Line {\n"
"	border: 1px solid #ced3d7;\n"
"}")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_17.addWidget(self.line_5)

        self.label_18 = QLabel(self.framePosAndHome_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 30))
        self.label_18.setFont(font13)

        self.verticalLayout_17.addWidget(self.label_18)

        self.label_19 = QLabel(self.framePosAndHome_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 40))
        self.label_19.setFont(font14)

        self.verticalLayout_17.addWidget(self.label_19)


        self.horizontalLayout_7.addWidget(self.framePosAndHome_2)


        self.verticalLayout_19.addWidget(self.widget_9)

        self.widget_14 = QWidget(self.pagePreCrimp)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frameLogs_2 = QFrame(self.widget_14)
        self.frameLogs_2.setObjectName(u"frameLogs_2")
        self.frameLogs_2.setMaximumSize(QSize(16777215, 190))
        self.frameLogs_2.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameLogs {\n"
"	\n"
"	border-radius: 7px;\n"
"	border: 1px solid #cdced2;\n"
"}")
        self.frameLogs_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLogs_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frameLogs_2)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(10, 5, 10, 10)
        self.widget_15 = QWidget(self.frameLogs_2)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 5, 0, 5)
        self.label_17 = QLabel(self.widget_15)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_10.addWidget(self.label_17)

        self.horizontalSpacer_3 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)


        self.verticalLayout_18.addWidget(self.widget_15)

        self.plainLogPre = QPlainTextEdit(self.frameLogs_2)
        self.plainLogPre.setObjectName(u"plainLogPre")
        self.plainLogPre.setMaximumSize(QSize(16777215, 160))
        self.plainLogPre.setStyleSheet(u"QPlainTextEdit {\n"
"	padding: 5px;\n"
"	border: 1px solid #e0e1e6;\n"
"	background-color: #f3f4f6;\n"
"	border-radius: 7px;\n"
"}\n"
"")
        self.plainLogPre.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.plainLogPre.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.plainLogPre.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.plainLogPre.setTabChangesFocus(False)
        self.plainLogPre.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.plainLogPre.setReadOnly(True)
        self.plainLogPre.setOverwriteMode(False)
        self.plainLogPre.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_18.addWidget(self.plainLogPre)


        self.horizontalLayout_11.addWidget(self.frameLogs_2)

        self.framePreCrimpGraph = QFrame(self.widget_14)
        self.framePreCrimpGraph.setObjectName(u"framePreCrimpGraph")
        self.framePreCrimpGraph.setMinimumSize(QSize(155, 155))
        self.framePreCrimpGraph.setMaximumSize(QSize(162, 155))
        self.framePreCrimpGraph.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#framePreCrimpGraph {\n"
"	\n"
"	border-radius: 7px;\n"
"	border: 1px solid #cdced2;\n"
"}")
        self.framePreCrimpGraph.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePreCrimpGraph.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.framePreCrimpGraph)
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(5, 5, 5, 5)
        self.pushButton = QPushButton(self.framePreCrimpGraph)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 26))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_20.addWidget(self.pushButton)

        self.graphPreCrimp = QChartView(self.framePreCrimpGraph)
        self.graphPreCrimp.setObjectName(u"graphPreCrimp")

        self.verticalLayout_20.addWidget(self.graphPreCrimp)


        self.horizontalLayout_11.addWidget(self.framePreCrimpGraph)


        self.verticalLayout_19.addWidget(self.widget_14)

        self.stackedWidget.addWidget(self.pagePreCrimp)
        self.pagePostCrimp = QWidget()
        self.pagePostCrimp.setObjectName(u"pagePostCrimp")
        self.verticalLayout_42 = QVBoxLayout(self.pagePostCrimp)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.widget_26 = QWidget(self.pagePostCrimp)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setMinimumSize(QSize(0, 200))
        self.horizontalLayout_21 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.widget_27 = QWidget(self.widget_26)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout_36 = QVBoxLayout(self.widget_27)
        self.verticalLayout_36.setSpacing(10)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.widget_27)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 50))
        self.label_25.setFont(font9)
        self.label_25.setStyleSheet(u"QLabel {\n"
"	padding-left: 10px;\n"
"}")
        self.label_25.setWordWrap(True)

        self.verticalLayout_36.addWidget(self.label_25)

        self.frameLin_5 = QFrame(self.widget_27)
        self.frameLin_5.setObjectName(u"frameLin_5")
        self.frameLin_5.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameLin {\n"
"	background: #e9ecf1;\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.frameLin_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLin_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frameLin_5)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.btnPostForward = QToolButton(self.frameLin_5)
        self.btnPostForward.setObjectName(u"btnPostForward")
        sizePolicy.setHeightForWidth(self.btnPostForward.sizePolicy().hasHeightForWidth())
        self.btnPostForward.setSizePolicy(sizePolicy)
        self.btnPostForward.setMinimumSize(QSize(0, 60))
        self.btnPostForward.setFont(font9)
        self.btnPostForward.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.btnPostForward.setIcon(icon7)
        self.btnPostForward.setIconSize(QSize(50, 50))
        self.btnPostForward.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_37.addWidget(self.btnPostForward)

        self.btnPostBack = QToolButton(self.frameLin_5)
        self.btnPostBack.setObjectName(u"btnPostBack")
        sizePolicy.setHeightForWidth(self.btnPostBack.sizePolicy().hasHeightForWidth())
        self.btnPostBack.setSizePolicy(sizePolicy)
        self.btnPostBack.setMinimumSize(QSize(0, 60))
        self.btnPostBack.setFont(font9)
        self.btnPostBack.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.btnPostBack.setIcon(icon6)
        self.btnPostBack.setIconSize(QSize(50, 50))
        self.btnPostBack.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_37.addWidget(self.btnPostBack)

        self.lblPostSpeed = QLabel(self.frameLin_5)
        self.lblPostSpeed.setObjectName(u"lblPostSpeed")
        self.lblPostSpeed.setMaximumSize(QSize(16777215, 30))
        self.lblPostSpeed.setFont(font2)
        self.lblPostSpeed.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)

        self.verticalLayout_37.addWidget(self.lblPostSpeed)

        self.postSpeed = QSlider(self.frameLin_5)
        self.postSpeed.setObjectName(u"postSpeed")
        self.postSpeed.setMinimumSize(QSize(0, 30))
        self.postSpeed.setStyleSheet(u"/* \u0414\u043e\u0440\u043e\u0436\u043a\u0430 */\n"
"QSlider::groove:horizontal {\n"
"    height: 8px;\n"
"    background: #d5d8df;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u0437\u0443\u043d\u043e\u043a (\u043a\u0440\u0443\u0436\u043e\u043a) */\n"
"QSlider::handle:horizontal {\n"
"    background: #bdcfdd;\n"
"    border: 2px solid #a6b8c6;\n"
"    border-radius: 10px;      /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 = \u043f\u043e\u043b\u043e\u0432\u0438\u043d\u0430 \u0448\u0438\u0440\u0438\u043d\u044b \u0434\u043b\u044f \u043a\u0440\u0443\u0433\u0430 */\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    margin: -8px 0;          /* (40-8)/2 = 16 */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: #cfddeb;\n"
"    border-color: #4A8AB5;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background: #4A8AB5;\n"
"    border-color: #2c6a8f;\n"
"}\n"
"\n"
"/* \u0417\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u0430\u044f \u0447\u0430\u0441"
                        "\u0442\u044c */\n"
"QSlider::sub-page:horizontal {\n"
"    background: #4A8AB5;\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.postSpeed.setMinimum(1)
        self.postSpeed.setMaximum(100)
        self.postSpeed.setValue(30)
        self.postSpeed.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_37.addWidget(self.postSpeed)

        self.btnSetPostSpeed = QPushButton(self.frameLin_5)
        self.btnSetPostSpeed.setObjectName(u"btnSetPostSpeed")
        self.btnSetPostSpeed.setMinimumSize(QSize(0, 30))
        self.btnSetPostSpeed.setStyleSheet(u"QPushButton {\n"
"	background: #d5d8df;\n"
"	border: 2px solid #babec7;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_37.addWidget(self.btnSetPostSpeed)


        self.verticalLayout_36.addWidget(self.frameLin_5)


        self.horizontalLayout_21.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.widget_26)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMinimumSize(QSize(0, 0))
        self.widget_28.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_38 = QVBoxLayout(self.widget_28)
        self.verticalLayout_38.setSpacing(10)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.framePos_4 = QFrame(self.widget_28)
        self.framePos_4.setObjectName(u"framePos_4")
        self.framePos_4.setMinimumSize(QSize(0, 135))
        self.framePos_4.setMaximumSize(QSize(16777215, 135))
        self.framePos_4.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#framePos {\n"
"	\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.framePos_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePos_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.framePos_4)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(10, 10, 10, 5)
        self.label_29 = QLabel(self.framePos_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(16777215, 30))
        self.label_29.setFont(font13)

        self.verticalLayout_39.addWidget(self.label_29)

        self.label_30 = QLabel(self.framePos_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(16777215, 40))
        self.label_30.setFont(font14)

        self.verticalLayout_39.addWidget(self.label_30)


        self.verticalLayout_38.addWidget(self.framePos_4)

        self.frameXPos_4 = QFrame(self.widget_28)
        self.frameXPos_4.setObjectName(u"frameXPos_4")
        self.frameXPos_4.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameXPos {\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.frameXPos_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameXPos_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frameXPos_4)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_31 = QLabel(self.frameXPos_4)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(0, 25))
        self.label_31.setFont(font2)

        self.verticalLayout_40.addWidget(self.label_31)

        self.widget_29 = QWidget(self.frameXPos_4)
        self.widget_29.setObjectName(u"widget_29")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.btnPre5mm = QPushButton(self.widget_29)
        self.btnPre5mm.setObjectName(u"btnPre5mm")
        self.btnPre5mm.setMinimumSize(QSize(0, 40))
        self.btnPre5mm.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.horizontalLayout_22.addWidget(self.btnPre5mm)

        self.pushButton_34 = QPushButton(self.widget_29)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setMinimumSize(QSize(0, 40))
        self.pushButton_34.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.horizontalLayout_22.addWidget(self.pushButton_34)

        self.pushButton_35 = QPushButton(self.widget_29)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setMinimumSize(QSize(0, 40))
        self.pushButton_35.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.horizontalLayout_22.addWidget(self.pushButton_35)

        self.pushButton_36 = QPushButton(self.widget_29)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setMinimumSize(QSize(0, 40))
        self.pushButton_36.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.horizontalLayout_22.addWidget(self.pushButton_36)


        self.verticalLayout_40.addWidget(self.widget_29)

        self.exPostPos = QSpinBox(self.frameXPos_4)
        self.exPostPos.setObjectName(u"exPostPos")
        self.exPostPos.setMinimumSize(QSize(0, 30))

        self.verticalLayout_40.addWidget(self.exPostPos)

        self.widget_30 = QWidget(self.frameXPos_4)
        self.widget_30.setObjectName(u"widget_30")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.toolButton_20 = QToolButton(self.widget_30)
        self.toolButton_20.setObjectName(u"toolButton_20")
        sizePolicy.setHeightForWidth(self.toolButton_20.sizePolicy().hasHeightForWidth())
        self.toolButton_20.setSizePolicy(sizePolicy)
        self.toolButton_20.setMinimumSize(QSize(0, 45))
        self.toolButton_20.setFont(font5)
        self.toolButton_20.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.toolButton_20.setIcon(icon6)
        self.toolButton_20.setIconSize(QSize(35, 35))
        self.toolButton_20.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_23.addWidget(self.toolButton_20)

        self.toolButton_21 = QToolButton(self.widget_30)
        self.toolButton_21.setObjectName(u"toolButton_21")
        sizePolicy.setHeightForWidth(self.toolButton_21.sizePolicy().hasHeightForWidth())
        self.toolButton_21.setSizePolicy(sizePolicy)
        self.toolButton_21.setMinimumSize(QSize(0, 45))
        self.toolButton_21.setFont(font5)
        self.toolButton_21.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.toolButton_21.setIcon(icon7)
        self.toolButton_21.setIconSize(QSize(35, 35))
        self.toolButton_21.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_23.addWidget(self.toolButton_21)


        self.verticalLayout_40.addWidget(self.widget_30)


        self.verticalLayout_38.addWidget(self.frameXPos_4)


        self.horizontalLayout_21.addWidget(self.widget_28)

        self.framePosAndHome_4 = QFrame(self.widget_26)
        self.framePosAndHome_4.setObjectName(u"framePosAndHome_4")
        self.framePosAndHome_4.setMaximumSize(QSize(200, 16777215))
        self.framePosAndHome_4.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#framePosAndHome {\n"
"	\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.framePosAndHome_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePosAndHome_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.framePosAndHome_4)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.btnPostHome = QToolButton(self.framePosAndHome_4)
        self.btnPostHome.setObjectName(u"btnPostHome")
        sizePolicy.setHeightForWidth(self.btnPostHome.sizePolicy().hasHeightForWidth())
        self.btnPostHome.setSizePolicy(sizePolicy)
        self.btnPostHome.setMinimumSize(QSize(0, 120))
        self.btnPostHome.setFont(font9)
        self.btnPostHome.setStyleSheet(u"QToolButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")
        self.btnPostHome.setIcon(icon2)
        self.btnPostHome.setIconSize(QSize(80, 80))
        self.btnPostHome.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_41.addWidget(self.btnPostHome)

        self.line_8 = QFrame(self.framePosAndHome_4)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setStyleSheet(u"Line {\n"
"	border: 1px solid #ced3d7;\n"
"}")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_41.addWidget(self.line_8)

        self.pushButton_37 = QPushButton(self.framePosAndHome_4)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setMinimumSize(QSize(0, 40))
        self.pushButton_37.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_41.addWidget(self.pushButton_37)

        self.pushButton_38 = QPushButton(self.framePosAndHome_4)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setMinimumSize(QSize(0, 40))
        self.pushButton_38.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_41.addWidget(self.pushButton_38)

        self.pushButton_39 = QPushButton(self.framePosAndHome_4)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setMinimumSize(QSize(0, 40))
        self.pushButton_39.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_41.addWidget(self.pushButton_39)


        self.horizontalLayout_21.addWidget(self.framePosAndHome_4)


        self.verticalLayout_42.addWidget(self.widget_26)

        self.widget_23 = QWidget(self.pagePostCrimp)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frameLogs_5 = QFrame(self.widget_23)
        self.frameLogs_5.setObjectName(u"frameLogs_5")
        self.frameLogs_5.setMaximumSize(QSize(16777215, 190))
        self.frameLogs_5.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameLogs {\n"
"	\n"
"	border-radius: 7px;\n"
"	border: 1px solid #cdced2;\n"
"}")
        self.frameLogs_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLogs_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frameLogs_5)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(10, 5, 10, 10)
        self.widget_25 = QWidget(self.frameLogs_5)
        self.widget_25.setObjectName(u"widget_25")
        self.widget_25.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout_20 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 5, 0, 5)
        self.label_28 = QLabel(self.widget_25)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_20.addWidget(self.label_28)

        self.horizontalSpacer_6 = QSpacerItem(544, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_6)


        self.verticalLayout_34.addWidget(self.widget_25)

        self.plainLogPost = QPlainTextEdit(self.frameLogs_5)
        self.plainLogPost.setObjectName(u"plainLogPost")
        self.plainLogPost.setMaximumSize(QSize(16777215, 160))
        self.plainLogPost.setStyleSheet(u"QPlainTextEdit {\n"
"	padding: 5px;\n"
"	border: 1px solid #e0e1e6;\n"
"	background-color: #f3f4f6;\n"
"	border-radius: 7px;\n"
"}\n"
"")
        self.plainLogPost.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.plainLogPost.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.plainLogPost.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.plainLogPost.setTabChangesFocus(False)
        self.plainLogPost.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.plainLogPost.setReadOnly(True)
        self.plainLogPost.setOverwriteMode(False)
        self.plainLogPost.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)

        self.verticalLayout_34.addWidget(self.plainLogPost)


        self.horizontalLayout_19.addWidget(self.frameLogs_5)

        self.framePreCrimpGraph_4 = QFrame(self.widget_23)
        self.framePreCrimpGraph_4.setObjectName(u"framePreCrimpGraph_4")
        self.framePreCrimpGraph_4.setMinimumSize(QSize(155, 155))
        self.framePreCrimpGraph_4.setMaximumSize(QSize(16777215, 155))
        self.framePreCrimpGraph_4.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#framePreCrimpGraph {\n"
"	\n"
"	border-radius: 7px;\n"
"	border: 1px solid #cdced2;\n"
"}")
        self.framePreCrimpGraph_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePreCrimpGraph_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.framePreCrimpGraph_4)
        self.verticalLayout_35.setSpacing(5)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(5, 5, 5, 5)
        self.pushButton_31 = QPushButton(self.framePreCrimpGraph_4)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setMinimumSize(QSize(0, 26))
        self.pushButton_31.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_35.addWidget(self.pushButton_31)

        self.graphPreCrimp_4 = QChartView(self.framePreCrimpGraph_4)
        self.graphPreCrimp_4.setObjectName(u"graphPreCrimp_4")

        self.verticalLayout_35.addWidget(self.graphPreCrimp_4)


        self.horizontalLayout_19.addWidget(self.framePreCrimpGraph_4)


        self.verticalLayout_42.addWidget(self.widget_23)

        self.stackedWidget.addWidget(self.pagePostCrimp)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(8)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblDate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btnExit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.btnAutoMode.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0440\u0435\u0436\u0438\u043c", None))
        self.btnManualMode.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0447\u043d\u043e\u0439 \u0440\u0435\u0436\u0438\u043c", None))
        self.btnLinear.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0433\u043e\n"
"\u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u044f", None))
        self.btnFixation.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u0444\u0438\u043a\u0441\u0430\u0446\u0438\u0438", None))
        self.btnPreCrimp.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u043f\u0440\u0435\u0434\u043e\u0431\u0436\u0438\u043c\u0430", None))
        self.btnPostCrimp.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u043f\u043e\u0441\u0442\u043e\u0431\u0436\u0438\u043c\u0430", None))
        self.btnCalibration.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043b\u0438\u0431\u0440\u043e\u0432\u043a\u0430", None))
        self.btnDebug.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u0430\u0434\u043a\u0430", None))
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.lblTemp.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430: 20\u00b0C ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0441\u0441... \u041f\u0443\u0441\u0442\u043e(\n"
"\u0417\u0434\u0435\u0441\u044c \u0441\u043a\u043e\u0440\u043e \u0447\u0442\u043e-\u0442\u043e \u0431\u0443\u0434\u0435\u0442!", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0433\u043e \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u044f", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0415\u041a\u0423\u0429\u0410\u042f \u041f\u041e\u0417\u0418\u0426\u0418\u042f", None))
        self.lblLinPosMan.setText(QCoreApplication.translate("MainWindow", u"230 \u043c\u043c", None))
        self.btnLinForwardMan.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043f\u0435\u0440\u0435\u0434", None))
        self.btnLinBackMan.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.btnGoLinPos1Man.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0437\u0438\u0446\u0438\u044f \u043f\u0440\u0435\u0434\u043e\u0431\u0436\u0438\u043c\u0430", None))
        self.btnGoLinPos2Man.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0437\u0438\u0446\u0438\u044f \u043f\u043e\u0441\u0442\u043e\u0431\u0436\u0438\u043c\u0430", None))
        self.btnLinHomeMan.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u043e\u0439", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u043f\u0440\u0435\u0434\u043e\u0431\u0436\u0438\u043c\u0430", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0415\u041a\u0423\u0429\u0410\u042f \u041f\u041e\u0417\u0418\u0426\u0418\u042f", None))
        self.lblPrePosMan.setText(QCoreApplication.translate("MainWindow", u"122 \u043c\u043c", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0415\u041a\u0423\u0429\u0415\u0415 \u0423\u0421\u0418\u041b\u0418\u0415", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"65 \u041d", None))
        self.btnPreUpMan.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0440\u0445", None))
        self.btnPreDownMan.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0438\u0437", None))
        self.btnPreDown11.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e \u0443\u0441\u0438\u043b\u0438\u044f", None))
        self.btnPreHomeMan.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u043e\u0439", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u0444\u0438\u043a\u0441\u0430\u0446\u0438\u0438", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0415\u041a\u0423\u0429\u0410\u042f \u0421\u0418\u041b\u0410 \u0422\u041e\u041a\u0410", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"0.07 \u0410", None))
        self.btnFixBackMan.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0432\u043e\u0434\u0438\u0442\u044c", None))
        self.btnFixForwardMan.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0434\u0438\u0442\u044c", None))
        self.toolButton_28.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0436\u0430\u0442\u044c", None))
        self.toolButton_29.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0436\u0430\u0442\u044c", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u043f\u043e\u0441\u0442\u043e\u0431\u0436\u0438\u043c\u0430", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0415\u041a\u0423\u0429\u0418\u0419 \u041c\u041e\u041c\u0415\u041d\u0422", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"3 \u041d\u00b7\u043c", None))
        self.btnPostBackMan.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0432\u043e\u0434\u0438\u0442\u044c", None))
        self.btnPostForwardMan.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0434\u0438\u0442\u044c", None))
        self.toolButton_25.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0436\u0430\u0442\u044c", None))
        self.toolButton_26.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0436\u0430\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0441\u0441... \u041f\u0443\u0441\u0442\u043e(\n"
"\u0417\u0434\u0435\u0441\u044c \u0441\u043a\u043e\u0440\u043e \u0447\u0442\u043e-\u0442\u043e \u0431\u0443\u0434\u0435\u0442!", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0441\u0441... \u041f\u0443\u0441\u0442\u043e(\n"
"\u0417\u0434\u0435\u0441\u044c \u0441\u043a\u043e\u0440\u043e \u0447\u0442\u043e-\u0442\u043e \u0431\u0443\u0434\u0435\u0442!", None))
        self.label_4.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0432\u0435\u043d\u0442\u0438\u043b\u044f\u0442\u043e\u0440\u043e\u043c \u043a\u043e\u0440\u043f\u0443\u0441\u0430", None))
        self.label_9.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c \u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0440\u0435\u0436\u0438\u043c (\u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u043c\u044b\u0439)", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0447\u043d\u043e\u0439 \u0440\u0435\u0436\u0438\u043c (\u0444\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u0430\u044f \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c)", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043a\u043b\u044e\u0447\u0438\u0442\u044c", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0440\u0443\u0447\u043d\u043e\u0433\u043e \u0440\u0435\u0436\u0438\u043c\u0430", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u0430\u044f \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c (0-100%):", None))
        self.lblFanSpeed.setText(QCoreApplication.translate("MainWindow", u"50%", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u0440\u0435\u0436\u0438\u043c\u0430", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041f\u043e\u0440\u043e\u0433 \u0432\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u044f (<span style=\" font-style:italic;\">T</span><span style=\" vertical-align:sub;\">\u043c\u0438\u043d</span>):</p></body></html>", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0439 \u043c\u043e\u0449\u043d\u043e\u0441\u0442\u0438 (<span style=\" font-style:italic;\">T</span><span style=\" vertical-align:sub;\">\u043c\u0430\u043a\u0441</span>):</p></body></html>", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0435 \u043e\u0431\u043e\u0440\u043e\u0442\u044b \u043f\u0440\u0438 \u0441\u0442\u0430\u0440\u0442\u0435:", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u043b\u0438\u043d\u0435\u0439\u043d\u043e\u0433\u043e \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u044f", None))
        self.btnLinForward.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043f\u0435\u0440\u0435\u0434", None))
        self.btnLinBack.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.lblLinSpeed.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u044f: 30%", None))
        self.btnSetLinSpeed.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0415\u041a\u0423\u0429\u0410\u042f \u041f\u041e\u0417\u0418\u0426\u0418\u042f", None))
        self.lblLinPos.setText(QCoreApplication.translate("MainWindow", u"230 \u043c\u043c", None))
        self.btnResLinPos.setText(QCoreApplication.translate("MainWindow", u"C\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u0442\u0435\u043a\u0443\u0449\u0443\u044e \u043f\u043e\u0437\u0438\u0446\u0438\u044e", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043d\u043e\u0435 \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u0435", None))
        self.btnBackLin5mm.setText(QCoreApplication.translate("MainWindow", u"-5 \u043c\u043c", None))
        self.btnBackLin1mm.setText(QCoreApplication.translate("MainWindow", u"-1 \u043c\u043c", None))
        self.btnForwardLin1mm.setText(QCoreApplication.translate("MainWindow", u"+1 \u043c\u043c", None))
        self.btnForwardLin5mm.setText(QCoreApplication.translate("MainWindow", u"+5 \u043c\u043c", None))
        self.btnLinBackEx.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.btnLinForwardEx.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043f\u0435\u0440\u0435\u0434", None))
        self.btnLinHome.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u043e\u0439", None))
        self.btnSaveLinPos1.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043f\u043e\u0437\u0438\u0446\u0438\u044e 1", None))
        self.btnSaveLinPos2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043f\u043e\u0437\u0438\u0446\u0438\u044e 2", None))
        self.btnGoLinPos1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u043c\u0435\u0441\u0442\u0438\u0442\u044c\u0441\u044f \u043a \u043f\u043e\u0437\u0438\u0446\u0438\u0438 1", None))
        self.btnGoLinPos2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u043c\u0435\u0441\u0442\u0438\u0442\u044c\u0441\u044f \u043a \u043f\u043e\u0437\u0438\u0446\u0438\u0438 2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0439 \u0438 \u043e\u0448\u0438\u0431\u043e\u043a:", None))
        self.plainLogLin.setPlaceholderText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u0444\u0438\u043a\u0441\u0430\u0446\u0438\u0438", None))
        self.btnFixForward.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0436\u0430\u0442\u044c", None))
        self.btnFixBack.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0436\u0430\u0442\u044c", None))
        self.lblFixSpeed.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u0437\u0430\u0436\u0430\u0442\u0438\u044f: 30%", None))
        self.btnSetFixSpeed.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0415\u041a\u0423\u0429\u0410\u042f \u0421\u0418\u041b\u0410 \u0422\u041e\u041a\u0410", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"0.07 \u0410", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043d\u043e\u0435 \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u0435", None))
        self.btnBackFix5grad.setText(QCoreApplication.translate("MainWindow", u"-5\u00b0", None))
        self.btnBackFix1grad.setText(QCoreApplication.translate("MainWindow", u"-1\u00b0", None))
        self.btnForwardFix1grad.setText(QCoreApplication.translate("MainWindow", u"+1\u00b0", None))
        self.btnForwardFix5grad.setText(QCoreApplication.translate("MainWindow", u"+5\u00b0", None))
        self.btnFixBackEx.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0436\u0430\u0442\u044c", None))
        self.btnFixForwardEx.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0436\u0430\u0442\u044c", None))
        self.btnFixHome.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u0430\u0448\u043d\u044f\u044f \u043f\u043e\u0437\u0438\u0446\u0438\u044f", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0441\u0438\u043b\u0443 \u0442\u043e\u043a\u0430", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0434\u043e\u043c. \u043f\u043e\u0437\u0438\u0446\u0438\u044e", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0436\u0430\u0442\u044c \u0434\u043e \u0441\u0438\u043b\u044b \u0442\u043e\u043a\u0430", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0439 \u0438 \u043e\u0448\u0438\u0431\u043e\u043a:", None))
        self.plainLogFix.setPlaceholderText("")
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u0430\u0434\u043a\u0430", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u043f\u0440\u0435\u0434\u043e\u0431\u0436\u0438\u043c\u0430", None))
        self.btnPreUp.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0440\u0445", None))
        self.btnDownBack.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0438\u0437", None))
        self.lblPreSpeed.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u044f: 30%", None))
        self.btnSetPreSpeed.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0415\u041a\u0423\u0429\u0410\u042f \u041f\u041e\u0417\u0418\u0426\u0418\u042f", None))
        self.lblPrePos.setText(QCoreApplication.translate("MainWindow", u"122 \u043c\u043c", None))
        self.btnResPrePos.setText(QCoreApplication.translate("MainWindow", u"C\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u0442\u0435\u043a\u0443\u0449\u0443\u044e \u043f\u043e\u0437\u0438\u0446\u0438\u044e", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043d\u043e\u0435 \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u0435", None))
        self.btnUpPre5mm.setText(QCoreApplication.translate("MainWindow", u"-5 \u043c\u043c", None))
        self.btnUpPre1mm.setText(QCoreApplication.translate("MainWindow", u"-1 \u043c\u043c", None))
        self.btnDownPre1mm.setText(QCoreApplication.translate("MainWindow", u"+1 \u043c\u043c", None))
        self.btnDownPre5mm.setText(QCoreApplication.translate("MainWindow", u"+5 \u043c\u043c", None))
        self.btnPreUpEx.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0440\u0445", None))
        self.btnPreDownEx.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0438\u0437", None))
        self.btnPreHome.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u043e\u0439", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0443\u0441\u0438\u043b\u0438\u0435", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u043c\u0435\u0441\u0442\u0438\u0442\u044c\u0441\u044f \u0434\u043e \u0443\u0441\u0438\u043b\u0438\u044f", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0415\u041a\u0423\u0429\u0415\u0415 \u0423\u0421\u0418\u041b\u0418\u0415", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"65 \u041d", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0439 \u0438 \u043e\u0448\u0438\u0431\u043e\u043a:", None))
        self.plainLogPre.setPlaceholderText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u0430\u0434\u043a\u0430", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u043f\u043e\u0441\u0442\u043e\u0431\u0436\u0438\u043c\u0430", None))
        self.btnPostForward.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0436\u0430\u0442\u044c", None))
        self.btnPostBack.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0436\u0430\u0442\u044c", None))
        self.lblPostSpeed.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u0437\u0430\u0436\u0430\u0442\u0438\u044f: 30%", None))
        self.btnSetPostSpeed.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0415\u041a\u0423\u0429\u0418\u0419 \u041c\u041e\u041c\u0415\u041d\u0422", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"3 \u041d\u00b7\u043c", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043d\u043e\u0435 \u0437\u0430\u0436\u0430\u0442\u0438\u0435", None))
        self.btnPre5mm.setText(QCoreApplication.translate("MainWindow", u"-5\u00b0", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"-1\u00b0", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"+1\u00b0", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"+5\u00b0", None))
        self.toolButton_20.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0436\u0430\u0442\u044c", None))
        self.toolButton_21.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0436\u0430\u0442\u044c", None))
        self.btnPostHome.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u0430\u0448\u043d\u044f\u044f \u043f\u043e\u0437\u0438\u0446\u0438\u044f", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043c\u043e\u043c\u0435\u043d\u0442", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0434\u043e\u043c. \u043f\u043e\u0437\u0438\u0446\u0438\u044e", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0436\u0430\u0442\u044c \u0434\u043e \u043c\u043e\u043c\u0435\u043d\u0442\u0430", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0439 \u0438 \u043e\u0448\u0438\u0431\u043e\u043a:", None))
        self.plainLogPost.setPlaceholderText("")
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u043b\u0430\u0434\u043a\u0430", None))
    # retranslateUi

