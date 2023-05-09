from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QVBoxLayout

class Ui_fitnessDay(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(521, 202)
        font = QFont()
        font.setFamilies([u"Arial"])
        Form.setFont(font)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(25)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.oneDayButton = QPushButton(Form)
        self.oneDayButton.setObjectName(u"oneDayButton")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(21)
        self.oneDayButton.setFont(font2)

        self.horizontalLayout.addWidget(self.oneDayButton)

        self.twoDayButton = QPushButton(Form)
        self.twoDayButton.setObjectName(u"twoDayButton")
        self.twoDayButton.setFont(font2)

        self.horizontalLayout.addWidget(self.twoDayButton)

        self.threeDayButton = QPushButton(Form)
        self.threeDayButton.setObjectName(u"threeDayButton")
        self.threeDayButton.setFont(font2)

        self.horizontalLayout.addWidget(self.threeDayButton)

        self.fourDayButton = QPushButton(Form)
        self.fourDayButton.setObjectName(u"fourDayButton")
        self.fourDayButton.setFont(font2)

        self.horizontalLayout.addWidget(self.fourDayButton)

        self.fiveDayButton = QPushButton(Form)
        self.fiveDayButton.setObjectName(u"fiveDayButton")
        self.fiveDayButton.setFont(font2)

        self.horizontalLayout.addWidget(self.fiveDayButton)

        self.sixDayButton = QPushButton(Form)
        self.sixDayButton.setObjectName(u"sixDayButton")
        self.sixDayButton.setFont(font2)

        self.horizontalLayout.addWidget(self.sixDayButton)

        self.sevenDayButton = QPushButton(Form)
        self.sevenDayButton.setObjectName(u"sevenDayButton")
        self.sevenDayButton.setFont(font2)

        self.horizontalLayout.addWidget(self.sevenDayButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Welcome!", None))
        self.label.setText(QCoreApplication.translate("Form", u"How many days would you like to workout?", None))
        self.oneDayButton.setText(QCoreApplication.translate("Form", u"1", None))
        self.twoDayButton.setText(QCoreApplication.translate("Form", u"2", None))
        self.threeDayButton.setText(QCoreApplication.translate("Form", u"3", None))
        self.fourDayButton.setText(QCoreApplication.translate("Form", u"4", None))
        self.fiveDayButton.setText(QCoreApplication.translate("Form", u"5", None))
        self.sixDayButton.setText(QCoreApplication.translate("Form", u"6", None))
        self.sevenDayButton.setText(QCoreApplication.translate("Form", u"7", None))
    # retranslateUi

