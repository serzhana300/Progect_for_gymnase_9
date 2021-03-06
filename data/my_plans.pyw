import os
import sqlite3
import func
from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 143)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 178, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.regs)
        self.pushButton_2.clicked.connect(self.log)
        self.pushButton_3.clicked.connect(self.pas_gen)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "???????? ?? ??????????????"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Login..."))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password..."))
        self.pushButton_2.setText(_translate("MainWindow", "????????"))
        self.pushButton.setText(_translate("MainWindow", "??????????????????????"))
        self.pushButton_3.setText(_translate("MainWindow", "?????????????????????????? ????????????"))

    def coding_pass(self, password):
        result = ""

        # transverse the plain txt
        for i in range(len(password)):
            char = password[i]
            # encypt_func uppercase characters in plain txt
            if char.isdigit():
                if int(char) + 9 >= 10:
                    result += str((int(char) + 9) % 10)
                else:
                    result += str(int(char) + 9)
            elif (char.isupper()):
                result += chr((ord(char) + 9 - 64) % 26 + 65)
                # encypt_func lowercase characters in plain txt
            else:
                result += chr((ord(char) + 9 - 96) % 26 + 97)
        return result

    def encoding_pass(self, password):
        result = ""

        # transverse the plain txt
        for i in range(len(password)):
            char = password[i]
            # encypt_func uppercase characters in plain txt
            if char.isdigit():
                if int(char) - 9 < 0:
                    result += str((int(char) + 10) - 9)
                result += str(int(char) - 9)
            elif (char.isupper()):
                result += chr((ord(char) - 9 - 64) % 26 + 65)
                # encypt_func lowercase characters in plain txt
            else:
                result += chr((ord(char) - 9 - 96) % 26 + 95)
        return result

    def check_passw(self, n):
        if len(n) < 8:
            self.statusbar.showMessage('???????????? ???????????? ???????????? 8 ??????.')
            self.statusbar.setStyleSheet('background-color:yellow')
            return False
        if len(set(n)) == 1:
            self.statusbar.showMessage('???????????? ?????????????? ???? ???????????? ??????????????.')
            self.statusbar.setStyleSheet('background-color:yellow')
            return False
        if len(n.split(' ')) > 1:
            self.statusbar.showMessage('???????????? ???????????????? ????????????.')
            self.statusbar.setStyleSheet('background-color:yellow')
            return False
        for i in n:
            if i in '????????????????????????????????????????????????????????????????':
                self.statusbar.showMessage('???????????? ???????????????? ?????????????? ??????????????.')
                self.statusbar.setStyleSheet('background-color:yellow')
                return False
            else:
                continue
        return True

    def pas_gen(self):
        self.lineEdit_2.setText(func.password_generate())

    def regs(self):
        logn = self.lineEdit.text()
        pasw = self.lineEdit_2.text()

        if func.check_edits(logn, pasw):
            if self.check_passw(pasw):
                coding_log = self.coding_pass(logn)
                coding_pas = self.coding_pass(pasw)
                con = sqlite3.connect('data/users.db')
                cur = con.cursor()
                cur.execute(f'SELECT * FROM users WHERE login="{coding_log}"')
                value = cur.fetchall()
                if value != []:
                    self.statusbar.showMessage('?????????? ???????????????????????? ?????? ????????????????????????, ?????????????? ????????????.')
                    self.statusbar.setStyleSheet('background-color:yellow')
                else:
                    cur.execute(f'''INSERT INTO users (login, passwords) VALUES ('{coding_log}', '{coding_pas}')''')
                    self.statusbar.showMessage('???? ?????????????? ????????????????????????????????!')
                    self.statusbar.setStyleSheet('background-color:green')
                    con.commit()

                cur.close()
                con.close()
        else:
            self.statusbar.showMessage('?????????????????? ???????????????????? ??????????')
            self.statusbar.setStyleSheet('background-color:yellow')

    def log(self):
        logn = self.lineEdit.text()
        pasw = self.lineEdit_2.text()
        if self.check_passw(pasw):
            if func.check_edits(logn, pasw):
                coding_log = self.coding_pass(logn)
                coding_pas = self.coding_pass(pasw)
                con = sqlite3.connect('data/users.db')
                cur = con.cursor()

                cur.execute(f'SELECT * FROM users WHERE login="{coding_log}";')
                value = cur.fetchall()

                if value != [] and value[0][2] == coding_pas:
                    with open('data/cash/online_cash.txt', mode='w+', encoding='utf-8') as file_cash:
                        file_cash.write(f'{logn}')
                    os.chdir('data')
                    os.system('programm_itog.exe')
                    exit()
                else:
                    self.statusbar.showMessage('?????????????????? ?????????? ?????? ????????????.')
                    self.statusbar.setStyleSheet('background-color:red')

                cur.close()
                con.close()
            else:
                self.statusbar.showMessage('?????????????????? ???????????????????? ??????????')
                self.statusbar.setStyleSheet('background-color:yellow')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
