# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fitnessGoals.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_fitnessLevelQuestion(object):
    def setupUi(self, fitnessGoalQuestion):
        if not fitnessGoalQuestion.objectName():
            fitnessGoalQuestion.setObjectName(u"fitnessGoalQuestion")
        fitnessGoalQuestion.resize(480, 202)
        font = QFont()
        font.setFamilies([u"Arial"])
        fitnessGoalQuestion.setFont(font)
        self.verticalLayout = QVBoxLayout(fitnessGoalQuestion)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(fitnessGoalQuestion)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(26)
        self.label.setFont(font1)
        self.label.setTextFormat(Qt.PlainText)
        self.label.setWordWrap(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.beginnerRadio = QRadioButton(fitnessGoalQuestion)
        self.beginnerRadio.setObjectName(u"beginnerRadio")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(20)
        self.beginnerRadio.setFont(font2)

        self.horizontalLayout.addWidget(self.beginnerRadio)

        self.intermediateRadio = QRadioButton(fitnessGoalQuestion)
        self.intermediateRadio.setObjectName(u"intermediateRadio")
        self.intermediateRadio.setFont(font2)

        self.horizontalLayout.addWidget(self.intermediateRadio)

        self.athleteRadio = QRadioButton(fitnessGoalQuestion)
        self.athleteRadio.setObjectName(u"athleteRadio")
        self.athleteRadio.setFont(font2)

        self.horizontalLayout.addWidget(self.athleteRadio)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.Submit = QPushButton(fitnessGoalQuestion)
        self.Submit.setObjectName(u"Submit")

        self.horizontalLayout_2.addWidget(self.Submit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(fitnessGoalQuestion)

        QMetaObject.connectSlotsByName(fitnessGoalQuestion)
    # setupUi

    def retranslateUi(self, fitnessGoalQuestion):
        fitnessGoalQuestion.setWindowTitle(QCoreApplication.translate("fitnessGoalQuestion", u"Welcome!", None))
        self.label.setText(QCoreApplication.translate("fitnessGoalQuestion", u"What level are you?", None))
        self.beginnerRadio.setText(QCoreApplication.translate("fitnessGoalQuestion", u"Beginner", None))
        self.intermediateRadio.setText(QCoreApplication.translate("fitnessGoalQuestion", u"Intermediate", None))
        self.athleteRadio.setText(QCoreApplication.translate("fitnessGoalQuestion", u"Athlete", None))
        self.Submit.setText(QCoreApplication.translate("fitnessGoalQuestion", u"Submit", None))
    # retranslateUi

