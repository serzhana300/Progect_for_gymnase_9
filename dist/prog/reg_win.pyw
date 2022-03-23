import os
import sqlite3
import func
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(260, 140)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setObjectName("login")
        self.verticalLayout.addWidget(self.login)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.opening = QtWidgets.QPushButton(self.centralwidget)
        self.opening.setObjectName("opening")
        self.verticalLayout.addWidget(self.opening)
        self.registration = QtWidgets.QPushButton(self.centralwidget)
        self.registration.setObjectName("registration")
        self.verticalLayout.addWidget(self.registration)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 242, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.registration.clicked.connect(self.regs)
        self.opening.clicked.connect(self.log)

    def regs(self):
        logn = self.login.text()
        pasw = self.password.text()
        if func.check_edits(logn, pasw):
            con = sqlite3.connect('users.db')
            cur = con.cursor()

            cur.execute(f'SELECT * FROM users WHERE login="{logn}";')
            value = cur.fetchall()

            if value != []:
                self.statusbar.showMessage('Такой пользователь уже используется, введите пароль.')
                self.statusbar.setStyleSheet('background-color:yellow')
            else:
                cur.execute(f"INSERT INTO users (login, passwords) VALUES ('{logn}', '{pasw}')")
                self.statusbar.showMessage('Вы успешно зарегистрированы!')
                self.statusbar.setStyleSheet('background-color:green')
                con.commit()

            cur.close()
            con.close()
        else:
            self.statusbar.showMessage('Проверьте заполнение полей')
            self.statusbar.setStyleSheet('background-color:yellow')

    def log(self):
        logn = self.login.text()
        pasw = self.password.text()
        if func.check_edits(logn, pasw):
            con = sqlite3.connect('users.db')
            cur = con.cursor()

            cur.execute(f'SELECT * FROM users WHERE login="{logn}";')
            value = cur.fetchall()

            if value != [] and value[0][2] == pasw:
                with open('online_cash.txt', mode='w+', encoding='utf-8') as file_cash:
                    file_cash.write(f'{logn}\n')
                os.system('mmm.py')
                exit()
            else:
                self.statusbar.showMessage('Проверьте логин или пароль.')
                self.statusbar.setStyleSheet('background-color:red')

            cur.close()
            con.close()
        else:
            self.statusbar.showMessage('Проверьте заполнение полей')
            self.statusbar.setStyleSheet('background-color:yellow')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Вход в систему"))
        self.login.setPlaceholderText(_translate("MainWindow", "Login.."))
        self.password.setPlaceholderText(_translate("MainWindow", "Password.."))
        self.opening.setText(_translate("MainWindow", "Войти"))
        self.registration.setText(_translate("MainWindow", "Регистрация"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
