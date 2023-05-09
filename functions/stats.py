import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from csv import DictReader, DictWriter

#Import Statements
cs=0
tot=0

def read_file():
    with open('wdata.csv', 'r') as f:
        read=DictReader(f)
        data=[i for i in read]
    return data

#Reads the file of the user inputs and takes all necessary data.
def write(data,filename):
    q=data[0].keys()
    with open(filename,'w',newline='') as y:
        writ=DictWriter(y,q)
        writ.writeheader()
        for i in data:
            writ.writerow(i)

#Writes the data from the user inputs' file and converts it to stats.
def current_streak(s):
    global cs
    cs+=1
    s['Streak']=cs

#Gets current streak and is declared globally within class.
def total(s):
    global tot
    tot+=1
    s['Total']=tot

#Gets total entries and is declared globally within class.
class SubWindow(QWidget):
    global tot
    global cs
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Workout Stats")
        self.resize(500, 350)
        x=str(cs)
        y=str(tot)
        self.x=x
        self.y=y
        self.excel()
        self.show()

#Initializes the class and how it's sized.
    def excel(self):
        self.sheet= QTableWidget(1, 2)
        self.sheet.setHorizontalHeaderLabels(["Current Streak","Overall"])
        self.sheet.setItem(0,0, QTableWidgetItem(self.x))
        self.sheet.setItem(0,1, QTableWidgetItem(self.y))
        self.sheet.setColumnWidth(0, 100)
        self.box=QVBoxLayout()
        self.box.addWidget(self.sheet)
        self.setLayout(self.box)

#Creates the table, headers, and all necessary information.
def run():
    stat=read_file()
    for i in stat:
        total(i)
        current_streak(i)
    e=write(stat,'stats.csv')
    app = QApplication(sys.argv)
    subwindow = SubWindow()
    sys.exit(app.exec())

#Runs all necessary functions.
if __name__ == '__main__':
    run()
