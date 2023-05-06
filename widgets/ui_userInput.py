# IMPORTS
from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QRadioButton, QWidget

class Ui_userInput(object):
    def setupUi(self, userInput):
        if not userInput.objectName():
            userInput.setObjectName(u"userInput")
        userInput.resize(480, 465)
        self.pushButton = QPushButton(userInput)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(339, 400, 131, 51))
        font = QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.lineEdit = QLineEdit(userInput)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 70, 461, 261))
        font1 = QFont()
        font1.setPointSize(25)
        self.lineEdit.setFont(font1)
        self.lineEdit.setMaxLength(32767)
        self.lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.widget = QWidget(userInput)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 461, 41))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.streakLabel = QLabel(self.widget)
        self.streakLabel.setObjectName(u"streakLabel")
        self.streakLabel.setEnabled(True)
        font2 = QFont()
        font2.setPointSize(30)
        font2.setBold(True)
        self.streakLabel.setFont(font2)

        self.horizontalLayout.addWidget(self.streakLabel)

        self.dayLabel = QLabel(self.widget)
        self.dayLabel.setObjectName(u"dayLabel")
        self.dayLabel.setEnabled(True)
        font3 = QFont()
        font3.setPointSize(30)
        self.dayLabel.setFont(font3)
        self.dayLabel.setAlignment(Qt.AlignRight) # Delete just in case if issues
        self.dayLabel.setLayoutDirection(Qt.LeftToRight)
        self.dayLabel.setAutoFillBackground(False)
        self.dayLabel.setTextFormat(Qt.PlainText)
        self.dayLabel.setMargin(0)

        self.horizontalLayout.addWidget(self.dayLabel)

        self.widget1 = QWidget(userInput)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 350, 469, 35))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.widget1)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget1)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.widget1)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.radioButton_3)


        self.retranslateUi(userInput)

        QMetaObject.connectSlotsByName(userInput)
    # setupUi

    def retranslateUi(self, userInput):
        userInput.setWindowTitle(QCoreApplication.translate("userInput", u"User Input", None))
        self.pushButton.setText(QCoreApplication.translate("userInput", u"Submit", None))
        self.lineEdit.setInputMask("")
        # self.lineEdit.setText(QCoreApplication.translate("userInput", u"Type your workout here", None))
        self.streakLabel.setText(QCoreApplication.translate("userInput", u"Day X", None))
        self.dayLabel.setText(QCoreApplication.translate("userInput", u"MONTH DAY, YEAR", None))
        self.radioButton.setText(QCoreApplication.translate("userInput", u"Upper Body", None))
        self.radioButton_2.setText(QCoreApplication.translate("userInput", u"Lower Body", None))
        self.radioButton_3.setText(QCoreApplication.translate("userInput", u"Rest Day", None))
    # retranslateUi

