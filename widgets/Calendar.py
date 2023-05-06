import sys
from PySide6.QtWidgets import QWidget, QCalendarWidget, QLabel, QApplication, QToolBar, QHBoxLayout, QMainWindow, QListWidget, QPushButton, QVBoxLayout, QSizePolicy
from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve, QParallelAnimationGroup

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

        self.toolbar = QToolBar()
        self.toolbar.setStyleSheet("background-color : lightgray;")
        self.toolbar.setFixedSize(150, 110)

        button_widget = QWidget(self.toolbar)
        button_layout = QVBoxLayout(button_widget)
        self.workouts_label = QLabel('Workouts for today: ')

        self.bench_press_button = QPushButton('Bench Press 3x8', button_widget)
        self.bench_press_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.tricep_pushdown_button = QPushButton('Tricep Pushdown 3x12', button_widget)
        self.tricep_pushdown_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.incline_bench_button = QPushButton('Incline Bench 4x8', button_widget)
        self.incline_bench_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        button_layout.addWidget(self.workouts_label)
        button_layout.addWidget(self.bench_press_button)
        button_layout.addWidget(self.tricep_pushdown_button)
        button_layout.addWidget(self.incline_bench_button)
        button_widget.setLayout(button_layout)
        self.toolbar.addWidget(button_widget)

        self.bench_press_button.clicked.connect(self.show_new_window)

        self.anim = QPropertyAnimation(button_widget, b"pos")
        self.anim.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim.setStartValue(QPoint(400, 0))
        self.anim.setDuration(1500)
        self.anim.start()

        self.date_lbl = QLabel(self)
        date = cal.selectedDate()
        font = self.date_lbl.font()
        font.setPointSize(14)
        self.date_lbl.setFont(font)
        self.date_lbl.setText(date.toString())
        self.date_lbl.setFixedSize(5000, 20)
        self.date_lbl.move(440, 60)

        self.anim2 = QPropertyAnimation(self.date_lbl, b"pos")
        self.anim2.setEasingCurve(QEasingCurve.InOutCubic)
        self.anim2.setStartValue(QPoint(620, 60))
        self.anim2.setDuration(1300)
        self.anim2.start()

        layout.addWidget(self.toolbar)
        centralWidget.setLayout(layout)

        self.setGeometry(600, 200, 600, 400)
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

    sys.exit(app.exec())
