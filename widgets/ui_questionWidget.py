from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtGui import QFont  
from PySide6.QtWidgets import QComboBox, QLabel, QPushButton, QVBoxLayout, QWidget

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

