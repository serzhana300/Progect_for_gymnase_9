import datetime as dt
import os
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import sqlite3
import func

date_inf = dt.date.today()
hour_inf = dt.datetime.today().hour
minut_inf = dt.datetime.today().minute
sec_inf = dt.datetime.today().second


with open('cash/online_cash.txt', mode='r', encoding='utf-8') as f:
    per = f.readline().rstrip()
    if not per:
        os.abort()

try:
    with open(f'cash/user_{per}.txt', mode='a+', encoding='utf-8') as file_cash:
        cash_user = file_cash.readlines()
        try:
            file_cash.write(f'{func.verif_date(date_inf)} -- {func.verif_date(hour_inf)}:'
                            f'{func.verif_date(minut_inf)}:'
                            f'{func.verif_date(sec_inf)}\n')
            last_seen = cash_user[-2]
        except IndexError:
            last_seen = ''
except FileNotFoundError:
    with open(f'cash/user_{per}.txt', mode='a+', encoding='utf-8') as file_cash:
        file_cash.write(f'{func.verif_date(date_inf)} -- {func.verif_date(hour_inf)}:'
                        f'{func.verif_date(minut_inf)}:'
                        f'{func.verif_date(sec_inf)}\n')
        last_seen = ''


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(866, 755)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.welck_lb = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.welck_lb.setFont(font)
        self.welck_lb.setObjectName("welck_lb")
        self.horizontalLayout_2.addWidget(self.welck_lb)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.info_date = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.info_date.setFont(font)
        self.info_date.setObjectName("info_date")
        self.verticalLayout_2.addWidget(self.info_date)
        self.info_start_session = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.info_start_session.setFont(font)
        self.info_start_session.setObjectName("info_start_session")
        self.verticalLayout_2.addWidget(self.info_start_session)
        self.info_login = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.info_login.setFont(font)
        self.info_login.setObjectName("info_login")
        self.verticalLayout_2.addWidget(self.info_login)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout.addWidget(self.timeEdit)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.text_zamet = QtWidgets.QTextEdit(self.centralwidget)
        self.text_zamet.setObjectName("text_zamet")
        self.verticalLayout.addWidget(self.text_zamet)
        self.add_zamet = QtWidgets.QPushButton(self.centralwidget)
        self.add_zamet.setObjectName("add_zamet")
        self.verticalLayout.addWidget(self.add_zamet)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(420, 404))
        self.tableWidget.setMaximumSize(QtCore.QSize(420, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.upd = QtWidgets.QPushButton(self.centralwidget)
        self.upd.setObjectName("update")
        self.gridLayout.addWidget(self.upd, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 866, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.add_zamet.clicked.connect(self.f)
        self.pushButton.clicked.connect(self.del_note)
        self.pushButton_2.clicked.connect(self.history)
        self.upd.clicked.connect(self.update)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        time.sleep(2)

    def update(self):
        try:
            self.tableWidget.clear()

            con = sqlite3.connect('table_zamet_users.db')
            cur = con.cursor()
            result = cur.execute('''SELECT date, time, zamet, recording_time FROM table_zamet
                                 WHERE user = (?)''', [per]).fetchall()
            # Заполнили размеры таблицы
            self.tableWidget.setRowCount(len(result) + 999999)
            self.tableWidget.setColumnCount(len(result[0]))
            self.titles = [description[0] for description in cur.description]
            # Заполнили таблицу полученными элементами
            sch = 0
            for i, elem in enumerate(result):
                sch += 1
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            self.statusbar.showMessage('Таблица обновлена!')
            self.statusbar.setStyleSheet('background-color:green')
            self.statusbar.showMessage('')
            self.statusbar.setStyleSheet('background-color:white')

        except IndexError:
            pass

    def del_note(self):
        os.system('del_win.exe')

    def history(self):
        os.system('output_win.exe')

    def f(self):
        date = str((self.calendarWidget.selectedDate()).toPyDate())
        time = f'{(self.timeEdit.time()).toPyTime()}'
        work = self.text_zamet.toPlainText()
        recording_time = f'{dt.datetime.today()}'
        con = sqlite3.connect('table_zamet_users.db')
        cur = con.cursor()
        try:
            # Получили результат запроса, который ввели в текстовое поле
            result = cur.execute(f"SELECT date, time, zamet, "
                                 f"recording_time FROM table_zamet WHERE user = '{str(per)}'").fetchall()
            # Заполнили размеры таблицы
            num_id = ((cur.execute(f"SELECT id FROM table_zamet WHERE user = '{str(per)}'").fetchall()[-1])[0]) + 1
            self.tableWidget.setRowCount(len(result) + 999999)
            self.tableWidget.setColumnCount(len(result[0]))
            self.titles = [description[0] for description in cur.description]
            # Заполнили таблицу полученными элементами
            sch = 0
            for i, elem in enumerate(result):
                sch += 1
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            cash = [date, time, work, recording_time]
            for i, val in enumerate(cash):
                self.tableWidget.setItem(sch, i, QTableWidgetItem(str(val)))
            cur.execute('''INSERT INTO table_zamet (id,user,date,time,zamet,recording_time) VALUES
                            (?, ?, ?, ?, ?, ?)''', [num_id, per, date, time, work, recording_time])
            con.commit()
        except IndexError:
            num_id = ((cur.execute(f"SELECT id FROM table_zamet").fetchall()[-1])[0]) + 1
            cur.execute('''INSERT INTO table_zamet (id,user,date,time,zamet,recording_time) VALUES
                        (?, ?, ?, ?, ?, ?)''', [num_id, per, date, time, work, recording_time])
            cash = [date, time, work, recording_time]
            for i, val in enumerate(cash):
                self.tableWidget.setItem(0, i, QTableWidgetItem(str(val)))
            con.commit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Планировщик"))
        self.welck_lb.setText(_translate("MainWindow", f"Welcome {per}"))
        self.info_date.setText(_translate("MainWindow", f"Дата: {func.verif_date(date_inf)}"))
        self.info_start_session.setText(_translate("MainWindow", f"Время начала сессии: {func.verif_date(hour_inf)}:"
                                                                 f"{func.verif_date(minut_inf)}"))
        self.info_login.setText(_translate("MainWindow", f"Логин: {per}"))
        self.label_2.setText(_translate("MainWindow", f"Дата поледней авторизации: {last_seen}"))
        self.text_zamet.setHtml(_translate("MainWindow", ""))
        self.add_zamet.setText(_translate("MainWindow", "Добавить событие"))
        self.pushButton.setText(_translate("MainWindow", "Удалить событие"))
        self.upd.setText(_translate("MainWindow", "Обновить данные"))
        self.pushButton_2.setText(_translate("MainWindow", "Запросить историю входов"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "date"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "time"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "notes"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "recording time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
