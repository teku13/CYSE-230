from PySide6.QtCore import Qt 
from PySide6.QtWidgets import QWidget
from questionsWidget.ui_questionWidget import Ui_questionsWidget

class QuestionWidget(QWidget, Ui_questionsWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('New User')
        