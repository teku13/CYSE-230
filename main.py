#!/usr/bin/python3
# from Calendar import main

# if __name__ == "__main__":
#     main

import sys

from PySide6 import QtWidgets
from userInput import userInput

app = QtWidgets.QApplication(sys.argv)
window = userInput()
window.show()

app.exec()