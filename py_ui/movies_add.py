# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'movies_addqRlAkz.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
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
"    color: white;\n"
"    border: none;\n"
"}\n"
"\n"
"QDialog QLabel {\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"")
        self.gridLayout_3 = QGridLayout(add_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.api_button = QPushButton(add_widget)
        self.api_button.setObjectName(u"api_button")
        self.api_button.setStyleSheet(u"QPushButton {\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-transform: uppercase;\n"
"    color: #ffffff;\n"
"    background-color: #262e39;\n"
"    border: 1px solid #7D8082;\n"
"    border-radius: 4px;\n"
"    padding: 10px 20px;\n"
"    min-height: 40px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1a2430; /* slightly lighter on hover */\n"
"    border-color: #ffffff;      /* highlight border */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0a1017; /* darker when pressed */\n"
"    border-color: #ff4655;     /* red highlight */\n"
"}\n"
"\n"
"/* Optional: checked state if toggle button */\n"
"QPushButton:checked {\n"
"    background-color: #ff4655; /* red to indicate active */\n"
"    color: #ffffff;\n"
"    border-color: #ffffff;\n"
"}\n"
"")
        self.api_button.setCheckable(True)
        self.api_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.api_button)

        self.manual_button = QPushButton(add_widget)
        self.manual_button.setObjectName(u"manual_button")
        self.manual_button.setStyleSheet(u"QPushButton {\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    text-transform: uppercase;\n"
"    color: #ffffff;\n"
"    background-color: #262e39;\n"
"    border: 1px solid #7D8082;\n"
"    border-radius: 4px;\n"
"    padding: 10px 20px;\n"
"    min-height: 40px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1a2430; /* slightly lighter on hover */\n"
"    border-color: #ffffff;      /* highlight border */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #0a1017; /* darker when pressed */\n"
"    border-color: #ff4655;     /* red highlight */\n"
"}\n"
"\n"
"/* Optional: checked state if toggle button */\n"
"QPushButton:checked {\n"
"    background-color: #ff4655; /* red to indicate active */\n"
"    color: #ffffff;\n"
"    border-color: #ffffff;\n"
"}\n"
"")
        self.manual_button.setCheckable(True)
        self.manual_button.setChecked(True)
        self.manual_button.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.manual_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.stackedWidget = QStackedWidget(add_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.manual_page = QWidget()
        self.manual_page.setObjectName(u"manual_page")
        self.gridLayout = QGridLayout(self.manual_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.manual_apply_button = QPushButton(self.manual_page)
        self.manual_apply_button.setObjectName(u"manual_apply_button")
        self.manual_apply_button.setFlat(False)

        self.horizontalLayout_3.addWidget(self.manual_apply_button)

        self.manual_cancel_button = QPushButton(self.manual_page)
        self.manual_cancel_button.setObjectName(u"manual_cancel_button")

        self.horizontalLayout_3.addWidget(self.manual_cancel_button)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 30, -1)
        self.manual_image_label = QLabel(self.manual_page)
        self.manual_image_label.setObjectName(u"manual_image_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manual_image_label.sizePolicy().hasHeightForWidth())
        self.manual_image_label.setSizePolicy(sizePolicy)
        self.manual_image_label.setMinimumSize(QSize(180, 270))
        self.manual_image_label.setMaximumSize(QSize(180, 270))
        self.manual_image_label.setStyleSheet(u"")
        self.manual_image_label.setScaledContents(True)
        self.manual_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.manual_image_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.image_url = QLineEdit(self.manual_page)
        self.image_url.setObjectName(u"image_url")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.image_url.sizePolicy().hasHeightForWidth())
        self.image_url.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.image_url)

        self.line_2 = QFrame(self.manual_page)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.manual_section_selector = QComboBox(self.manual_page)
        self.manual_section_selector.setObjectName(u"manual_section_selector")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.manual_section_selector.sizePolicy().hasHeightForWidth())
        self.manual_section_selector.setSizePolicy(sizePolicy2)
        self.manual_section_selector.setMaximumSize(QSize(100, 30))
        font = QFont()
        self.manual_section_selector.setFont(font)
        self.manual_section_selector.setAutoFillBackground(False)
        self.manual_section_selector.setStyleSheet(u"")
        self.manual_section_selector.setEditable(False)
        self.manual_section_selector.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.manual_section_selector.setIconSize(QSize(16, 10))
        self.manual_section_selector.setFrame(False)
        self.manual_section_selector.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.horizontalLayout_2.addWidget(self.manual_section_selector)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.manual_name_input = QLineEdit(self.manual_page)
        self.manual_name_input.setObjectName(u"manual_name_input")
        self.manual_name_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.manual_name_input)

        self.manual_time_input = QLineEdit(self.manual_page)
        self.manual_time_input.setObjectName(u"manual_time_input")
        self.manual_time_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.manual_time_input)

        self.manual_date_input = QLineEdit(self.manual_page)
        self.manual_date_input.setObjectName(u"manual_date_input")
        self.manual_date_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.manual_date_input)

        self.manual_plot_input = QLineEdit(self.manual_page)
        self.manual_plot_input.setObjectName(u"manual_plot_input")
        self.manual_plot_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.manual_plot_input)

        self.manual_gener_input = QLineEdit(self.manual_page)
        self.manual_gener_input.setObjectName(u"manual_gener_input")
        self.manual_gener_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.manual_gener_input)

        self.manual_imdb_rate_input = QLineEdit(self.manual_page)
        self.manual_imdb_rate_input.setObjectName(u"manual_imdb_rate_input")
        self.manual_imdb_rate_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.manual_imdb_rate_input)

        self.manual_user_rate_input = QLineEdit(self.manual_page)
        self.manual_user_rate_input.setObjectName(u"manual_user_rate_input")
        self.manual_user_rate_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.manual_user_rate_input)

        self.manual_trailer_input = QLineEdit(self.manual_page)
        self.manual_trailer_input.setObjectName(u"manual_trailer")
        self.manual_trailer_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.manual_trailer_input)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.manual_page)
        self.api_page = QWidget()
        self.api_page.setObjectName(u"api_page")
        self.gridLayout_2 = QGridLayout(self.api_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.api_apply_button = QPushButton(self.api_page)
        self.api_apply_button.setObjectName(u"api_apply_button")
        self.api_apply_button.setFlat(False)

        self.horizontalLayout_10.addWidget(self.api_apply_button)

        self.api_cancel_button = QPushButton(self.api_page)
        self.api_cancel_button.setObjectName(u"api_cancel_button")

        self.horizontalLayout_10.addWidget(self.api_cancel_button)


        self.gridLayout_2.addLayout(self.horizontalLayout_10, 2, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 50, -1)
        self.api_image_label = QLabel(self.api_page)
        self.api_image_label.setObjectName(u"api_image_label")
        sizePolicy.setHeightForWidth(self.api_image_label.sizePolicy().hasHeightForWidth())
        self.api_image_label.setSizePolicy(sizePolicy)
        self.api_image_label.setMinimumSize(QSize(180, 175))
        self.api_image_label.setMaximumSize(QSize(180, 270))
        self.api_image_label.setStyleSheet(u"QLabel {\n"
"    border: 1px solid white;   /* White border */\n"
"    border-radius: 6px;        /* Rounded corners (optional) */\n"
"    padding: 4px;              /* Space inside */\n"
"}\n"
"")
        self.api_image_label.setScaledContents(True)
        self.api_image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.api_image_label)

        self.api_section_selector = QComboBox(self.api_page)
        self.api_section_selector.setObjectName(u"api_section_selector")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.api_section_selector.sizePolicy().hasHeightForWidth())
        self.api_section_selector.setSizePolicy(sizePolicy3)
        self.api_section_selector.setMinimumSize(QSize(0, 0))
        self.api_section_selector.setMaximumSize(QSize(16777215, 30))
        self.api_section_selector.setFont(font)
        self.api_section_selector.setAutoFillBackground(False)
        self.api_section_selector.setEditable(False)
        self.api_section_selector.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.api_section_selector.setIconSize(QSize(16, 10))
        self.api_section_selector.setFrame(False)
        self.api_section_selector.setLabelDrawingMode(QComboBox.LabelDrawingMode.UseStyle)

        self.verticalLayout_4.addWidget(self.api_section_selector)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(120, 6, -1, 6)
        self.api_name_input = QLineEdit(self.api_page)
        self.api_name_input.setObjectName(u"api_name_input")
        self.api_name_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.api_name_input)

        self.api_time_input = QLineEdit(self.api_page)
        self.api_time_input.setObjectName(u"api_time_input")
        self.api_time_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.api_time_input)

        self.api_date_input = QLineEdit(self.api_page)
        self.api_date_input.setObjectName(u"api_date_input")
        self.api_date_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.api_date_input)

        self.api_plot_input = QLineEdit(self.api_page)
        self.api_plot_input.setObjectName(u"api_plot_input")
        self.api_plot_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.api_plot_input)

        self.api_gener_input = QLineEdit(self.api_page)
        self.api_gener_input.setObjectName(u"api_gener_input")
        self.api_gener_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.api_gener_input)

        self.api_imdb_rate_input = QLineEdit(self.api_page)
        self.api_imdb_rate_input.setObjectName(u"api_imdb_rate_input")
        self.api_imdb_rate_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.api_imdb_rate_input)

        self.api_user_rate_input = QLineEdit(self.api_page)
        self.api_user_rate_input.setObjectName(u"api_user_rate_input")
        self.api_user_rate_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.api_user_rate_input)

        self.api_trailer_input = QLineEdit(self.api_page)
        self.api_trailer_input.setObjectName(u"api_trailer")
        self.api_trailer_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.api_trailer_input)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 0, 1, 2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.search_button = QPushButton(self.api_page)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setFlat(False)

        self.horizontalLayout_6.addWidget(self.search_button)

        self.search_line = QLineEdit(self.api_page)
        self.search_line.setObjectName(u"search_line")
        self.search_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.search_line)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.api_page)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(add_widget)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(add_widget)
    # setupUi

    def retranslateUi(self, add_widget):
        add_widget.setWindowTitle(QCoreApplication.translate("add_widget", u"Form", None))
        self.api_button.setText(QCoreApplication.translate("add_widget", u"API", None))
        self.manual_button.setText(QCoreApplication.translate("add_widget", u"Manual", None))
        self.manual_apply_button.setText(QCoreApplication.translate("add_widget", u"Apply", None))
        self.manual_cancel_button.setText(QCoreApplication.translate("add_widget", u"Cancel", None))
        self.manual_image_label.setText("")
        self.image_url.setPlaceholderText(QCoreApplication.translate("add_widget", u"Past the image URL", None))
        self.manual_section_selector.setCurrentText("")
        self.manual_section_selector.setPlaceholderText(QCoreApplication.translate("add_widget", u"Add to", None))
        self.manual_name_input.setText("")
        self.manual_name_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Name", None))
        self.manual_time_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Runtime (min)", None))
        self.manual_date_input.setText("")
        self.manual_date_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Release", None))
        self.manual_plot_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Plot", None))
        self.manual_gener_input.setText("")
        self.manual_gener_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Genre  (Action-Horror)", None))
        self.manual_imdb_rate_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"IMDB rate", None))
        self.manual_user_rate_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"User rate", None))
        self.manual_trailer_input.setText("")
        self.manual_trailer_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Trailer", None))
        self.api_apply_button.setText(QCoreApplication.translate("add_widget", u"Apply", None))
        self.api_cancel_button.setText(QCoreApplication.translate("add_widget", u"Cancel", None))
        self.api_image_label.setText("")
        self.api_section_selector.setCurrentText("")
        self.api_section_selector.setPlaceholderText(QCoreApplication.translate("add_widget", u"Add to", None))
        self.api_name_input.setText("")
        self.api_name_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Name", None))
        self.api_time_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Runtime (min)", None))
        self.api_date_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Release", None))
        self.api_plot_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Plot", None))
        self.api_gener_input.setText("")
        self.api_gener_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Genre  (Action-Horror)", None))
        self.api_imdb_rate_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"IMDB rate", None))
        self.api_user_rate_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"User rate", None))
        self.api_trailer_input.setPlaceholderText(QCoreApplication.translate("add_widget", u"Trailer", None))
        self.search_button.setText(QCoreApplication.translate("add_widget", u"Search", None))
        self.search_line.setPlaceholderText(QCoreApplication.translate("add_widget", u"Search Online", None))
    # retranslateUi

