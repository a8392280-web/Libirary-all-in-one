# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'movies_addAPCzgi.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import py_ui.resources_rc

class Ui_add_widget(object):
    def setupUi(self, add_widget):
        if not add_widget.objectName():
            add_widget.setObjectName(u"add_widget")
        add_widget.resize(741, 530)
        add_widget.setMinimumSize(QSize(741, 530))
        add_widget.setMaximumSize(QSize(741, 530))
        add_widget.setStyleSheet(u"QLineEdit {\n"
"    color: #e0e6f0; /* light gray text for dark bg */\n"
"    font-size: 14px;\n"
"    background-color: rgba(255, 255, 255, 0.05); /* slightly visible bg for input field */\n"
"    padding: 6px;\n"
"    border: none;\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 0.2); /* soft light line before focus */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgba(255, 255, 255, 0.1); /* slightly brighter on hover */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    outline: none;\n"
"    border-bottom: 2px solid #5891ff; /* bright blue focus line */\n"
"    background-color: rgba(255, 255, 255, 0.12);\n"
"}\n"
"\n"
"QLabel {\n"
"    border: 1px solid white;   /* White border */\n"
"    border-radius: 6px;        /* Rounded corners (optional) */\n"
"    padding: 4px;              /* Space inside */\n"
"}\n"
"\n"
"QWidget { \n"
"	background-color: #2b3640;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: #e0e6f0; /* light text */\n"
"    font-size: 14px;\n"
"    background"
                        "-color: #2e3a4b; /* dark gray-blue button */\n"
"    border: 1px solid rgba(255, 255, 255, 0.15);\n"
"    border-radius: 6px;\n"
"    padding: 6px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c4d63; /* lighter on hover */\n"
"    border: 1px solid #5891ff; /* subtle blue glow */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1e2a3a; /* darker when pressed */\n"
"    border: 1px solid #4f7de0;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: rgba(255, 255, 255, 0.4);\n"
"    background-color: rgba(255, 255, 255, 0.05);\n"
"    border: 1px solid rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"QComboBox {\n"
"    color: #e0e6f0; /* light text */\n"
"    font-size: 14px;\n"
"    background-color: rgba(255, 255, 255, 0.05); /* subtle transparent bg */\n"
"    border: 1px solid rgba(255, 255, 255, 0.15);\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    border: 1px solid #5891ff; /*"
                        " subtle blue border */\n"
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
"    border: 1px solid #5891ff;\n"
"    selection-background-color: #3c4d63; /* selected item background */\n"
"    selection-color: #ffffff;\n"
"}\n"
"\n"
"QDialog {\n"
"   color: white;\n"
"   border: none;\n"
"}\n"
"\n"
"QDialog QLabel {\n"
"    color: white;\n"
"    border: none;\n"
"}")
        self.gridLayout = QGridLayout(add_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)

        self.search_button = QPushButton(add_widget)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setFlat(False)

        self.horizontalLayout_13.addWidget(self.search_button)

        self.search_line = QLineEdit(add_widget)
        self.search_line.setObjectName(u"search_line")
        self.search_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.search_line)


        self.gridLayout.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, -1, 50, -1)
        self.image_label = QLabel(add_widget)
        self.image_label.setObjectName(u"image_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setMinimumSize(QSize(180, 175))
        self.image_label.setMaximumSize(QSize(180, 270))
        self.image_label.setStyleSheet(u"QLabel {\n"
"    border: 1px solid white;   /* White border */\n"
"    border-radius: 6px;        /* Rounded corners (optional) */\n"
"    padding: 4px;              /* Space inside */\n"
"}\n"
"")
        self.image_label.setScaledContents(True)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.image_label)

        self.image_url_input = QLineEdit(add_widget)
        self.image_url_input.setObjectName(u"image_url_input")
        self.image_url_input.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout_8.addWidget(self.image_url_input)

        self.section_selector = QComboBox(add_widget)
        self.section_selector.setObjectName(u"section_selector")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.section_selector.sizePolicy().hasHeightForWidth())
        self.section_selector.setSizePolicy(sizePolicy1)
        self.section_selector.setMinimumSize(QSize(0, 0))
        self.section_selector.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        self.section_selector.setFont(font)
        self.section_selector.setAutoFillBackground(False)
        self.section_selector.setEditable(False)
        self.section_selector.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.section_selector.setIconSize(QSize(16, 10))
        self.section_selector.setFrame(False)
        self.section_selector.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.verticalLayout_8.addWidget(self.section_selector)


        self.horizontalLayout_9.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(120, 6, -1, 6)
        self.name_input = QLineEdit(add_widget)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.name_input)

        self.time_input = QLineEdit(add_widget)
        self.time_input.setObjectName(u"time_input")
        self.time_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.time_input)

        self.date_input = QLineEdit(add_widget)
        self.date_input.setObjectName(u"date_input")
        self.date_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.date_input)

        self.plot_input = QLineEdit(add_widget)
        self.plot_input.setObjectName(u"plot_input")
        self.plot_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.plot_input)

        self.gener_input = QLineEdit(add_widget)
        self.gener_input.setObjectName(u"gener_input")
        self.gener_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.gener_input)

        self.imdb_rate_input = QLineEdit(add_widget)
        self.imdb_rate_input.setObjectName(u"imdb_rate_input")
        self.imdb_rate_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.imdb_rate_input)

        self.user_rate_input = QLineEdit(add_widget)
        self.user_rate_input.setObjectName(u"user_rate_input")
        self.user_rate_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.user_rate_input)

        self.trailer_input = QLineEdit(add_widget)
        self.trailer_input.setObjectName(u"trailer_input")
        self.trailer_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.trailer_input)


        self.horizontalLayout_9.addLayout(self.verticalLayout_9)


        self.gridLayout.addLayout(self.horizontalLayout_9, 1, 0, 1, 2)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.apply_button = QPushButton(add_widget)
        self.apply_button.setObjectName(u"apply_button")
        self.apply_button.setFlat(False)

        self.horizontalLayout_12.addWidget(self.apply_button)

        self.cancel_button = QPushButton(add_widget)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout_12.addWidget(self.cancel_button)


        self.gridLayout.addLayout(self.horizontalLayout_12, 2, 1, 1, 1)

#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(add_widget)

        QMetaObject.connectSlotsByName(add_widget)
    # setupUi

    def retranslateUi(self, add_widget):
        add_widget.setWindowTitle(QCoreApplication.translate("add_widget", u"Form", None))
        self.search_button.setText(QCoreApplication.translate("add_widget", u"Search", None))
        self.search_line.setPlaceholderText(QCoreApplication.translate("add_widget", u"Search Online", None))
        self.image_label.setText("")
        self.image_url_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Image URL", None))
        self.section_selector.setCurrentText("")
        self.section_selector.setPlaceholderText(QCoreApplication.translate("add_widget", u"Add to", None))
        self.name_input.setText("")
        self.name_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Name", None))
        self.time_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Runtime (min)", None))
        self.date_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Release", None))
        self.plot_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Plot", None))
        self.gener_input.setText("")
        self.gener_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Genre  (Action-Horror)", None))
        self.imdb_rate_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"IMDB rate", None))
        self.user_rate_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"User rate", None))
        self.trailer_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Trailer", None))
        self.apply_button.setText(QCoreApplication.translate("add_widget", u"Apply", None))
        self.cancel_button.setText(QCoreApplication.translate("add_widget", u"Cancel", None))
    # retranslateUi

