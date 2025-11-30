# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'movies_show_uiPakuHk.ui'
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
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QVBoxLayout, QWidget)
import py_ui.resources_rc

class Ui_show(object):
    def setupUi(self, show):
        if not show.objectName():
            show.setObjectName(u"show")
        show.resize(674, 713)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(show.sizePolicy().hasHeightForWidth())
        show.setSizePolicy(sizePolicy)
        show.setMinimumSize(QSize(674, 713))
        show.setMaximumSize(QSize(1000, 16777215))
        show.setStyleSheet(u"/* ===== SCROLL AREAS & CONTAINERS ===== */\n"
"QScrollArea, QStackedWidget,\n"
"QWidget#scroll_content, \n"
"QWidget#info_scrollarea {\n"
"    background-color: #182126;\n"
"    border: none;\n"
"}\n"
"\n"
"QWidget#show {\n"
"    background-color: #262e39;\n"
"}\n"
"\n"
"/* ===== BASE TEXT STYLES ===== */\n"
"QLabel, QLineEdit, QPushButton, QComboBox {\n"
"    color: #e0e6f0;\n"
"    font-size: 14px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* ===== INPUT FIELDS ===== */\n"
"QLineEdit {\n"
"    background-color: rgba(255, 255, 255, 0.05);\n"
"    padding: 6px;\n"
"    border: none;\n"
"    border-bottom: 1px solid rgba(255, 255, 255, 0.2);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-bottom: 2px solid #5891ff;\n"
"    background-color: rgba(255, 255, 255, 0.12);\n"
"    outline: none;\n"
"}\n"
"\n"
"/* ===== BUTTONS ===== */\n"
"QPushButton {\n"
"    background-color: #2e3a4b;\n"
" "
                        "   border: 1px solid rgba(255, 255, 255, 0.15);\n"
"    border-radius: 6px;\n"
"    padding: 6px 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c4d63;\n"
"    border: 1px solid #5891ff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1e2a3a;\n"
"    border: 1px solid #4f7de0;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    color: rgba(255, 255, 255, 0.4);\n"
"    background-color: rgba(255, 255, 255, 0.05);\n"
"    border: 1px solid rgba(255, 255, 255, 0.1);\n"
"}\n"
"\n"
"/* ===== COMBO BOXES ===== */\n"
"QComboBox {\n"
"    background-color: rgba(255, 255, 255, 0.05);\n"
"    border: 1px solid rgba(255, 255, 255, 0.15);\n"
"    border-radius: 6px;\n"
"    padding: 6px 10px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: rgba(255, 255, 255, 0.1);\n"
"    border: 1px solid #5891ff;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 1px solid #5891ff;\n"
"    background-color: rgba(255, 255, 255, 0.12);\n"
"    outline: none;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
""
                        "    border: none;\n"
"    width: 25px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/Icons/sort_by.png);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #2e3a4b;\n"
"    color: #e0e6f0;\n"
"    border: 1px solid #5891ff;\n"
"    selection-background-color: #3c4d63;\n"
"    selection-color: #ffffff;\n"
"}\n"
"\n"
"/* ===== TABS ===== */\n"
"QTabWidget::pane {\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QTabBar {\n"
"    qproperty-drawBase: 0;\n"
"    alignment: center;\n"
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
"    color: #cad1d9;\n"
"    border-bottom: 3px solid #fbffff;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    color: #cad1d9;\n"
"}\n"
"\n"
"/*"
                        " ===== LABELS ===== */\n"
"QLabel#show_image_lable {\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QDialog {\n"
"    background-color:#182126;    /* your dark color */\n"
"    color: white;\n"
"}\n"
"\n"
"QDialog QLabel {\n"
"    color: white;\n"
"}\n"
"")
        self.gridLayout = QGridLayout(show)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(show)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setDocumentMode(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(10, 30, 10, 5)
        self.stackedWidget = QStackedWidget(self.tab)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.show_widget = QWidget()
        self.show_widget.setObjectName(u"show_widget")
        self.gridLayout_2 = QGridLayout(self.show_widget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.show_widget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.info_scrollarea = QWidget()
        self.info_scrollarea.setObjectName(u"info_scrollarea")
        self.info_scrollarea.setGeometry(QRect(0, 0, 637, 1201))
        self.gridLayout_7 = QGridLayout(self.info_scrollarea)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(5, -1, 10, -1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 15)
        self.show_image_lable = QLabel(self.info_scrollarea)
        self.show_image_lable.setObjectName(u"show_image_lable")
        self.show_image_lable.setMinimumSize(QSize(180, 270))
        self.show_image_lable.setMaximumSize(QSize(180, 270))
        self.show_image_lable.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.show_image_lable)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.show_name_lable = QLabel(self.info_scrollarea)
        self.show_name_lable.setObjectName(u"show_name_lable")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.show_name_lable.sizePolicy().hasHeightForWidth())
        self.show_name_lable.setSizePolicy(sizePolicy1)
        self.show_name_lable.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        self.show_name_lable.setFont(font)
        self.show_name_lable.setStyleSheet(u"")
        self.show_name_lable.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.show_name_lable)

        self.verticalSpacer_4 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.show_label = QLabel(self.info_scrollarea)
        self.show_label.setObjectName(u"show_label")
        sizePolicy1.setHeightForWidth(self.show_label.sizePolicy().hasHeightForWidth())
        self.show_label.setSizePolicy(sizePolicy1)
        self.show_label.setMaximumSize(QSize(1111111, 25))
        self.show_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.show_label)

        self.show_gener_lable = QLabel(self.info_scrollarea)
        self.show_gener_lable.setObjectName(u"show_gener_lable")
        sizePolicy1.setHeightForWidth(self.show_gener_lable.sizePolicy().hasHeightForWidth())
        self.show_gener_lable.setSizePolicy(sizePolicy1)
        self.show_gener_lable.setMaximumSize(QSize(16777215, 25))
        self.show_gener_lable.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.show_gener_lable)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(0)
        self.gridLayout_8.setVerticalSpacing(10)
        self.gridLayout_8.setContentsMargins(0, 20, -1, 15)
        self.widget_2 = QWidget(self.info_scrollarea)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/icons/Icons/star.png"))
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.show_user_rate_lable = QLabel(self.widget_2)
        self.show_user_rate_lable.setObjectName(u"show_user_rate_lable")
        self.show_user_rate_lable.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.show_user_rate_lable)


        self.gridLayout_8.addWidget(self.widget_2, 1, 5, 1, 1)

        self.plot_widget = QWidget(self.info_scrollarea)
        self.plot_widget.setObjectName(u"plot_widget")
        self.plot_widget.setStyleSheet(u"QWidget#plot_widget{\n"
"    border-radius: 12px;            /* round corners */\n"
"\n"
"}\n"
"\n"
"QWidget#plot_widget:hover {\n"
"    border: 2px solid #555;         /* highlight border only */\n"
"    background-color: #1e1e1e;      /* SAME bg \u2192 no bg change */\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.plot_widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.show_plot_lable = QLabel(self.plot_widget)
        self.show_plot_lable.setObjectName(u"show_plot_lable")
        self.show_plot_lable.setMaximumSize(QSize(16777215, 16777215))
        self.show_plot_lable.setPixmap(QPixmap(u":/icons/Icons/file.png"))
        self.show_plot_lable.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.show_plot_lable)

        self.label_5 = QLabel(self.plot_widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_5)


        self.gridLayout_8.addWidget(self.plot_widget, 0, 5, 1, 1)

        self.widget_4 = QWidget(self.info_scrollarea)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_14 = QVBoxLayout(self.widget_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.tmdb_icon_label = QLabel(self.widget_4)
        self.tmdb_icon_label.setObjectName(u"tmdb_icon_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tmdb_icon_label.sizePolicy().hasHeightForWidth())
        self.tmdb_icon_label.setSizePolicy(sizePolicy2)
        self.tmdb_icon_label.setMaximumSize(QSize(32, 32))
        self.tmdb_icon_label.setPixmap(QPixmap(u":/icons/Icons/tmdb.png"))
        self.tmdb_icon_label.setScaledContents(True)
        self.tmdb_icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.tmdb_icon_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.tmdb_rate = QLabel(self.widget_4)
        self.tmdb_rate.setObjectName(u"tmdb_rate")
        self.tmdb_rate.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.tmdb_rate)

        self.tmdb_votes = QLabel(self.widget_4)
        self.tmdb_votes.setObjectName(u"tmdb_votes")
        self.tmdb_votes.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.tmdb_votes)


        self.gridLayout_8.addWidget(self.widget_4, 1, 1, 1, 1)

        self.widget_5 = QWidget(self.info_scrollarea)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_15 = QVBoxLayout(self.widget_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.rottentomato_icon_label = QLabel(self.widget_5)
        self.rottentomato_icon_label.setObjectName(u"rottentomato_icon_label")
        self.rottentomato_icon_label.setMinimumSize(QSize(32, 32))
        self.rottentomato_icon_label.setMaximumSize(QSize(16777215, 16777215))
        self.rottentomato_icon_label.setPixmap(QPixmap(u":/icons/Icons/rotten tomatoes.png"))
        self.rottentomato_icon_label.setScaledContents(True)

        self.verticalLayout_15.addWidget(self.rottentomato_icon_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.rotten_tomatos_rate = QLabel(self.widget_5)
        self.rotten_tomatos_rate.setObjectName(u"rotten_tomatos_rate")
        self.rotten_tomatos_rate.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.rotten_tomatos_rate)


        self.gridLayout_8.addWidget(self.widget_5, 1, 0, 1, 1)

        self.trailer_widget = QWidget(self.info_scrollarea)
        self.trailer_widget.setObjectName(u"trailer_widget")
        self.trailer_widget.setStyleSheet(u"QWidget#trailer_widget{\n"
"    border-radius: 12px;            /* round corners */\n"
"\n"
"}\n"
"\n"
"QWidget#trailer_widget:hover {\n"
"    border: 2px solid #555;         /* highlight border only */\n"
"    background-color: #1e1e1e;      /* SAME bg \u2192 no bg change */\n"
"}\n"
"")
        self.verticalLayout_13 = QVBoxLayout(self.trailer_widget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.show_trailer_lable = QLabel(self.trailer_widget)
        self.show_trailer_lable.setObjectName(u"show_trailer_lable")
        self.show_trailer_lable.setPixmap(QPixmap(u":/icons/Icons/trailer.png"))
        self.show_trailer_lable.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.show_trailer_lable)

        self.label_6 = QLabel(self.trailer_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_6)


        self.gridLayout_8.addWidget(self.trailer_widget, 0, 4, 1, 1)

        self.widget_3 = QWidget(self.info_scrollarea)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/icons/Icons/chronometer.png"))
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_4)

        self.show_time_lable = QLabel(self.widget_3)
        self.show_time_lable.setObjectName(u"show_time_lable")
        self.show_time_lable.setMaximumSize(QSize(16777215, 25))
        self.show_time_lable.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.show_time_lable)


        self.gridLayout_8.addWidget(self.widget_3, 0, 1, 1, 1)

        self.move_to_combobox = QComboBox(self.info_scrollarea)
        self.move_to_combobox.setObjectName(u"move_to_combobox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.move_to_combobox.sizePolicy().hasHeightForWidth())
        self.move_to_combobox.setSizePolicy(sizePolicy3)
        self.move_to_combobox.setMinimumSize(QSize(110, 0))
        self.move_to_combobox.setMaximumSize(QSize(100, 16777215))
        self.move_to_combobox.setStyleSheet(u"")
        self.move_to_combobox.setIconSize(QSize(16, 16))
        self.move_to_combobox.setFrame(False)

        self.gridLayout_8.addWidget(self.move_to_combobox, 0, 0, 1, 1)

        self.widget = QWidget(self.info_scrollarea)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_2.setSizeIncrement(QSize(0, 0))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setPixmap(QPixmap(u":/icons/Icons/imdb.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.show_imdb_rate_lable = QLabel(self.widget)
        self.show_imdb_rate_lable.setObjectName(u"show_imdb_rate_lable")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(2)
        sizePolicy5.setHeightForWidth(self.show_imdb_rate_lable.sizePolicy().hasHeightForWidth())
        self.show_imdb_rate_lable.setSizePolicy(sizePolicy5)
        self.show_imdb_rate_lable.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.show_imdb_rate_lable)

        self.imdb_votes = QLabel(self.widget)
        self.imdb_votes.setObjectName(u"imdb_votes")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(1)
        sizePolicy6.setHeightForWidth(self.imdb_votes.sizePolicy().hasHeightForWidth())
        self.imdb_votes.setSizePolicy(sizePolicy6)
        self.imdb_votes.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.imdb_votes)


        self.gridLayout_8.addWidget(self.widget, 1, 4, 1, 1)

        self.widget_6 = QWidget(self.info_scrollarea)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 0))
        self.verticalLayout_16 = QVBoxLayout(self.widget_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.metascore_icon_label = QLabel(self.widget_6)
        self.metascore_icon_label.setObjectName(u"metascore_icon_label")
        self.metascore_icon_label.setMaximumSize(QSize(40, 40))
        self.metascore_icon_label.setPixmap(QPixmap(u":/icons/Icons/metascore.png"))
        self.metascore_icon_label.setScaledContents(True)

        self.verticalLayout_16.addWidget(self.metascore_icon_label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.metascore_rate = QLabel(self.widget_6)
        self.metascore_rate.setObjectName(u"metascore_rate")
        self.metascore_rate.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.metascore_rate)


        self.gridLayout_8.addWidget(self.widget_6, 2, 5, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_8)

        self.widget_7 = QWidget(self.info_scrollarea)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 0))
        self.widget_7.setSizeIncrement(QSize(0, 0))
        self.gridLayout_10 = QGridLayout(self.widget_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.director_label = QLabel(self.widget_7)
        self.director_label.setObjectName(u"director_label")
        self.director_label.setMinimumSize(QSize(180, 250))
        self.director_label.setMaximumSize(QSize(180, 200))
        self.director_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.director_label, 0, Qt.AlignmentFlag.AlignTop)

        self.director_name = QLabel(self.widget_7)
        self.director_name.setObjectName(u"director_name")

        self.horizontalLayout_5.addWidget(self.director_name, 0, Qt.AlignmentFlag.AlignTop)


        self.gridLayout_10.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_7)

        self.scrollArea_3 = QScrollArea(self.info_scrollarea)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMinimumSize(QSize(0, 285))
        self.scrollArea_3.setStyleSheet(u"QWidget {\n"
"    background-color: #262e39;\n"
"    border: none;\n"
"}")
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_3.setWidgetResizable(True)
        self.cast_scroll_area = QWidget()
        self.cast_scroll_area.setObjectName(u"cast_scroll_area")
        self.cast_scroll_area.setGeometry(QRect(0, 0, 620, 285))
        self.gridLayout_9 = QGridLayout(self.cast_scroll_area)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.cast_layout = QHBoxLayout()
        self.cast_layout.setObjectName(u"cast_layout")

        self.gridLayout_9.addLayout(self.cast_layout, 0, 0, 1, 1)

        self.scrollArea_3.setWidget(self.cast_scroll_area)

        self.verticalLayout_3.addWidget(self.scrollArea_3)


        self.gridLayout_7.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.info_scrollarea)

        self.gridLayout_2.addWidget(self.scrollArea_2, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 5)
        self.show_edit_button = QPushButton(self.show_widget)
        self.show_edit_button.setObjectName(u"show_edit_button")

        self.horizontalLayout.addWidget(self.show_edit_button)

        self.line_2 = QFrame(self.show_widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.show_delete_button = QPushButton(self.show_widget)
        self.show_delete_button.setObjectName(u"show_delete_button")

        self.horizontalLayout.addWidget(self.show_delete_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.show_apply_button = QPushButton(self.show_widget)
        self.show_apply_button.setObjectName(u"show_apply_button")

        self.horizontalLayout.addWidget(self.show_apply_button)

        self.line_3 = QFrame(self.show_widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.show_cancel_button = QPushButton(self.show_widget)
        self.show_cancel_button.setObjectName(u"show_cancel_button")

        self.horizontalLayout.addWidget(self.show_cancel_button)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.show_widget)
        self.edit_widget = QWidget()
        self.edit_widget.setObjectName(u"edit_widget")
        self.gridLayout_3 = QGridLayout(self.edit_widget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.show_edit_image_label = QLabel(self.edit_widget)
        self.show_edit_image_label.setObjectName(u"show_edit_image_label")
        sizePolicy2.setHeightForWidth(self.show_edit_image_label.sizePolicy().hasHeightForWidth())
        self.show_edit_image_label.setSizePolicy(sizePolicy2)
        self.show_edit_image_label.setMinimumSize(QSize(180, 270))
        self.show_edit_image_label.setMaximumSize(QSize(180, 270))
        self.show_edit_image_label.setStyleSheet(u"QLabel {\n"
"    border: 1px solid white;   /* White border */\n"
"    border-radius: 6px;        /* Rounded corners (optional) */\n"
"    padding: 4px;              /* Space inside */\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.show_edit_image_label)

        self.show_edit_image_url = QLineEdit(self.edit_widget)
        self.show_edit_image_url.setObjectName(u"show_edit_image_url")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.show_edit_image_url.sizePolicy().hasHeightForWidth())
        self.show_edit_image_url.setSizePolicy(sizePolicy7)
        self.show_edit_image_url.setMaximumSize(QSize(180, 16777215))

        self.verticalLayout_5.addWidget(self.show_edit_image_url)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(30)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 20, -1)
        self.show_edit_name_line = QLineEdit(self.edit_widget)
        self.show_edit_name_line.setObjectName(u"show_edit_name_line")
        self.show_edit_name_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.show_edit_name_line)

        self.show_edit_time_line = QLineEdit(self.edit_widget)
        self.show_edit_time_line.setObjectName(u"show_edit_time_line")
        self.show_edit_time_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.show_edit_time_line)

        self.show_edit_date_line = QLineEdit(self.edit_widget)
        self.show_edit_date_line.setObjectName(u"show_edit_date_line")
        self.show_edit_date_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.show_edit_date_line)

        self.show_edit_gener_line = QLineEdit(self.edit_widget)
        self.show_edit_gener_line.setObjectName(u"show_edit_gener_line")
        self.show_edit_gener_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.show_edit_gener_line)

        self.show_edit_plot_line = QLineEdit(self.edit_widget)
        self.show_edit_plot_line.setObjectName(u"show_edit_plot_line")
        self.show_edit_plot_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.show_edit_plot_line)

        self.show_edit_imdb_rate_line = QLineEdit(self.edit_widget)
        self.show_edit_imdb_rate_line.setObjectName(u"show_edit_imdb_rate_line")
        self.show_edit_imdb_rate_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.show_edit_imdb_rate_line)

        self.show_edit_user_rate_line = QLineEdit(self.edit_widget)
        self.show_edit_user_rate_line.setObjectName(u"show_edit_user_rate_line")
        self.show_edit_user_rate_line.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.show_edit_user_rate_line)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 10)
        self.show_edit_apply_button = QPushButton(self.edit_widget)
        self.show_edit_apply_button.setObjectName(u"show_edit_apply_button")

        self.horizontalLayout_4.addWidget(self.show_edit_apply_button)

        self.show_edit_cancel_button = QPushButton(self.edit_widget)
        self.show_edit_cancel_button.setObjectName(u"show_edit_cancel_button")

        self.horizontalLayout_4.addWidget(self.show_edit_cancel_button)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.edit_widget)

        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 2, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_5 = QGridLayout(self.tab_2)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.tab_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_content.setObjectName(u"scroll_content")
        self.scroll_content.setGeometry(QRect(0, 0, 674, 668))
        self.gridLayout_6 = QGridLayout(self.scroll_content)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.watch_group = QGroupBox(self.scroll_content)
        self.watch_group.setObjectName(u"watch_group")
        font1 = QFont()
        font1.setPointSize(20)
        self.watch_group.setFont(font1)
        self.watch_group.setStyleSheet(u"QGroupBox {\n"
"    background-color: transparent;\n"
"    border: 1px solid #333;\n"
"    border-radius: 8px;\n"
"    margin-top: 40px;          /* space for the title */\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	\n"
"	image: url(:/icons/Icons/watch.png);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;    /* left title */\n"
"    padding: 0 5px;\n"
"    color: #cccccc;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.watch_group.setFlat(False)
        self.verticalLayout_11 = QVBoxLayout(self.watch_group)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.watch_button_1 = QPushButton(self.watch_group)
        self.watch_button_1.setObjectName(u"watch_button_1")
        self.watch_button_1.setFlat(False)

        self.verticalLayout_11.addWidget(self.watch_button_1)

        self.watch_button_2 = QPushButton(self.watch_group)
        self.watch_button_2.setObjectName(u"watch_button_2")

        self.verticalLayout_11.addWidget(self.watch_button_2)

        self.watch_button_3 = QPushButton(self.watch_group)
        self.watch_button_3.setObjectName(u"watch_button_3")

        self.verticalLayout_11.addWidget(self.watch_button_3)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_6)


        self.verticalLayout_10.addWidget(self.watch_group)

        self.download_group = QGroupBox(self.scroll_content)
        self.download_group.setObjectName(u"download_group")
        self.download_group.setFont(font1)
        self.download_group.setStyleSheet(u"QGroupBox {\n"
"    background-color: transparent;\n"
"    border: 1px solid #333;\n"
"    border-radius: 8px;\n"
"    margin-top: 40px;          /* space for the title */\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"	\n"
"	\n"
"	image: url(:/icons/Icons/download.png);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;    /* left title */\n"
"    padding: 0 5px;\n"
"    color: #cccccc;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.verticalLayout_12 = QVBoxLayout(self.download_group)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.download_button_1 = QPushButton(self.download_group)
        self.download_button_1.setObjectName(u"download_button_1")

        self.verticalLayout_12.addWidget(self.download_button_1)

        self.download_button_2 = QPushButton(self.download_group)
        self.download_button_2.setObjectName(u"download_button_2")

        self.verticalLayout_12.addWidget(self.download_button_2)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_8)


        self.verticalLayout_10.addWidget(self.download_group)


        self.gridLayout_6.addLayout(self.verticalLayout_10, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scroll_content)

        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(show)

        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(show)
    # setupUi

    def retranslateUi(self, show):
        show.setWindowTitle(QCoreApplication.translate("show", u"Form", None))
        self.show_image_lable.setText("")
        self.show_name_lable.setText(QCoreApplication.translate("show", u"Name", None))
        self.show_label.setText(QCoreApplication.translate("show", u"Date", None))
        self.show_gener_lable.setText(QCoreApplication.translate("show", u"Gener", None))
        self.label_3.setText("")
        self.show_user_rate_lable.setText(QCoreApplication.translate("show", u"User rate", None))
        self.show_plot_lable.setText("")
        self.label_5.setText(QCoreApplication.translate("show", u"Press to see the Plot", None))
        self.tmdb_icon_label.setText("")
        self.tmdb_rate.setText(QCoreApplication.translate("show", u"TMDB Rate", None))
        self.tmdb_votes.setText(QCoreApplication.translate("show", u"votes", None))
        self.rottentomato_icon_label.setText("")
        self.rotten_tomatos_rate.setText(QCoreApplication.translate("show", u"roten rate", None))
        self.show_trailer_lable.setText("")
        self.label_6.setText(QCoreApplication.translate("show", u"Press to see the Trailer", None))
        self.label_4.setText("")
        self.show_time_lable.setText(QCoreApplication.translate("show", u"Runtime", None))
        self.move_to_combobox.setPlaceholderText(QCoreApplication.translate("show", u"Move to", None))
        self.label_2.setText("")
        self.show_imdb_rate_lable.setText(QCoreApplication.translate("show", u"IMDBRate", None))
        self.imdb_votes.setText(QCoreApplication.translate("show", u"votes", None))
        self.metascore_icon_label.setText("")
        self.metascore_rate.setText(QCoreApplication.translate("show", u"meta rate", None))
        self.director_label.setText(QCoreApplication.translate("show", u"director Photo", None))
        self.director_name.setText(QCoreApplication.translate("show", u"Director name", None))
        self.show_edit_button.setText(QCoreApplication.translate("show", u"Edit", None))
        self.show_delete_button.setText(QCoreApplication.translate("show", u"Delete", None))
        self.show_apply_button.setText(QCoreApplication.translate("show", u"Apply", None))
        self.show_cancel_button.setText(QCoreApplication.translate("show", u"Cancel", None))
        self.show_edit_image_label.setText("")
        self.show_edit_image_url.setPlaceholderText(QCoreApplication.translate("show", u"   New image URL", None))
        self.show_edit_name_line.setPlaceholderText(QCoreApplication.translate("show", u"Name", None))
        self.show_edit_time_line.setText("")
        self.show_edit_time_line.setPlaceholderText(QCoreApplication.translate("show", u"Runtime", None))
        self.show_edit_date_line.setPlaceholderText(QCoreApplication.translate("show", u"Release", None))
        self.show_edit_gener_line.setPlaceholderText(QCoreApplication.translate("show", u"Genre", None))
        self.show_edit_plot_line.setPlaceholderText(QCoreApplication.translate("show", u"Plot", None))
        self.show_edit_imdb_rate_line.setPlaceholderText(QCoreApplication.translate("show", u"IMDB rate", None))
        self.show_edit_user_rate_line.setPlaceholderText(QCoreApplication.translate("show", u"User rate", None))
        self.show_edit_apply_button.setText(QCoreApplication.translate("show", u"Apply", None))
        self.show_edit_cancel_button.setText(QCoreApplication.translate("show", u"Cancel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("show", u"Info", None))
        self.watch_group.setTitle(QCoreApplication.translate("show", u"Watch                  ", None))
        self.watch_button_1.setText("")
        self.watch_button_2.setText("")
        self.watch_button_3.setText("")
        self.download_group.setTitle(QCoreApplication.translate("show", u"Download                         ", None))
        self.download_button_1.setText("")
        self.download_button_2.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("show", u"Find", None))
    # retranslateUi

