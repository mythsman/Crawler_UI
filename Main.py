import sys
from  PyQt5 import QtWidgets
from Ui_Window import Ui_MainWindow
from LoginDialog import LoginDialog
from SignUpDialog import SignUpDialog
from HelpDialog import HelpDialog
from AboutDialog import AboutDialog
from UpdateDialog import UpdateDialog

class Main(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.label_2.setText("请登录。。。")
        self.tabWidget.setEnabled(False)
        self.action_login.triggered.connect(self.loginSlot)
        self.action_signin.triggered.connect(self.signUpSlot)
        self.action_help.triggered.connect(self.helpSlot)
        self.action_about.triggered.connect(self.aboutSlot)
        self.action_update.triggered.connect(self.updateSlot)
        self.show()

    def updateSlot(self):
        UpdateDialog().exec()

    def aboutSlot(self):
        AboutDialog().exec()

    def helpSlot(self):
        HelpDialog().exec()

    def loginSlot(self):
        res=LoginDialog().work()
        if res :
            self.tabWidget.setEnabled(True)
            self.label_2.setText("欢迎登陆，"+res)

    def signUpSlot(self):
        res=SignUpDialog().work()

app = QtWidgets.QApplication(sys.argv)
main = Main()
sys.exit(app.exec_())
