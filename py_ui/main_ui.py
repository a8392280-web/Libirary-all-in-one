# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_uidUjXgU.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QVBoxLayout, QWidget)
import py_ui.resources_rc

class Ui_main_widget(object):
    def setupUi(self, main_widget):
        if not main_widget.objectName():
            main_widget.setObjectName(u"main_widget")
        main_widget.resize(1118, 838)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_widget.sizePolicy().hasHeightForWidth())
        main_widget.setSizePolicy(sizePolicy)
        main_widget.setMinimumSize(QSize(0, 0))
        main_widget.setMaximumSize(QSize(16777215, 16777215))
        main_widget.setStyleSheet(u"QWidget#main_widget {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 10px;\n"
"}")
        self.gridLayout = QGridLayout(main_widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.main_body_widget = QWidget(main_widget)
        self.main_body_widget.setObjectName(u"main_body_widget")
        sizePolicy.setHeightForWidth(self.main_body_widget.sizePolicy().hasHeightForWidth())
        self.main_body_widget.setSizePolicy(sizePolicy)
        self.main_body_widget.setStyleSheet(u"QLabel {\n"
"    color: rgb(230, 230, 230);}")
        self.gridLayout_2 = QGridLayout(self.main_body_widget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stacked_body_Widget = QStackedWidget(self.main_body_widget)
        self.stacked_body_Widget.setObjectName(u"stacked_body_Widget")
        self.stacked_body_Widget.setEnabled(True)
        self.stacked_body_Widget.setStyleSheet(u"QStackedWidget {\n"
"    background-color: #262e39;}\n"
"\n"
"QListWidget{\n"
"	background-color: #182126;\n"
"	border:none;\n"
"}\n"
"\n"
"/* Navigation Buttons */\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    text-align: middle;\n"
"    border: none;\n"
"    padding: 5px 5px 5px 5px;\n"
"    font-size: 14px;\n"
"    font-weight: normal;\n"
"    border-radius: 6px;\n"
"	margin: 0px 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(79, 79, 79);\n"
"}\n"
"QLineEdit {\n"
"    background-color: #2d2d2d;\n"
"    border: 2px solid #404040;\n"
"    border-radius: 8px;\n"
"    font-size: 14px;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #888888;\n"
"    font-size: 14px;\n"
"    font-style: normal;\n"
"}\n"
"\n"
"\n"
"/* Separator Line */\n"
"Line {\n"
"    background-color: rgb(70, 70, 70);\n"
"}\n"
"\n"
"QComboBox {\n"
"    color: #e0e6f0; /* "
                        "light text */\n"
"    font-size: 14px;\n"
"    background-color: rgba(255, 255, 255, 0.05); /* subtle transparent bg */\n"
"    border: 1px solid rgba(255, 255, 255, 0.15);\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    border: 1px solid #5891ff; /* subtle blue border */\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #5891ff;\n"
"    background-color: rgba(255, 255, 255, 0.12);\n"
"    outline: none;\n"
"}\n"
"\n"
"/* \u25bc Dropdown arrow */\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 25px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/Icons/sort_by.png); /* replace with your icon */\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"/* Popup (the dropdown list) */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #2e3a4b; /* darker popup background */\n"
"    color: #e0e6f0;\n"
"    border: 1px solid #5"
                        "891ff;\n"
"    selection-background-color: #3c4d63; /* selected item background */\n"
"    selection-color: #ffffff;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: none;\n"
"    background:transparent;  /* light clean background */\n"
"}\n"
"\n"
"QTabBar {\n"
"    qproperty-drawBase: 0;\n"
"    alignment: center;  /* center the tabs */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: transparent;\n"
"    color: #6d747e;\n"
"    padding: 10px 25px;\n"
"    margin: 0px 5px;\n"
"    font: 13pt \"Segoe UI\";\n"
"    border-bottom: 3px solid transparent;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    color: #cad1d9;  /* accent blue */\n"
"    border-bottom: 3px solid #fbffff;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    color: #cad1d9;\n"
"}\n"
"")
        self.welcome_section = QWidget()
        self.welcome_section.setObjectName(u"welcome_section")
        self.welcome_section.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.welcome_section)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.label_2 = QLabel(self.welcome_section)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(self.welcome_section)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial Rounded MT"])
        font.setPointSize(36)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"    color: rgb(230, 230, 230);}")
        self.label.setTextFormat(Qt.TextFormat.RichText)
        self.label.setScaledContents(False)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.stacked_body_Widget.addWidget(self.welcome_section)
        self.movies_section = QWidget()
        self.movies_section.setObjectName(u"movies_section")
        self.movies_section.setStyleSheet(u"")
        self.gridLayout_7 = QGridLayout(self.movies_section)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 5, -1, 10)
        self.movies_menu = QPushButton(self.movies_section)
        self.movies_menu.setObjectName(u"movies_menu")
        self.movies_menu.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/icons/Icons/more.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.movies_menu.setIcon(icon)
        self.movies_menu.setIconSize(QSize(20, 20))
        self.movies_menu.setCheckable(True)
        self.movies_menu.setFlat(False)

        self.horizontalLayout_2.addWidget(self.movies_menu)

        self.movies_label = QLabel(self.movies_section)
        self.movies_label.setObjectName(u"movies_label")
        font1 = QFont()
        font1.setFamilies([u"Arial Rounded MT"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.movies_label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.movies_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.movies_add_botton = QPushButton(self.movies_section)
        self.movies_add_botton.setObjectName(u"movies_add_botton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.movies_add_botton.sizePolicy().hasHeightForWidth())
        self.movies_add_botton.setSizePolicy(sizePolicy1)
        self.movies_add_botton.setMinimumSize(QSize(100, 0))
        self.movies_add_botton.setMaximumSize(QSize(50, 16777215))
        self.movies_add_botton.setAutoFillBackground(False)
        self.movies_add_botton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.movies_add_botton.setIcon(icon1)
        self.movies_add_botton.setIconSize(QSize(30, 30))
        self.movies_add_botton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.movies_add_botton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.movies_tap_widget = QTabWidget(self.movies_section)
        self.movies_tap_widget.setObjectName(u"movies_tap_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.movies_tap_widget.sizePolicy().hasHeightForWidth())
        self.movies_tap_widget.setSizePolicy(sizePolicy2)
        self.movies_tap_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.movies_tap_widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.movies_tap_widget.setAutoFillBackground(False)
        self.movies_tap_widget.setStyleSheet(u"")
        self.movies_tap_widget.setTabPosition(QTabWidget.TabPosition.North)
        self.movies_tap_widget.setTabShape(QTabWidget.TabShape.Rounded)
        self.movies_tap_widget.setElideMode(Qt.TextElideMode.ElideNone)
        self.movies_tap_widget.setDocumentMode(True)
        self.movies_tap_widget.setTabsClosable(False)
        self.movies_tap_widget.setMovable(False)
        self.movies_tap_widget.setTabBarAutoHide(False)
        self.movies_watching = QWidget()
        self.movies_watching.setObjectName(u"movies_watching")
        self.gridLayout_13 = QGridLayout(self.movies_watching)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 10, -1, -1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 0, 5, -1)
        self.movies_search_icon_1 = QPushButton(self.movies_watching)
        self.movies_search_icon_1.setObjectName(u"movies_search_icon_1")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.movies_search_icon_1.setIcon(icon2)
        self.movies_search_icon_1.setIconSize(QSize(32, 32))
        self.movies_search_icon_1.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.movies_search_icon_1)

        self.movies_search_1 = QLineEdit(self.movies_watching)
        self.movies_search_1.setObjectName(u"movies_search_1")
        self.movies_search_1.setMaximumSize(QSize(200, 30))
        self.movies_search_1.setStyleSheet(u"")
        self.movies_search_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.movies_search_1)

        self.line_2 = QFrame(self.movies_watching)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line_2)

        self.movies_random_button_1 = QPushButton(self.movies_watching)
        self.movies_random_button_1.setObjectName(u"movies_random_button_1")
        self.movies_random_button_1.setAutoFillBackground(False)
        self.movies_random_button_1.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/dice.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.movies_random_button_1.setIcon(icon3)
        self.movies_random_button_1.setIconSize(QSize(32, 32))
        self.movies_random_button_1.setFlat(True)

        self.horizontalLayout_5.addWidget(self.movies_random_button_1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.movies_view_1 = QPushButton(self.movies_watching)
        self.movies_view_1.setObjectName(u"movies_view_1")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/list.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icons/Icons/grid.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.movies_view_1.setIcon(icon4)
        self.movies_view_1.setIconSize(QSize(32, 32))
        self.movies_view_1.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.movies_view_1)

        self.line = QFrame(self.movies_watching)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"/* Separator Line */\n"
"Line {\n"
"    background-color: rgb(70, 70, 70);\n"
"}\n"
"")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_5.addWidget(self.line)

        self.movies_sort_by_1 = QComboBox(self.movies_watching)
        self.movies_sort_by_1.setObjectName(u"movies_sort_by_1")
        self.movies_sort_by_1.setStyleSheet(u"")
        self.movies_sort_by_1.setEditable(False)
        self.movies_sort_by_1.setIconSize(QSize(32, 32))
        self.movies_sort_by_1.setDuplicatesEnabled(False)
        self.movies_sort_by_1.setFrame(False)
        self.movies_sort_by_1.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_5.addWidget(self.movies_sort_by_1)


        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.movies_list_1 = QListWidget(self.movies_watching)
        self.movies_list_1.setObjectName(u"movies_list_1")

        self.verticalLayout_8.addWidget(self.movies_list_1)


        self.gridLayout_13.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.movies_tap_widget.addTab(self.movies_watching, "")
        self.movies_want_to_watch = QWidget()
        self.movies_want_to_watch.setObjectName(u"movies_want_to_watch")
        self.gridLayout_12 = QGridLayout(self.movies_want_to_watch)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 10, -1, -1)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, -1, 5, -1)
        self.movies_search_icon_2 = QPushButton(self.movies_want_to_watch)
        self.movies_search_icon_2.setObjectName(u"movies_search_icon_2")
        self.movies_search_icon_2.setIcon(icon2)
        self.movies_search_icon_2.setIconSize(QSize(32, 32))
        self.movies_search_icon_2.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.movies_search_icon_2)

        self.movies_search_2 = QLineEdit(self.movies_want_to_watch)
        self.movies_search_2.setObjectName(u"movies_search_2")
        self.movies_search_2.setMaximumSize(QSize(200, 30))
        self.movies_search_2.setStyleSheet(u"")
        self.movies_search_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.movies_search_2)

        self.line_5 = QFrame(self.movies_want_to_watch)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_5)

        self.movies_random_button_2 = QPushButton(self.movies_want_to_watch)
        self.movies_random_button_2.setObjectName(u"movies_random_button_2")
        self.movies_random_button_2.setAutoFillBackground(False)
        self.movies_random_button_2.setIcon(icon3)
        self.movies_random_button_2.setIconSize(QSize(32, 32))
        self.movies_random_button_2.setFlat(True)

        self.horizontalLayout_8.addWidget(self.movies_random_button_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.movies_view_2 = QPushButton(self.movies_want_to_watch)
        self.movies_view_2.setObjectName(u"movies_view_2")
        self.movies_view_2.setIcon(icon4)
        self.movies_view_2.setIconSize(QSize(32, 32))
        self.movies_view_2.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.movies_view_2)

        self.line_6 = QFrame(self.movies_want_to_watch)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_6)

        self.movies_sort_by_2 = QComboBox(self.movies_want_to_watch)
        self.movies_sort_by_2.setObjectName(u"movies_sort_by_2")
        self.movies_sort_by_2.setIconSize(QSize(32, 32))
        self.movies_sort_by_2.setFrame(False)
        self.movies_sort_by_2.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_8.addWidget(self.movies_sort_by_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.movies_list_2 = QListWidget(self.movies_want_to_watch)
        self.movies_list_2.setObjectName(u"movies_list_2")

        self.verticalLayout_10.addWidget(self.movies_list_2)


        self.gridLayout_12.addLayout(self.verticalLayout_10, 0, 0, 1, 1)

        self.movies_tap_widget.addTab(self.movies_want_to_watch, "")
        self.movies_continue_later = QWidget()
        self.movies_continue_later.setObjectName(u"movies_continue_later")
        self.gridLayout_9 = QGridLayout(self.movies_continue_later)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 9, 0, 0)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, -1, 5, -1)
        self.movies_search_icon_3 = QPushButton(self.movies_continue_later)
        self.movies_search_icon_3.setObjectName(u"movies_search_icon_3")
        self.movies_search_icon_3.setIcon(icon2)
        self.movies_search_icon_3.setIconSize(QSize(32, 32))
        self.movies_search_icon_3.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.movies_search_icon_3)

        self.movies_search_3 = QLineEdit(self.movies_continue_later)
        self.movies_search_3.setObjectName(u"movies_search_3")
        self.movies_search_3.setMaximumSize(QSize(200, 30))
        self.movies_search_3.setStyleSheet(u"")
        self.movies_search_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.movies_search_3)

        self.line_7 = QFrame(self.movies_continue_later)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_9.addWidget(self.line_7)

        self.movies_random_button_3 = QPushButton(self.movies_continue_later)
        self.movies_random_button_3.setObjectName(u"movies_random_button_3")
        self.movies_random_button_3.setAutoFillBackground(False)
        self.movies_random_button_3.setIcon(icon3)
        self.movies_random_button_3.setIconSize(QSize(32, 32))
        self.movies_random_button_3.setFlat(True)

        self.horizontalLayout_9.addWidget(self.movies_random_button_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.movies_view_3 = QPushButton(self.movies_continue_later)
        self.movies_view_3.setObjectName(u"movies_view_3")
        self.movies_view_3.setIcon(icon4)
        self.movies_view_3.setIconSize(QSize(32, 32))
        self.movies_view_3.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.movies_view_3)

        self.line_8 = QFrame(self.movies_continue_later)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_9.addWidget(self.line_8)

        self.movies_sort_by_3 = QComboBox(self.movies_continue_later)
        self.movies_sort_by_3.setObjectName(u"movies_sort_by_3")
        self.movies_sort_by_3.setIconSize(QSize(32, 32))
        self.movies_sort_by_3.setFrame(False)
        self.movies_sort_by_3.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_9.addWidget(self.movies_sort_by_3)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)

        self.movies_list_3 = QListWidget(self.movies_continue_later)
        self.movies_list_3.setObjectName(u"movies_list_3")

        self.verticalLayout_11.addWidget(self.movies_list_3)


        self.gridLayout_9.addLayout(self.verticalLayout_11, 0, 0, 1, 1)

        self.movies_tap_widget.addTab(self.movies_continue_later, "")
        self.movies_dont_want_to_watch = QWidget()
        self.movies_dont_want_to_watch.setObjectName(u"movies_dont_want_to_watch")
        self.gridLayout_10 = QGridLayout(self.movies_dont_want_to_watch)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, -1, 5, -1)
        self.movies_search_icon_4 = QPushButton(self.movies_dont_want_to_watch)
        self.movies_search_icon_4.setObjectName(u"movies_search_icon_4")
        self.movies_search_icon_4.setIcon(icon2)
        self.movies_search_icon_4.setIconSize(QSize(32, 32))
        self.movies_search_icon_4.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.movies_search_icon_4)

        self.movies_search_4 = QLineEdit(self.movies_dont_want_to_watch)
        self.movies_search_4.setObjectName(u"movies_search_4")
        self.movies_search_4.setMaximumSize(QSize(200, 30))
        self.movies_search_4.setStyleSheet(u"")
        self.movies_search_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.movies_search_4)

        self.line_9 = QFrame(self.movies_dont_want_to_watch)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_10.addWidget(self.line_9)

        self.movies_random_button_4 = QPushButton(self.movies_dont_want_to_watch)
        self.movies_random_button_4.setObjectName(u"movies_random_button_4")
        self.movies_random_button_4.setAutoFillBackground(False)
        self.movies_random_button_4.setIcon(icon3)
        self.movies_random_button_4.setIconSize(QSize(32, 32))
        self.movies_random_button_4.setFlat(True)

        self.horizontalLayout_10.addWidget(self.movies_random_button_4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.movies_view_4 = QPushButton(self.movies_dont_want_to_watch)
        self.movies_view_4.setObjectName(u"movies_view_4")
        self.movies_view_4.setIcon(icon4)
        self.movies_view_4.setIconSize(QSize(32, 32))
        self.movies_view_4.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.movies_view_4)

        self.line_10 = QFrame(self.movies_dont_want_to_watch)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.VLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_10.addWidget(self.line_10)

        self.movies_sort_by_4 = QComboBox(self.movies_dont_want_to_watch)
        self.movies_sort_by_4.setObjectName(u"movies_sort_by_4")
        self.movies_sort_by_4.setIconSize(QSize(32, 32))
        self.movies_sort_by_4.setFrame(False)
        self.movies_sort_by_4.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_10.addWidget(self.movies_sort_by_4)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)

        self.movies_list_4 = QListWidget(self.movies_dont_want_to_watch)
        self.movies_list_4.setObjectName(u"movies_list_4")

        self.verticalLayout_12.addWidget(self.movies_list_4)


        self.gridLayout_10.addLayout(self.verticalLayout_12, 0, 0, 1, 1)

        self.movies_tap_widget.addTab(self.movies_dont_want_to_watch, "")
        self.movies_ended = QWidget()
        self.movies_ended.setObjectName(u"movies_ended")
        self.gridLayout_11 = QGridLayout(self.movies_ended)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(5, -1, 5, -1)
        self.movies_search_icon_5 = QPushButton(self.movies_ended)
        self.movies_search_icon_5.setObjectName(u"movies_search_icon_5")
        self.movies_search_icon_5.setIcon(icon2)
        self.movies_search_icon_5.setIconSize(QSize(32, 32))
        self.movies_search_icon_5.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.movies_search_icon_5)

        self.movies_search_5 = QLineEdit(self.movies_ended)
        self.movies_search_5.setObjectName(u"movies_search_5")
        self.movies_search_5.setEnabled(True)
        self.movies_search_5.setMaximumSize(QSize(200, 30))
        self.movies_search_5.setStyleSheet(u"")
        self.movies_search_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.movies_search_5)

        self.line_11 = QFrame(self.movies_ended)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.line_11)

        self.movies_random_button_5 = QPushButton(self.movies_ended)
        self.movies_random_button_5.setObjectName(u"movies_random_button_5")
        self.movies_random_button_5.setAutoFillBackground(False)
        self.movies_random_button_5.setIcon(icon3)
        self.movies_random_button_5.setIconSize(QSize(32, 32))
        self.movies_random_button_5.setFlat(True)

        self.horizontalLayout_11.addWidget(self.movies_random_button_5)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)

        self.movies_view_5 = QPushButton(self.movies_ended)
        self.movies_view_5.setObjectName(u"movies_view_5")
        self.movies_view_5.setIcon(icon4)
        self.movies_view_5.setIconSize(QSize(32, 32))
        self.movies_view_5.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.movies_view_5)

        self.line_12 = QFrame(self.movies_ended)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.VLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.line_12)

        self.movies_sort_by_5 = QComboBox(self.movies_ended)
        self.movies_sort_by_5.setObjectName(u"movies_sort_by_5")
        self.movies_sort_by_5.setAutoFillBackground(False)
        self.movies_sort_by_5.setStyleSheet(u"")
        self.movies_sort_by_5.setIconSize(QSize(32, 32))
        self.movies_sort_by_5.setFrame(False)
        self.movies_sort_by_5.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_11.addWidget(self.movies_sort_by_5)


        self.verticalLayout_13.addLayout(self.horizontalLayout_11)

        self.movies_list_5 = QListWidget(self.movies_ended)
        self.movies_list_5.setObjectName(u"movies_list_5")

        self.verticalLayout_13.addWidget(self.movies_list_5)


        self.gridLayout_11.addLayout(self.verticalLayout_13, 0, 0, 1, 1)

        self.movies_tap_widget.addTab(self.movies_ended, "")

        self.verticalLayout_3.addWidget(self.movies_tap_widget)


        self.gridLayout_7.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.stacked_body_Widget.addWidget(self.movies_section)
        self.series_section = QWidget()
        self.series_section.setObjectName(u"series_section")
        self.gridLayout_6 = QGridLayout(self.series_section)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.series_label = QLabel(self.series_section)
        self.series_label.setObjectName(u"series_label")
        self.series_label.setFont(font)

        self.horizontalLayout_4.addWidget(self.series_label)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_9)

        self.series_add_button = QPushButton(self.series_section)
        self.series_add_button.setObjectName(u"series_add_button")
        self.series_add_button.setMinimumSize(QSize(100, 0))
        self.series_add_button.setMaximumSize(QSize(50, 16777215))
        self.series_add_button.setAutoFillBackground(False)
        self.series_add_button.setStyleSheet(u"")
        self.series_add_button.setIcon(icon1)
        self.series_add_button.setIconSize(QSize(60, 60))
        self.series_add_button.setFlat(True)

        self.horizontalLayout_4.addWidget(self.series_add_button)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.series_tap_widget = QTabWidget(self.series_section)
        self.series_tap_widget.setObjectName(u"series_tap_widget")
        sizePolicy2.setHeightForWidth(self.series_tap_widget.sizePolicy().hasHeightForWidth())
        self.series_tap_widget.setSizePolicy(sizePolicy2)
        self.series_tap_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.series_tap_widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.series_tap_widget.setAutoFillBackground(False)
        self.series_tap_widget.setStyleSheet(u"")
        self.series_tap_widget.setTabPosition(QTabWidget.TabPosition.North)
        self.series_tap_widget.setTabShape(QTabWidget.TabShape.Rounded)
        self.series_tap_widget.setElideMode(Qt.TextElideMode.ElideNone)
        self.series_tap_widget.setDocumentMode(True)
        self.series_tap_widget.setTabsClosable(False)
        self.series_tap_widget.setMovable(False)
        self.series_tap_widget.setTabBarAutoHide(False)
        self.movies_watching_2 = QWidget()
        self.movies_watching_2.setObjectName(u"movies_watching_2")
        self.gridLayout_15 = QGridLayout(self.movies_watching_2)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 10, -1, -1)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 0, 5, -1)
        self.series_search_1 = QLineEdit(self.movies_watching_2)
        self.series_search_1.setObjectName(u"series_search_1")
        self.series_search_1.setMaximumSize(QSize(200, 30))
        self.series_search_1.setStyleSheet(u"QLineEdit {\n"
"    background-color: #2d2d2d;\n"
"    border: 2px solid #404040;\n"
"    border-radius: 8px;\n"
"    font-size: 14px;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #888888;\n"
"    font-size: 14px;\n"
"    font-style: normal;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #2196F3;\n"
"}")
        self.series_search_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.series_search_1)

        self.line_13 = QFrame(self.movies_watching_2)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.VLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_6.addWidget(self.line_13)

        self.series_random_button_1 = QPushButton(self.movies_watching_2)
        self.series_random_button_1.setObjectName(u"series_random_button_1")
        self.series_random_button_1.setAutoFillBackground(False)
        self.series_random_button_1.setStyleSheet(u"/* Navigation Buttons */\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    text-align: left;\n"
"    border: none;\n"
"    padding: 6px 12px;\n"
"    font-size: 14px;\n"
"    font-weight: normal;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(79, 79, 79);\n"
"}")
        self.series_random_button_1.setIcon(icon3)
        self.series_random_button_1.setIconSize(QSize(50, 30))
        self.series_random_button_1.setFlat(True)

        self.horizontalLayout_6.addWidget(self.series_random_button_1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)

        self.line_14 = QFrame(self.movies_watching_2)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setStyleSheet(u"/* Separator Line */\n"
"Line {\n"
"    background-color: rgb(70, 70, 70);\n"
"}\n"
"")
        self.line_14.setFrameShape(QFrame.Shape.VLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_6.addWidget(self.line_14)

        self.series_sort_box_1 = QComboBox(self.movies_watching_2)
        self.series_sort_box_1.setObjectName(u"series_sort_box_1")
        self.series_sort_box_1.setStyleSheet(u"")
        self.series_sort_box_1.setEditable(False)
        self.series_sort_box_1.setDuplicatesEnabled(False)
        self.series_sort_box_1.setFrame(False)
        self.series_sort_box_1.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_6.addWidget(self.series_sort_box_1)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.series_list_1 = QListWidget(self.movies_watching_2)
        self.series_list_1.setObjectName(u"series_list_1")

        self.verticalLayout_9.addWidget(self.series_list_1)


        self.gridLayout_15.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.series_tap_widget.addTab(self.movies_watching_2, "")
        self.movies_want_to_watch_2 = QWidget()
        self.movies_want_to_watch_2.setObjectName(u"movies_want_to_watch_2")
        self.gridLayout_16 = QGridLayout(self.movies_want_to_watch_2)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 10, -1, -1)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(5, -1, 5, -1)
        self.series_search_2 = QLineEdit(self.movies_want_to_watch_2)
        self.series_search_2.setObjectName(u"series_search_2")
        self.series_search_2.setMaximumSize(QSize(200, 30))
        self.series_search_2.setStyleSheet(u"")
        self.series_search_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.series_search_2)

        self.line_15 = QFrame(self.movies_want_to_watch_2)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.Shape.VLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_12.addWidget(self.line_15)

        self.series_random_button_2 = QPushButton(self.movies_want_to_watch_2)
        self.series_random_button_2.setObjectName(u"series_random_button_2")
        self.series_random_button_2.setAutoFillBackground(False)
        self.series_random_button_2.setIcon(icon3)
        self.series_random_button_2.setIconSize(QSize(50, 30))
        self.series_random_button_2.setFlat(True)

        self.horizontalLayout_12.addWidget(self.series_random_button_2)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_11)

        self.line_16 = QFrame(self.movies_want_to_watch_2)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.Shape.VLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_12.addWidget(self.line_16)

        self.series_sort_box_2 = QComboBox(self.movies_want_to_watch_2)
        self.series_sort_box_2.setObjectName(u"series_sort_box_2")
        self.series_sort_box_2.setFrame(False)
        self.series_sort_box_2.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_12.addWidget(self.series_sort_box_2)


        self.verticalLayout_14.addLayout(self.horizontalLayout_12)

        self.series_list_2 = QListWidget(self.movies_want_to_watch_2)
        self.series_list_2.setObjectName(u"series_list_2")

        self.verticalLayout_14.addWidget(self.series_list_2)


        self.gridLayout_16.addLayout(self.verticalLayout_14, 0, 0, 1, 1)

        self.series_tap_widget.addTab(self.movies_want_to_watch_2, "")
        self.movies_continue_later_2 = QWidget()
        self.movies_continue_later_2.setObjectName(u"movies_continue_later_2")
        self.gridLayout_17 = QGridLayout(self.movies_continue_later_2)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 9, 0, 0)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(5, -1, 5, -1)
        self.series_search_3 = QLineEdit(self.movies_continue_later_2)
        self.series_search_3.setObjectName(u"series_search_3")
        self.series_search_3.setMaximumSize(QSize(200, 30))
        self.series_search_3.setStyleSheet(u"")
        self.series_search_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.series_search_3)

        self.line_17 = QFrame(self.movies_continue_later_2)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.Shape.VLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_13.addWidget(self.line_17)

        self.series_random_button_3 = QPushButton(self.movies_continue_later_2)
        self.series_random_button_3.setObjectName(u"series_random_button_3")
        self.series_random_button_3.setAutoFillBackground(False)
        self.series_random_button_3.setIcon(icon3)
        self.series_random_button_3.setIconSize(QSize(50, 30))
        self.series_random_button_3.setFlat(True)

        self.horizontalLayout_13.addWidget(self.series_random_button_3)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_12)

        self.line_18 = QFrame(self.movies_continue_later_2)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.Shape.VLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_13.addWidget(self.line_18)

        self.series_sort_box_3 = QComboBox(self.movies_continue_later_2)
        self.series_sort_box_3.setObjectName(u"series_sort_box_3")
        self.series_sort_box_3.setFrame(False)
        self.series_sort_box_3.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_13.addWidget(self.series_sort_box_3)


        self.verticalLayout_15.addLayout(self.horizontalLayout_13)

        self.series_list_3 = QListWidget(self.movies_continue_later_2)
        self.series_list_3.setObjectName(u"series_list_3")

        self.verticalLayout_15.addWidget(self.series_list_3)


        self.gridLayout_17.addLayout(self.verticalLayout_15, 0, 0, 1, 1)

        self.series_tap_widget.addTab(self.movies_continue_later_2, "")
        self.movies_dont_want_to_watch_2 = QWidget()
        self.movies_dont_want_to_watch_2.setObjectName(u"movies_dont_want_to_watch_2")
        self.gridLayout_18 = QGridLayout(self.movies_dont_want_to_watch_2)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(5, -1, 5, -1)
        self.series_search_4 = QLineEdit(self.movies_dont_want_to_watch_2)
        self.series_search_4.setObjectName(u"series_search_4")
        self.series_search_4.setMaximumSize(QSize(200, 30))
        self.series_search_4.setStyleSheet(u"")
        self.series_search_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_14.addWidget(self.series_search_4)

        self.line_19 = QFrame(self.movies_dont_want_to_watch_2)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.Shape.VLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_14.addWidget(self.line_19)

        self.series_random_button_4 = QPushButton(self.movies_dont_want_to_watch_2)
        self.series_random_button_4.setObjectName(u"series_random_button_4")
        self.series_random_button_4.setAutoFillBackground(False)
        self.series_random_button_4.setIcon(icon3)
        self.series_random_button_4.setIconSize(QSize(50, 30))
        self.series_random_button_4.setFlat(True)

        self.horizontalLayout_14.addWidget(self.series_random_button_4)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_13)

        self.line_20 = QFrame(self.movies_dont_want_to_watch_2)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.Shape.VLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_14.addWidget(self.line_20)

        self.series_sort_box_4 = QComboBox(self.movies_dont_want_to_watch_2)
        self.series_sort_box_4.setObjectName(u"series_sort_box_4")
        self.series_sort_box_4.setFrame(False)
        self.series_sort_box_4.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_14.addWidget(self.series_sort_box_4)


        self.verticalLayout_16.addLayout(self.horizontalLayout_14)

        self.series_list_4 = QListWidget(self.movies_dont_want_to_watch_2)
        self.series_list_4.setObjectName(u"series_list_4")

        self.verticalLayout_16.addWidget(self.series_list_4)


        self.gridLayout_18.addLayout(self.verticalLayout_16, 0, 0, 1, 1)

        self.series_tap_widget.addTab(self.movies_dont_want_to_watch_2, "")
        self.movies_ended_2 = QWidget()
        self.movies_ended_2.setObjectName(u"movies_ended_2")
        self.gridLayout_19 = QGridLayout(self.movies_ended_2)
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(5, -1, 5, -1)
        self.series_search_5 = QLineEdit(self.movies_ended_2)
        self.series_search_5.setObjectName(u"series_search_5")
        self.series_search_5.setMaximumSize(QSize(200, 30))
        self.series_search_5.setStyleSheet(u"")
        self.series_search_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_15.addWidget(self.series_search_5)

        self.line_21 = QFrame(self.movies_ended_2)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.Shape.VLine)
        self.line_21.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_15.addWidget(self.line_21)

        self.series_random_button_5 = QPushButton(self.movies_ended_2)
        self.series_random_button_5.setObjectName(u"series_random_button_5")
        self.series_random_button_5.setAutoFillBackground(False)
        self.series_random_button_5.setIcon(icon3)
        self.series_random_button_5.setIconSize(QSize(50, 30))
        self.series_random_button_5.setFlat(True)

        self.horizontalLayout_15.addWidget(self.series_random_button_5)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_14)

        self.line_22 = QFrame(self.movies_ended_2)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.Shape.VLine)
        self.line_22.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_15.addWidget(self.line_22)

        self.series_sort_box_5 = QComboBox(self.movies_ended_2)
        self.series_sort_box_5.setObjectName(u"series_sort_box_5")
        self.series_sort_box_5.setFrame(False)
        self.series_sort_box_5.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_15.addWidget(self.series_sort_box_5)


        self.verticalLayout_17.addLayout(self.horizontalLayout_15)

        self.series_list_5 = QListWidget(self.movies_ended_2)
        self.series_list_5.setObjectName(u"series_list_5")

        self.verticalLayout_17.addWidget(self.series_list_5)


        self.gridLayout_19.addLayout(self.verticalLayout_17, 0, 0, 1, 1)

        self.series_tap_widget.addTab(self.movies_ended_2, "")

        self.verticalLayout_5.addWidget(self.series_tap_widget)


        self.gridLayout_6.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.stacked_body_Widget.addWidget(self.series_section)
        self.games_section = QWidget()
        self.games_section.setObjectName(u"games_section")
        self.gridLayout_26 = QGridLayout(self.games_section)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.games_label = QLabel(self.games_section)
        self.games_label.setObjectName(u"games_label")
        self.games_label.setFont(font)

        self.horizontalLayout_18.addWidget(self.games_label)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_17)

        self.games_add_botton = QPushButton(self.games_section)
        self.games_add_botton.setObjectName(u"games_add_botton")
        self.games_add_botton.setMinimumSize(QSize(100, 0))
        self.games_add_botton.setMaximumSize(QSize(50, 16777215))
        self.games_add_botton.setAutoFillBackground(False)
        self.games_add_botton.setStyleSheet(u"")
        self.games_add_botton.setIcon(icon1)
        self.games_add_botton.setIconSize(QSize(60, 60))
        self.games_add_botton.setFlat(True)

        self.horizontalLayout_18.addWidget(self.games_add_botton)


        self.verticalLayout_6.addLayout(self.horizontalLayout_18)

        self.games_tap_widget = QTabWidget(self.games_section)
        self.games_tap_widget.setObjectName(u"games_tap_widget")
        sizePolicy2.setHeightForWidth(self.games_tap_widget.sizePolicy().hasHeightForWidth())
        self.games_tap_widget.setSizePolicy(sizePolicy2)
        self.games_tap_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.games_tap_widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.games_tap_widget.setAutoFillBackground(False)
        self.games_tap_widget.setStyleSheet(u"")
        self.games_tap_widget.setTabPosition(QTabWidget.TabPosition.North)
        self.games_tap_widget.setTabShape(QTabWidget.TabShape.Rounded)
        self.games_tap_widget.setElideMode(Qt.TextElideMode.ElideNone)
        self.games_tap_widget.setDocumentMode(True)
        self.games_tap_widget.setTabsClosable(False)
        self.games_tap_widget.setMovable(False)
        self.games_tap_widget.setTabBarAutoHide(False)
        self.movies_watching_3 = QWidget()
        self.movies_watching_3.setObjectName(u"movies_watching_3")
        self.gridLayout_21 = QGridLayout(self.movies_watching_3)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(5)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(5, -1, 5, -1)
        self.games_search_1 = QLineEdit(self.movies_watching_3)
        self.games_search_1.setObjectName(u"games_search_1")
        self.games_search_1.setMaximumSize(QSize(200, 30))
        self.games_search_1.setStyleSheet(u"")
        self.games_search_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_19.addWidget(self.games_search_1)

        self.line_25 = QFrame(self.movies_watching_3)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.Shape.VLine)
        self.line_25.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_19.addWidget(self.line_25)

        self.games_random_button_1 = QPushButton(self.movies_watching_3)
        self.games_random_button_1.setObjectName(u"games_random_button_1")
        self.games_random_button_1.setAutoFillBackground(False)
        self.games_random_button_1.setIcon(icon3)
        self.games_random_button_1.setIconSize(QSize(50, 30))
        self.games_random_button_1.setFlat(True)

        self.horizontalLayout_19.addWidget(self.games_random_button_1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_18)

        self.line_26 = QFrame(self.movies_watching_3)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShape(QFrame.Shape.VLine)
        self.line_26.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_19.addWidget(self.line_26)

        self.games_sort_box_1 = QComboBox(self.movies_watching_3)
        self.games_sort_box_1.setObjectName(u"games_sort_box_1")
        self.games_sort_box_1.setFrame(False)
        self.games_sort_box_1.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_19.addWidget(self.games_sort_box_1)


        self.verticalLayout_20.addLayout(self.horizontalLayout_19)

        self.games_list_1 = QListWidget(self.movies_watching_3)
        self.games_list_1.setObjectName(u"games_list_1")

        self.verticalLayout_20.addWidget(self.games_list_1)


        self.gridLayout_21.addLayout(self.verticalLayout_20, 0, 0, 1, 1)

        self.games_tap_widget.addTab(self.movies_watching_3, "")
        self.movies_want_to_watch_3 = QWidget()
        self.movies_want_to_watch_3.setObjectName(u"movies_want_to_watch_3")
        self.gridLayout_22 = QGridLayout(self.movies_want_to_watch_3)
        self.gridLayout_22.setSpacing(0)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.gridLayout_22.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(5)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(5, -1, 5, -1)
        self.games_search_2 = QLineEdit(self.movies_want_to_watch_3)
        self.games_search_2.setObjectName(u"games_search_2")
        self.games_search_2.setMaximumSize(QSize(200, 30))
        self.games_search_2.setStyleSheet(u"")
        self.games_search_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_20.addWidget(self.games_search_2)

        self.line_27 = QFrame(self.movies_want_to_watch_3)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShape(QFrame.Shape.VLine)
        self.line_27.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_20.addWidget(self.line_27)

        self.games_random_button_2 = QPushButton(self.movies_want_to_watch_3)
        self.games_random_button_2.setObjectName(u"games_random_button_2")
        self.games_random_button_2.setAutoFillBackground(False)
        self.games_random_button_2.setIcon(icon3)
        self.games_random_button_2.setIconSize(QSize(50, 30))
        self.games_random_button_2.setFlat(True)

        self.horizontalLayout_20.addWidget(self.games_random_button_2)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_19)

        self.line_28 = QFrame(self.movies_want_to_watch_3)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShape(QFrame.Shape.VLine)
        self.line_28.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_20.addWidget(self.line_28)

        self.games_sort_box_2 = QComboBox(self.movies_want_to_watch_3)
        self.games_sort_box_2.setObjectName(u"games_sort_box_2")
        self.games_sort_box_2.setFrame(False)
        self.games_sort_box_2.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_20.addWidget(self.games_sort_box_2)


        self.verticalLayout_21.addLayout(self.horizontalLayout_20)

        self.games_list_2 = QListWidget(self.movies_want_to_watch_3)
        self.games_list_2.setObjectName(u"games_list_2")

        self.verticalLayout_21.addWidget(self.games_list_2)


        self.gridLayout_22.addLayout(self.verticalLayout_21, 0, 0, 1, 1)

        self.games_tap_widget.addTab(self.movies_want_to_watch_3, "")
        self.movies_continue_later_3 = QWidget()
        self.movies_continue_later_3.setObjectName(u"movies_continue_later_3")
        self.gridLayout_23 = QGridLayout(self.movies_continue_later_3)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 9, 0, 0)
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(5)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(5, -1, 5, -1)
        self.games_search_3 = QLineEdit(self.movies_continue_later_3)
        self.games_search_3.setObjectName(u"games_search_3")
        self.games_search_3.setMaximumSize(QSize(200, 30))
        self.games_search_3.setStyleSheet(u"")
        self.games_search_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_21.addWidget(self.games_search_3)

        self.line_29 = QFrame(self.movies_continue_later_3)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShape(QFrame.Shape.VLine)
        self.line_29.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_21.addWidget(self.line_29)

        self.games_random_button_3 = QPushButton(self.movies_continue_later_3)
        self.games_random_button_3.setObjectName(u"games_random_button_3")
        self.games_random_button_3.setAutoFillBackground(False)
        self.games_random_button_3.setIcon(icon3)
        self.games_random_button_3.setIconSize(QSize(50, 30))
        self.games_random_button_3.setFlat(True)

        self.horizontalLayout_21.addWidget(self.games_random_button_3)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_20)

        self.line_30 = QFrame(self.movies_continue_later_3)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShape(QFrame.Shape.VLine)
        self.line_30.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_21.addWidget(self.line_30)

        self.games_sort_box_3 = QComboBox(self.movies_continue_later_3)
        self.games_sort_box_3.setObjectName(u"games_sort_box_3")
        self.games_sort_box_3.setFrame(False)
        self.games_sort_box_3.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_21.addWidget(self.games_sort_box_3)


        self.verticalLayout_22.addLayout(self.horizontalLayout_21)

        self.games_list_3 = QListWidget(self.movies_continue_later_3)
        self.games_list_3.setObjectName(u"games_list_3")

        self.verticalLayout_22.addWidget(self.games_list_3)


        self.gridLayout_23.addLayout(self.verticalLayout_22, 0, 0, 1, 1)

        self.games_tap_widget.addTab(self.movies_continue_later_3, "")
        self.movies_dont_want_to_watch_3 = QWidget()
        self.movies_dont_want_to_watch_3.setObjectName(u"movies_dont_want_to_watch_3")
        self.gridLayout_24 = QGridLayout(self.movies_dont_want_to_watch_3)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(5, -1, 5, -1)
        self.games_search_4 = QLineEdit(self.movies_dont_want_to_watch_3)
        self.games_search_4.setObjectName(u"games_search_4")
        self.games_search_4.setMaximumSize(QSize(200, 30))
        self.games_search_4.setStyleSheet(u"")
        self.games_search_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_22.addWidget(self.games_search_4)

        self.line_31 = QFrame(self.movies_dont_want_to_watch_3)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setFrameShape(QFrame.Shape.VLine)
        self.line_31.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_22.addWidget(self.line_31)

        self.games_random_button_4 = QPushButton(self.movies_dont_want_to_watch_3)
        self.games_random_button_4.setObjectName(u"games_random_button_4")
        self.games_random_button_4.setAutoFillBackground(False)
        self.games_random_button_4.setIcon(icon3)
        self.games_random_button_4.setIconSize(QSize(50, 30))
        self.games_random_button_4.setFlat(True)

        self.horizontalLayout_22.addWidget(self.games_random_button_4)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_21)

        self.line_32 = QFrame(self.movies_dont_want_to_watch_3)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setFrameShape(QFrame.Shape.VLine)
        self.line_32.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_22.addWidget(self.line_32)

        self.games_sort_box_4 = QComboBox(self.movies_dont_want_to_watch_3)
        self.games_sort_box_4.setObjectName(u"games_sort_box_4")
        self.games_sort_box_4.setFrame(False)
        self.games_sort_box_4.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_22.addWidget(self.games_sort_box_4)


        self.verticalLayout_23.addLayout(self.horizontalLayout_22)

        self.games_list_4 = QListWidget(self.movies_dont_want_to_watch_3)
        self.games_list_4.setObjectName(u"games_list_4")

        self.verticalLayout_23.addWidget(self.games_list_4)


        self.gridLayout_24.addLayout(self.verticalLayout_23, 0, 0, 1, 1)

        self.games_tap_widget.addTab(self.movies_dont_want_to_watch_3, "")
        self.movies_ended_3 = QWidget()
        self.movies_ended_3.setObjectName(u"movies_ended_3")
        self.gridLayout_25 = QGridLayout(self.movies_ended_3)
        self.gridLayout_25.setSpacing(0)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(5)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(5, -1, 5, -1)
        self.games_search_5 = QLineEdit(self.movies_ended_3)
        self.games_search_5.setObjectName(u"games_search_5")
        self.games_search_5.setMaximumSize(QSize(200, 30))
        self.games_search_5.setStyleSheet(u"")
        self.games_search_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_23.addWidget(self.games_search_5)

        self.line_33 = QFrame(self.movies_ended_3)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setFrameShape(QFrame.Shape.VLine)
        self.line_33.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_23.addWidget(self.line_33)

        self.games_random_button_5 = QPushButton(self.movies_ended_3)
        self.games_random_button_5.setObjectName(u"games_random_button_5")
        self.games_random_button_5.setAutoFillBackground(False)
        self.games_random_button_5.setIcon(icon3)
        self.games_random_button_5.setIconSize(QSize(50, 30))
        self.games_random_button_5.setFlat(True)

        self.horizontalLayout_23.addWidget(self.games_random_button_5)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_22)

        self.line_34 = QFrame(self.movies_ended_3)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setFrameShape(QFrame.Shape.VLine)
        self.line_34.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_23.addWidget(self.line_34)

        self.games_sort_box_5 = QComboBox(self.movies_ended_3)
        self.games_sort_box_5.setObjectName(u"games_sort_box_5")
        self.games_sort_box_5.setFrame(False)
        self.games_sort_box_5.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_23.addWidget(self.games_sort_box_5)


        self.verticalLayout_24.addLayout(self.horizontalLayout_23)

        self.games_list_5 = QListWidget(self.movies_ended_3)
        self.games_list_5.setObjectName(u"games_list_5")

        self.verticalLayout_24.addWidget(self.games_list_5)


        self.gridLayout_25.addLayout(self.verticalLayout_24, 0, 0, 1, 1)

        self.games_tap_widget.addTab(self.movies_ended_3, "")

        self.verticalLayout_6.addWidget(self.games_tap_widget)


        self.gridLayout_26.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.stacked_body_Widget.addWidget(self.games_section)
        self.books_section = QWidget()
        self.books_section.setObjectName(u"books_section")
        self.gridLayout_5 = QGridLayout(self.books_section)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.books_label = QLabel(self.books_section)
        self.books_label.setObjectName(u"books_label")
        self.books_label.setFont(font)

        self.horizontalLayout_3.addWidget(self.books_label)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_23)

        self.books_add_botton = QPushButton(self.books_section)
        self.books_add_botton.setObjectName(u"books_add_botton")
        self.books_add_botton.setMinimumSize(QSize(100, 0))
        self.books_add_botton.setMaximumSize(QSize(50, 16777215))
        self.books_add_botton.setAutoFillBackground(False)
        self.books_add_botton.setStyleSheet(u"")
        self.books_add_botton.setIcon(icon1)
        self.books_add_botton.setIconSize(QSize(60, 60))
        self.books_add_botton.setFlat(True)

        self.horizontalLayout_3.addWidget(self.books_add_botton)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.books_tap_widget = QTabWidget(self.books_section)
        self.books_tap_widget.setObjectName(u"books_tap_widget")
        sizePolicy2.setHeightForWidth(self.books_tap_widget.sizePolicy().hasHeightForWidth())
        self.books_tap_widget.setSizePolicy(sizePolicy2)
        self.books_tap_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.books_tap_widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.books_tap_widget.setAutoFillBackground(False)
        self.books_tap_widget.setStyleSheet(u"")
        self.books_tap_widget.setTabPosition(QTabWidget.TabPosition.North)
        self.books_tap_widget.setTabShape(QTabWidget.TabShape.Rounded)
        self.books_tap_widget.setElideMode(Qt.TextElideMode.ElideNone)
        self.books_tap_widget.setDocumentMode(True)
        self.books_tap_widget.setTabsClosable(False)
        self.books_tap_widget.setMovable(False)
        self.books_tap_widget.setTabBarAutoHide(False)
        self.movies_watching_4 = QWidget()
        self.movies_watching_4.setObjectName(u"movies_watching_4")
        self.gridLayout_27 = QGridLayout(self.movies_watching_4)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(5)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(5, -1, 5, -1)
        self.books_search_1 = QLineEdit(self.movies_watching_4)
        self.books_search_1.setObjectName(u"books_search_1")
        self.books_search_1.setMaximumSize(QSize(200, 30))
        self.books_search_1.setStyleSheet(u"")
        self.books_search_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_24.addWidget(self.books_search_1)

        self.line_35 = QFrame(self.movies_watching_4)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setFrameShape(QFrame.Shape.VLine)
        self.line_35.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_24.addWidget(self.line_35)

        self.books_random_button_1 = QPushButton(self.movies_watching_4)
        self.books_random_button_1.setObjectName(u"books_random_button_1")
        self.books_random_button_1.setAutoFillBackground(False)
        self.books_random_button_1.setIcon(icon3)
        self.books_random_button_1.setIconSize(QSize(50, 30))
        self.books_random_button_1.setFlat(True)

        self.horizontalLayout_24.addWidget(self.books_random_button_1)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_24)

        self.line_36 = QFrame(self.movies_watching_4)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setFrameShape(QFrame.Shape.VLine)
        self.line_36.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_24.addWidget(self.line_36)

        self.books_sort_box_1 = QComboBox(self.movies_watching_4)
        self.books_sort_box_1.setObjectName(u"books_sort_box_1")
        self.books_sort_box_1.setFrame(False)
        self.books_sort_box_1.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_24.addWidget(self.books_sort_box_1)


        self.verticalLayout_25.addLayout(self.horizontalLayout_24)

        self.books_list_1 = QListWidget(self.movies_watching_4)
        self.books_list_1.setObjectName(u"books_list_1")

        self.verticalLayout_25.addWidget(self.books_list_1)


        self.gridLayout_27.addLayout(self.verticalLayout_25, 0, 0, 1, 1)

        self.books_tap_widget.addTab(self.movies_watching_4, "")
        self.movies_want_to_watch_4 = QWidget()
        self.movies_want_to_watch_4.setObjectName(u"movies_want_to_watch_4")
        self.gridLayout_28 = QGridLayout(self.movies_want_to_watch_4)
        self.gridLayout_28.setSpacing(0)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(5)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(5, -1, 5, -1)
        self.books_search_2 = QLineEdit(self.movies_want_to_watch_4)
        self.books_search_2.setObjectName(u"books_search_2")
        self.books_search_2.setMaximumSize(QSize(200, 30))
        self.books_search_2.setStyleSheet(u"")
        self.books_search_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_25.addWidget(self.books_search_2)

        self.line_37 = QFrame(self.movies_want_to_watch_4)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setFrameShape(QFrame.Shape.VLine)
        self.line_37.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_25.addWidget(self.line_37)

        self.books_random_button_2 = QPushButton(self.movies_want_to_watch_4)
        self.books_random_button_2.setObjectName(u"books_random_button_2")
        self.books_random_button_2.setAutoFillBackground(False)
        self.books_random_button_2.setIcon(icon3)
        self.books_random_button_2.setIconSize(QSize(50, 30))
        self.books_random_button_2.setFlat(True)

        self.horizontalLayout_25.addWidget(self.books_random_button_2)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_25)

        self.line_38 = QFrame(self.movies_want_to_watch_4)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setFrameShape(QFrame.Shape.VLine)
        self.line_38.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_25.addWidget(self.line_38)

        self.books_sort_box_2 = QComboBox(self.movies_want_to_watch_4)
        self.books_sort_box_2.setObjectName(u"books_sort_box_2")
        self.books_sort_box_2.setFrame(False)
        self.books_sort_box_2.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_25.addWidget(self.books_sort_box_2)


        self.verticalLayout_26.addLayout(self.horizontalLayout_25)

        self.books_list_2 = QListWidget(self.movies_want_to_watch_4)
        self.books_list_2.setObjectName(u"books_list_2")

        self.verticalLayout_26.addWidget(self.books_list_2)


        self.gridLayout_28.addLayout(self.verticalLayout_26, 0, 0, 1, 1)

        self.books_tap_widget.addTab(self.movies_want_to_watch_4, "")
        self.movies_continue_later_4 = QWidget()
        self.movies_continue_later_4.setObjectName(u"movies_continue_later_4")
        self.gridLayout_29 = QGridLayout(self.movies_continue_later_4)
        self.gridLayout_29.setSpacing(0)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 9, 0, 0)
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(5)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(5, -1, 5, -1)
        self.books_search_3 = QLineEdit(self.movies_continue_later_4)
        self.books_search_3.setObjectName(u"books_search_3")
        self.books_search_3.setMaximumSize(QSize(200, 30))
        self.books_search_3.setStyleSheet(u"")
        self.books_search_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_26.addWidget(self.books_search_3)

        self.line_39 = QFrame(self.movies_continue_later_4)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setFrameShape(QFrame.Shape.VLine)
        self.line_39.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_26.addWidget(self.line_39)

        self.books_random_button_3 = QPushButton(self.movies_continue_later_4)
        self.books_random_button_3.setObjectName(u"books_random_button_3")
        self.books_random_button_3.setAutoFillBackground(False)
        self.books_random_button_3.setIcon(icon3)
        self.books_random_button_3.setIconSize(QSize(50, 30))
        self.books_random_button_3.setFlat(True)

        self.horizontalLayout_26.addWidget(self.books_random_button_3)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_26)

        self.line_40 = QFrame(self.movies_continue_later_4)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setFrameShape(QFrame.Shape.VLine)
        self.line_40.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_26.addWidget(self.line_40)

        self.books_sort_box_3 = QComboBox(self.movies_continue_later_4)
        self.books_sort_box_3.setObjectName(u"books_sort_box_3")
        self.books_sort_box_3.setFrame(False)
        self.books_sort_box_3.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_26.addWidget(self.books_sort_box_3)


        self.verticalLayout_27.addLayout(self.horizontalLayout_26)

        self.books_list_3 = QListWidget(self.movies_continue_later_4)
        self.books_list_3.setObjectName(u"books_list_3")

        self.verticalLayout_27.addWidget(self.books_list_3)


        self.gridLayout_29.addLayout(self.verticalLayout_27, 0, 0, 1, 1)

        self.books_tap_widget.addTab(self.movies_continue_later_4, "")
        self.movies_dont_want_to_watch_4 = QWidget()
        self.movies_dont_want_to_watch_4.setObjectName(u"movies_dont_want_to_watch_4")
        self.gridLayout_30 = QGridLayout(self.movies_dont_want_to_watch_4)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setSpacing(5)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(5, -1, 5, -1)
        self.books_search_4 = QLineEdit(self.movies_dont_want_to_watch_4)
        self.books_search_4.setObjectName(u"books_search_4")
        self.books_search_4.setMaximumSize(QSize(200, 30))
        self.books_search_4.setStyleSheet(u"")
        self.books_search_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_27.addWidget(self.books_search_4)

        self.line_41 = QFrame(self.movies_dont_want_to_watch_4)
        self.line_41.setObjectName(u"line_41")
        self.line_41.setFrameShape(QFrame.Shape.VLine)
        self.line_41.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_27.addWidget(self.line_41)

        self.books_random_button_4 = QPushButton(self.movies_dont_want_to_watch_4)
        self.books_random_button_4.setObjectName(u"books_random_button_4")
        self.books_random_button_4.setAutoFillBackground(False)
        self.books_random_button_4.setIcon(icon3)
        self.books_random_button_4.setIconSize(QSize(50, 30))
        self.books_random_button_4.setFlat(True)

        self.horizontalLayout_27.addWidget(self.books_random_button_4)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_27)

        self.line_42 = QFrame(self.movies_dont_want_to_watch_4)
        self.line_42.setObjectName(u"line_42")
        self.line_42.setFrameShape(QFrame.Shape.VLine)
        self.line_42.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_27.addWidget(self.line_42)

        self.books_sort_box_4 = QComboBox(self.movies_dont_want_to_watch_4)
        self.books_sort_box_4.setObjectName(u"books_sort_box_4")
        self.books_sort_box_4.setFrame(False)
        self.books_sort_box_4.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_27.addWidget(self.books_sort_box_4)


        self.verticalLayout_28.addLayout(self.horizontalLayout_27)

        self.books_list_4 = QListWidget(self.movies_dont_want_to_watch_4)
        self.books_list_4.setObjectName(u"books_list_4")

        self.verticalLayout_28.addWidget(self.books_list_4)


        self.gridLayout_30.addLayout(self.verticalLayout_28, 0, 0, 1, 1)

        self.books_tap_widget.addTab(self.movies_dont_want_to_watch_4, "")
        self.movies_ended_4 = QWidget()
        self.movies_ended_4.setObjectName(u"movies_ended_4")
        self.gridLayout_31 = QGridLayout(self.movies_ended_4)
        self.gridLayout_31.setSpacing(0)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setSpacing(5)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(5, -1, 5, -1)
        self.books_search_5 = QLineEdit(self.movies_ended_4)
        self.books_search_5.setObjectName(u"books_search_5")
        self.books_search_5.setMaximumSize(QSize(200, 30))
        self.books_search_5.setStyleSheet(u"")
        self.books_search_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_28.addWidget(self.books_search_5)

        self.line_43 = QFrame(self.movies_ended_4)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setFrameShape(QFrame.Shape.VLine)
        self.line_43.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_28.addWidget(self.line_43)

        self.books_random_button_5 = QPushButton(self.movies_ended_4)
        self.books_random_button_5.setObjectName(u"books_random_button_5")
        self.books_random_button_5.setAutoFillBackground(False)
        self.books_random_button_5.setIcon(icon3)
        self.books_random_button_5.setIconSize(QSize(50, 30))
        self.books_random_button_5.setFlat(True)

        self.horizontalLayout_28.addWidget(self.books_random_button_5)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_28)

        self.line_44 = QFrame(self.movies_ended_4)
        self.line_44.setObjectName(u"line_44")
        self.line_44.setFrameShape(QFrame.Shape.VLine)
        self.line_44.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_28.addWidget(self.line_44)

        self.books_sort_box_5 = QComboBox(self.movies_ended_4)
        self.books_sort_box_5.setObjectName(u"books_sort_box_5")
        self.books_sort_box_5.setFrame(False)
        self.books_sort_box_5.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_28.addWidget(self.books_sort_box_5)


        self.verticalLayout_29.addLayout(self.horizontalLayout_28)

        self.books_list_5 = QListWidget(self.movies_ended_4)
        self.books_list_5.setObjectName(u"books_list_5")

        self.verticalLayout_29.addWidget(self.books_list_5)


        self.gridLayout_31.addLayout(self.verticalLayout_29, 0, 0, 1, 1)

        self.books_tap_widget.addTab(self.movies_ended_4, "")

        self.verticalLayout_7.addWidget(self.books_tap_widget)


        self.gridLayout_5.addLayout(self.verticalLayout_7, 0, 0, 1, 1)

        self.stacked_body_Widget.addWidget(self.books_section)
        self.comics_section = QWidget()
        self.comics_section.setObjectName(u"comics_section")
        self.gridLayout_4 = QGridLayout(self.comics_section)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.comics_label = QLabel(self.comics_section)
        self.comics_label.setObjectName(u"comics_label")
        self.comics_label.setFont(font)

        self.horizontalLayout_34.addWidget(self.comics_label)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_35)

        self.comics_add_botton = QPushButton(self.comics_section)
        self.comics_add_botton.setObjectName(u"comics_add_botton")
        self.comics_add_botton.setMinimumSize(QSize(100, 0))
        self.comics_add_botton.setMaximumSize(QSize(50, 16777215))
        self.comics_add_botton.setAutoFillBackground(False)
        self.comics_add_botton.setStyleSheet(u"")
        self.comics_add_botton.setIcon(icon1)
        self.comics_add_botton.setIconSize(QSize(60, 60))
        self.comics_add_botton.setFlat(True)

        self.horizontalLayout_34.addWidget(self.comics_add_botton)


        self.verticalLayout_36.addLayout(self.horizontalLayout_34)

        self.comics_tap_widget = QTabWidget(self.comics_section)
        self.comics_tap_widget.setObjectName(u"comics_tap_widget")
        sizePolicy2.setHeightForWidth(self.comics_tap_widget.sizePolicy().hasHeightForWidth())
        self.comics_tap_widget.setSizePolicy(sizePolicy2)
        self.comics_tap_widget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.comics_tap_widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.comics_tap_widget.setAutoFillBackground(False)
        self.comics_tap_widget.setStyleSheet(u"")
        self.comics_tap_widget.setTabPosition(QTabWidget.TabPosition.North)
        self.comics_tap_widget.setTabShape(QTabWidget.TabShape.Rounded)
        self.comics_tap_widget.setElideMode(Qt.TextElideMode.ElideNone)
        self.comics_tap_widget.setDocumentMode(True)
        self.comics_tap_widget.setTabsClosable(False)
        self.comics_tap_widget.setMovable(False)
        self.comics_tap_widget.setTabBarAutoHide(False)
        self.movies_watching_6 = QWidget()
        self.movies_watching_6.setObjectName(u"movies_watching_6")
        self.gridLayout_37 = QGridLayout(self.movies_watching_6)
        self.gridLayout_37.setSpacing(0)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setSpacing(5)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(5, -1, 5, -1)
        self.comics_search_1 = QLineEdit(self.movies_watching_6)
        self.comics_search_1.setObjectName(u"comics_search_1")
        self.comics_search_1.setMaximumSize(QSize(200, 30))
        self.comics_search_1.setStyleSheet(u"")
        self.comics_search_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_35.addWidget(self.comics_search_1)

        self.line_55 = QFrame(self.movies_watching_6)
        self.line_55.setObjectName(u"line_55")
        self.line_55.setFrameShape(QFrame.Shape.VLine)
        self.line_55.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_35.addWidget(self.line_55)

        self.comics_random_button_1 = QPushButton(self.movies_watching_6)
        self.comics_random_button_1.setObjectName(u"comics_random_button_1")
        self.comics_random_button_1.setAutoFillBackground(False)
        self.comics_random_button_1.setIcon(icon3)
        self.comics_random_button_1.setIconSize(QSize(50, 30))
        self.comics_random_button_1.setFlat(True)

        self.horizontalLayout_35.addWidget(self.comics_random_button_1)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_36)

        self.line_56 = QFrame(self.movies_watching_6)
        self.line_56.setObjectName(u"line_56")
        self.line_56.setFrameShape(QFrame.Shape.VLine)
        self.line_56.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_35.addWidget(self.line_56)

        self.comics_sort_box_1 = QComboBox(self.movies_watching_6)
        self.comics_sort_box_1.setObjectName(u"comics_sort_box_1")
        self.comics_sort_box_1.setFrame(False)
        self.comics_sort_box_1.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_35.addWidget(self.comics_sort_box_1)


        self.verticalLayout_37.addLayout(self.horizontalLayout_35)

        self.comics_list_1 = QListWidget(self.movies_watching_6)
        self.comics_list_1.setObjectName(u"comics_list_1")

        self.verticalLayout_37.addWidget(self.comics_list_1)


        self.gridLayout_37.addLayout(self.verticalLayout_37, 0, 0, 1, 1)

        self.comics_tap_widget.addTab(self.movies_watching_6, "")
        self.movies_want_to_watch_6 = QWidget()
        self.movies_want_to_watch_6.setObjectName(u"movies_want_to_watch_6")
        self.gridLayout_38 = QGridLayout(self.movies_want_to_watch_6)
        self.gridLayout_38.setSpacing(0)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.gridLayout_38.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setSpacing(5)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(5, -1, 5, -1)
        self.comics_search_2 = QLineEdit(self.movies_want_to_watch_6)
        self.comics_search_2.setObjectName(u"comics_search_2")
        self.comics_search_2.setMaximumSize(QSize(200, 30))
        self.comics_search_2.setStyleSheet(u"")
        self.comics_search_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_36.addWidget(self.comics_search_2)

        self.line_57 = QFrame(self.movies_want_to_watch_6)
        self.line_57.setObjectName(u"line_57")
        self.line_57.setFrameShape(QFrame.Shape.VLine)
        self.line_57.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_36.addWidget(self.line_57)

        self.comics_random_button_2 = QPushButton(self.movies_want_to_watch_6)
        self.comics_random_button_2.setObjectName(u"comics_random_button_2")
        self.comics_random_button_2.setAutoFillBackground(False)
        self.comics_random_button_2.setIcon(icon3)
        self.comics_random_button_2.setIconSize(QSize(50, 30))
        self.comics_random_button_2.setFlat(True)

        self.horizontalLayout_36.addWidget(self.comics_random_button_2)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_37)

        self.line_58 = QFrame(self.movies_want_to_watch_6)
        self.line_58.setObjectName(u"line_58")
        self.line_58.setFrameShape(QFrame.Shape.VLine)
        self.line_58.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_36.addWidget(self.line_58)

        self.comics_sort_box_2 = QComboBox(self.movies_want_to_watch_6)
        self.comics_sort_box_2.setObjectName(u"comics_sort_box_2")
        self.comics_sort_box_2.setFrame(False)
        self.comics_sort_box_2.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_36.addWidget(self.comics_sort_box_2)


        self.verticalLayout_38.addLayout(self.horizontalLayout_36)

        self.comics_list_2 = QListWidget(self.movies_want_to_watch_6)
        self.comics_list_2.setObjectName(u"comics_list_2")

        self.verticalLayout_38.addWidget(self.comics_list_2)


        self.gridLayout_38.addLayout(self.verticalLayout_38, 0, 0, 1, 1)

        self.comics_tap_widget.addTab(self.movies_want_to_watch_6, "")
        self.movies_continue_later_6 = QWidget()
        self.movies_continue_later_6.setObjectName(u"movies_continue_later_6")
        self.gridLayout_39 = QGridLayout(self.movies_continue_later_6)
        self.gridLayout_39.setSpacing(0)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(0, 9, 0, 0)
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setSpacing(5)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(5, -1, 5, -1)
        self.comics_search_3 = QLineEdit(self.movies_continue_later_6)
        self.comics_search_3.setObjectName(u"comics_search_3")
        self.comics_search_3.setMaximumSize(QSize(200, 30))
        self.comics_search_3.setStyleSheet(u"")
        self.comics_search_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_37.addWidget(self.comics_search_3)

        self.line_59 = QFrame(self.movies_continue_later_6)
        self.line_59.setObjectName(u"line_59")
        self.line_59.setFrameShape(QFrame.Shape.VLine)
        self.line_59.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_37.addWidget(self.line_59)

        self.comics_random_button_3 = QPushButton(self.movies_continue_later_6)
        self.comics_random_button_3.setObjectName(u"comics_random_button_3")
        self.comics_random_button_3.setAutoFillBackground(False)
        self.comics_random_button_3.setIcon(icon3)
        self.comics_random_button_3.setIconSize(QSize(50, 30))
        self.comics_random_button_3.setFlat(True)

        self.horizontalLayout_37.addWidget(self.comics_random_button_3)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_38)

        self.line_60 = QFrame(self.movies_continue_later_6)
        self.line_60.setObjectName(u"line_60")
        self.line_60.setFrameShape(QFrame.Shape.VLine)
        self.line_60.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_37.addWidget(self.line_60)

        self.comics_sort_box_3 = QComboBox(self.movies_continue_later_6)
        self.comics_sort_box_3.setObjectName(u"comics_sort_box_3")
        self.comics_sort_box_3.setFrame(False)
        self.comics_sort_box_3.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_37.addWidget(self.comics_sort_box_3)


        self.verticalLayout_39.addLayout(self.horizontalLayout_37)

        self.comics_list_3 = QListWidget(self.movies_continue_later_6)
        self.comics_list_3.setObjectName(u"comics_list_3")

        self.verticalLayout_39.addWidget(self.comics_list_3)


        self.gridLayout_39.addLayout(self.verticalLayout_39, 0, 0, 1, 1)

        self.comics_tap_widget.addTab(self.movies_continue_later_6, "")
        self.movies_dont_want_to_watch_6 = QWidget()
        self.movies_dont_want_to_watch_6.setObjectName(u"movies_dont_want_to_watch_6")
        self.gridLayout_40 = QGridLayout(self.movies_dont_want_to_watch_6)
        self.gridLayout_40.setSpacing(0)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.gridLayout_40.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setSpacing(5)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(5, -1, 5, -1)
        self.comics_search_4 = QLineEdit(self.movies_dont_want_to_watch_6)
        self.comics_search_4.setObjectName(u"comics_search_4")
        self.comics_search_4.setMaximumSize(QSize(200, 30))
        self.comics_search_4.setStyleSheet(u"QLineEdit {\n"
"    color: rgb(0, 0, 0);\n"
"    font-size: 14px;\n"
"    background-color: transparent;\n"
"    padding: 6px;\n"
"    border: none;\n"
"    border-bottom: 1px solid rgba(221, 221, 221, 100); /* \u0642\u0628\u0644 \u0627\u0644\u062a\u0631\u0643\u064a\u0632 */\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgba(73, 133, 224, 0.12); /* \u0632\u064a input-hovered-color */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    outline: none;\n"
"    border-bottom: 2px solid #5891ff; /* \u0628\u0639\u062f \u0627\u0644\u062a\u0631\u0643\u064a\u0632 */\n"
"}\n"
"")
        self.comics_search_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_38.addWidget(self.comics_search_4)

        self.line_61 = QFrame(self.movies_dont_want_to_watch_6)
        self.line_61.setObjectName(u"line_61")
        self.line_61.setFrameShape(QFrame.Shape.VLine)
        self.line_61.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_38.addWidget(self.line_61)

        self.comics_random_button_4 = QPushButton(self.movies_dont_want_to_watch_6)
        self.comics_random_button_4.setObjectName(u"comics_random_button_4")
        self.comics_random_button_4.setAutoFillBackground(False)
        self.comics_random_button_4.setIcon(icon3)
        self.comics_random_button_4.setIconSize(QSize(50, 30))
        self.comics_random_button_4.setFlat(True)

        self.horizontalLayout_38.addWidget(self.comics_random_button_4)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_39)

        self.line_62 = QFrame(self.movies_dont_want_to_watch_6)
        self.line_62.setObjectName(u"line_62")
        self.line_62.setFrameShape(QFrame.Shape.VLine)
        self.line_62.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_38.addWidget(self.line_62)

        self.comics_sort_box_4 = QComboBox(self.movies_dont_want_to_watch_6)
        self.comics_sort_box_4.setObjectName(u"comics_sort_box_4")
        self.comics_sort_box_4.setFrame(False)
        self.comics_sort_box_4.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_38.addWidget(self.comics_sort_box_4)


        self.verticalLayout_40.addLayout(self.horizontalLayout_38)

        self.comics_list_4 = QListWidget(self.movies_dont_want_to_watch_6)
        self.comics_list_4.setObjectName(u"comics_list_4")

        self.verticalLayout_40.addWidget(self.comics_list_4)


        self.gridLayout_40.addLayout(self.verticalLayout_40, 0, 0, 1, 1)

        self.comics_tap_widget.addTab(self.movies_dont_want_to_watch_6, "")
        self.movies_ended_6 = QWidget()
        self.movies_ended_6.setObjectName(u"movies_ended_6")
        self.gridLayout_41 = QGridLayout(self.movies_ended_6)
        self.gridLayout_41.setSpacing(0)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setSpacing(5)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(5, -1, 5, -1)
        self.comics_search_5 = QLineEdit(self.movies_ended_6)
        self.comics_search_5.setObjectName(u"comics_search_5")
        self.comics_search_5.setMaximumSize(QSize(200, 30))
        self.comics_search_5.setStyleSheet(u"")
        self.comics_search_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_39.addWidget(self.comics_search_5)

        self.line_63 = QFrame(self.movies_ended_6)
        self.line_63.setObjectName(u"line_63")
        self.line_63.setFrameShape(QFrame.Shape.VLine)
        self.line_63.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_39.addWidget(self.line_63)

        self.comics_random_button_5 = QPushButton(self.movies_ended_6)
        self.comics_random_button_5.setObjectName(u"comics_random_button_5")
        self.comics_random_button_5.setAutoFillBackground(False)
        self.comics_random_button_5.setIcon(icon3)
        self.comics_random_button_5.setIconSize(QSize(50, 30))
        self.comics_random_button_5.setFlat(True)

        self.horizontalLayout_39.addWidget(self.comics_random_button_5)

        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_40)

        self.line_64 = QFrame(self.movies_ended_6)
        self.line_64.setObjectName(u"line_64")
        self.line_64.setFrameShape(QFrame.Shape.VLine)
        self.line_64.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_39.addWidget(self.line_64)

        self.comics_sort_box_5 = QComboBox(self.movies_ended_6)
        self.comics_sort_box_5.setObjectName(u"comics_sort_box_5")
        self.comics_sort_box_5.setFrame(False)
        self.comics_sort_box_5.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_39.addWidget(self.comics_sort_box_5)


        self.verticalLayout_41.addLayout(self.horizontalLayout_39)

        self.comics_list_5 = QListWidget(self.movies_ended_6)
        self.comics_list_5.setObjectName(u"comics_list_5")

        self.verticalLayout_41.addWidget(self.comics_list_5)


        self.gridLayout_41.addLayout(self.verticalLayout_41, 0, 0, 1, 1)

        self.comics_tap_widget.addTab(self.movies_ended_6, "")

        self.verticalLayout_36.addWidget(self.comics_tap_widget)


        self.gridLayout_4.addLayout(self.verticalLayout_36, 0, 0, 1, 1)

        self.stacked_body_Widget.addWidget(self.comics_section)
        self.setting_section = QWidget()
        self.setting_section.setObjectName(u"setting_section")
        self.setting_section.setStyleSheet(u"")
        self.gridLayout_8 = QGridLayout(self.setting_section)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_4, 3, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_4, 2, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.label_6 = QLabel(self.setting_section)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_8.addWidget(self.label_6, 0, 0, 1, 2)

        self.stacked_body_Widget.addWidget(self.setting_section)

        self.gridLayout_2.addWidget(self.stacked_body_Widget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.main_body_widget, 0, 1, 1, 1)

        self.side_widget = QWidget(main_widget)
        self.side_widget.setObjectName(u"side_widget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.side_widget.sizePolicy().hasHeightForWidth())
        self.side_widget.setSizePolicy(sizePolicy3)
        self.side_widget.setStyleSheet(u"/* Sidebar Container */\n"
"QWidget {\n"
"    background-color:#2b3640;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Navigation Buttons */\n"
"QPushButton {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    text-align: left;\n"
"    border: none;\n"
"    padding:6px 50px 5px 20px;\n"
"    font-size: 14px;\n"
"    font-weight: normal;\n"
"    margin: 0px 0px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(65, 65, 65);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(75, 75, 75);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Section Headers/Labels */\n"
"QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    text-transform: normal;\n"
"    pad"
                        "ding: 8px 0px ;\n"
"    margin-top: 8px;\n"
"}\n"
"\n"
"/* Icon Labels (if you're using QLabel for icons) */\n"
"QLabel#iconLabel {\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    padding: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"/* Separator Line */\n"
"Line {\n"
"    background-color: rgb(70, 70, 70);\n"
"    border: none;\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"	margin: 0px 12px;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.side_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 0, 9)
        self.line_3 = QFrame(self.side_widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.account_layout = QHBoxLayout()
        self.account_layout.setObjectName(u"account_layout")
        self.account_layout.setContentsMargins(0, 0, 0, -1)
        self.name_lable = QLabel(self.side_widget)
        self.name_lable.setObjectName(u"name_lable")

        self.account_layout.addWidget(self.name_lable)

        self.photo_lable = QLabel(self.side_widget)
        self.photo_lable.setObjectName(u"photo_lable")

        self.account_layout.addWidget(self.photo_lable)


        self.verticalLayout.addLayout(self.account_layout)

        self.label_4 = QLabel(self.side_widget)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setBold(True)
        self.label_4.setFont(font2)

        self.verticalLayout.addWidget(self.label_4)

        self.show_movies = QPushButton(self.side_widget)
        self.show_movies.setObjectName(u"show_movies")
        sizePolicy1.setHeightForWidth(self.show_movies.sizePolicy().hasHeightForWidth())
        self.show_movies.setSizePolicy(sizePolicy1)
        self.show_movies.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.show_movies.setAutoFillBackground(False)
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/film 1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/icons/Icons/film.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.show_movies.setIcon(icon5)
        self.show_movies.setIconSize(QSize(23, 23))
        self.show_movies.setCheckable(True)
        self.show_movies.setAutoExclusive(True)
        self.show_movies.setFlat(True)

        self.verticalLayout.addWidget(self.show_movies)

        self.show_series = QPushButton(self.side_widget)
        self.show_series.setObjectName(u"show_series")
        sizePolicy1.setHeightForWidth(self.show_series.sizePolicy().hasHeightForWidth())
        self.show_series.setSizePolicy(sizePolicy1)
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/watching 1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/icons/Icons/watching.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.show_series.setIcon(icon6)
        self.show_series.setIconSize(QSize(25, 25))
        self.show_series.setCheckable(True)
        self.show_series.setAutoExclusive(True)
        self.show_series.setFlat(True)

        self.verticalLayout.addWidget(self.show_series)

        self.show_games = QPushButton(self.side_widget)
        self.show_games.setObjectName(u"show_games")
        sizePolicy1.setHeightForWidth(self.show_games.sizePolicy().hasHeightForWidth())
        self.show_games.setSizePolicy(sizePolicy1)
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/console 1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/icons/Icons/console.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.show_games.setIcon(icon7)
        self.show_games.setIconSize(QSize(25, 25))
        self.show_games.setCheckable(True)
        self.show_games.setAutoExclusive(True)
        self.show_games.setFlat(True)

        self.verticalLayout.addWidget(self.show_games)

        self.show_books = QPushButton(self.side_widget)
        self.show_books.setObjectName(u"show_books")
        sizePolicy1.setHeightForWidth(self.show_books.sizePolicy().hasHeightForWidth())
        self.show_books.setSizePolicy(sizePolicy1)
        icon8 = QIcon()
        icon8.addFile(u":/icons/Icons/book 1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/icons/Icons/book.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.show_books.setIcon(icon8)
        self.show_books.setIconSize(QSize(25, 25))
        self.show_books.setCheckable(True)
        self.show_books.setAutoExclusive(True)
        self.show_books.setFlat(True)

        self.verticalLayout.addWidget(self.show_books)

        self.show_comics = QPushButton(self.side_widget)
        self.show_comics.setObjectName(u"show_comics")
        sizePolicy1.setHeightForWidth(self.show_comics.sizePolicy().hasHeightForWidth())
        self.show_comics.setSizePolicy(sizePolicy1)
        icon9 = QIcon()
        icon9.addFile(u":/icons/Icons/comic 1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(u":/icons/Icons/comic.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.show_comics.setIcon(icon9)
        self.show_comics.setIconSize(QSize(25, 25))
        self.show_comics.setCheckable(True)
        self.show_comics.setAutoExclusive(True)
        self.show_comics.setFlat(True)

        self.verticalLayout.addWidget(self.show_comics)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.line_4 = QFrame(self.side_widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.label_5 = QLabel(self.side_widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.show_home = QPushButton(self.side_widget)
        self.show_home.setObjectName(u"show_home")
        sizePolicy1.setHeightForWidth(self.show_home.sizePolicy().hasHeightForWidth())
        self.show_home.setSizePolicy(sizePolicy1)
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/home 1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(u":/icons/Icons/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.show_home.setIcon(icon10)
        self.show_home.setIconSize(QSize(25, 25))
        self.show_home.setCheckable(True)
        self.show_home.setAutoExclusive(True)
        self.show_home.setFlat(True)

        self.verticalLayout.addWidget(self.show_home)

        self.show_profile = QPushButton(self.side_widget)
        self.show_profile.setObjectName(u"show_profile")
        sizePolicy1.setHeightForWidth(self.show_profile.sizePolicy().hasHeightForWidth())
        self.show_profile.setSizePolicy(sizePolicy1)
        icon11 = QIcon()
        icon11.addFile(u":/icons/Icons/user 1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon11.addFile(u":/icons/Icons/user.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.show_profile.setIcon(icon11)
        self.show_profile.setIconSize(QSize(25, 25))
        self.show_profile.setCheckable(True)
        self.show_profile.setAutoExclusive(True)
        self.show_profile.setFlat(True)

        self.verticalLayout.addWidget(self.show_profile)

        self.show_dashboard = QPushButton(self.side_widget)
        self.show_dashboard.setObjectName(u"show_dashboard")
        sizePolicy1.setHeightForWidth(self.show_dashboard.sizePolicy().hasHeightForWidth())
        self.show_dashboard.setSizePolicy(sizePolicy1)
        icon12 = QIcon()
        icon12.addFile(u":/icons/Icons/dashboard 1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon12.addFile(u":/icons/Icons/dashboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon12.addFile(u":/icons/Icons/dashboard.png", QSize(), QIcon.Mode.Disabled, QIcon.State.Off)
        self.show_dashboard.setIcon(icon12)
        self.show_dashboard.setIconSize(QSize(30, 30))
        self.show_dashboard.setCheckable(True)
        self.show_dashboard.setAutoExclusive(True)
        self.show_dashboard.setFlat(True)

        self.verticalLayout.addWidget(self.show_dashboard)

        self.show_setting = QPushButton(self.side_widget)
        self.show_setting.setObjectName(u"show_setting")
        sizePolicy1.setHeightForWidth(self.show_setting.sizePolicy().hasHeightForWidth())
        self.show_setting.setSizePolicy(sizePolicy1)
        icon13 = QIcon()
        icon13.addFile(u":/icons/Icons/setting 1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon13.addFile(u":/icons/Icons/setting.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.show_setting.setIcon(icon13)
        self.show_setting.setIconSize(QSize(25, 25))
        self.show_setting.setCheckable(True)
        self.show_setting.setAutoExclusive(True)
        self.show_setting.setFlat(True)

        self.verticalLayout.addWidget(self.show_setting)

        self.verticalSpacer = QSpacerItem(143, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.logout = QPushButton(self.side_widget)
        self.logout.setObjectName(u"logout")
        icon14 = QIcon()
        icon14.addFile(u":/icons/Icons/exit 1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon14.addFile(u":/icons/Icons/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.logout.setIcon(icon14)
        self.logout.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.logout)


        self.gridLayout.addWidget(self.side_widget, 0, 0, 1, 1)


        self.retranslateUi(main_widget)
        self.movies_menu.toggled.connect(self.side_widget.setHidden)
        self.movies_search_icon_5.toggled.connect(self.movies_search_5.setVisible)
        self.movies_search_icon_1.toggled.connect(self.movies_search_1.setVisible)
        self.movies_search_icon_2.toggled.connect(self.movies_search_2.setVisible)
        self.movies_search_icon_3.toggled.connect(self.movies_search_3.setVisible)
        self.movies_search_icon_4.toggled.connect(self.movies_search_4.setVisible)

        self.stacked_body_Widget.setCurrentIndex(0)
        self.movies_tap_widget.setCurrentIndex(0)
        self.series_tap_widget.setCurrentIndex(0)
        self.games_tap_widget.setCurrentIndex(0)
        self.books_tap_widget.setCurrentIndex(0)
        self.comics_tap_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main_widget)
    # setupUi

    def retranslateUi(self, main_widget):
        main_widget.setWindowTitle(QCoreApplication.translate("main_widget", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("main_widget", u"This app is designed to be your perfect library for (movies, series, games, etc.)", None))
        self.label.setText(QCoreApplication.translate("main_widget", u"Welcome, to your libirary", None))
#if QT_CONFIG(tooltip)
        self.movies_menu.setToolTip(QCoreApplication.translate("main_widget", u"Show/Hide the menu", None))
#endif // QT_CONFIG(tooltip)
        self.movies_menu.setText("")
        self.movies_label.setText(QCoreApplication.translate("main_widget", u" Movies", None))
#if QT_CONFIG(tooltip)
        self.movies_add_botton.setToolTip(QCoreApplication.translate("main_widget", u"Add a new movie", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.movies_add_botton.setStatusTip(QCoreApplication.translate("main_widget", u"Add a new movie", None))
#endif // QT_CONFIG(statustip)
        self.movies_add_botton.setText("")
#if QT_CONFIG(shortcut)
        self.movies_add_botton.setShortcut(QCoreApplication.translate("main_widget", u"+", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.movies_search_icon_1.setToolTip(QCoreApplication.translate("main_widget", u"Press to show the search bar ", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.movies_search_icon_1.setStatusTip(QCoreApplication.translate("main_widget", u"Press to show the search bar ", None))
#endif // QT_CONFIG(statustip)
        self.movies_search_icon_1.setText("")
        self.movies_search_1.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
#if QT_CONFIG(tooltip)
        self.movies_random_button_1.setToolTip(QCoreApplication.translate("main_widget", u"Choose a random movie from this tap", None))
#endif // QT_CONFIG(tooltip)
        self.movies_random_button_1.setText("")
#if QT_CONFIG(tooltip)
        self.movies_view_1.setToolTip(QCoreApplication.translate("main_widget", u"Veiw", None))
#endif // QT_CONFIG(tooltip)
        self.movies_view_1.setText("")
#if QT_CONFIG(tooltip)
        self.movies_sort_by_1.setToolTip(QCoreApplication.translate("main_widget", u"Sort list by", None))
#endif // QT_CONFIG(tooltip)
        self.movies_sort_by_1.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort By", None))
        self.movies_tap_widget.setTabText(self.movies_tap_widget.indexOf(self.movies_watching), QCoreApplication.translate("main_widget", u" Watching", None))
#if QT_CONFIG(tooltip)
        self.movies_search_icon_2.setToolTip(QCoreApplication.translate("main_widget", u"Press to show the search bar ", None))
#endif // QT_CONFIG(tooltip)
        self.movies_search_icon_2.setText("")
        self.movies_search_2.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
#if QT_CONFIG(tooltip)
        self.movies_random_button_2.setToolTip(QCoreApplication.translate("main_widget", u"Choose a random movie from this tap", None))
#endif // QT_CONFIG(tooltip)
        self.movies_random_button_2.setText("")
#if QT_CONFIG(tooltip)
        self.movies_view_2.setToolTip(QCoreApplication.translate("main_widget", u"Veiw", None))
#endif // QT_CONFIG(tooltip)
        self.movies_view_2.setText("")
#if QT_CONFIG(tooltip)
        self.movies_sort_by_2.setToolTip(QCoreApplication.translate("main_widget", u"Sort list by", None))
#endif // QT_CONFIG(tooltip)
        self.movies_sort_by_2.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort By", None))
        self.movies_tap_widget.setTabText(self.movies_tap_widget.indexOf(self.movies_want_to_watch), QCoreApplication.translate("main_widget", u"Want To Watch", None))
#if QT_CONFIG(tooltip)
        self.movies_search_icon_3.setToolTip(QCoreApplication.translate("main_widget", u"Press to show the search bar ", None))
#endif // QT_CONFIG(tooltip)
        self.movies_search_icon_3.setText("")
        self.movies_search_3.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
#if QT_CONFIG(tooltip)
        self.movies_random_button_3.setToolTip(QCoreApplication.translate("main_widget", u"Choose a random movie from this tap", None))
#endif // QT_CONFIG(tooltip)
        self.movies_random_button_3.setText("")
#if QT_CONFIG(tooltip)
        self.movies_view_3.setToolTip(QCoreApplication.translate("main_widget", u"Veiw", None))
#endif // QT_CONFIG(tooltip)
        self.movies_view_3.setText("")
#if QT_CONFIG(tooltip)
        self.movies_sort_by_3.setToolTip(QCoreApplication.translate("main_widget", u"Sort list by", None))
#endif // QT_CONFIG(tooltip)
        self.movies_sort_by_3.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort By", None))
        self.movies_tap_widget.setTabText(self.movies_tap_widget.indexOf(self.movies_continue_later), QCoreApplication.translate("main_widget", u"Continue Later", None))
#if QT_CONFIG(tooltip)
        self.movies_search_icon_4.setToolTip(QCoreApplication.translate("main_widget", u"Press to show the search bar ", None))
#endif // QT_CONFIG(tooltip)
        self.movies_search_icon_4.setText("")
        self.movies_search_4.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
#if QT_CONFIG(tooltip)
        self.movies_random_button_4.setToolTip(QCoreApplication.translate("main_widget", u"Choose a random movie from this tap", None))
#endif // QT_CONFIG(tooltip)
        self.movies_random_button_4.setText("")
#if QT_CONFIG(tooltip)
        self.movies_view_4.setToolTip(QCoreApplication.translate("main_widget", u"Veiw", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.movies_view_4.setStatusTip(QCoreApplication.translate("main_widget", u"Veiw", None))
#endif // QT_CONFIG(statustip)
        self.movies_view_4.setText("")
#if QT_CONFIG(tooltip)
        self.movies_sort_by_4.setToolTip(QCoreApplication.translate("main_widget", u"Sort list by", None))
#endif // QT_CONFIG(tooltip)
        self.movies_sort_by_4.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort By", None))
        self.movies_tap_widget.setTabText(self.movies_tap_widget.indexOf(self.movies_dont_want_to_watch), QCoreApplication.translate("main_widget", u"Dont Wnat To Continue", None))
#if QT_CONFIG(tooltip)
        self.movies_search_icon_5.setToolTip(QCoreApplication.translate("main_widget", u"Press to show the search bar ", None))
#endif // QT_CONFIG(tooltip)
        self.movies_search_icon_5.setText("")
        self.movies_search_5.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
#if QT_CONFIG(tooltip)
        self.movies_random_button_5.setToolTip(QCoreApplication.translate("main_widget", u"Choose a random movie from this tap", None))
#endif // QT_CONFIG(tooltip)
        self.movies_random_button_5.setText("")
#if QT_CONFIG(tooltip)
        self.movies_view_5.setToolTip(QCoreApplication.translate("main_widget", u"Veiw", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.movies_view_5.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.movies_view_5.setText("")
#if QT_CONFIG(tooltip)
        self.movies_sort_by_5.setToolTip(QCoreApplication.translate("main_widget", u"Sort list by", None))
#endif // QT_CONFIG(tooltip)
        self.movies_sort_by_5.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort By", None))
        self.movies_tap_widget.setTabText(self.movies_tap_widget.indexOf(self.movies_ended), QCoreApplication.translate("main_widget", u"Watched", None))
        self.series_label.setText(QCoreApplication.translate("main_widget", u" Series", None))
#if QT_CONFIG(tooltip)
        self.series_add_button.setToolTip(QCoreApplication.translate("main_widget", u"Add a new movie", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.series_add_button.setStatusTip(QCoreApplication.translate("main_widget", u"Add a new movie", None))
#endif // QT_CONFIG(statustip)
        self.series_add_button.setText("")
#if QT_CONFIG(shortcut)
        self.series_add_button.setShortcut(QCoreApplication.translate("main_widget", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.series_search_1.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
#if QT_CONFIG(tooltip)
        self.series_random_button_1.setToolTip(QCoreApplication.translate("main_widget", u"Choose a random movie from this tap", None))
#endif // QT_CONFIG(tooltip)
        self.series_random_button_1.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.series_sort_box_1.setPlaceholderText("")
        self.series_tap_widget.setTabText(self.series_tap_widget.indexOf(self.movies_watching_2), QCoreApplication.translate("main_widget", u" Watching", None))
        self.series_search_2.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
        self.series_random_button_2.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.series_sort_box_2.setPlaceholderText("")
        self.series_tap_widget.setTabText(self.series_tap_widget.indexOf(self.movies_want_to_watch_2), QCoreApplication.translate("main_widget", u"Want To Watch", None))
        self.series_search_3.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
        self.series_random_button_3.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.series_sort_box_3.setPlaceholderText("")
        self.series_tap_widget.setTabText(self.series_tap_widget.indexOf(self.movies_continue_later_2), QCoreApplication.translate("main_widget", u"Continue Later", None))
        self.series_search_4.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
        self.series_random_button_4.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.series_sort_box_4.setPlaceholderText("")
        self.series_tap_widget.setTabText(self.series_tap_widget.indexOf(self.movies_dont_want_to_watch_2), QCoreApplication.translate("main_widget", u"Dont Wnat To Continue", None))
        self.series_search_5.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
        self.series_random_button_5.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.series_sort_box_5.setPlaceholderText("")
        self.series_tap_widget.setTabText(self.series_tap_widget.indexOf(self.movies_ended_2), QCoreApplication.translate("main_widget", u"Watched", None))
        self.games_label.setText(QCoreApplication.translate("main_widget", u" Games", None))
#if QT_CONFIG(tooltip)
        self.games_add_botton.setToolTip(QCoreApplication.translate("main_widget", u"Add a new movie", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.games_add_botton.setStatusTip(QCoreApplication.translate("main_widget", u"Add a new movie", None))
#endif // QT_CONFIG(statustip)
        self.games_add_botton.setText("")
#if QT_CONFIG(shortcut)
        self.games_add_botton.setShortcut(QCoreApplication.translate("main_widget", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.games_search_1.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
#if QT_CONFIG(tooltip)
        self.games_random_button_1.setToolTip(QCoreApplication.translate("main_widget", u"Choose a random movie from this tap", None))
#endif // QT_CONFIG(tooltip)
        self.games_random_button_1.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.games_sort_box_1.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort by", None))
        self.games_tap_widget.setTabText(self.games_tap_widget.indexOf(self.movies_watching_3), QCoreApplication.translate("main_widget", u"Playing", None))
        self.games_search_2.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
        self.games_random_button_2.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.games_sort_box_2.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort by", None))
        self.games_tap_widget.setTabText(self.games_tap_widget.indexOf(self.movies_want_to_watch_3), QCoreApplication.translate("main_widget", u"Want To Play", None))
        self.games_search_3.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
        self.games_random_button_3.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.games_sort_box_3.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort by", None))
        self.games_tap_widget.setTabText(self.games_tap_widget.indexOf(self.movies_continue_later_3), QCoreApplication.translate("main_widget", u"Continue Later", None))
        self.games_search_4.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
        self.games_random_button_4.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.games_sort_box_4.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort by", None))
        self.games_tap_widget.setTabText(self.games_tap_widget.indexOf(self.movies_dont_want_to_watch_3), QCoreApplication.translate("main_widget", u"Dont Wnat To Continue", None))
        self.games_search_5.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
        self.games_random_button_5.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.games_sort_box_5.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort by", None))
        self.games_tap_widget.setTabText(self.games_tap_widget.indexOf(self.movies_ended_3), QCoreApplication.translate("main_widget", u"Played", None))
        self.books_label.setText(QCoreApplication.translate("main_widget", u" Books", None))
#if QT_CONFIG(tooltip)
        self.books_add_botton.setToolTip(QCoreApplication.translate("main_widget", u"Add a new movie", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.books_add_botton.setStatusTip(QCoreApplication.translate("main_widget", u"Add a new movie", None))
#endif // QT_CONFIG(statustip)
        self.books_add_botton.setText("")
#if QT_CONFIG(shortcut)
        self.books_add_botton.setShortcut(QCoreApplication.translate("main_widget", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.books_search_1.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
#if QT_CONFIG(tooltip)
        self.books_random_button_1.setToolTip(QCoreApplication.translate("main_widget", u"Choose a random movie from this tap", None))
#endif // QT_CONFIG(tooltip)
        self.books_random_button_1.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.books_sort_box_1.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort by", None))
        self.books_tap_widget.setTabText(self.books_tap_widget.indexOf(self.movies_watching_4), QCoreApplication.translate("main_widget", u"Reading", None))
        self.books_search_2.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
        self.books_random_button_2.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.books_sort_box_2.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort by", None))
        self.books_tap_widget.setTabText(self.books_tap_widget.indexOf(self.movies_want_to_watch_4), QCoreApplication.translate("main_widget", u"Want To Read", None))
        self.books_search_3.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
        self.books_random_button_3.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.books_sort_box_3.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort by", None))
        self.books_tap_widget.setTabText(self.books_tap_widget.indexOf(self.movies_continue_later_4), QCoreApplication.translate("main_widget", u"Continue Later", None))
        self.books_search_4.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
        self.books_random_button_4.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.books_sort_box_4.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort by", None))
        self.books_tap_widget.setTabText(self.books_tap_widget.indexOf(self.movies_dont_want_to_watch_4), QCoreApplication.translate("main_widget", u"Dont Wnat To Continue", None))
        self.books_search_5.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
        self.books_random_button_5.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.books_sort_box_5.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort by", None))
        self.books_tap_widget.setTabText(self.books_tap_widget.indexOf(self.movies_ended_4), QCoreApplication.translate("main_widget", u"Ended", None))
        self.comics_label.setText(QCoreApplication.translate("main_widget", u" Comics & Manga", None))
#if QT_CONFIG(tooltip)
        self.comics_add_botton.setToolTip(QCoreApplication.translate("main_widget", u"Add a new movie", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.comics_add_botton.setStatusTip(QCoreApplication.translate("main_widget", u"Add a new movie", None))
#endif // QT_CONFIG(statustip)
        self.comics_add_botton.setText("")
#if QT_CONFIG(shortcut)
        self.comics_add_botton.setShortcut(QCoreApplication.translate("main_widget", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.comics_search_1.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
#if QT_CONFIG(tooltip)
        self.comics_random_button_1.setToolTip(QCoreApplication.translate("main_widget", u"Choose a random movie from this tap", None))
#endif // QT_CONFIG(tooltip)
        self.comics_random_button_1.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.comics_sort_box_1.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort by", None))
        self.comics_tap_widget.setTabText(self.comics_tap_widget.indexOf(self.movies_watching_6), QCoreApplication.translate("main_widget", u"Reading", None))
        self.comics_search_2.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
        self.comics_random_button_2.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.comics_sort_box_2.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort by", None))
        self.comics_tap_widget.setTabText(self.comics_tap_widget.indexOf(self.movies_want_to_watch_6), QCoreApplication.translate("main_widget", u"Want To Read", None))
        self.comics_search_3.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
        self.comics_random_button_3.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.comics_sort_box_3.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort by", None))
        self.comics_tap_widget.setTabText(self.comics_tap_widget.indexOf(self.movies_continue_later_6), QCoreApplication.translate("main_widget", u"Continue Later", None))
        self.comics_search_4.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
        self.comics_random_button_4.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.comics_sort_box_4.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort by", None))
        self.comics_tap_widget.setTabText(self.comics_tap_widget.indexOf(self.movies_dont_want_to_watch_6), QCoreApplication.translate("main_widget", u"Dont Wnat To Continue", None))
        self.comics_search_5.setPlaceholderText(QCoreApplication.translate("main_widget", u"Search (Name or Year)", None))
        self.comics_random_button_5.setText(QCoreApplication.translate("main_widget", u"Choose One", None))
        self.comics_sort_box_5.setPlaceholderText(QCoreApplication.translate("main_widget", u"Sort by", None))
        self.comics_tap_widget.setTabText(self.comics_tap_widget.indexOf(self.movies_ended_6), QCoreApplication.translate("main_widget", u"Ended", None))
        self.label_6.setText(QCoreApplication.translate("main_widget", u"Setting", None))
        self.name_lable.setText("")
        self.photo_lable.setText("")
        self.label_4.setText(QCoreApplication.translate("main_widget", u"Media", None))
        self.show_movies.setText(QCoreApplication.translate("main_widget", u"   Movies", None))
        self.show_series.setText(QCoreApplication.translate("main_widget", u"  TV Series", None))
        self.show_games.setText(QCoreApplication.translate("main_widget", u"  Games", None))
        self.show_books.setText(QCoreApplication.translate("main_widget", u"  Books", None))
        self.show_comics.setText(QCoreApplication.translate("main_widget", u"  Comics", None))
        self.label_5.setText(QCoreApplication.translate("main_widget", u"Account", None))
        self.show_home.setText(QCoreApplication.translate("main_widget", u"   Home", None))
        self.show_profile.setText(QCoreApplication.translate("main_widget", u"   Profile", None))
        self.show_dashboard.setText(QCoreApplication.translate("main_widget", u"  Dashboard", None))
        self.show_setting.setText(QCoreApplication.translate("main_widget", u"   Settings", None))
        self.logout.setText(QCoreApplication.translate("main_widget", u"Logout", None))
    # retranslateUi

