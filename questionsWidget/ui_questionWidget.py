# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'questions.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_questionsWidget(object):
    def setupUi(self, questionsWidget):
        if not questionsWidget.objectName():
            questionsWidget.setObjectName(u"questionsWidget")
        questionsWidget.resize(480, 200)
        self.widget = QWidget(questionsWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 461, 171))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.questionLabel = QLabel(self.widget)
        self.questionLabel.setObjectName(u"questionLabel")
        font = QFont()
        font.setPointSize(25)
        self.questionLabel.setFont(font)

        self.verticalLayout.addWidget(self.questionLabel)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.submitButton = QPushButton(self.widget)
        self.submitButton.setObjectName(u"submitButton")

        self.verticalLayout.addWidget(self.submitButton)


        self.retranslateUi(questionsWidget)

        QMetaObject.connectSlotsByName(questionsWidget)
    # setupUi

    def retranslateUi(self, questionsWidget):
        questionsWidget.setWindowTitle(QCoreApplication.translate("questionsWidget", u"Form", None))
        self.questionLabel.setText(QCoreApplication.translate("questionsWidget", u"[INSERT QUESTION HERE]", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("questionsWidget", u"INSERT ANSWER 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("questionsWidget", u"INSERT ANSWER 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("questionsWidget", u"INSERT ANSWER 3", None))

        self.submitButton.setText(QCoreApplication.translate("questionsWidget", u"Submit", None))
    # retranslateUi

