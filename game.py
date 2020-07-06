# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tbnsgMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#keep unnecessary features down to improve performance

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, QRunnable, QObject
import time, json, random, threading, logging
import matplotlib.pyplot as plt
import tkinter

global money

#hello teeler
#do not use capitals when possible
money = 20000000
taxation = 0.1
econOutput = 100000
happiness = 5.0

affirmative = ["yes", "Yes", "sure", "Sure", "WHY NOT", "Y", "y", "ohok", "ook", "YEE"]
negative = ['no', 'nothx', 'nope', 'NO', 'AAAA', 'please no']



#Records when the game was started - important for function time() later on
gameStart = time.time()
            
#Imports data from world.json
world = json.load(open('world.json', 'r'))
countries = world['otherCountries']
countryList = countries.keys()

#Imports data from defaultworld.json
defaultWorld = json.load(open('defaultworld.json', 'r'))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2104, 1080)
        MainWindow.setStyleSheet("background-color: rgb(28, 44, 84);\n"
        
"alternate-background-color: rgb(12, 20, 44);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("background-color: rgb(12, 20, 44);\n"
"border-radius: 10;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(11, 83, 148);\n"
"border-radius: 10;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Quantico")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Quantico")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Quantico")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Quantico")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 3, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Quantico")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setAutoFillBackground(False)
        self.plainTextEdit.setStyleSheet("border-radius: 10;\n"
"color: rgb(255, 255, 255);")
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 4, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setStyleSheet("border-color: rgb(28, 44, 84);\n"
"background-color: rgb(11, 83, 148);\n"
"border-radius: 10;")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans ExtraBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(11, 83, 148);\n"
"border-radius: 10;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout.addWidget(self.groupBox_3, 5, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #Most gameplay functions below: 

        def changeTax(cmd):
            global taxation
            changeTRTo = userInput.replace('change tax rate to', '')
            changeTRTo = changeTRTo.strip('%')
            taxation = float(changeTRTo)
            taxation = taxation/100
            dispOutput(f'Your tax rate has been changed to {round(taxation*100)}%')
            if taxation == 1:
                dispOutput('Welcome to communism, comrade.')
            refreshInfoBar()
        
        def tax():
            global money
            global econOutput
            money += econOutput*taxation
            econOutput -= econOutput*taxation
            dispOutput('You have taxed the population.')
            refreshInfoBar()

        #The fundamentals - display output, parse input

        def dispOutput(text):
            self.plainTextEdit.appendPlainText(text)
            
#abc abc abc abc
        
        def dispUsrInput():
            global userInput
            userInput = self.lineEdit.displayText()
            dispOutput(f" >   {userInput} ")

        def parseInput():
            if userInput in ['help', 'Help', '?']:
                dispOutput('You can find information on TBNSG in howto.txt, found in the root directory of the game, or type readme')
            if userInput in ['declare war']:
                #declareWar()
                pass
            if 'change tax rate to' in userInput:
                changeTax(userInput)
            if userInput == 'tax':
                tax()
            if userInput in ['clock', 'time', 'years', 'days']:
                dispOutput(f'Your country has existed for {years} years and {days} days.')
            if userInput == 'tax rate':
                statistics('tax rate')
            if userInput == 'readme':
                with open('howto.txt') as readme:
                    dispOutput(readme.read())
            if 'stats' in userInput:
                Input = userInput.replace('stats ', '')
                statistics(Input)
            if userInput == "":
                refreshInfoBar()
        

            
        #Stats
        def statistics(statistic):
            if statistic == 'time':
                dispOutput(f'Your country has existed for {years} years and {days} day(s).')
            if statistic == 'tax rate':
                dispOutput(f'The tax rate is currently {taxation*100}%')
            if statistic in ["financial", 'money']:
                thr2 = threading.Thread(target=graph, args=(1,), daemon=True)
                thr2.start()
            if statistic in ['help', '?']:
                dispOutput('Statistics are:\ntime\ntax rate\nfinancial/money')

        #Other functions that aren't really gameplay
        def refreshInfoBar():
            _translate = QtCore.QCoreApplication.translate
            self.label_3.setText(_translate("MainWindow", f"Money - {round(money/1000000, 3)} million FuBucks"))
            self.label.setText(_translate("MainWindow", f"Economic Output - {round(econOutput/1000000, 3)} million FuBucks"))
            self.label_2.setText(_translate("MainWindow", f"Happiness - {round(happiness/10, 2)}"))
            self.label_5.setText(_translate("MainWindow", f"Taxation Rate - {taxation*100}%"))

        self.retranslateUi(MainWindow)
        self.lineEdit.returnPressed.connect(dispUsrInput)
        self.lineEdit.returnPressed.connect(parseInput)
        self.lineEdit.returnPressed.connect(self.lineEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #f-strings are faster and the preferred method of embedding variables in strings - more readable, less error prone, etc; yeah I know tyler, i just wanted to make it simple at first; yes but they are BETTER i loike dem f strings - not Fu;
        self.label_3.setText(_translate("MainWindow", f"Money - {round(money/1000000, 3)} million FuBucks"))
        self.label.setText(_translate("MainWindow", f"Economic Output - {round(econOutput/1000000, 3)} million FuBucks"))
        self.label_2.setText(_translate("MainWindow", f"Happiness - {round(happiness/10, 2)}"))
        self.label_5.setText(_translate("MainWindow", f"Taxation Rate - {taxation*100}%"))
        self.label_4.setText(_translate("MainWindow", "TBNSG"))
        self.label_6.setText(_translate("MainWindow", "  >  "))

        def update_loop(name):
            while True:
                pass

def thread_loop(name):
    global years, days, money, y
    x = []
    y = []
    dayss =1
    while True:
        #this is actually a lot better than taxes b/c it's a constant stream of money, but is it realistic enough?; 
        econStability = (10-happiness)*50000
        time.sleep(0.5)
        dayss += 1
        randy = random.randint((econOutput-econStability), (econOutput+econStability))
        money += randy
        # x.append(days)
        y.append(money)
        # I think this method of keeping time is simpler and easier than the previous one. Every 3 seconds a day ticks past - it's approx. 20m = 1 year in game; 
        currentTime = time.time() - gameStart
        days = round((dayss % 365)/3)
        years = round((dayss // 365)/3)
        
        

def graph(name):
    global y
    plt.plot(y)
    plt.title('Financial Stats')
    plt.ylabel('Money (FuBucks)')
    plt.xlabel("Time (GameDays)")
    plt.show()



if __name__ == "__main__":
    import sys
    # Call and start threads here
    
    print('Threads Starting')
    thr1 = threading.Thread(target=thread_loop, args=(1,), daemon=True)
    thr1.start()
    thr3 = threading.Thread(target=Ui_MainWindow.setupUi.update_loop, args=(1,), daemon=True)
    thr3.start()
    # UI Main Startup, do not block
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
    



