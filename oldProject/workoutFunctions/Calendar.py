import sys
from PySide6.QtWidgets import QWidget, QCalendarWidget, QLabel, QApplication, QHBoxLayout, QMainWindow, QListWidget, QPushButton, QVBoxLayout, QLineEdit
from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve, Qt

class calendar(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.initUI()

    def initUI(self):

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        layout = QHBoxLayout(centralWidget)

        cal = QCalendarWidget()
        date = cal.selectedDate()
        cal.setGridVisible(True)
        cal.setStyleSheet("background-color : darkgray;")
        cal.clicked.connect(self.showDate)

        layout.addWidget(cal)

        # create a QVBoxLayout for the textbox and submit button
        vbox = QVBoxLayout()

        self.textbox = QLineEdit()
        self.textbox.setPlaceholderText("Enter your text")
        self.textbox.setFixedSize(200, 50)
        vbox.addWidget(self.textbox)

        self.submit = QPushButton("Submit", self)
        vbox.addWidget(self.submit)
        vbox.setAlignment(Qt.AlignBottom)

        # add the QVBoxLayout to the QHBoxLayout
        layout.addLayout(vbox)

        self.date_lbl = QLabel(self)
        date = cal.selectedDate()
        font = self.date_lbl.font()
        font.setPointSize(14)
        self.date_lbl.setFont(font)
        self.date_lbl.setText(date.toString())
        self.date_lbl.setFixedSize(5000, 20)
        self.date_lbl.move(440, 60)

        centralWidget.setLayout(layout)

        self.setGeometry(600, 200, 650, 400)
        self.setWindowTitle('Calendar')
        self.show()


    def showDate(self, date):
        self.date_lbl.setText(date.toString())

    def show_new_window(self, checked):
        self.w = workout_help()
        self.w.show()

class workout_help(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("AAAAAAAAAAAAA")
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.setGeometry(300, 100, 400, 400)
        self.setWindowTitle('Bench Press')
        self.show()


def main():

    app = QApplication(sys.argv)
    ca = calendar()
    ca.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
