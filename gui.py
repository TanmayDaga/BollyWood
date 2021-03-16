import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import functions


class MainWindow(object):
    def __init__(self, mainwindow: QtWidgets.QMainWindow):
        # setting mainwindow
        self.mainWindow = mainwindow
        self.mainWindow.setObjectName('mainwindow')
        self.mainWindow.resize(765, 377)
        self.mainWindow.setWindowTitle('BollyWood')
        self.stringComplete = None

        # setting stackWidget
        self.centralWidget = QtWidgets.QWidget(self.mainWindow)
        self.centralWidget.setObjectName('central_widget')

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 769, 377))
        self.stackedWidget.setObjectName('stackedWidget')

        # setting standard font for buttons in gui
        self.standardFont = QtGui.QFont()
        self.standardFont.setFamily('Comic Sans Ms')
        self.standardFont.setPointSize(26)
        self.standardFont.setWeight(75)
        self.standardFont.setBold(True)
        self.standardFont.setItalic(False)
        self.standardFont.setUnderline(False)

        # setting homeScreen
        self.homeScreen = QtWidgets.QWidget()
        self.homeScreen.setObjectName('homeScreen')
        # play button on homeScreen
        self.playButtonHomeScreen = QtWidgets.QPushButton('Play', self.homeScreen)
        self.playButtonHomeScreen.setGeometry(QtCore.QRect(290, 220, 161, 81))
        self.playButtonHomeScreen.setFont(self.standardFont)
        self.playButtonHomeScreen.setObjectName('playButtonHomeScreen')
        self.playButtonHomeScreen.clicked.connect(self.onClickHomeScreenPlayButton)
        # exit button on homeScreen
        self.exitButtonHomeScreen = QtWidgets.QPushButton('Exit', self.homeScreen)
        self.exitButtonHomeScreen.setGeometry(QtCore.QRect(632, 291, 121, 61))
        self.exitButtonHomeScreen.setFont(self.standardFont)
        self.exitButtonHomeScreen.clicked.connect(exit)
        # custom input button on home screen
        self.customInputButtonHomeScreen = QtWidgets.QPushButton('Custom \n Input', self.homeScreen)
        self.customInputButtonHomeScreen.setGeometry(QtCore.QRect(290, 80, 161, 81))
        self.customInputButtonHomeScreen.setFont(self.standardFont)
        # TODO
        self.customInputButtonHomeScreen.clicked.connect(self.onClickCustomButtonHomeScreen)
        # adding homeScreen to stackWidget
        self.stackedWidget.addWidget(self.homeScreen)

        # making play screen
        self.playScreen = QtWidgets.QWidget()
        # horizontal layout in which text to be shown
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.playScreen)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 100, 731, 50))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        # name to be cut
        self.nameToBeCut = QtWidgets.QLabel(self.playScreen)
        self.nameToBeCut.setGeometry(QtCore.QRect(80, 20, 591, 51))
        self.nameToBeCut.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.nameToBeCut.setAlignment(QtCore.Qt.AlignCenter)
        # making its font
        self.nameToBeCutFont = QtGui.QFont()
        self.nameToBeCutFont.setFamily('Verdana')
        self.nameToBeCutFont.setPointSize(30)
        self.nameToBeCutFont.setWeight(75)
        self.nameToBeCutFont.setBold(True)
        self.nameToBeCutFont.setUnderline(True)
        self.nameToBeCut.setFont(self.nameToBeCutFont)
        # making decision image
        self.decisionImage = QtWidgets.QLabel(self.playScreen)
        self.decisionImage.setGeometry(QtCore.QRect(330, 250, 131, 111))
        # creating exit button
        self.exitButtonPlayScreen = QtWidgets.QPushButton('Exit', self.playScreen)
        self.exitButtonPlayScreen.setGeometry(QtCore.QRect(632, 291, 121, 61))
        self.exitButtonPlayScreen.setFont(self.standardFont)
        self.exitButtonPlayScreen.clicked.connect(partial(self.stackedWidget.setCurrentIndex, 0))
        # adding to  playScreen stackWidget
        self.stackedWidget.addWidget(self.playScreen)

        # customInput page
        self.customInputScreen = QtWidgets.QWidget()
        self.nameToBeCutInputCustomScreen = QtWidgets.QLineEdit(self.customInputScreen)
        # user to enter name to be cut
        self.nameToBeCutInputCustomScreen.setGeometry(QtCore.QRect(180, 60, 421, 41))
        self.nameToBeCutInputCustomScreen.setFont(self.standardFont)
        self.nameToBeCutInputCustomScreen.setPlaceholderText('Name to be Cut')
        # user to enter name to be displayed
        self.nameToBeDisplayed = QtWidgets.QLineEdit(self.customInputScreen)
        self.nameToBeDisplayed.setGeometry(QtCore.QRect(180, 110, 421, 41))
        self.nameToBeDisplayed.setFont(self.standardFont)
        self.nameToBeDisplayed.setPlaceholderText('Name to be Displayed')
        # submit button
        self.submitButtonCustomScreen = QtWidgets.QPushButton(self.customInputScreen)
        self.submitButtonCustomScreen.setGeometry(QtCore.QRect(590, 301, 131, 51))
        self.submitButtonCustomScreen.setText('Submit')
        self.submitButtonCustomScreen.setFont(self.standardFont)
        self.submitButtonCustomScreen.clicked.connect(self.onClickSubmitButtonCustomScreen)
        # TODO - its function
        # setting up options for user to show
        self.widget = QtWidgets.QWidget(self.customInputScreen)
        self.widget.setGeometry(QtCore.QRect(230, 170, 291, 151))
        self.verticalLayoutCustomInputScreen = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayoutCustomInputScreen.setContentsMargins(0, 0, 0, 0)
        # vowels checkbox
        self.hideVowelsCheck = QtWidgets.QCheckBox('Hide Vowels', self.widget)
        self.hideConsonantsCheck = QtWidgets.QCheckBox('Hide Consonants', self.widget)
        self.hideNumbersCheck = QtWidgets.QCheckBox('Hide Numbers', self.widget)
        self.hideSpecialCheck = QtWidgets.QCheckBox('Hide Special Symbols', self.widget)
        # adding all of them to vertical layout
        self.verticalLayoutCustomInputScreen.addWidget(self.hideVowelsCheck)
        self.verticalLayoutCustomInputScreen.addWidget(self.hideConsonantsCheck)
        self.verticalLayoutCustomInputScreen.addWidget(self.hideNumbersCheck)
        self.verticalLayoutCustomInputScreen.addWidget(self.hideSpecialCheck)
        # adding page to stackWidget
        self.stackedWidget.addWidget(self.customInputScreen)
        # setting centralWidget of mainWindow
        self.mainWindow.setCentralWidget(self.stackedWidget)

        QtCore.QMetaObject.connectSlotsByName(self.mainWindow)

    def setPlayScreen(self, nametobecut: str, listofwidget: list):
        self.nameToBeCut.setText(nametobecut.upper())
        self.nameToBeCut.setFont(self.nameToBeCutFont)
        self.decisionImage.setPixmap(QtGui.QPixmap())

        # Deleting previous items
        for i in reversed(range(self.horizontalLayout.count())):
            self.horizontalLayout.itemAt(i).widget().setParent(None)

        # adding items
        for i in listofwidget:
            i.setFont(self.standardFont)
            i.setAlignment(QtCore.Qt.AlignCenter)
            self.horizontalLayout.addWidget(i)

    def onEnteringValue(self, lineedit: QtWidgets.QLineEdit, counter):
        if lineedit.displayText() != "":
            if lineedit.displayText() == self.stringComplete[counter]:
                img = QtGui.QPixmap('images/right.png').scaled(131, 111)
                self.decisionImage.setPixmap(img)

            else:
                img = QtGui.QPixmap('images/wrong.png').scaled(131, 111)
                self.decisionImage.setPixmap(img)
                self.cutName()

    def cutName(self):
        text = self.nameToBeCut.text()
        if len(text) != 0:
            self.nameToBeCut.setText(text.replace(text[0], ''))
            return
        self.stackedWidget.setCurrentIndex(0)

    # buttons clicked methods
    def onClickHomeScreenPlayButton(self):
        string_incomplete, string_complete = functions.string_parse(0, random_movie_name=True)
        counter = 0
        ls = []
        for items in string_incomplete.lower():
            if items == "_":
                lineedit = QtWidgets.QLineEdit("")
                lineedit.textChanged.connect(partial(self.onEnteringValue, lineedit, counter))
                ls.append(lineedit)
            else:
                ls.append(QtWidgets.QLabel(items))
            counter += 1
        self.stringComplete = string_complete.lower()
        self.setPlayScreen('BOLLYWOOD', ls)
        self.stackedWidget.setCurrentIndex(1)

    def onClickCustomButtonHomeScreen(self):
        self.stackedWidget.setCurrentIndex(2)

    def onClickSubmitButtonCustomScreen(self):
        nametobecut = self.nameToBeCutInputCustomScreen.text()
        nametobedisplayed = self.nameToBeDisplayed.text()
        itemsnottoshow = []
        if self.hideVowelsCheck.checkState() == 2:
            itemsnottoshow.append(0)
        if self.hideConsonantsCheck.checkState() == 2:
            itemsnottoshow.append(1)
        if self.hideNumbersCheck.checkState() == 2:
            itemsnottoshow.append(2)
        if self.hideNumbersCheck.checkState() == 2:
            itemsnottoshow.append(2)

        string_incomplete, string_complete = functions.string_parse(nametobedisplayed, *itemsnottoshow,
                                                                    random_movie_name=False)
        counter = 0
        ls = []
        for items in string_incomplete:
            if items == "_":
                lineedit = QtWidgets.QLineEdit("")
                lineedit.textChanged.connect(partial(self.onEnteringValue, lineedit, counter))
                ls.append(lineedit)
            else:
                ls.append(QtWidgets.QLabel(items))
            counter += 1
        self.stringComplete = string_complete.lower()
        self.setPlayScreen(nametobecut, ls)
        self.stackedWidget.setCurrentIndex(1)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Mainwindow = QtWidgets.QMainWindow()
    ui = MainWindow(Mainwindow)
    Mainwindow.show()
    sys.exit(app.exec_())
