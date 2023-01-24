# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tulip_predictor.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(506, 222)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.petal_length_lineedit = QLineEdit(self.centralwidget)
        self.petal_length_lineedit.setObjectName(u"petal_length_lineedit")
        self.petal_length_lineedit.setGeometry(QRect(130, 10, 113, 31))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(16)
        self.petal_length_lineedit.setFont(font)
        self.petal_length_label = QLabel(self.centralwidget)
        self.petal_length_label.setObjectName(u"petal_length_label")
        self.petal_length_label.setGeometry(QRect(10, 10, 108, 31))
        self.petal_length_label.setMinimumSize(QSize(0, 31))
        self.petal_length_label.setMaximumSize(QSize(16777215, 31))
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.petal_length_label.setFont(font1)
        self.petal_width_label = QLabel(self.centralwidget)
        self.petal_width_label.setObjectName(u"petal_width_label")
        self.petal_width_label.setGeometry(QRect(10, 50, 102, 31))
        self.petal_width_label.setMinimumSize(QSize(0, 31))
        self.petal_width_label.setMaximumSize(QSize(16777215, 31))
        self.petal_width_label.setFont(font1)
        self.sepal_length_label = QLabel(self.centralwidget)
        self.sepal_length_label.setObjectName(u"sepal_length_label")
        self.sepal_length_label.setGeometry(QRect(260, 10, 111, 31))
        self.sepal_length_label.setMinimumSize(QSize(0, 31))
        self.sepal_length_label.setMaximumSize(QSize(16777215, 31))
        self.sepal_length_label.setFont(font1)
        self.sepal_width_label = QLabel(self.centralwidget)
        self.sepal_width_label.setObjectName(u"sepal_width_label")
        self.sepal_width_label.setGeometry(QRect(260, 50, 105, 31))
        self.sepal_width_label.setMinimumSize(QSize(0, 31))
        self.sepal_width_label.setMaximumSize(QSize(16777215, 31))
        self.sepal_width_label.setFont(font1)
        self.petal_width_lineedit = QLineEdit(self.centralwidget)
        self.petal_width_lineedit.setObjectName(u"petal_width_lineedit")
        self.petal_width_lineedit.setGeometry(QRect(120, 50, 113, 31))
        self.petal_width_lineedit.setFont(font)
        self.sepal_length_lineedit = QLineEdit(self.centralwidget)
        self.sepal_length_lineedit.setObjectName(u"sepal_length_lineedit")
        self.sepal_length_lineedit.setGeometry(QRect(380, 10, 113, 31))
        self.sepal_length_lineedit.setFont(font)
        self.sepal_width_lineedit = QLineEdit(self.centralwidget)
        self.sepal_width_lineedit.setObjectName(u"sepal_width_lineedit")
        self.sepal_width_lineedit.setGeometry(QRect(370, 50, 113, 31))
        self.sepal_width_lineedit.setFont(font)
        self.prediction_label = QLabel(self.centralwidget)
        self.prediction_label.setObjectName(u"prediction_label")
        self.prediction_label.setGeometry(QRect(120, 150, 94, 31))
        self.prediction_label.setMinimumSize(QSize(0, 31))
        self.prediction_label.setMaximumSize(QSize(16777215, 31))
        self.prediction_label.setFont(font1)
        self.predict_button = QPushButton(self.centralwidget)
        self.predict_button.setObjectName(u"predict_button")
        self.predict_button.setGeometry(QRect(190, 100, 108, 34))
        self.predict_button.setFont(font1)
        self.result_label = QLabel(self.centralwidget)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setGeometry(QRect(220, 150, 139, 31))
        self.result_label.setMinimumSize(QSize(0, 31))
        self.result_label.setMaximumSize(QSize(16777215, 31))
        self.result_label.setFont(font1)
        self.accuracy_label = QLabel(self.centralwidget)
        self.accuracy_label.setObjectName(u"accuracy_label")
        self.accuracy_label.setGeometry(QRect(420, 190, 45, 13))
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(8)
        font2.setBold(True)
        self.accuracy_label.setFont(font2)
        self.accuracy_score = QLabel(self.centralwidget)
        self.accuracy_score.setObjectName(u"accuracy_score")
        self.accuracy_score.setGeometry(QRect(470, 190, 45, 13))
        self.accuracy_score.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tulip Species Predictor", None))
        self.petal_length_label.setText(QCoreApplication.translate("MainWindow", u"Petal Length", None))
        self.petal_width_label.setText(QCoreApplication.translate("MainWindow", u"Petal Width", None))
        self.sepal_length_label.setText(QCoreApplication.translate("MainWindow", u"Sepal Length", None))
        self.sepal_width_label.setText(QCoreApplication.translate("MainWindow", u"Sepal Width", None))
        self.prediction_label.setText(QCoreApplication.translate("MainWindow", u"Prediction:", None))
        self.predict_button.setText(QCoreApplication.translate("MainWindow", u"Predict", None))
        self.result_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.accuracy_label.setText(QCoreApplication.translate("MainWindow", u"Accuracy:", None))
        self.accuracy_score.setText(QCoreApplication.translate("MainWindow", u"-", None))
    # retranslateUi

