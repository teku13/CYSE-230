#!/usr/bin/env python3

# IMPORTS
from PySide6.QtCore import Qt 
from PySide6.QtWidgets import QWidget
from widgets.ui_fitnessGoals import Ui_fitnessGoalQuestion

# Initiate userInput class
class fitnessGoalsQuestionWidget(QWidget, Ui_fitnessGoalQuestion):
    def __init__(self):
        # Grabs the parent functions
        super().__init__()

        # Set up window
        self.setupUi(self)
        
    