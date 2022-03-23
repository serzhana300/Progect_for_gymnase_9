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
        MainWindow.setWindowTitle(_translate("MainWindow", "Вход в систему"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Login..."))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password..."))
        self.pushButton_2.setText(_translate("MainWindow", "Вход"))
        self.pushButton.setText(_translate("MainWindow", "Регистрация"))
        self.pushButton_3.setText(_translate("MainWindow", "Сгенерировать пароль"))

    def check_passw(self, n):
        if len(n) < 8:
            self.statusbar.showMessage('Длинна пароля меньше 8 сим.')
            self.statusbar.setStyleSheet('background-color:yellow')
            return False
        if len(set(n)) == 1:
            self.statusbar.showMessage('Пароль состоит из одного символа.')
            self.statusbar.setStyleSheet('background-color:yellow')
            return False
        if len(n.split(' ')) > 1:
            self.statusbar.showMessage('Пароль содердит пробел.')
            self.statusbar.setStyleSheet('background-color:yellow')
            return False
        for i in n:
            if i in 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя':
                self.statusbar.showMessage('Пароль содержит русские символы.')
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
                con = sqlite3.connect('users.db')
                cur = con.cursor()
                cur.execute(f'SELECT * FROM users WHERE login=(?)', logn)
                value = cur.fetchall()
                if value != []:
                    self.statusbar.showMessage('Такой пользователь уже используется, введите пароль.')
                    self.statusbar.setStyleSheet('background-color:yellow')
                else:
                    cur.execute('''INSERT INTO users (login, passwords) VALUES (?, ?)''', [logn, pasw])
                    self.statusbar.showMessage('Вы успешно зарегистрированы!')
                    self.statusbar.setStyleSheet('background-color:green')
                    con.commit()

                cur.close()
                con.close()
        else:
            self.statusbar.showMessage('Проверьте заполнение полей')
            self.statusbar.setStyleSheet('background-color:yellow')

    def log(self):
        logn = self.lineEdit.text()
        pasw = self.lineEdit_2.text()
        if self.check_passw(pasw):
            if func.check_edits(logn, pasw):
                con = sqlite3.connect('users.db')
                cur = con.cursor()

                cur.execute(f'SELECT * FROM users WHERE login="{logn}";')
                value = cur.fetchall()

                if value != [] and value[0][2] == pasw:
                    with open('online_cash.txt', mode='w+', encoding='utf-8') as file_cash:
                        file_cash.write(f'{logn}')
                    os.system('programm_itog.pyw')
                    exit()
                else:
                    self.statusbar.showMessage('Проверьте логин или пароль.')
                    self.statusbar.setStyleSheet('background-color:red')

                cur.close()
                con.close()
            else:
                self.statusbar.showMessage('Проверьте заполнение полей')
                self.statusbar.setStyleSheet('background-color:yellow')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
