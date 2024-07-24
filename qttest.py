import sys
from PyQt5.QtWidgets import *
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import csv 


class Ui_PageFirst(QMainWindow):    #Page1
    def __init__(self):
        super().__init__()
        self.setWindowTitle('111111111111111111111111')
        disconnect_button = QPushButton('Disconnect', self)
        disconnect_button.clicked.connect(self.changeToPage2)
    
    def changeToPage2(self):
        widget.setCurrentWidget(secondpage)

class Ui_PageSecond(QMainWindow):   #Page2
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("PLEEASe lORD GOD WORK")
        disconnect_button = QPushButton('GO BACK PLS WORDKEFBWJFBWF', self)
        disconnect_button.clicked.connect(self.changeToPage1)
    def changeToPage1(self):
        widget.setCurrentWidget(firstpage)

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
#######
firstpage = Ui_PageFirst()
widget.addWidget(firstpage)   # create an instance of the first page class and add it to stackedwidget

secondpage = Ui_PageSecond() 
widget.addWidget(secondpage)   # adding second page

widget.setCurrentWidget(firstpage)   # setting the page that you want to load when application starts up. you can also use setCurrentIndex(int)
########
widget.show()
app.exec_()