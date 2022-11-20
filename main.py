import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('kk5.ui', self)
        self.con = sqlite3.connect("coffee.sqlite")
        self.select()

    def select(self):
        res = self.con.cursor().execute("SELECT * FROM coffee").fetchall()
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(2)
        print(res)
        print(1)
        for i, elem in enumerate(res):
            for j in range(len(elem) - 2):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem[j + 1])))

        for i, elem in enumerate(res):
            for j in range(len(elem) - 2):
                self.tableWidget.setItem(i, j + 1, QTableWidgetItem(str(elem[j + 2])))


        self.tableWidget.setHorizontalHeaderLabels(['type', 'kol-vo'])
        print(1)



app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
################################################
