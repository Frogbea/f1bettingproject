import requests, json
import sys
from PySide6 import QtCore, QtWidgets, QtGui
import csv 

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        response = requests.get('http://ergast.com/api/f1/current/constructorStandings.json') 
        self.print = jprint(response.json())

        self.button = QtWidgets.QPushButton('Click me!')
        self.text = QtWidgets.QLabel('Current team data', alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(self.print)

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# MAIN **************************************************************************************************
if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())