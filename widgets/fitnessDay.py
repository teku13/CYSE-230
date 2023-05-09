#!/usr/bin/env python3
# Author: Tony Nguyen
# IMPORTS
from PySide6.QtWidgets import QWidget
from widgets.ui_fitnessDay import Ui_fitnessDay

# Initiate userInput class
class fitnessDayWidget(QWidget, Ui_fitnessDay):
    def __init__(self):
        # Grabs the parent functions
        super().__init__()

        # Set up window
        self.setupUi(self)
        self.file = open('newUserData/workoutplan.txt', 'a')
        self.oneDayButton.clicked.connect(self.buttonOneClicked)
        self.twoDayButton.clicked.connect(self.buttonTwoClicked)
        self.threeDayButton.clicked.connect(self.buttonThreeClicked)
        self.fourDayButton.clicked.connect(self.buttonFourClicked)
        self.fiveDayButton.clicked.connect(self.buttonFiveClicked)
        self.sixDayButton.clicked.connect(self.buttonSixClicked)
        self.sevenDayButton.clicked.connect(self.buttonSevenClicked)
        
    def buttonOneClicked(self):
        self.file.write('1\n')
        self.file.close()
        self.closeEvent()
        self.close()

    def buttonTwoClicked(self):
        self.file.write('2\n')
        self.file.close()
        self.close()

    def buttonThreeClicked(self):
        self.file.write('3\n')
        self.file.close()
        self.close()

    def buttonFourClicked(self):
        self.file.write('4\n')
        self.file.close()
        self.close()

    def buttonFiveClicked(self):
        self.file.write('5\n')
        self.file.close()
        self.close()

    def buttonSixClicked(self):
        self.file.write('6\n')
        self.file.close()
        self.close()

    def buttonSevenClicked(self):
        self.file.write('7\n')
        self.file.close()
        self.close()

def startFitnessDayWidget():
    import sys
    from PySide6 import QtWidgets
    app = QtWidgets.QApplication(sys.argv)
    window = fitnessDayWidget()
    window.show()
    app.exec()