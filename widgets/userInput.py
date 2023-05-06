#!/usr/bin/env python3

# IMPORTS
from PySide6.QtCore import Qt 
from PySide6.QtWidgets import QWidget
from ui_userInput import Ui_userInput

# Initiate userInput class
class userInput(QWidget, Ui_userInput):
    def __init__(self):
        # Grabs the parent functions
        super().__init__()

        # Set up window
        self.setupUi(self)
        self.setWindowTitle('User Input')