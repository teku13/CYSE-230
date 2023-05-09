from PySide6.QtCore import QCoreApplication, QMetaObject,Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import  QHBoxLayout, QLabel, QPushButton, QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout

class Ui_fitnessGoalQuestion(object):
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
        self.bodybuildingRadio = QRadioButton(fitnessGoalQuestion)
        self.bodybuildingRadio.setObjectName(u"bodybuildingRadio")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(20)
        self.bodybuildingRadio.setFont(font2)

        self.horizontalLayout.addWidget(self.bodybuildingRadio)

        self.powerliftingRadio = QRadioButton(fitnessGoalQuestion)
        self.powerliftingRadio.setObjectName(u"powerliftingRadio")
        self.powerliftingRadio.setFont(font2)

        self.horizontalLayout.addWidget(self.powerliftingRadio)

        self.crossfitRadio = QRadioButton(fitnessGoalQuestion)
        self.crossfitRadio.setObjectName(u"crossfitRadio")
        self.crossfitRadio.setFont(font2)

        self.horizontalLayout.addWidget(self.crossfitRadio)


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


    def retranslateUi(self, fitnessGoalQuestion):
        fitnessGoalQuestion.setWindowTitle(QCoreApplication.translate("fitnessGoalQuestion", u"Welcome!", None))
        self.label.setText(QCoreApplication.translate("fitnessGoalQuestion", u"What are your fitness goals?", None))
        self.bodybuildingRadio.setText(QCoreApplication.translate("fitnessGoalQuestion", u"Bodybuilding", None))
        self.powerliftingRadio.setText(QCoreApplication.translate("fitnessGoalQuestion", u"Powerlifting", None))
        self.crossfitRadio.setText(QCoreApplication.translate("fitnessGoalQuestion", u"CrossFit", None))
        self.Submit.setText(QCoreApplication.translate("fitnessGoalQuestion", u"Submit", None))