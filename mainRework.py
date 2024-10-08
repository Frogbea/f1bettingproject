# IMPORTS ***********************************************************************************************
import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
import csv 
import requests, json

#Varibles ****************************************************************************************
startEC = 15
currentEC = 0


#CLASSES************* ********************************************************************************
class Welcomepage(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # INITIAL STUFF **********************************************
        self.setStyleSheet('QLabel{font-family: Garamond; font-size: 40px;}')

        # LAYOUT SET UP ***************************************************
        layout = QVBoxLayout()
        # welcome button
        welcome = QLabel('WELCOME! To the official F1 betting program!!', alignment=QtCore.Qt.AlignCenter)

        # sign in button
        buttonIn = QPushButton('Sign in')
        buttonIn.clicked.connect(self.usersigninchange)
        buttonIn.setStyleSheet('background-image: url(f1car.jpg);')
        buttonIn.resize(280, 40)
        buttonIn.setStyleSheet("border : 2px solid white; border-radius : 20px;")
        
        # sign up button
        buttonUp = QPushButton('Sign up')
        buttonUp.clicked.connect(self.usersignupchange)
        buttonUp.setIcon(QIcon('checkeredflag.jpg'))
        buttonUp.setStyleSheet("border : 2px solid white; border-radius : 20px;")

        # add image
        welcomeimage = QLabel(self, alignment=QtCore.Qt.AlignCenter)
        pixmap = QPixmap('f1.jpg')
        welcomeimage.setPixmap(pixmap)
        
        # set layout order
        layout.addWidget(welcome)
        layout.addWidget(buttonIn)
        layout.addWidget(buttonUp)
        layout.addWidget(welcomeimage)

        # set layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    # change pages when button pushed
    def usersigninchange(self):
        widget.setCurrentWidget(signin)
    def usersignupchange(self):
        widget.setCurrentWidget(signup)

class signIn(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.previousUser()

    # previous user layout
    def previousUser(self):
        # username text box
        self.user = QLineEdit(self)
        user = QLabel('Please enter your username:')

        # password text box
        self.passw = QLineEdit(self)
        self.passw.setEchoMode(QLineEdit.EchoMode.Password)
        passwr = QLabel('Please enter your password:')

        # sign in button
        self.confirm = QPushButton('Sign in', self)
        self.confirm.clicked.connect(self.signin)

        # back button
        self.inback = QPushButton('Return to welcome page', self)
        self.inback.clicked.connect(self.changeTowelcome)

        # adding to layout
        layout = QFormLayout()
        layout.addRow(user, self.user)
        layout.addRow(passwr, self.passw)
        layout.addRow(self.inback, self.confirm)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    # function for user sign in
    def signin(self):
        global currentEC
        username = self.user.text()
        password = self.passw.text()
        currentEC = 0
        # checking username and password entered
        if username == '' or password == '':
            QMessageBox.warning(self, 'ERROR', 'Please enter a username and password!', QMessageBox.Ok, QMessageBox.Ok)
        else:
            # testing username and password are correct
            test1 = False
            file = open('users.csv')
            colu = 0
            colp = 1
            while True:
                for row in csv.reader(file):
                    if row[colu] == username and row[colp] == password:
                    # dialog box to take user to home page
                        userFound = QMessageBox(self)
                        userFound.setWindowTitle('Successful')
                        userFound.setText('Welcome back ' + username + '!')
                        userFound.setStandardButtons(QMessageBox.Ok)
                        userFound.setIcon(QMessageBox.Information)
                        currentEC = row[2]
                        goToHome = userFound.exec()
                        test1 = True
                        if goToHome == QMessageBox.Ok:
                            self.changetohome()
                if test1:
                    print(currentEC)
                    break; 
                else:
                    QMessageBox.critical(self, 'ERROR', 'User not found. Please re-enter details or sign up instead', QMessageBox.Ok, QMessageBox.Ok)
                    break;
    # change back to welcome page
    def changeTowelcome(self):
        widget.setCurrentWidget(welcome)
    def changetohome(self):
        widget.setCurrentWidget(homepage)

class signUp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.newUser()
    #code for new user
    def newUser(self):
        # create username text box
        self.createuser = QLineEdit(self)

        #  create password text box
        self.createpassw = QLineEdit(self)
        self.createpassw.setEchoMode(QLineEdit.EchoMode.Password)

        #  check password text box
        self.checkpassw = QLineEdit(self)
        self.checkpassw.setEchoMode(QLineEdit.EchoMode.Password)

        # sign up button
        self.create = QPushButton('Sign up', self)
        self.create.setStyleSheet('background-image: url(f1signup.png)')
        self.create.clicked.connect(self.signupp)

        # back button 
        self.upback = QPushButton('Return to welcome page', self)
        self.upback.clicked.connect(self.changetowelcome)

        # layout setup
        layout = QFormLayout()
        layout.addRow('Please create a username:', self.createuser)
        layout.addRow('Please create a passowrd:', self.createpassw)
        layout.addRow('Re-enter password to confirm:', self.checkpassw)
        layout.addRow(self.upback, self.create)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    # code to sign user up
    def signupp(self):
        username = self.createuser.text()
        password = self.createpassw.text()
        password2 = self.checkpassw.text()
        emilycoins = startEC
        # check usernmae/password is entered
        if username == '' or password == '' or password2 == '':
            QMessageBox.warning(self, 'ERROR', 'Please create username and password!', QMessageBox.Ok, QMessageBox.Ok)
        else:
            # check passwords match
            if password != password2:
                # password's do not match dialog box
                noMatch = QMessageBox(self)
                noMatch.setWindowTitle('ERROR')
                noMatch.setText('Passwords do not match')
                noMatch.setStandardButtons(QMessageBox.Ok)
                noMatch.setIcon(QMessageBox.Warning)
                noMatch.exec()
            else:
                # write user & pass into csv
                with open('users.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([username, password, emilycoins])
                # dialog box to take user to home page
                accCreated = QMessageBox(self)
                accCreated.setWindowTitle('Welcome!')
                accCreated.setText('Account created successfully. Welcome to the program!\n You have ' + str(startEC) + ' Emily Coins as a signing bonus!!')
                accCreated.setStandardButtons(QMessageBox.Ok)
                accCreated.setIcon(QMessageBox.Information)
                goToHome = accCreated.exec()
                if goToHome == QMessageBox.Ok:
                    self.changetohome()
    # change back to welcome page
    def changetowelcome(self):
        widget.setCurrentWidget(welcome)
    # change to home page
    def changetohome(self):
        widget.setCurrentWidget(homepage)

class homePage(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        currentEC = 100

        displayCurrent = QLabel('You have' + str(currentEC) + ' emily coins to use!')
        pick = QLabel('Pick what you would like to bet on:')




# MAIN *******************************************************************************************************************************
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    # create welcome page instance
    welcome = Welcomepage()
    widget.addWidget(welcome)

    # create sign in page instance
    signin = signIn() 
    widget.addWidget(signin) 

    # create sign up page instance
    signup = signUp()
    widget.addWidget(signup)

    # create home page instance
    homepage = homePage()
    widget.addWidget(homepage)

    # create redbull page instance


    # showing and starting widgets
    widget.setCurrentWidget(welcome)  
    widget.setWindowTitle('F1 betting system')
    widget.resize(500, 900)
    widget.show()
    app.exec()
