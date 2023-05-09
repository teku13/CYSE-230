# IMPORTS
from PySide6.QtCore import Qt 
from PySide6.QtWidgets import QWidget
from widgets.ui_fitnessLevel import Ui_fitnessLevelQuestion

# Initiate userInput class
class fitnessLevelWidget(QWidget, Ui_fitnessLevelQuestion):
    def __init__(self):
        # Grabs the parent functions
        super().__init__()

        # Set up window
        self.setupUi(self)
