from PySide6.QtCore import QObject, Slot, Signal

class MainWindow(QObject):
    def __init__(self):
        QObject.__init__(self)

    staticUser = "admin"
    staticPass = "password"

    signalUser = Signal(str)
    signalPass = Signal(str)
    signalLogin = Signal(bool)

    @Slot(str, str)
    def checkLogin(self, getUser, getPass):
        if(self.staticUser.lower() == getUser.lower() and self.staticPass == getPass):
            self.signalUser.emit("Username: " + getUser)
            self.signalPass.emit("Password: " + getPass)
            self.signalLogin.emit(True)

            print("Login passed!")
        else:
            self.signalLogin.emit(False)

            print("Login error!")

    # @Slot(str, str)
    def registerAccount(self, getUser, getPass):
        raise NotImplementedError
    