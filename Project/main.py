import time

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QPushButton, QLineEdit, QCheckBox
import os
import sys
import pyautogui as pg
import winshell
from voice_assistant.main import startVA

# Global variables
buttonStyle = """
    background: white;
    border: 0.5px solid #E2E2E2; 
    }
    *:hover {
    border: 2px solid 'grey';
    }
"""
actionType = ''

# Variable and Func where using Path method adding a new Button
existingButtonsP = []

def existingButtonsPath():
    global existingButtonsP
    i = len(existingButtonsP) + 1
    while i < 5:

        with open('button' + str(i) + '.txt', 'r') as btn:

            temp = btn.read()
            if temp:
                existingButtonsP.append((temp.split()[0], temp.split()[1]))
                i += 1
            else:
                break
    return existingButtonsP

# Variable and Func where using Shell Commands method adding a new Button
existingButtonsS = []

def existingButtonsShell():
    global existingButtonsS
    i = len(existingButtonsS) + 1
    while i < 5:

        with open('shellButton' + str(i) + '.txt', 'r') as btn:

            temp = btn.read()
            if temp:
                existingButtonsS.append((temp.split()[0], temp.split()[1]))
                i += 1
            else:
                break
    return existingButtonsS

# System Opportunity's Window (2)
class OpenSysWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(885, 400))
        self.setWindowTitle("NichCom")

        def buttons():

            global buttonStyle
            lenPathButton = len(existingButtonsPath())
            lenShellButton = len(existingButtonsShell())

            style = """
            *{
                padding: 10px 20px;
                font-size: 15px;
                font-weight: 600;
                width: 300px;
                text-transform: uppercase;
                border-radius: 20px;\n
            """ + buttonStyle
            cursor = Qt.CursorShape.PointingHandCursor

            # Button 1.1
            buttonTempFiles = QPushButton('Delete Temporary Files', self)
            buttonTempFiles.move(30, 80)
            buttonTempFiles.setFixedSize(256, 40)
            buttonTempFiles.setStyleSheet(style)
            buttonTempFiles.setCursor(cursor)
            buttonTempFiles.clicked.connect(self.delTempFiles)

            # Button 1.2
            buttonHostsFile = QPushButton('Open The Hosts File', self)
            buttonHostsFile.move(30, 135)
            buttonHostsFile.setFixedSize(256, 40)
            buttonHostsFile.setStyleSheet(style)
            buttonHostsFile.setCursor(cursor)
            buttonHostsFile.clicked.connect(self.openHostsFile)

            # Button 1.3
            buttonVirtualK = QPushButton('Open The Virtual Keyboard', self) # osk
            buttonVirtualK.move(30, 190)
            buttonVirtualK.setFixedSize(256, 40)
            buttonVirtualK.setStyleSheet(style)
            buttonVirtualK.setCursor(cursor)
            buttonVirtualK.clicked.connect(self.openVKeyboard)

            # Button 1.4
            buttonControlPanel = QPushButton('Open Control Panel', self)
            buttonControlPanel.move(30, 245)
            buttonControlPanel.setFixedSize(256, 40)
            buttonControlPanel.setStyleSheet(style)
            buttonControlPanel.setCursor(cursor)
            buttonControlPanel.clicked.connect(self.openCPanel)

            # Button 1.5
            buttonRecycleBin = QPushButton('Empty The Recycle Bin', self)
            buttonRecycleBin.move(30, 300)
            buttonRecycleBin.setFixedSize(256, 40)
            buttonRecycleBin.setStyleSheet(style)
            buttonRecycleBin.setCursor(cursor)
            buttonRecycleBin.clicked.connect(self.emptyRecBin)

            # Button 2.1
            buttonAddPath = QPushButton('+ (Path To File)', self)
            buttonAddPath.move(315, 80)
            buttonAddPath.setFixedSize(256, 40)
            buttonAddPath.setStyleSheet(style)
            if lenPathButton < 4:
                buttonAddPath.setCursor(cursor)
                buttonAddPath.clicked.connect(lambda: self.addButton('path'))
                self.close()
            else:
                buttonAddPath.setEnabled(False)

            # Calling buttons 2.2 & 2.3 & 2.4 & 2.5
            def button22():
                try:
                    button = QPushButton(existingButtonsP[0][0], self)
                    button.move(315, 135)
                    button.setFixedSize(256, 40)
                    button.setStyleSheet(style)
                    button.setCursor(cursor)
                    button.clicked.connect(lambda: self.buttonAction(existingButtonsP[0][1]))
                except:
                    print('Error occurred in the button 2.2')

            def button23():
                try:
                    button = QPushButton(existingButtonsP[1][0], self)
                    button.move(315, 190)
                    button.setFixedSize(256, 40)
                    button.setStyleSheet(style)
                    button.setCursor(cursor)
                    button.clicked.connect(lambda: self.buttonAction(existingButtonsP[1][1]))
                except:
                    print('Error occurred in the button 2.3')

            def button24():
                try:
                    button = QPushButton(existingButtonsP[2][0], self)
                    button.move(315, 245)
                    button.setFixedSize(256, 40)
                    button.setStyleSheet(style)
                    button.setCursor(cursor)
                    button.clicked.connect(lambda: self.buttonAction(existingButtonsP[2][1]))
                except:
                    print('Error occurred in the button 2.4')

            def button25():
                try:
                    button = QPushButton(existingButtonsP[3][0], self)
                    button.move(315, 300)
                    button.setFixedSize(256, 40)
                    button.setStyleSheet(style)
                    button.setCursor(cursor)
                    button.clicked.connect(lambda: self.buttonAction(existingButtonsP[3][1]))
                except:
                    print('Error occurred in the button 2.5')

            button22()
            button23()
            button24()
            button25()

            # Button 3.1
            buttonShell = QPushButton('+ (Shell Commands)', self)
            buttonShell.move(600, 80)
            buttonShell.setFixedSize(256, 40)
            buttonShell.setStyleSheet(style)
            if lenShellButton < 4:
                buttonShell.setCursor(cursor)
                buttonShell.clicked.connect(lambda: self.addButton('shell'))
                self.close()
            else:
                buttonShell.setEnabled(False)

            # Calling buttons 3.2 & 3.3 & 3.4 & 3.5
            def button32():
                try:
                    button = QPushButton(existingButtonsS[0][0], self)
                    button.move(600, 135)
                    button.setFixedSize(256, 40)
                    button.setStyleSheet(style)
                    button.setCursor(cursor)
                    button.clicked.connect(lambda: self.buttonAction(existingButtonsS[0][1]))
                except:
                    print('Error occurred in the button 3.2')

            def button33():
                try:
                    button = QPushButton(existingButtonsS[1][0], self)
                    button.move(600, 190)
                    button.setFixedSize(256, 40)
                    button.setStyleSheet(style)
                    button.setCursor(cursor)
                    button.clicked.connect(lambda: self.buttonAction(existingButtonsS[1][1]))
                except:
                    print('Error occurred in the button 3.3')

            def button34():
                try:
                    button = QPushButton(existingButtonsS[2][0], self)
                    button.move(600, 245)
                    button.setFixedSize(256, 40)
                    button.setStyleSheet(style)
                    button.setCursor(cursor)
                    button.clicked.connect(lambda: self.buttonAction(existingButtonsS[2][1]))
                except:
                    print('Error occurred in the button 3.4')

            def button35():
                try:
                    print(existingButtonsS)
                    button = QPushButton(existingButtonsS[3][0], self)
                    button.move(600, 300)
                    button.setFixedSize(256, 40)
                    button.setStyleSheet(style)
                    button.setCursor(cursor)
                    button.clicked.connect(lambda: self.buttonAction(existingButtonsS[3][1]))
                except:
                    print('Error occurred in the button 3.5')

            button32()
            button33()
            button34()
            button35()



        def labels():
            labelStyle = """
                font-size: 27px;
                font-weight: 670;
                border-bottom: 1px solid black;
            """
            labelTitle = QLabel('System Opportunities', self)
            labelTitle.move(300, 20)
            labelTitle.setStyleSheet(labelStyle)

            lang = 'EN' #!
            labelVersion = QLabel('v1.0  ' + lang, self)
            labelVersion.move(820, 370)

        buttons()
        labels()


    def delTempFiles(self):
        pg.hotkey('win', 'r')
        pg.write('%TEMP%')
        pg.press('enter')
        pg.hotkey('ctrl', 'a')
        pg.press('delete')

    def openHostsFile(self):
        os.startfile('C:\Windows\System32\drivers\etc\hosts')

    def openVKeyboard(self):
        # os.system("osk")
        os.popen("osk")

    def openCPanel(self):
        os.system("control")

    def emptyRecBin(self):
        winshell.recycle_bin().empty(confirm=True, show_progress=True, sound=False)

    def addButton(self, type):

        self.close()

        global actionType
        actionType = type

        self.newButton = OpenAddingWindow()
        self.newButton.setStyleSheet('background-color: #FAFAFA;')
        self.newButton.show()


    def buttonAction(self, path):
        print('working')
        os.startfile(path)


# Adding a New Feature using absolute Path (2.1)
# or
# Adding a New Button using Shell Commands (3.1)
class OpenAddingWindow(QWidget):

    global buttonStyle
    global actionType

    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(400, 400))
        self.setWindowTitle("NichCom")

        labelStyle = """
            font-size: 24px;
            font-weight: 550;
        """
        lableTitle = QLabel('Adding A New Thing', self)
        lableTitle.move(90, 30)
        lableTitle.setStyleSheet(labelStyle)

        labelName = QLabel('Name', self)
        labelName.move(50, 100)
        labelName.setStyleSheet("""
            font-size: 18px;
            font-weight: 400;
        """)

        if actionType == 'path':
            labelPath = QLabel('Path', self)
        else:
            labelPath = QLabel('Shell Command(s)', self)
        labelPath.move(50, 185)
        labelPath.setStyleSheet("""
            font-size: 18px;
            font-weight: 400;
        """)

        style = """
            padding: 10px 20px;
            font-size: 15px;
            font-weight: 600;
            width: 300px;
            border-radius: 20px;\n
        """ + buttonStyle

        self.inputName = QLineEdit(self)
        self.inputName.setFixedSize(330, 40)
        self.inputName.setMaxLength(25)
        self.inputName.move(30, 130)
        self.inputName.setStyleSheet("*{\n text-transform: uppercase;\n" + style)

        self.inputPath = QLineEdit(self)
        self.inputPath.move(30, 215)
        self.inputPath.setFixedSize(330, 40)
        self.inputPath.setStyleSheet(style)

        cursor = Qt.CursorShape.PointingHandCursor

        if actionType == 'path':
            buttonCheck = QPushButton('Check the Path', self)
        else:
            buttonCheck = QPushButton('Check', self)
        buttonCheck.move(100, 280)
        buttonCheck.setFixedSize(200, 40)
        buttonCheck.setStyleSheet("*{\n text-transform: uppercase;\n" + style)
        buttonCheck.setCursor(cursor)
        if actionType == 'path':
            buttonCheck.clicked.connect(self.checkPath)
        else:
            buttonCheck.clicked.connect(self.checkShell)

        buttonSave = QPushButton('Save', self)
        buttonSave.move(100, 330)
        buttonSave.setFixedSize(200, 40)
        buttonSave.setStyleSheet("*{\n text-transform: uppercase;\n" + style)
        buttonSave.setCursor(cursor)
        buttonSave.clicked.connect(self.save)

    def checkPath(self):
        os.startfile(self.inputPath.text())

    def checkShell(self):
        os.popen(self.inputPath.text())

    def save(self):

        global actionType
        self.close()
        print('ACTION TYPE =' + actionType)

        if actionType == 'path':
            global existingButtonsP

            with open('button' + str(len(existingButtonsP) + 1) + '.txt', 'w') as btn:
                btn.write(self.inputName.text() + '\n')
                btn.write(self.inputPath.text())
        else:
            global existingButtonsS

            with open('shellButton' + str(len(existingButtonsS) + 1) + '.txt', 'w') as btn:
                btn.write(self.inputName.text() + '\n')
                btn.write(self.inputPath.text())

        self.backToSysWindow = OpenSysWindow()
        self.backToSysWindow.setStyleSheet('background-color: #FAFAFA;')
        self.backToSysWindow.show()

class OpenVaWindow(QWidget):

    lang = 'english'
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(600, 400))
        self.setWindowTitle("NichCom")

        def chooseLang():
            self.radio = QCheckBox("Russian", self)
            self.radio.toggled.connect(self.changeLang)
            self.radio.move(260, 70)

        def buttons():
            style = """
                            padding: 10px 20px;
                            font-size: 15px;
                            font-weight: 600;
                            width: 300px;
                            text-transform: uppercase;
                            border-radius: 100px;
                            border: 0.5px solid #E2E2E2; }"""
            styleStart = """
                        *{
                            background: #9DFFBD;\n
                        """ + style + """
                        \n 
                        *:hover {
                            background: #66FF99;
                            border: 2px solid 'grey';
                        }
                        """
            styleStop = """
                        *{
                            background: #F75D59;\n
                        """ + style + """
                        \n 
                        *:hover {
                            background: #FF4500;
                            border: 2px solid 'grey';
                        }
                        """
            cursor = Qt.CursorShape.PointingHandCursor


            #Button start using
            self.buttonStart = QPushButton('Start', self)
            self.buttonStart.move(200, 120)
            self.buttonStart.setFixedSize(200, 200)
            self.buttonStart.setStyleSheet(styleStart)
            self.buttonStart.setCursor(cursor)
            self.buttonStart.clicked.connect(self.callVA)

            # #Button stop using
            # buttonStop = QPushButton('Stop', self)
            # buttonStop.move(320, 100)
            # buttonStop.setFixedSize(200, 200)
            # buttonStop.setStyleSheet(styleStop)
            # buttonStop.setCursor(cursor)

        chooseLang()
        buttons()
    def callVA(self):
        startVA(lang)

    def changeLang(self):
        global lang
        if self.sender().isChecked():
            lang = 'russian'
        else:
            lang = 'english'
        print(lang)


# Main Window (1)
class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(700, 450))
        self.setWindowTitle("NichCom")

        # Describing the app buttons
        def buttons():

            global buttonStyle

            style = """
                *{
                padding: 10px 20px;
                font-size: 15px;
                font-weight: 600;
                width: 300px;
                text-transform: uppercase;
                border-radius: 20px;\n
            """ + buttonStyle
            cursor = Qt.CursorShape.PointingHandCursor

            # System Opportunities
            self.buttonSys = QPushButton("Sys Opportunities", self)
            self.buttonSys.setFixedSize(300, 40)
            self.buttonSys.setStyleSheet(style)
            self.buttonSys.move(210, 180)
            self.buttonSys.setCursor(cursor)
            self.buttonSys.clicked.connect(self.sysButton)

            # Games
            buttonGame = QPushButton("Games", self)
            buttonGame.setFixedSize(300,40)
            buttonGame.setStyleSheet(style)
            buttonGame.move(210, 240)
            buttonGame.setCursor(cursor)
            buttonGame.clicked.connect(self.gameBtn)

            # Voice Assistant
            buttonVA = QPushButton("Voice assistant", self)
            buttonVA.setFixedSize(300,40)
            buttonVA.setStyleSheet(style)
            buttonVA.move(210, 300)
            buttonVA.setCursor(cursor)
            buttonVA.clicked.connect(self.vaBtn)

            # App's Language
            # buttonLang = QPushButton("Rus", self)
            # buttonLang.setStyleSheet("""
            #     *{
            #     padding: 5px 10px;
            #     font-size: 13px;
            #     font-weight: 500;
            #     width: 50px;
            #     text-transform: uppercase;
            #     border-radius: 15px;\n
            # """ + buttonStyle)
            # buttonLang.move(10, 10)

        # Call
        buttons()

        # Describing the app's labels
        def labels():
            labelStyle = """
                font-size: 40px;
                font-weight: 700;
                border-bottom: 1px solid 'black';
            """

            lang = 'EN'
            labelVersion = QLabel('v1.0   ' + lang, self)
            labelVersion.move(640,420)

            labelTitle = QLabel('NichCom', self)
            labelTitle.move(280, 90)
            labelTitle.setFixedSize(180, 55)
            labelTitle.setStyleSheet(labelStyle)

        # Call
        labels()

    def sysButton(self):
        self.sysWindow = OpenSysWindow()
        self.sysWindow.setStyleSheet('background-color: #FAFAFA;')
        self.sysWindow.show()
    def gameBtn(self):
        os.system("start cmd")
        time.sleep(2)
        pg.write('cd tic-toe')
        pg.press('enter')
        time.sleep(0.5)
        pg.write('npm start')
        pg.press('enter')

    def vaBtn(self):
        self.vaWindow = OpenVaWindow()
        self.vaWindow.setStyleSheet('background-color: #FAFAFA;')
        self.vaWindow.show()

    def closeEvent(self, event):
        QApplication.closeAllWindows()
        event.accept()


app = QApplication(sys.argv)
window = Window()
window.setStyleSheet('background-color: #FAFAFA;')
window.show()
sys.exit(app.exec())



