import sys
from PySide6.QtWidgets import QWidget, QCalendarWidget, QLabel, QApplication, QToolBar
from PySide6.QtCore import Qt

class calendar(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.initUI()

    def initUI(self):

        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(100, 40)
        cal.setStyleSheet("background-color : lightblue;")
        cal.clicked.connect(self.showDate)
        cal.clicked.connect(self.dispworkouts)

        self.toolbar = QToolBar(self)
        self.toolbar.setStyleSheet("background-color : lightgray;")
        self.toolbar.move(400, 40)
        self.toolbar.setFixedSize(150, 195)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.setFixedSize(5000, 20)
        self.lbl.move(405, 40)

        self.setGeometry(600, 200, 600, 400)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())


    def dispworkouts(self):
        workouts = QLabel('Workouts: \nBench Press 3x8 \nTricep Pushdown 3x12 \nIncline Bench 4x8 \n', self)
        self.toolbar.addWidget(workouts)

def main():

    app = QApplication(sys.argv)
    ca = calendar()
    ca.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
