# IMPORTS
from PySide6.QtCore import Qt 
from PySide6.QtWidgets import QWidget
from widgets.ui_fitnessDay import Ui_fitnessDay

# Initiate userInput class
class fitnessDayWidget(QWidget, Ui_fitnessDay):
    def __init__(self):
        # Grabs the parent functions
        super().__init__()

        # Set up window
        self.setupUi(self)
