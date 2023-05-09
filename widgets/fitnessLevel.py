#!/usr/bin/env python3
# Author: Tony Nguyen
# IMPORTS
from PySide6.QtWidgets import QWidget
from widgets.ui_fitnessLevel import Ui_fitnessLevelQuestion

# Initiate userInput class
class fitnessLevelWidget(QWidget, Ui_fitnessLevelQuestion):
    def __init__(self):
        # Grabs the parent functions
        super().__init__()

        # Set up window
        self.setupUi(self)
        self.Submit.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        if self.beginnerRadio.isChecked() or self.intermediateRadio.isChecked() or self.athleteRadio.isChecked():
            file = open('newUserData/workoutplan.txt', 'a')
            if self.beginnerRadio.isChecked():
                file.write('beginner\n')
            if self.intermediateRadio.isChecked():
                file.write('intermediate\n')
            if self.athleteRadio.isChecked():
                file.write('athlete\n')
            file.close()
            self.closeEvent()
            self.exit()

def startFitnessLevelWidget():
    import sys
    from PySide6 import QtWidgets
    app = QtWidgets.QApplication(sys.argv)
    window = fitnessLevelWidget()
    window.show()
    app.exec()