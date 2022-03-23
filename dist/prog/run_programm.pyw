import datetime as dt
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

with open('online_cash.txt', mode='r', encoding='utf-8') as f:
    per = f.readline().rstrip()
    if not per:
        os.abort()

date_inf = dt.date.today()
hour_inf = dt.datetime.today().hour
minut_inf = dt.datetime.today().minute


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(669, 581)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
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
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 669, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.add_zamet.clicked.connect(self.f)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def f(self):
        date = str((self.calendarWidget.selectedDate()).toPyDate())
        time = (self.timeEdit.time()).toPyTime()
        work = self.text_zamet.toPlainText()
        con = sqlite3.connect('table_zamet_users.db')
        cur = con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute(f"SELECT * FROM table_zamet WHERE user = '{str(per)}'").fetchall()
        # Заполнили размеры таблицы
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        # Заполнили таблицу полученными элементами
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Планировщик"))
        self.welck_lb.setText(_translate("MainWindow", f"Welcome {per}"))
        self.info_date.setText(_translate("MainWindow", f"Дата: {date_inf}"))
        self.info_start_session.setText(_translate("MainWindow", f"Время начала сессии: {hour_inf}:{minut_inf}"))
        self.info_login.setText(_translate("MainWindow", f"Логин: {per}"))
        self.text_zamet.setHtml(_translate("MainWindow", ""))
        self.add_zamet.setText(_translate("MainWindow", "Добавить событие"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
