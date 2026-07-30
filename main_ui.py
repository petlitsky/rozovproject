# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)
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
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.widget.setStyleSheet(u"background: #F5F6F8;")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.lblDate = QLabel(self.widget)
        self.lblDate.setObjectName(u"lblDate")

        self.horizontalLayout_2.addWidget(self.lblDate)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_5 = QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.widget_4)

        self.line_19 = QFrame(self.widget)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.Shape.VLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_19)

        self.lblTimeStart = QLabel(self.widget)
        self.lblTimeStart.setObjectName(u"lblTimeStart")

        self.horizontalLayout_2.addWidget(self.lblTimeStart)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

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
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 10, 0, 0)
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
"QPushButton:pressed {\n"
"	background-color: #D5DAE0;\n"
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
        self.horizontalLayout_10 = QHBoxLayout(self.pageManualMode)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
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
        self.verticalLayout_18 = QVBoxLayout(self.widget_34)
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frameXPos_7 = QFrame(self.widget_34)
        self.frameXPos_7.setObjectName(u"frameXPos_7")
        self.frameXPos_7.setMaximumSize(QSize(16777215, 16777215))
        self.frameXPos_7.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameXPos_7 {\n"
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
        self.horizontalLayout_4 = QHBoxLayout(self.widget_42)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.widget_42)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(16777215, 23))
        font3 = QFont()
        font3.setPointSize(8)
        self.label_43.setFont(font3)
        self.label_43.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.label_43)

        self.line_17 = QFrame(self.widget_42)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.Shape.VLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_17)

        self.lblLinPosMan = QLabel(self.widget_42)
        self.lblLinPosMan.setObjectName(u"lblLinPosMan")
        self.lblLinPosMan.setMaximumSize(QSize(16777215, 23))
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(True)
        self.lblLinPosMan.setFont(font4)

        self.horizontalLayout_4.addWidget(self.lblLinPosMan)


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
        self.btnLinForwardMan.setMinimumSize(QSize(0, 60))
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
        icon.addFile(u":/icons/icons/left.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLinForwardMan.setIcon(icon)
        self.btnLinForwardMan.setIconSize(QSize(35, 35))
        self.btnLinForwardMan.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.gridLayout.addWidget(self.btnLinForwardMan, 0, 1, 1, 1)

        self.btnLinBackMan = QToolButton(self.widget_43)
        self.btnLinBackMan.setObjectName(u"btnLinBackMan")
        sizePolicy.setHeightForWidth(self.btnLinBackMan.sizePolicy().hasHeightForWidth())
        self.btnLinBackMan.setSizePolicy(sizePolicy)
        self.btnLinBackMan.setMinimumSize(QSize(0, 60))
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
        icon1.addFile(u":/icons/icons/right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLinBackMan.setIcon(icon1)
        self.btnLinBackMan.setIconSize(QSize(35, 35))
        self.btnLinBackMan.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.gridLayout.addWidget(self.btnLinBackMan, 0, 0, 1, 1)

        self.btnGoLinPos1Man = QPushButton(self.widget_43)
        self.btnGoLinPos1Man.setObjectName(u"btnGoLinPos1Man")
        self.btnGoLinPos1Man.setMinimumSize(QSize(0, 60))
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
        self.btnGoLinPos2Man.setMinimumSize(QSize(0, 60))
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
        self.btnLinHomeMan.setMinimumSize(QSize(0, 60))
        self.btnLinHomeMan.setFont(font5)
        self.btnLinHomeMan.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btnLinHomeMan.setAutoFillBackground(False)
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
        icon2.addFile(u":/icons/icons/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLinHomeMan.setIcon(icon2)
        self.btnLinHomeMan.setIconSize(QSize(35, 35))
        self.btnLinHomeMan.setAutoRepeat(False)
        self.btnLinHomeMan.setAutoExclusive(False)
        self.btnLinHomeMan.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.btnLinHomeMan.setAutoRaise(False)
        self.btnLinHomeMan.setArrowType(Qt.ArrowType.NoArrow)

        self.verticalLayout_46.addWidget(self.btnLinHomeMan)


        self.verticalLayout_58.addWidget(self.widget_32)


        self.verticalLayout_56.addWidget(self.widget_41)


        self.verticalLayout_18.addWidget(self.frameXPos_7)

        self.frameXPos_6 = QFrame(self.widget_34)
        self.frameXPos_6.setObjectName(u"frameXPos_6")
        self.frameXPos_6.setMinimumSize(QSize(0, 252))
        self.frameXPos_6.setMaximumSize(QSize(16777215, 252))
        self.frameXPos_6.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameXPos_6 {\n"
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

        self.line_6 = QFrame(self.frameXPos_6)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"Line {\n"
"	border: 1px solid #ced3d7;\n"
"}")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_53.addWidget(self.line_6)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_53.addItem(self.verticalSpacer_4)

        self.widget_38 = QWidget(self.frameXPos_6)
        self.widget_38.setObjectName(u"widget_38")
        self.widget_38.setMaximumSize(QSize(16777215, 125))
        self.horizontalLayout_29 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_29.setSpacing(5)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.widget_49 = QWidget(self.widget_38)
        self.widget_49.setObjectName(u"widget_49")
        self.widget_49.setMaximumSize(QSize(16777215, 125))
        self.verticalLayout_48 = QVBoxLayout(self.widget_49)
        self.verticalLayout_48.setSpacing(5)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.btnFixBackMan = QToolButton(self.widget_49)
        self.btnFixBackMan.setObjectName(u"btnFixBackMan")
        sizePolicy.setHeightForWidth(self.btnFixBackMan.sizePolicy().hasHeightForWidth())
        self.btnFixBackMan.setSizePolicy(sizePolicy)
        self.btnFixBackMan.setMinimumSize(QSize(0, 60))
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
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/unfix.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnFixBackMan.setIcon(icon3)
        self.btnFixBackMan.setIconSize(QSize(35, 35))
        self.btnFixBackMan.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_48.addWidget(self.btnFixBackMan)

        self.btnFixForwardMan = QToolButton(self.widget_49)
        self.btnFixForwardMan.setObjectName(u"btnFixForwardMan")
        sizePolicy.setHeightForWidth(self.btnFixForwardMan.sizePolicy().hasHeightForWidth())
        self.btnFixForwardMan.setSizePolicy(sizePolicy)
        self.btnFixForwardMan.setMinimumSize(QSize(0, 60))
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
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/fix.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnFixForwardMan.setIcon(icon4)
        self.btnFixForwardMan.setIconSize(QSize(35, 35))
        self.btnFixForwardMan.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_48.addWidget(self.btnFixForwardMan)


        self.horizontalLayout_29.addWidget(self.widget_49)

        self.widget_40 = QWidget(self.widget_38)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setMaximumSize(QSize(16777215, 125))
        self.verticalLayout_55 = QVBoxLayout(self.widget_40)
        self.verticalLayout_55.setSpacing(5)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.toolButton_28 = QToolButton(self.widget_40)
        self.toolButton_28.setObjectName(u"toolButton_28")
        sizePolicy.setHeightForWidth(self.toolButton_28.sizePolicy().hasHeightForWidth())
        self.toolButton_28.setSizePolicy(sizePolicy)
        self.toolButton_28.setMinimumSize(QSize(0, 60))
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
        self.toolButton_28.setIcon(icon3)
        self.toolButton_28.setIconSize(QSize(35, 35))
        self.toolButton_28.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_55.addWidget(self.toolButton_28)

        self.toolButton_29 = QToolButton(self.widget_40)
        self.toolButton_29.setObjectName(u"toolButton_29")
        sizePolicy.setHeightForWidth(self.toolButton_29.sizePolicy().hasHeightForWidth())
        self.toolButton_29.setSizePolicy(sizePolicy)
        self.toolButton_29.setMinimumSize(QSize(0, 60))
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
        self.toolButton_29.setIcon(icon4)
        self.toolButton_29.setIconSize(QSize(35, 35))
        self.toolButton_29.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_55.addWidget(self.toolButton_29)


        self.horizontalLayout_29.addWidget(self.widget_40)


        self.verticalLayout_53.addWidget(self.widget_38)


        self.verticalLayout_18.addWidget(self.frameXPos_6)


        self.horizontalLayout_26.addWidget(self.widget_34)

        self.widget_35 = QWidget(self.widget_33)
        self.widget_35.setObjectName(u"widget_35")
        self.widget_35.setMinimumSize(QSize(300, 0))
        self.widget_35.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_47 = QVBoxLayout(self.widget_35)
        self.verticalLayout_47.setSpacing(5)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frameXPos_8 = QFrame(self.widget_35)
        self.frameXPos_8.setObjectName(u"frameXPos_8")
        self.frameXPos_8.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameXPos_8 {\n"
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
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        self.label_45.setFont(font6)

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
        self.label_46.setFont(font3)
        self.label_46.setWordWrap(True)

        self.verticalLayout_60.addWidget(self.label_46)

        self.lblPrePosMan = QLabel(self.widget_47)
        self.lblPrePosMan.setObjectName(u"lblPrePosMan")
        self.lblPrePosMan.setMaximumSize(QSize(16777215, 40))
        font7 = QFont()
        font7.setPointSize(18)
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
        self.label_48.setFont(font3)
        self.label_48.setWordWrap(True)

        self.verticalLayout_61.addWidget(self.label_48)

        self.lblPreForceMan = QLabel(self.widget_48)
        self.lblPreForceMan.setObjectName(u"lblPreForceMan")
        self.lblPreForceMan.setMaximumSize(QSize(16777215, 40))
        self.lblPreForceMan.setFont(font7)

        self.verticalLayout_61.addWidget(self.lblPreForceMan)


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
        self.btnPreUpMan.setMinimumSize(QSize(0, 60))
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
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/up.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPreUpMan.setIcon(icon5)
        self.btnPreUpMan.setIconSize(QSize(35, 35))
        self.btnPreUpMan.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.gridLayout_2.addWidget(self.btnPreUpMan, 0, 0, 1, 1)

        self.btnPreDownMan = QToolButton(self.widget_46)
        self.btnPreDownMan.setObjectName(u"btnPreDownMan")
        sizePolicy.setHeightForWidth(self.btnPreDownMan.sizePolicy().hasHeightForWidth())
        self.btnPreDownMan.setSizePolicy(sizePolicy)
        self.btnPreDownMan.setMinimumSize(QSize(0, 60))
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
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/down.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnPreDownMan.setIcon(icon6)
        self.btnPreDownMan.setIconSize(QSize(35, 35))
        self.btnPreDownMan.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.gridLayout_2.addWidget(self.btnPreDownMan, 1, 0, 1, 1)

        self.btnGoPreForceMan = QToolButton(self.widget_46)
        self.btnGoPreForceMan.setObjectName(u"btnGoPreForceMan")
        sizePolicy.setHeightForWidth(self.btnGoPreForceMan.sizePolicy().hasHeightForWidth())
        self.btnGoPreForceMan.setSizePolicy(sizePolicy)
        self.btnGoPreForceMan.setMinimumSize(QSize(0, 60))
        self.btnGoPreForceMan.setFont(font5)
        self.btnGoPreForceMan.setStyleSheet(u"QToolButton {\n"
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
        icon7.addFile(u":/icons/icons/press.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnGoPreForceMan.setIcon(icon7)
        self.btnGoPreForceMan.setIconSize(QSize(35, 35))
        self.btnGoPreForceMan.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.gridLayout_2.addWidget(self.btnGoPreForceMan, 0, 1, 1, 1)

        self.btnPreHomeMan = QToolButton(self.widget_46)
        self.btnPreHomeMan.setObjectName(u"btnPreHomeMan")
        sizePolicy.setHeightForWidth(self.btnPreHomeMan.sizePolicy().hasHeightForWidth())
        self.btnPreHomeMan.setSizePolicy(sizePolicy)
        self.btnPreHomeMan.setMinimumSize(QSize(0, 60))
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


        self.verticalLayout_47.addWidget(self.frameXPos_8)

        self.frameXPos_5 = QFrame(self.widget_35)
        self.frameXPos_5.setObjectName(u"frameXPos_5")
        self.frameXPos_5.setMinimumSize(QSize(0, 252))
        self.frameXPos_5.setMaximumSize(QSize(16777215, 252))
        self.frameXPos_5.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameXPos_5 {\n"
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
        self.verticalLayout_20 = QVBoxLayout(self.widget_36)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.widget_36)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(16777215, 30))
        self.label_37.setFont(font3)
        self.label_37.setWordWrap(True)

        self.verticalLayout_20.addWidget(self.label_37)

        self.lblPostTorqMan = QLabel(self.widget_36)
        self.lblPostTorqMan.setObjectName(u"lblPostTorqMan")
        self.lblPostTorqMan.setMaximumSize(QSize(16777215, 35))
        font8 = QFont()
        font8.setPointSize(20)
        font8.setBold(True)
        self.lblPostTorqMan.setFont(font8)

        self.verticalLayout_20.addWidget(self.lblPostTorqMan)


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
        self.widget_50.setMaximumSize(QSize(16777215, 125))
        self.verticalLayout_50 = QVBoxLayout(self.widget_50)
        self.verticalLayout_50.setSpacing(5)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.btnPostBackMan = QToolButton(self.widget_50)
        self.btnPostBackMan.setObjectName(u"btnPostBackMan")
        sizePolicy.setHeightForWidth(self.btnPostBackMan.sizePolicy().hasHeightForWidth())
        self.btnPostBackMan.setSizePolicy(sizePolicy)
        self.btnPostBackMan.setMinimumSize(QSize(0, 60))
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
        self.btnPostBackMan.setIcon(icon3)
        self.btnPostBackMan.setIconSize(QSize(35, 35))
        self.btnPostBackMan.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_50.addWidget(self.btnPostBackMan)

        self.btnPostForwardMan = QToolButton(self.widget_50)
        self.btnPostForwardMan.setObjectName(u"btnPostForwardMan")
        sizePolicy.setHeightForWidth(self.btnPostForwardMan.sizePolicy().hasHeightForWidth())
        self.btnPostForwardMan.setSizePolicy(sizePolicy)
        self.btnPostForwardMan.setMinimumSize(QSize(0, 60))
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
        self.btnPostForwardMan.setIcon(icon4)
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
        self.toolButton_25.setMinimumSize(QSize(0, 60))
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
        self.toolButton_25.setIcon(icon3)
        self.toolButton_25.setIconSize(QSize(35, 35))
        self.toolButton_25.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_51.addWidget(self.toolButton_25)

        self.toolButton_26 = QToolButton(self.widget_31)
        self.toolButton_26.setObjectName(u"toolButton_26")
        sizePolicy.setHeightForWidth(self.toolButton_26.sizePolicy().hasHeightForWidth())
        self.toolButton_26.setSizePolicy(sizePolicy)
        self.toolButton_26.setMinimumSize(QSize(0, 60))
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
        self.toolButton_26.setIcon(icon4)
        self.toolButton_26.setIconSize(QSize(35, 35))
        self.toolButton_26.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.verticalLayout_51.addWidget(self.toolButton_26)


        self.horizontalLayout_28.addWidget(self.widget_31)


        self.verticalLayout_49.addWidget(self.widget_37)


        self.verticalLayout_47.addWidget(self.frameXPos_5)


        self.horizontalLayout_26.addWidget(self.widget_35)


        self.horizontalLayout_10.addWidget(self.widget_33)

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
        self.verticalLayout_28 = QVBoxLayout(self.pageDebug)
        self.verticalLayout_28.setSpacing(5)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(10, 10, 10, 10)
        self.widget_8 = QWidget(self.pageDebug)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(16777215, 95))
        self.verticalLayout_31 = QVBoxLayout(self.widget_8)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.widget_14 = QWidget(self.widget_8)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_14)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))
        self.label_3.setFont(font6)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.btnResetStats = QPushButton(self.widget_14)
        self.btnResetStats.setObjectName(u"btnResetStats")
        self.btnResetStats.setMinimumSize(QSize(0, 30))
        self.btnResetStats.setMaximumSize(QSize(180, 30))
        self.btnResetStats.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.btnResetStats)


        self.verticalLayout_31.addWidget(self.widget_14)

        self.comboBoxSensor = QComboBox(self.widget_8)
        self.comboBoxSensor.addItem("")
        self.comboBoxSensor.addItem("")
        self.comboBoxSensor.addItem("")
        self.comboBoxSensor.addItem("")
        self.comboBoxSensor.setObjectName(u"comboBoxSensor")
        self.comboBoxSensor.setMinimumSize(QSize(0, 35))
        self.comboBoxSensor.setFont(font5)

        self.verticalLayout_31.addWidget(self.comboBoxSensor)


        self.verticalLayout_28.addWidget(self.widget_8)

        self.frameGraph = QFrame(self.pageDebug)
        self.frameGraph.setObjectName(u"frameGraph")
        self.frameGraph.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame {\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.frameGraph.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameGraph.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_28.addWidget(self.frameGraph)

        self.widget_13 = QWidget(self.pageDebug)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setMinimumSize(QSize(0, 100))
        self.widget_13.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_32 = QVBoxLayout(self.widget_13)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.lblSensData = QLabel(self.widget_13)
        self.lblSensData.setObjectName(u"lblSensData")

        self.verticalLayout_32.addWidget(self.lblSensData)


        self.verticalLayout_28.addWidget(self.widget_13)

        self.stackedWidget.addWidget(self.pageDebug)
        self.pageSettings = QWidget()
        self.pageSettings.setObjectName(u"pageSettings")
        self.pageSettings.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.verticalLayout_43 = QVBoxLayout(self.pageSettings)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.widget_51 = QWidget(self.pageSettings)
        self.widget_51.setObjectName(u"widget_51")
        self.widget_51.setMaximumSize(QSize(16777215, 40))
        self.widget_51.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.horizontalLayout_24 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_51)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.label_4.setPixmap(QPixmap(u":/icons/fan.jpg"))

        self.horizontalLayout_24.addWidget(self.label_4)

        self.label_8 = QLabel(self.widget_51)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 40))
        self.label_8.setFont(font4)
        self.label_8.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_8)

        self.label_9 = QLabel(self.widget_51)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(40, 40))
        self.label_9.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.label_9.setPixmap(QPixmap(u":/icons/fan.jpg"))

        self.horizontalLayout_24.addWidget(self.label_9)


        self.verticalLayout_43.addWidget(self.widget_51)

        self.widget_52 = QWidget(self.pageSettings)
        self.widget_52.setObjectName(u"widget_52")
        self.widget_52.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.horizontalLayout_25 = QHBoxLayout(self.widget_52)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.widget_53 = QWidget(self.widget_52)
        self.widget_53.setObjectName(u"widget_53")
        self.widget_53.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.verticalLayout_62 = QVBoxLayout(self.widget_53)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.groupBox_2 = QGroupBox(self.widget_53)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font6)
        self.groupBox_2.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.verticalLayout_64 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_64.setSpacing(5)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(10, 10, 10, 10)
        self.getAutoFan = QRadioButton(self.groupBox_2)
        self.getAutoFan.setObjectName(u"getAutoFan")
        font9 = QFont()
        font9.setBold(True)
        self.getAutoFan.setFont(font9)
        self.getAutoFan.setStyleSheet(u"QRadioButton {\n"
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
        self.getAutoFan.setChecked(True)

        self.verticalLayout_64.addWidget(self.getAutoFan)

        self.getManualFan = QRadioButton(self.groupBox_2)
        self.getManualFan.setObjectName(u"getManualFan")
        self.getManualFan.setFont(font9)
        self.getManualFan.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.getManualFan.setStyleSheet(u"QRadioButton {\n"
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
        self.getManualFan.setChecked(False)
        self.getManualFan.setAutoRepeat(False)
        self.getManualFan.setAutoExclusive(True)

        self.verticalLayout_64.addWidget(self.getManualFan)

        self.fanOff = QRadioButton(self.groupBox_2)
        self.fanOff.setObjectName(u"fanOff")
        self.fanOff.setFont(font9)
        self.fanOff.setStyleSheet(u"QRadioButton {\n"
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

        self.verticalLayout_64.addWidget(self.fanOff)


        self.verticalLayout_62.addWidget(self.groupBox_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_62.addItem(self.verticalSpacer_2)


        self.horizontalLayout_25.addWidget(self.widget_53)

        self.widget_54 = QWidget(self.widget_52)
        self.widget_54.setObjectName(u"widget_54")
        self.widget_54.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.verticalLayout_63 = QVBoxLayout(self.widget_54)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.groupBox_3 = QGroupBox(self.widget_54)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font6)
        self.groupBox_3.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.label_32 = QLabel(self.groupBox_3)
        self.label_32.setObjectName(u"label_32")
        font10 = QFont()
        font10.setPointSize(10)
        font10.setBold(False)
        self.label_32.setFont(font10)
        self.label_32.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.gridLayout_3.addWidget(self.label_32, 0, 0, 1, 1)

        self.fanSpeed = QSlider(self.groupBox_3)
        self.fanSpeed.setObjectName(u"fanSpeed")
        self.fanSpeed.setMinimumSize(QSize(0, 0))
        self.fanSpeed.setFont(font)
        self.fanSpeed.setStyleSheet(u"")
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
        font11 = QFont()
        font11.setPointSize(9)
        font11.setBold(False)
        self.lblFanSpeed.setFont(font11)
        self.lblFanSpeed.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.gridLayout_3.addWidget(self.lblFanSpeed, 1, 1, 1, 1)


        self.verticalLayout_63.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.widget_54)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font6)
        self.groupBox_4.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_34 = QLabel(self.groupBox_4)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font11)
        self.label_34.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.gridLayout_4.addWidget(self.label_34, 0, 0, 1, 1)

        self.tempMin = QSpinBox(self.groupBox_4)
        self.tempMin.setObjectName(u"tempMin")
        self.tempMin.setMinimumSize(QSize(0, 40))
        self.tempMin.setMaximumSize(QSize(110, 16777215))
        self.tempMin.setFont(font11)
        self.tempMin.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.tempMin.setInputMethodHints(Qt.InputMethodHint.ImhPreferNumbers)
        self.tempMin.setMinimum(1)
        self.tempMin.setMaximum(40)
        self.tempMin.setValue(10)

        self.gridLayout_4.addWidget(self.tempMin, 0, 1, 1, 1)

        self.label_51 = QLabel(self.groupBox_4)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMaximumSize(QSize(30, 16777215))
        self.label_51.setFont(font11)
        self.label_51.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.gridLayout_4.addWidget(self.label_51, 0, 2, 1, 1)

        self.label_35 = QLabel(self.groupBox_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font11)
        self.label_35.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.gridLayout_4.addWidget(self.label_35, 1, 0, 1, 1)

        self.tempMax = QSpinBox(self.groupBox_4)
        self.tempMax.setObjectName(u"tempMax")
        self.tempMax.setMinimumSize(QSize(101, 40))
        self.tempMax.setMaximumSize(QSize(90, 16777215))
        self.tempMax.setFont(font11)
        self.tempMax.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.tempMax.setInputMethodHints(Qt.InputMethodHint.ImhPreferNumbers)
        self.tempMax.setMinimum(20)
        self.tempMax.setValue(30)

        self.gridLayout_4.addWidget(self.tempMax, 1, 1, 1, 1)

        self.label_52 = QLabel(self.groupBox_4)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font11)
        self.label_52.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.gridLayout_4.addWidget(self.label_52, 1, 2, 1, 1)

        self.label_50 = QLabel(self.groupBox_4)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font11)
        self.label_50.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.gridLayout_4.addWidget(self.label_50, 2, 0, 1, 1)

        self.startSpeed = QSpinBox(self.groupBox_4)
        self.startSpeed.setObjectName(u"startSpeed")
        self.startSpeed.setMinimumSize(QSize(0, 40))
        self.startSpeed.setMaximumSize(QSize(110, 16777215))
        self.startSpeed.setFont(font11)
        self.startSpeed.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.startSpeed.setInputMethodHints(Qt.InputMethodHint.ImhPreferNumbers)
        self.startSpeed.setMinimum(5)
        self.startSpeed.setMaximum(70)
        self.startSpeed.setValue(10)

        self.gridLayout_4.addWidget(self.startSpeed, 2, 1, 1, 1)

        self.label_53 = QLabel(self.groupBox_4)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font11)
        self.label_53.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.gridLayout_4.addWidget(self.label_53, 2, 2, 1, 1)


        self.verticalLayout_63.addWidget(self.groupBox_4)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_63.addItem(self.verticalSpacer_3)


        self.horizontalLayout_25.addWidget(self.widget_54)


        self.verticalLayout_43.addWidget(self.widget_52)

        self.stackedWidget.addWidget(self.pageSettings)
        self.pageLinear = QWidget()
        self.pageLinear.setObjectName(u"pageLinear")
        self.pageLinear.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.verticalLayout_4 = QVBoxLayout(self.pageLinear)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.widget_3 = QWidget(self.pageLinear)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 200))
        self.widget_3.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(250, 16777215))
        self.widget_5.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.verticalLayout_8 = QVBoxLayout(self.widget_5)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 50))
        self.label_6.setFont(font6)
        self.label_6.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.label_6.setStyleSheet(u"QLabel {\n"
"	padding-left: 10px;\n"
"}")
        self.label_6.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_6)

        self.frameLin = QFrame(self.widget_5)
        self.frameLin.setObjectName(u"frameLin")
        self.frameLin.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
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
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.btnLinForward = QToolButton(self.frameLin)
        self.btnLinForward.setObjectName(u"btnLinForward")
        sizePolicy.setHeightForWidth(self.btnLinForward.sizePolicy().hasHeightForWidth())
        self.btnLinForward.setSizePolicy(sizePolicy)
        self.btnLinForward.setMinimumSize(QSize(0, 60))
        self.btnLinForward.setFont(font6)
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
        self.btnLinForward.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_10.addWidget(self.btnLinForward)

        self.btnLinBack = QToolButton(self.frameLin)
        self.btnLinBack.setObjectName(u"btnLinBack")
        sizePolicy.setHeightForWidth(self.btnLinBack.sizePolicy().hasHeightForWidth())
        self.btnLinBack.setSizePolicy(sizePolicy)
        self.btnLinBack.setMinimumSize(QSize(0, 60))
        self.btnLinBack.setFont(font6)
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
        self.btnLinBack.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_10.addWidget(self.btnLinBack)

        self.line_9 = QFrame(self.frameLin)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.line_9.setStyleSheet(u"Line {\n"
"	border: 1px solid #ced3d7;\n"
"}")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_10.addWidget(self.line_9)

        self.btnLinHome = QToolButton(self.frameLin)
        self.btnLinHome.setObjectName(u"btnLinHome")
        sizePolicy.setHeightForWidth(self.btnLinHome.sizePolicy().hasHeightForWidth())
        self.btnLinHome.setSizePolicy(sizePolicy)
        self.btnLinHome.setMinimumSize(QSize(0, 120))
        self.btnLinHome.setFont(font6)
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
        self.btnLinHome.setIconSize(QSize(80, 80))
        self.btnLinHome.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_10.addWidget(self.btnLinHome)


        self.verticalLayout_8.addWidget(self.frameLin)


        self.horizontalLayout_3.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 0))
        self.widget_6.setMaximumSize(QSize(400, 16777215))
        self.widget_6.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.verticalLayout_7 = QVBoxLayout(self.widget_6)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.framePos = QFrame(self.widget_6)
        self.framePos.setObjectName(u"framePos")
        self.framePos.setMinimumSize(QSize(0, 155))
        self.framePos.setMaximumSize(QSize(16777215, 155))
        self.framePos.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
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
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.label_11 = QLabel(self.framePos)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 30))
        font12 = QFont()
        font12.setPointSize(11)
        self.label_11.setFont(font12)
        self.label_11.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.verticalLayout_9.addWidget(self.label_11)

        self.lblLinPos = QLabel(self.framePos)
        self.lblLinPos.setObjectName(u"lblLinPos")
        self.lblLinPos.setMaximumSize(QSize(16777215, 40))
        font13 = QFont()
        font13.setPointSize(27)
        font13.setBold(True)
        self.lblLinPos.setFont(font13)
        self.lblLinPos.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.verticalLayout_9.addWidget(self.lblLinPos)

        self.line_2 = QFrame(self.framePos)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.line_2.setStyleSheet(u"Line {\n"
"	border: 1px solid #ced3d7;\n"
"}")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line_2)

        self.btnResLinPos = QPushButton(self.framePos)
        self.btnResLinPos.setObjectName(u"btnResLinPos")
        self.btnResLinPos.setMinimumSize(QSize(0, 40))
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
        self.frameXPos.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
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
        self.label_14.setMaximumSize(QSize(16777215, 40))
        self.label_14.setFont(font4)
        self.label_14.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.verticalLayout_11.addWidget(self.label_14)

        self.line = QFrame(self.frameXPos)
        self.line.setObjectName(u"line")
        self.line.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.line.setStyleSheet(u"Line {\n"
"	border: 1px solid #ced3d7;\n"
"}")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_11.addWidget(self.line)

        self.widget_7 = QWidget(self.frameXPos)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(16777215, 70))
        self.widget_7.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btnBackLin5mm = QPushButton(self.widget_7)
        self.btnBackLin5mm.setObjectName(u"btnBackLin5mm")
        self.btnBackLin5mm.setMinimumSize(QSize(0, 60))
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
        self.btnBackLin1mm.setMinimumSize(QSize(0, 60))
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
        self.btnForwardLin1mm.setMinimumSize(QSize(0, 60))
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
        self.btnForwardLin5mm.setMinimumSize(QSize(0, 60))
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

        self.lblLinSpeed = QLabel(self.frameXPos)
        self.lblLinSpeed.setObjectName(u"lblLinSpeed")
        self.lblLinSpeed.setMaximumSize(QSize(16777215, 40))
        self.lblLinSpeed.setFont(font2)

        self.verticalLayout_11.addWidget(self.lblLinSpeed)

        self.linSpeed = QSlider(self.frameXPos)
        self.linSpeed.setObjectName(u"linSpeed")
        self.linSpeed.setMinimum(1)
        self.linSpeed.setMaximum(100)
        self.linSpeed.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_11.addWidget(self.linSpeed)


        self.verticalLayout_7.addWidget(self.frameXPos)


        self.horizontalLayout_3.addWidget(self.widget_6)

        self.framePosAndHome = QFrame(self.widget_3)
        self.framePosAndHome.setObjectName(u"framePosAndHome")
        self.framePosAndHome.setMaximumSize(QSize(200, 16777215))
        self.framePosAndHome.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
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
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.lblPosLinPre = QLabel(self.framePosAndHome)
        self.lblPosLinPre.setObjectName(u"lblPosLinPre")
        self.lblPosLinPre.setMaximumSize(QSize(16777215, 50))
        self.lblPosLinPre.setFont(font5)
        self.lblPosLinPre.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.lblPosLinPre)

        self.btnSaveLinPos1 = QPushButton(self.framePosAndHome)
        self.btnSaveLinPos1.setObjectName(u"btnSaveLinPos1")
        self.btnSaveLinPos1.setMinimumSize(QSize(0, 60))
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

        self.lblPosLinPost = QLabel(self.framePosAndHome)
        self.lblPosLinPost.setObjectName(u"lblPosLinPost")
        self.lblPosLinPost.setMaximumSize(QSize(16777215, 50))
        self.lblPosLinPost.setFont(font5)
        self.lblPosLinPost.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.lblPosLinPost)

        self.btnSaveLinPos2 = QPushButton(self.framePosAndHome)
        self.btnSaveLinPos2.setObjectName(u"btnSaveLinPos2")
        self.btnSaveLinPos2.setMinimumSize(QSize(0, 60))
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

        self.line_18 = QFrame(self.framePosAndHome)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.Shape.HLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_18)

        self.btnGoLinPos1 = QPushButton(self.framePosAndHome)
        self.btnGoLinPos1.setObjectName(u"btnGoLinPos1")
        self.btnGoLinPos1.setMinimumSize(QSize(0, 60))
        self.btnGoLinPos1.setFont(font3)
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
        self.btnGoLinPos2.setMinimumSize(QSize(0, 60))
        self.btnGoLinPos2.setFont(font3)
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

        self.stackedWidget.addWidget(self.pageLinear)
        self.pageFixation = QWidget()
        self.pageFixation.setObjectName(u"pageFixation")
        self.pageFixation.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.verticalLayout_29 = QVBoxLayout(self.pageFixation)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(5, 5, 5, 5)
        self.widget_16 = QWidget(self.pageFixation)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(0, 200))
        self.widget_16.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.horizontalLayout_12 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_17 = QWidget(self.widget_16)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMaximumSize(QSize(250, 16777215))
        self.widget_17.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.verticalLayout_21 = QVBoxLayout(self.widget_17)
        self.verticalLayout_21.setSpacing(10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.widget_17)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(16777215, 50))
        self.label_20.setFont(font6)
        self.label_20.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.label_20.setStyleSheet(u"QLabel {\n"
"	padding-left: 10px;\n"
"}")
        self.label_20.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.label_20)

        self.frameLin_3 = QFrame(self.widget_17)
        self.frameLin_3.setObjectName(u"frameLin_3")
        self.frameLin_3.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.frameLin_3.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameLin_3 {\n"
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
        self.btnFixForward.setFont(font6)
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
        self.btnFixForward.setIcon(icon4)
        self.btnFixForward.setIconSize(QSize(50, 50))
        self.btnFixForward.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_22.addWidget(self.btnFixForward)

        self.btnFixBack = QToolButton(self.frameLin_3)
        self.btnFixBack.setObjectName(u"btnFixBack")
        sizePolicy.setHeightForWidth(self.btnFixBack.sizePolicy().hasHeightForWidth())
        self.btnFixBack.setSizePolicy(sizePolicy)
        self.btnFixBack.setMinimumSize(QSize(0, 60))
        self.btnFixBack.setFont(font6)
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
        self.btnFixBack.setIcon(icon3)
        self.btnFixBack.setIconSize(QSize(50, 50))
        self.btnFixBack.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_22.addWidget(self.btnFixBack)

        self.line_7 = QFrame(self.frameLin_3)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.line_7.setStyleSheet(u"Line {\n"
"	border: 1px solid #ced3d7;\n"
"}")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_22.addWidget(self.line_7)

        self.btnFixHome = QToolButton(self.frameLin_3)
        self.btnFixHome.setObjectName(u"btnFixHome")
        sizePolicy.setHeightForWidth(self.btnFixHome.sizePolicy().hasHeightForWidth())
        self.btnFixHome.setSizePolicy(sizePolicy)
        self.btnFixHome.setMinimumSize(QSize(0, 120))
        self.btnFixHome.setFont(font6)
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
        self.btnFixHome.setIcon(icon3)
        self.btnFixHome.setIconSize(QSize(80, 80))
        self.btnFixHome.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_22.addWidget(self.btnFixHome)


        self.verticalLayout_21.addWidget(self.frameLin_3)


        self.horizontalLayout_12.addWidget(self.widget_17)

        self.widget_18 = QWidget(self.widget_16)
        self.widget_18.setObjectName(u"widget_18")
        self.widget_18.setMinimumSize(QSize(0, 0))
        self.widget_18.setMaximumSize(QSize(400, 16777215))
        self.widget_18.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.verticalLayout_23 = QVBoxLayout(self.widget_18)
        self.verticalLayout_23.setSpacing(10)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.framePos_3 = QFrame(self.widget_18)
        self.framePos_3.setObjectName(u"framePos_3")
        self.framePos_3.setMinimumSize(QSize(0, 135))
        self.framePos_3.setMaximumSize(QSize(16777215, 135))
        self.framePos_3.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.framePos_3.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#framePos_3 {\n"
"	\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.framePos_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePos_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.framePos_3)
        self.verticalLayout_24.setSpacing(5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(10, 10, 10, 10)
        self.label_21 = QLabel(self.framePos_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 30))
        self.label_21.setFont(font12)
        self.label_21.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.verticalLayout_24.addWidget(self.label_21)

        self.lblFixCur = QLabel(self.framePos_3)
        self.lblFixCur.setObjectName(u"lblFixCur")
        self.lblFixCur.setMaximumSize(QSize(16777215, 40))
        self.lblFixCur.setFont(font13)
        self.lblFixCur.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.verticalLayout_24.addWidget(self.lblFixCur)


        self.verticalLayout_23.addWidget(self.framePos_3)

        self.frameXPos_3 = QFrame(self.widget_18)
        self.frameXPos_3.setObjectName(u"frameXPos_3")
        self.frameXPos_3.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.frameXPos_3.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameXPos_3 {\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.frameXPos_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameXPos_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frameXPos_3)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_23 = QLabel(self.frameXPos_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 40))
        self.label_23.setMaximumSize(QSize(16777215, 40))
        self.label_23.setFont(font4)
        self.label_23.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.verticalLayout_25.addWidget(self.label_23)

        self.line_12 = QFrame(self.frameXPos_3)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_25.addWidget(self.line_12)

        self.widget_19 = QWidget(self.frameXPos_3)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMaximumSize(QSize(16777215, 70))
        self.widget_19.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.horizontalLayout_13 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.btnBackFix5grad = QPushButton(self.widget_19)
        self.btnBackFix5grad.setObjectName(u"btnBackFix5grad")
        self.btnBackFix5grad.setMinimumSize(QSize(0, 60))
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
        self.btnBackFix1grad.setMinimumSize(QSize(0, 60))
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
        self.btnForwardFix1grad.setMinimumSize(QSize(0, 60))
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
        self.btnForwardFix5grad.setMinimumSize(QSize(0, 60))
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

        self.lblFixSpeed = QLabel(self.frameXPos_3)
        self.lblFixSpeed.setObjectName(u"lblFixSpeed")
        self.lblFixSpeed.setMaximumSize(QSize(16777215, 40))
        self.lblFixSpeed.setFont(font2)

        self.verticalLayout_25.addWidget(self.lblFixSpeed)

        self.fixSpeed = QSlider(self.frameXPos_3)
        self.fixSpeed.setObjectName(u"fixSpeed")
        self.fixSpeed.setMinimum(1)
        self.fixSpeed.setMaximum(100)
        self.fixSpeed.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_25.addWidget(self.fixSpeed)


        self.verticalLayout_23.addWidget(self.frameXPos_3)


        self.horizontalLayout_12.addWidget(self.widget_18)

        self.framePosAndHome_3 = QFrame(self.widget_16)
        self.framePosAndHome_3.setObjectName(u"framePosAndHome_3")
        self.framePosAndHome_3.setMaximumSize(QSize(200, 16777215))
        self.framePosAndHome_3.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.framePosAndHome_3.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#framePosAndHome_3\n"
" {\n"
"	\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.framePosAndHome_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePosAndHome_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.framePosAndHome_3)
        self.verticalLayout_26.setSpacing(5)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(10, 10, 10, 10)
        self.pushButton_26 = QPushButton(self.framePosAndHome_3)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setMinimumSize(QSize(0, 60))
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
        self.pushButton_27.setMinimumSize(QSize(0, 60))
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
        self.pushButton_29.setMinimumSize(QSize(0, 60))
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

        self.stackedWidget.addWidget(self.pageFixation)
        self.pagePreCrimp = QWidget()
        self.pagePreCrimp.setObjectName(u"pagePreCrimp")
        self.pagePreCrimp.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.verticalLayout_19 = QVBoxLayout(self.pagePreCrimp)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(5, 5, 5, 5)
        self.widget_9 = QWidget(self.pagePreCrimp)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 200))
        self.widget_9.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.horizontalLayout_7 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMaximumSize(QSize(250, 16777215))
        self.widget_10.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.verticalLayout_12 = QVBoxLayout(self.widget_10)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget_10)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 50))
        self.label_7.setFont(font6)
        self.label_7.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.label_7.setStyleSheet(u"QLabel {\n"
"	padding-left: 10px;\n"
"}")
        self.label_7.setWordWrap(True)

        self.verticalLayout_12.addWidget(self.label_7)

        self.frameLin_2 = QFrame(self.widget_10)
        self.frameLin_2.setObjectName(u"frameLin_2")
        self.frameLin_2.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.frameLin_2.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameLin_2 {\n"
"	background: #e9ecf1;\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.frameLin_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLin_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frameLin_2)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(10, 10, 10, 10)
        self.btnPreUp = QToolButton(self.frameLin_2)
        self.btnPreUp.setObjectName(u"btnPreUp")
        sizePolicy.setHeightForWidth(self.btnPreUp.sizePolicy().hasHeightForWidth())
        self.btnPreUp.setSizePolicy(sizePolicy)
        self.btnPreUp.setMinimumSize(QSize(0, 60))
        self.btnPreUp.setFont(font6)
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
        self.btnPreUp.setIcon(icon5)
        self.btnPreUp.setIconSize(QSize(50, 50))
        self.btnPreUp.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_13.addWidget(self.btnPreUp)

        self.btnDownBack = QToolButton(self.frameLin_2)
        self.btnDownBack.setObjectName(u"btnDownBack")
        sizePolicy.setHeightForWidth(self.btnDownBack.sizePolicy().hasHeightForWidth())
        self.btnDownBack.setSizePolicy(sizePolicy)
        self.btnDownBack.setMinimumSize(QSize(0, 60))
        self.btnDownBack.setFont(font6)
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
        self.btnDownBack.setIcon(icon6)
        self.btnDownBack.setIconSize(QSize(50, 50))
        self.btnDownBack.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.btnDownBack.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.btnDownBack.setAutoRaise(False)

        self.verticalLayout_13.addWidget(self.btnDownBack)

        self.line_4 = QFrame(self.frameLin_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.line_4.setStyleSheet(u"Line {\n"
"	border: 1px solid #ced3d7;\n"
"}")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_4)

        self.btnPreHome = QToolButton(self.frameLin_2)
        self.btnPreHome.setObjectName(u"btnPreHome")
        sizePolicy.setHeightForWidth(self.btnPreHome.sizePolicy().hasHeightForWidth())
        self.btnPreHome.setSizePolicy(sizePolicy)
        self.btnPreHome.setMinimumSize(QSize(0, 120))
        self.btnPreHome.setFont(font6)
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

        self.verticalLayout_13.addWidget(self.btnPreHome)


        self.verticalLayout_12.addWidget(self.frameLin_2)


        self.horizontalLayout_7.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 0))
        self.widget_11.setMaximumSize(QSize(400, 16777215))
        self.widget_11.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.verticalLayout_14 = QVBoxLayout(self.widget_11)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.framePos_2 = QFrame(self.widget_11)
        self.framePos_2.setObjectName(u"framePos_2")
        self.framePos_2.setMinimumSize(QSize(0, 155))
        self.framePos_2.setMaximumSize(QSize(16777215, 155))
        font14 = QFont()
        font14.setPointSize(6)
        self.framePos_2.setFont(font14)
        self.framePos_2.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.framePos_2.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#framePos_2 {\n"
"	\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.framePos_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePos_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.framePos_2)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.label_13 = QLabel(self.framePos_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 30))
        self.label_13.setFont(font12)
        self.label_13.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.verticalLayout_15.addWidget(self.label_13)

        self.lblPrePos = QLabel(self.framePos_2)
        self.lblPrePos.setObjectName(u"lblPrePos")
        self.lblPrePos.setMaximumSize(QSize(16777215, 40))
        self.lblPrePos.setFont(font13)
        self.lblPrePos.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.verticalLayout_15.addWidget(self.lblPrePos)

        self.line_3 = QFrame(self.framePos_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.line_3.setStyleSheet(u"Line {\n"
"	border: 1px solid #ced3d7;\n"
"}")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_15.addWidget(self.line_3)

        self.btnResPrePos = QPushButton(self.framePos_2)
        self.btnResPrePos.setObjectName(u"btnResPrePos")
        self.btnResPrePos.setMinimumSize(QSize(0, 40))
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
        self.frameXPos_2.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.frameXPos_2.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameXPos_2 {\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.frameXPos_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameXPos_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frameXPos_2)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(10, 10, 10, 10)
        self.label_16 = QLabel(self.frameXPos_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(0, 40))
        self.label_16.setMaximumSize(QSize(16777215, 40))
        self.label_16.setFont(font4)
        self.label_16.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.verticalLayout_16.addWidget(self.label_16)

        self.line_15 = QFrame(self.frameXPos_2)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.line_15.setFrameShape(QFrame.Shape.HLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_16.addWidget(self.line_15)

        self.widget_12 = QWidget(self.frameXPos_2)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMaximumSize(QSize(16777215, 70))
        self.widget_12.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.horizontalLayout_8 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btnUpPre5mm = QPushButton(self.widget_12)
        self.btnUpPre5mm.setObjectName(u"btnUpPre5mm")
        self.btnUpPre5mm.setMinimumSize(QSize(0, 60))
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
        self.btnUpPre1mm.setMinimumSize(QSize(0, 60))
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
        self.btnDownPre1mm.setMinimumSize(QSize(0, 60))
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
        self.btnDownPre5mm.setMinimumSize(QSize(0, 60))
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

        self.lblPreSpeed = QLabel(self.frameXPos_2)
        self.lblPreSpeed.setObjectName(u"lblPreSpeed")
        self.lblPreSpeed.setMaximumSize(QSize(16777215, 40))
        self.lblPreSpeed.setFont(font2)

        self.verticalLayout_16.addWidget(self.lblPreSpeed)

        self.preSpeed = QSlider(self.frameXPos_2)
        self.preSpeed.setObjectName(u"preSpeed")
        self.preSpeed.setMinimum(1)
        self.preSpeed.setMaximum(100)
        self.preSpeed.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_16.addWidget(self.preSpeed)


        self.verticalLayout_14.addWidget(self.frameXPos_2)


        self.horizontalLayout_7.addWidget(self.widget_11)

        self.framePosAndHome_2 = QFrame(self.widget_9)
        self.framePosAndHome_2.setObjectName(u"framePosAndHome_2")
        self.framePosAndHome_2.setMaximumSize(QSize(200, 16777215))
        self.framePosAndHome_2.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.framePosAndHome_2.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#framePosAndHome_2 {\n"
"	\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.framePosAndHome_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePosAndHome_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.framePosAndHome_2)
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(10, 10, 10, 10)
        self.lblSaveForcePre = QLabel(self.framePosAndHome_2)
        self.lblSaveForcePre.setObjectName(u"lblSaveForcePre")
        self.lblSaveForcePre.setMinimumSize(QSize(0, 50))
        self.lblSaveForcePre.setMaximumSize(QSize(16777215, 50))
        self.lblSaveForcePre.setFont(font5)
        self.lblSaveForcePre.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.lblSaveForcePre)

        self.btnSavPreForce = QPushButton(self.framePosAndHome_2)
        self.btnSavPreForce.setObjectName(u"btnSavPreForce")
        self.btnSavPreForce.setMinimumSize(QSize(0, 60))
        self.btnSavPreForce.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_17.addWidget(self.btnSavPreForce)

        self.btnGoPreForce = QPushButton(self.framePosAndHome_2)
        self.btnGoPreForce.setObjectName(u"btnGoPreForce")
        self.btnGoPreForce.setMinimumSize(QSize(0, 60))
        self.btnGoPreForce.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.verticalLayout_17.addWidget(self.btnGoPreForce)

        self.line_5 = QFrame(self.framePosAndHome_2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.line_5.setStyleSheet(u"Line {\n"
"	border: 1px solid #ced3d7;\n"
"}")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_17.addWidget(self.line_5)

        self.label_18 = QLabel(self.framePosAndHome_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 30))
        self.label_18.setFont(font12)
        self.label_18.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.verticalLayout_17.addWidget(self.label_18)

        self.lblPreForce = QLabel(self.framePosAndHome_2)
        self.lblPreForce.setObjectName(u"lblPreForce")
        self.lblPreForce.setMaximumSize(QSize(16777215, 40))
        self.lblPreForce.setFont(font13)
        self.lblPreForce.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.verticalLayout_17.addWidget(self.lblPreForce)


        self.horizontalLayout_7.addWidget(self.framePosAndHome_2)


        self.verticalLayout_19.addWidget(self.widget_9)

        self.stackedWidget.addWidget(self.pagePreCrimp)
        self.pagePostCrimp = QWidget()
        self.pagePostCrimp.setObjectName(u"pagePostCrimp")
        self.pagePostCrimp.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.verticalLayout_42 = QVBoxLayout(self.pagePostCrimp)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(5, 5, 5, 5)
        self.widget_26 = QWidget(self.pagePostCrimp)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setMinimumSize(QSize(0, 200))
        self.widget_26.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.horizontalLayout_21 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_21.setSpacing(10)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.widget_27 = QWidget(self.widget_26)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMaximumSize(QSize(250, 16777215))
        self.widget_27.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.verticalLayout_36 = QVBoxLayout(self.widget_27)
        self.verticalLayout_36.setSpacing(10)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.widget_27)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 50))
        self.label_25.setFont(font6)
        self.label_25.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.label_25.setStyleSheet(u"QLabel {\n"
"	padding-left: 10px;\n"
"}")
        self.label_25.setWordWrap(True)

        self.verticalLayout_36.addWidget(self.label_25)

        self.frameLin_5 = QFrame(self.widget_27)
        self.frameLin_5.setObjectName(u"frameLin_5")
        self.frameLin_5.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.frameLin_5.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameLin_5 {\n"
"	background: #e9ecf1;\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.frameLin_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLin_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frameLin_5)
        self.verticalLayout_37.setSpacing(10)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(10, 10, 10, 10)
        self.btnPostForward = QToolButton(self.frameLin_5)
        self.btnPostForward.setObjectName(u"btnPostForward")
        sizePolicy.setHeightForWidth(self.btnPostForward.sizePolicy().hasHeightForWidth())
        self.btnPostForward.setSizePolicy(sizePolicy)
        self.btnPostForward.setMinimumSize(QSize(0, 60))
        self.btnPostForward.setFont(font6)
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
        self.btnPostForward.setIcon(icon4)
        self.btnPostForward.setIconSize(QSize(50, 50))
        self.btnPostForward.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_37.addWidget(self.btnPostForward)

        self.btnPostBack = QToolButton(self.frameLin_5)
        self.btnPostBack.setObjectName(u"btnPostBack")
        sizePolicy.setHeightForWidth(self.btnPostBack.sizePolicy().hasHeightForWidth())
        self.btnPostBack.setSizePolicy(sizePolicy)
        self.btnPostBack.setMinimumSize(QSize(0, 60))
        self.btnPostBack.setFont(font6)
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
        self.btnPostBack.setIcon(icon3)
        self.btnPostBack.setIconSize(QSize(50, 50))
        self.btnPostBack.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_37.addWidget(self.btnPostBack)

        self.line_8 = QFrame(self.frameLin_5)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.line_8.setStyleSheet(u"Line {\n"
"	border: 1px solid #ced3d7;\n"
"}")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_37.addWidget(self.line_8)

        self.btnPostHome = QToolButton(self.frameLin_5)
        self.btnPostHome.setObjectName(u"btnPostHome")
        sizePolicy.setHeightForWidth(self.btnPostHome.sizePolicy().hasHeightForWidth())
        self.btnPostHome.setSizePolicy(sizePolicy)
        self.btnPostHome.setMinimumSize(QSize(0, 120))
        self.btnPostHome.setFont(font6)
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
        self.btnPostHome.setIcon(icon3)
        self.btnPostHome.setIconSize(QSize(80, 80))
        self.btnPostHome.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.verticalLayout_37.addWidget(self.btnPostHome)


        self.verticalLayout_36.addWidget(self.frameLin_5)


        self.horizontalLayout_21.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.widget_26)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMinimumSize(QSize(0, 0))
        self.widget_28.setMaximumSize(QSize(400, 16777215))
        self.widget_28.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.verticalLayout_38 = QVBoxLayout(self.widget_28)
        self.verticalLayout_38.setSpacing(10)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.framePos_4 = QFrame(self.widget_28)
        self.framePos_4.setObjectName(u"framePos_4")
        self.framePos_4.setMinimumSize(QSize(0, 135))
        self.framePos_4.setMaximumSize(QSize(16777215, 135))
        self.framePos_4.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.framePos_4.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#framePos_4 {\n"
"	\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.framePos_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePos_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.framePos_4)
        self.verticalLayout_39.setSpacing(5)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(10, 10, 10, 10)
        self.label_29 = QLabel(self.framePos_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(16777215, 30))
        self.label_29.setFont(font12)
        self.label_29.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.verticalLayout_39.addWidget(self.label_29)

        self.lblPostTorq = QLabel(self.framePos_4)
        self.lblPostTorq.setObjectName(u"lblPostTorq")
        self.lblPostTorq.setMaximumSize(QSize(16777215, 40))
        self.lblPostTorq.setFont(font13)
        self.lblPostTorq.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.verticalLayout_39.addWidget(self.lblPostTorq)


        self.verticalLayout_38.addWidget(self.framePos_4)

        self.frameXPos_4 = QFrame(self.widget_28)
        self.frameXPos_4.setObjectName(u"frameXPos_4")
        self.frameXPos_4.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.frameXPos_4.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#frameXPos_4 {\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.frameXPos_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameXPos_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frameXPos_4)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_31 = QLabel(self.frameXPos_4)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(0, 40))
        self.label_31.setMaximumSize(QSize(16777215, 40))
        self.label_31.setFont(font4)
        self.label_31.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.verticalLayout_27.addWidget(self.label_31)

        self.line_16 = QFrame(self.frameXPos_4)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.line_16.setFrameShape(QFrame.Shape.HLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_27.addWidget(self.line_16)

        self.widget_29 = QWidget(self.frameXPos_4)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setMaximumSize(QSize(16777215, 70))
        self.widget_29.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.horizontalLayout_22 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.btnBackPost5grad = QPushButton(self.widget_29)
        self.btnBackPost5grad.setObjectName(u"btnBackPost5grad")
        self.btnBackPost5grad.setMinimumSize(QSize(0, 60))
        self.btnBackPost5grad.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.horizontalLayout_22.addWidget(self.btnBackPost5grad)

        self.btnBackPost1grad = QPushButton(self.widget_29)
        self.btnBackPost1grad.setObjectName(u"btnBackPost1grad")
        self.btnBackPost1grad.setMinimumSize(QSize(0, 60))
        self.btnBackPost1grad.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.horizontalLayout_22.addWidget(self.btnBackPost1grad)

        self.btnForwardPost1grad = QPushButton(self.widget_29)
        self.btnForwardPost1grad.setObjectName(u"btnForwardPost1grad")
        self.btnForwardPost1grad.setMinimumSize(QSize(0, 60))
        self.btnForwardPost1grad.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.horizontalLayout_22.addWidget(self.btnForwardPost1grad)

        self.btnForwardPost5grad = QPushButton(self.widget_29)
        self.btnForwardPost5grad.setObjectName(u"btnForwardPost5grad")
        self.btnForwardPost5grad.setMinimumSize(QSize(0, 60))
        self.btnForwardPost5grad.setStyleSheet(u"QPushButton {\n"
"	background: #bdcfdd;\n"
"	border: 2px solid #a6b8c6;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: #cfddeb;\n"
"\n"
"}")

        self.horizontalLayout_22.addWidget(self.btnForwardPost5grad)


        self.verticalLayout_27.addWidget(self.widget_29)

        self.lblPostSpeed = QLabel(self.frameXPos_4)
        self.lblPostSpeed.setObjectName(u"lblPostSpeed")
        self.lblPostSpeed.setMaximumSize(QSize(16777215, 40))
        self.lblPostSpeed.setFont(font2)

        self.verticalLayout_27.addWidget(self.lblPostSpeed)

        self.postSpeed = QSlider(self.frameXPos_4)
        self.postSpeed.setObjectName(u"postSpeed")
        self.postSpeed.setMinimum(1)
        self.postSpeed.setMaximum(100)
        self.postSpeed.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_27.addWidget(self.postSpeed)


        self.verticalLayout_38.addWidget(self.frameXPos_4)


        self.horizontalLayout_21.addWidget(self.widget_28)

        self.framePosAndHome_4 = QFrame(self.widget_26)
        self.framePosAndHome_4.setObjectName(u"framePosAndHome_4")
        self.framePosAndHome_4.setMaximumSize(QSize(200, 16777215))
        self.framePosAndHome_4.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.framePosAndHome_4.setStyleSheet(u"* {\n"
"	background: #e9ecf1;\n"
"}\n"
"\n"
"QFrame#framePosAndHome_4 {\n"
"	\n"
"	border-radius: 7px;\n"
"	border: 1px solid #c1c6cc;\n"
"}")
        self.framePosAndHome_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.framePosAndHome_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.framePosAndHome_4)
        self.verticalLayout_41.setSpacing(10)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(10, 10, 10, 10)
        self.pushButton_37 = QPushButton(self.framePosAndHome_4)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setMinimumSize(QSize(0, 60))
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
        self.pushButton_38.setMinimumSize(QSize(0, 60))
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
        self.pushButton_39.setMinimumSize(QSize(0, 60))
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

        self.stackedWidget.addWidget(self.pagePostCrimp)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblDate.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.lblTimeStart.setText(QCoreApplication.translate("MainWindow", u"sec", None))
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
        self.lblLinPosMan.setText(QCoreApplication.translate("MainWindow", u"--- \u043c\u043c", None))
        self.btnLinForwardMan.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043f\u0435\u0440\u0435\u0434", None))
        self.btnLinBackMan.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.btnGoLinPos1Man.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0437\u0438\u0446\u0438\u044f \u043f\u0440\u0435\u0434\u043e\u0431\u0436\u0438\u043c\u0430", None))
        self.btnGoLinPos2Man.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0437\u0438\u0446\u0438\u044f \u043f\u043e\u0441\u0442\u043e\u0431\u0436\u0438\u043c\u0430", None))
        self.btnLinHomeMan.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u043e\u0439", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u0444\u0438\u043a\u0441\u0430\u0446\u0438\u0438", None))
        self.btnFixBackMan.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0432\u043e\u0434\u0438\u0442\u044c", None))
        self.btnFixForwardMan.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0434\u0438\u0442\u044c", None))
        self.toolButton_28.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0436\u0430\u0442\u044c", None))
        self.toolButton_29.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0436\u0430\u0442\u044c", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u043f\u0440\u0435\u0434\u043e\u0431\u0436\u0438\u043c\u0430", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0415\u041a\u0423\u0429\u0410\u042f \u041f\u041e\u0417\u0418\u0426\u0418\u042f", None))
        self.lblPrePosMan.setText(QCoreApplication.translate("MainWindow", u"--- \u043c\u043c", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0415\u041a\u0423\u0429\u0415\u0415 \u0423\u0421\u0418\u041b\u0418\u0415", None))
        self.lblPreForceMan.setText(QCoreApplication.translate("MainWindow", u"--- \u041d", None))
        self.btnPreUpMan.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0440\u0445", None))
        self.btnPreDownMan.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0438\u0437", None))
        self.btnGoPreForceMan.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e \u0443\u0441\u0438\u043b\u0438\u044f", None))
        self.btnPreHomeMan.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u043e\u0439", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u043f\u043e\u0441\u0442\u043e\u0431\u0436\u0438\u043c\u0430", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0415\u041a\u0423\u0429\u0418\u0419 \u041c\u041e\u041c\u0415\u041d\u0422", None))
        self.lblPostTorqMan.setText(QCoreApplication.translate("MainWindow", u"--- \u041d\u00b7\u043c", None))
        self.btnPostBackMan.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0432\u043e\u0434\u0438\u0442\u044c", None))
        self.btnPostForwardMan.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0434\u0438\u0442\u044c", None))
        self.toolButton_25.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0436\u0430\u0442\u044c", None))
        self.toolButton_26.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0436\u0430\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043f\u0441\u0441... \u041f\u0443\u0441\u0442\u043e(\n"
"\u0417\u0434\u0435\u0441\u044c \u0441\u043a\u043e\u0440\u043e \u0447\u0442\u043e-\u0442\u043e \u0431\u0443\u0434\u0435\u0442!", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0434\u0430\u0442\u0447\u0438\u043a:", None))
        self.btnResetStats.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043e\u0442\u043a\u043b\u0430\u0434\u043a\u0438", None))
        self.comboBoxSensor.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a \u043c\u043e\u043c\u0435\u043d\u0442\u0430 BTQ-403A", None))
        self.comboBoxSensor.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a \u0443\u0441\u0438\u043b\u0438\u044f TCF-715A", None))
        self.comboBoxSensor.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a \u0442\u043e\u043a\u0430 ACS712", None))
        self.comboBoxSensor.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0447\u0438\u043a \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u044b BME280", None))

        self.lblSensData.setText(QCoreApplication.translate("MainWindow", u"sensors data", None))
        self.label_4.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0432\u0435\u043d\u0442\u0438\u043b\u044f\u0442\u043e\u0440\u043e\u043c \u043a\u043e\u0440\u043f\u0443\u0441\u0430", None))
        self.label_9.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0436\u0438\u043c \u0440\u0430\u0431\u043e\u0442\u044b", None))
        self.getAutoFan.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0440\u0435\u0436\u0438\u043c (\u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u043c\u044b\u0439)", None))
        self.getManualFan.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0447\u043d\u043e\u0439 \u0440\u0435\u0436\u0438\u043c (\u0444\u0438\u043a\u0441\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u0430\u044f \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c)", None))
        self.fanOff.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043a\u043b\u044e\u0447\u0438\u0442\u044c", None))
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
        self.btnLinHome.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u043e\u0439", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0415\u041a\u0423\u0429\u0410\u042f \u041f\u041e\u0417\u0418\u0426\u0418\u042f", None))
        self.lblLinPos.setText(QCoreApplication.translate("MainWindow", u"--- \u043c\u043c", None))
        self.btnResLinPos.setText(QCoreApplication.translate("MainWindow", u"C\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u0442\u0435\u043a\u0443\u0449\u0443\u044e \u043f\u043e\u0437\u0438\u0446\u0438\u044e", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043d\u043e\u0435 \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u0435", None))
        self.btnBackLin5mm.setText(QCoreApplication.translate("MainWindow", u"-5 \u043c\u043c", None))
        self.btnBackLin1mm.setText(QCoreApplication.translate("MainWindow", u"-1 \u043c\u043c", None))
        self.btnForwardLin1mm.setText(QCoreApplication.translate("MainWindow", u"+1 \u043c\u043c", None))
        self.btnForwardLin5mm.setText(QCoreApplication.translate("MainWindow", u"+5 \u043c\u043c", None))
        self.lblLinSpeed.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u044f: --%", None))
        self.lblPosLinPre.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u043f\u043e\u0437\u0438\u0446\u0438\u044f \u043f\u0440\u0435\u0434\u043e\u0431\u0436\u0438\u043c\u0430: --- \u043c\u043c", None))
        self.btnSaveLinPos1.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043f\u043e\u0437\u0438\u0446\u0438\u044e\n"
"\u043f\u0440\u0435\u0434\u043e\u0431\u0436\u0438\u043c\u0430", None))
        self.lblPosLinPost.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u043f\u043e\u0437\u0438\u0446\u0438\u044f \u043f\u043e\u0441\u0442\u043e\u0431\u0436\u0438\u043c\u0430: ---\u043c\u043c", None))
        self.btnSaveLinPos2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043f\u043e\u0437\u0438\u0446\u0438\u044e\n"
"\u043f\u043e\u0441\u0442\u043e\u0431\u0436\u0438\u043c\u0430", None))
        self.btnGoLinPos1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u043c\u0435\u0441\u0442\u0438\u0442\u044c\u0441\u044f \u043a \u043f\u043e\u0437\u0438\u0446\u0438\u0438\n"
"\u043f\u0440\u0435\u0434\u043e\u0431\u0436\u0438\u043c\u0430", None))
        self.btnGoLinPos2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u043c\u0435\u0441\u0442\u0438\u0442\u044c\u0441\u044f \u043a \u043f\u043e\u0437\u0438\u0446\u0438\u0438\n"
"\u043f\u043e\u0441\u0442\u043e\u0431\u0436\u0438\u043c\u0430", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u0444\u0438\u043a\u0441\u0430\u0446\u0438\u0438", None))
        self.btnFixForward.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0436\u0430\u0442\u044c", None))
        self.btnFixBack.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0436\u0430\u0442\u044c", None))
        self.btnFixHome.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e \u0440\u0430\u0437\u0436\u0430\u0442\u044c", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0415\u041a\u0423\u0429\u0410\u042f \u0421\u0418\u041b\u0410 \u0422\u041e\u041a\u0410", None))
        self.lblFixCur.setText(QCoreApplication.translate("MainWindow", u"--- \u0410", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043d\u043e\u0435 \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u0435", None))
        self.btnBackFix5grad.setText(QCoreApplication.translate("MainWindow", u"-5\u00b0", None))
        self.btnBackFix1grad.setText(QCoreApplication.translate("MainWindow", u"-1\u00b0", None))
        self.btnForwardFix1grad.setText(QCoreApplication.translate("MainWindow", u"+1\u00b0", None))
        self.btnForwardFix5grad.setText(QCoreApplication.translate("MainWindow", u"+5\u00b0", None))
        self.lblFixSpeed.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u0444\u0438\u043a\u0441\u0430\u0446\u0438\u0438: --%", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0441\u0438\u043b\u0443 \u0442\u043e\u043a\u0430", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043f\u043e\u0437\u0438\u0446\u0438\u044e\n"
"\u0440\u0430\u0437\u0436\u0430\u0442\u0438\u044f", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0436\u0430\u0442\u044c \u0434\u043e \u0441\u0438\u043b\u044b \u0442\u043e\u043a\u0430", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u043f\u0440\u0435\u0434\u043e\u0431\u0436\u0438\u043c\u0430", None))
        self.btnPreUp.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0440\u0445", None))
        self.btnDownBack.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0438\u0437", None))
        self.btnPreHome.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u043e\u0439", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0415\u041a\u0423\u0429\u0410\u042f \u041f\u041e\u0417\u0418\u0426\u0418\u042f", None))
        self.lblPrePos.setText(QCoreApplication.translate("MainWindow", u"--- \u043c\u043c", None))
        self.btnResPrePos.setText(QCoreApplication.translate("MainWindow", u"C\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u0442\u0435\u043a\u0443\u0449\u0443\u044e \u043f\u043e\u0437\u0438\u0446\u0438\u044e", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043d\u043e\u0435 \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u0435", None))
        self.btnUpPre5mm.setText(QCoreApplication.translate("MainWindow", u"-5 \u043c\u043c", None))
        self.btnUpPre1mm.setText(QCoreApplication.translate("MainWindow", u"-1 \u043c\u043c", None))
        self.btnDownPre1mm.setText(QCoreApplication.translate("MainWindow", u"+1 \u043c\u043c", None))
        self.btnDownPre5mm.setText(QCoreApplication.translate("MainWindow", u"+5 \u043c\u043c", None))
        self.lblPreSpeed.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u044f: --%", None))
        self.lblSaveForcePre.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043a\u0443\u0449\u0435\u0435 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u043d\u043e\u0435 \u0443\u0441\u0438\u043b\u0438\u0435: -- \u041d", None))
        self.btnSavPreForce.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0443\u0441\u0438\u043b\u0438\u0435", None))
        self.btnGoPreForce.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u043c\u0435\u0441\u0442\u0438\u0442\u044c\u0441\u044f \u0434\u043e \u0443\u0441\u0438\u043b\u0438\u044f", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0415\u041a\u0423\u0429\u0415\u0415 \u0423\u0421\u0418\u041b\u0418\u0415", None))
        self.lblPreForce.setText(QCoreApplication.translate("MainWindow", u"--- \u041d", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u043f\u043e\u0441\u0442\u043e\u0431\u0436\u0438\u043c\u0430", None))
        self.btnPostForward.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0436\u0430\u0442\u044c", None))
        self.btnPostBack.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0436\u0430\u0442\u044c", None))
        self.btnPostHome.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e \u0440\u0430\u0437\u0436\u0430\u0442\u044c", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0415\u041a\u0423\u0429\u0418\u0419 \u041c\u041e\u041c\u0415\u041d\u0422", None))
        self.lblPostTorq.setText(QCoreApplication.translate("MainWindow", u"-- \u041d\u00b7\u043c", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043d\u043e\u0435 \u0437\u0430\u0436\u0430\u0442\u0438\u0435", None))
        self.btnBackPost5grad.setText(QCoreApplication.translate("MainWindow", u"-5\u00b0", None))
        self.btnBackPost1grad.setText(QCoreApplication.translate("MainWindow", u"-1\u00b0", None))
        self.btnForwardPost1grad.setText(QCoreApplication.translate("MainWindow", u"+1\u00b0", None))
        self.btnForwardPost5grad.setText(QCoreApplication.translate("MainWindow", u"+5\u00b0", None))
        self.lblPostSpeed.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043e\u0431\u0436\u0438\u043c\u0430: --%", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043c\u043e\u043c\u0435\u043d\u0442", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043f\u043e\u0437\u0438\u0446\u0438\u044e\n"
"\u0440\u0430\u0437\u0436\u0430\u0442\u0438\u044f", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0436\u0430\u0442\u044c \u0434\u043e \u043c\u043e\u043c\u0435\u043d\u0442\u0430", None))
    # retranslateUi

