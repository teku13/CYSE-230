#!/usr/bin/env python3
# Author: Tony Nguyen
# IMPORTS
from PySide6.QtWidgets import QWidget
from .ui_fitnessGoals import Ui_fitnessGoalQuestion

# Initiate userInput class
class fitnessGoalsQuestionWidget(QWidget, Ui_fitnessGoalQuestion):
    def __init__(self):
        # Grabs the parent functions
        super().__init__()

        # Set up window
        self.setupUi(self)
        self.Submit.clicked.connect(self.buttonClicked)
        
    def buttonClicked(self):
        if self.bodybuildingRadio.isChecked() or self.powerliftingRadio.isChecked() or self.crossfitRadio.isChecked():
            file = open('newUserData/workoutplan.txt', 'w')
            if self.bodybuildingRadio.isChecked():
                file.write('bodybuilding\n')
            if self.powerliftingRadio.isChecked():
                file.write('powerlifting\n')
            if self.crossfitRadio.isChecked():
                file.write('crossfit\n')
            file.close()
            super().close()
            self.closeEvent()

def startFitnessGoalsWidget():
    import sys
    from PySide6 import QtWidgets
    app = QtWidgets.QApplication(sys.argv)
    window = fitnessGoalsQuestionWidget()
    window.show()
    app.exec()
