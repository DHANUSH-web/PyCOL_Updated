# PyCOL Application Development Source code
# Developed with PyQt5 by Dhanush H V - ASE, DSA and Python Programmer in TATA CONSULTANCY SERVICES(TCS)
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.colors as cols
import numpy as np
import sys
import webbrowser as web
import pyperclip as cp
import os

# Stack Overflow: https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# application files
LICENSE = resource_path('assets/docs/MITLIC.txt')
APP_INFO = resource_path('assets/docs/APP_INFO.txt')

# Important URL
GITHUB = 'https://www.github.com/DHANUSH-web'
PROJECT_REPO = 'https://www.github.com/DHANUSH-web/PyCOL'
FLATUI = 'https://www.flatuicolors.com/'

class Ui_PyCOL(object):
    def setupUi(self, PyCOL):
        # setup window
        PyCOL.setObjectName("PyCOL")
        PyCOL.setWindowModality(QtCore.Qt.ApplicationModal)
        PyCOL.resize(355, 565)
        PyCOL.setMinimumSize(QtCore.QSize(355, 565))
        PyCOL.setMaximumWidth(355)
        PyCOL.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # set font
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        PyCOL.setFont(font)
        # set icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("assets/docs/../icons/PyCOL.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PyCOL.setWindowIcon(icon)
        PyCOL.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(PyCOL)
        self.centralwidget.setObjectName("centralwidget")
        self.ColorPicker = QtWidgets.QLabel(self.centralwidget)
        self.ColorPicker.setGeometry(QtCore.QRect(120, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ColorPicker.setFont(font)
        self.ColorPicker.setObjectName("ColorPicker")
        self.RSlide = QtWidgets.QSlider(self.centralwidget)
        self.RSlide.setGeometry(QtCore.QRect(10, 53, 241, 21))
        # self.RSlide.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.RSlide.setMaximum(255)
        self.RSlide.setOrientation(QtCore.Qt.Horizontal)
        self.RSlide.setObjectName("RSlide")
        self.GSlide = QtWidgets.QSlider(self.centralwidget)
        self.GSlide.setGeometry(QtCore.QRect(10, 100, 241, 21))
        # self.GSlide.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.GSlide.setMaximum(255)
        self.GSlide.setOrientation(QtCore.Qt.Horizontal)
        self.GSlide.setObjectName("GSlide")
        self.BSlide = QtWidgets.QSlider(self.centralwidget)
        self.BSlide.setGeometry(QtCore.QRect(10, 147, 241, 21))
        # self.BSlide.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.BSlide.setMaximum(255)
        self.BSlide.setOrientation(QtCore.Qt.Horizontal)
        self.BSlide.setObjectName("BSlide")
        self.updateSlides([255, 255, 255])
        self.RSet = QtWidgets.QSpinBox(self.centralwidget)
        self.RSet.setGeometry(QtCore.QRect(270, 48, 71, 31))
        self.RSet.setObjectName("RSet")
        self.RSet.setMaximum(255)
        self.GSet = QtWidgets.QSpinBox(self.centralwidget)
        self.GSet.setGeometry(QtCore.QRect(270, 95, 71, 31))
        self.GSet.setObjectName("GSet")
        self.GSet.setMaximum(255)
        self.BSet = QtWidgets.QSpinBox(self.centralwidget)
        self.BSet.setGeometry(QtCore.QRect(270, 140, 71, 31))
        self.BSet.setObjectName("BSet")
        self.BSet.setMaximum(255)
        self.updateInputs([255, 255, 255])

        self.RSlide.valueChanged.connect(self.triggerSlide)
        self.GSlide.valueChanged.connect(self.triggerSlide)
        self.BSlide.valueChanged.connect(self.triggerSlide)

        self.ColorView = QtWidgets.QLabel(self.centralwidget)
        self.ColorView.setGeometry(QtCore.QRect(110, 180, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ColorView.setFont(font)
        self.ColorView.setObjectName("ColorView")
        self.showColor = QtWidgets.QWidget(self.centralwidget)
        self.showColor.setGeometry(QtCore.QRect(10, 210, 331, 80))
        self.showColor.setStyleSheet("background-color: white;\
            border: 1px solid;\
            border-radius: 5px;")
        self.showColor.setObjectName("showColor")
        self.HexDisplay = QtWidgets.QPushButton(self.centralwidget, clicked=self.copyHexCode)
        self.HexDisplay.setGeometry(QtCore.QRect(10, 300, 331, 51))
        self.HexDisplay.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.HexDisplay.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.HexDisplay.setObjectName("HexDisplay")
        self.HexDisplay.setStyleSheet("font-family: Arial;\
            font-weight: bold;\
            background-color: #3c6382;\
            border: 2px solid #0a3d62;\
            color: white;\
            border-radius: 5px;")
        cp = self.setKeySeq('Ctrl+C')
        cp.activated.connect(self.copyHexCode)
        self.Xplore = QtWidgets.QPushButton(self.centralwidget, clicked=self.XPloreColors)
        self.Xplore.setGeometry(QtCore.QRect(10, 410, 331, 51))
        self.Xplore.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Xplore.setObjectName("Xplore")
        self.Xplore.setStyleSheet('background-color: #2870ab;\
            color: white;\
            font-weight: bold;\
            border: 2px solid #4153a3;\
            border-radius: 5px;')
        xp = self.setKeySeq('Ctrl+X')
        xp.activated.connect(self.XPloreColors)
        self.UserInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.UserInput.setGeometry(QtCore.QRect(10, 359, 331, 41))
        self.UserInput.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.UserInput.setInputMethodHints(QtCore.Qt.ImhNone)
        self.UserInput.setObjectName("UserInput")
        self.UserInput.setStyleSheet("border: 2px solid grey; border-radius: 5px; font-weight: bold;")
        self.ApplyBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.applyColor())
        self.ApplyBtn.setGeometry(QtCore.QRect(10, 470, 161, 41))
        self.ApplyBtn.setObjectName("ApplyBtn")
        self.ApplyBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.ApplyBtn.setStyleSheet('background-color: #38ada9;\
            border: 2px solid #006266;\
            border-radius: 5px;\
            color: white;\
            font-weight: bold;')
        aply = self.setKeySeq('Ctrl+P')
        aply.activated.connect(self.applyColor)
        self.InfoBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.showWindow("PyCOL- APP INFO", APP_INFO))
        self.InfoBtn.setGeometry(QtCore.QRect(180, 470, 161, 41))
        self.InfoBtn.setObjectName("InfoBtn")
        self.InfoBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.InfoBtn.setStyleSheet('background-color: #ee5253;\
            border: 2px solid #c0392b;\
            border-radius: 5px;\
            font-weight: bold;\
            color: white;')
        hwnd = self.setKeySeq('Ctrl+I')
        hwnd.activated.connect(lambda: self.showWindow("PyCOL - APP INFO", APP_INFO))
        PyCOL.setCentralWidget(self.centralwidget)
        self.PyMenu = QtWidgets.QMenuBar(PyCOL)
        self.PyMenu.setGeometry(QtCore.QRect(0, 0, 355, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setWeight(50)
        self.PyMenu.setFont(font)
        self.PyMenu.setObjectName("PyMenu")
        self.PyCOL_Menu = QtWidgets.QMenu(self.PyMenu)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.PyCOL_Menu.setFont(font)
        self.PyCOL_Menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PyCOL_Menu.setObjectName("PyCOL_Menu")
        PyCOL.setMenuBar(self.PyMenu)
        self.statusbar = QtWidgets.QStatusBar(PyCOL)
        self.statusbar.setObjectName("statusbar")
        PyCOL.setStatusBar(self.statusbar)
        self.flatUI_op = QtWidgets.QAction(QtGui.QIcon(resource_path('assets/icons/flatui.png')), 'FaltUI Color', PyCOL)
        self.flatUI_op.setShortcut('Ctrl+F')
        self.flatUI_op.triggered.connect(lambda: web.open(FLATUI))
        self.flatUI_op.setObjectName("flatUI_op")
        self.RndColor = QtWidgets.QAction(QtGui.QIcon(resource_path("assets/icons/random.png")), 'Random Color', PyCOL)
        self.RndColor.setStatusTip("Generate Random Color")
        self.RndColor.setShortcut('Ctrl+R')
        self.RndColor.triggered.connect(self.generateRandom)
        self.RndColor.setObjectName("RndColor")
        self.PyDoc = QtWidgets.QAction(QtGui.QIcon(resource_path('assets/icons/information.png')), 'MIT LICENSE', PyCOL)
        self.PyDoc.setShortcut('Ctrl+J')
        self.PyDoc.triggered.connect(lambda: self.showWindow("PyCOL - License", LICENSE))
        self.PyDoc.setObjectName("PyDoc")
        self.Dev = QtWidgets.QAction(QtGui.QIcon(resource_path('assets/images/profile.jpg')), 'App Developer', PyCOL)
        self.Dev.setShortcut('Ctrl+D')
        self.Dev.triggered.connect(lambda: web.open(GITHUB))
        self.hotKey = QtWidgets.QAction(QtGui.QIcon(resource_path('assets/icons/hotKey.png')), 'View HotKeys', PyCOL)
        self.hotKey.setShortcut('Ctrl+S')
        self.hotKey.triggered.connect(lambda: self.showWindow("PyCOL - Hot Keys", 'assets/docs/keysh.txt'))
        self.ExitApp = QtWidgets.QAction(QtGui.QIcon(resource_path('assets/icons/exit.png')), 'Exit PyCOL', PyCOL)
        self.ExitApp.setShortcut('Ctrl+Q')
        self.ExitApp.triggered.connect(lambda: self.exitPyCOL())
        self.ExitApp.setObjectName("ExitApp")
        self.PyCOL_Menu.addAction(self.flatUI_op)
        self.PyCOL_Menu.addAction(self.RndColor)
        self.PyCOL_Menu.addSeparator()
        self.PyCOL_Menu.addAction(self.PyDoc)
        self.PyCOL_Menu.addAction(self.Dev)
        self.PyCOL_Menu.addSeparator()
        self.PyCOL_Menu.addAction(self.hotKey)
        self.PyCOL_Menu.addAction(self.ExitApp)
        self.PyMenu.addAction(self.PyCOL_Menu.menuAction())

        self.retranslateUi(PyCOL)
        QtCore.QMetaObject.connectSlotsByName(PyCOL)

    # update sliders when new values are updated
    def updateSlides(self, n):
        self.RSlide.setValue(n[0])
        self.GSlide.setValue(n[1])
        self.BSlide.setValue(n[2])

    # update spin boxes when sliders updated
    def updateInputs(self, n):
        self.RSet.setValue(n[0])
        self.GSet.setValue(n[1])
        self.BSet.setValue(n[2])

    # to get the slider values
    def getSlideValues(self):
        return [self.RSlide.value(), self.GSlide.value(), self.BSlide.value()]

    def triggerSlide(self):
        s = self.getSlideValues()
        self.updateInputs(s)
        s = self.getHexColor(s)
        self.HexDisplay.setText(s)
        self.showColor.setStyleSheet(f'background-color: {s};')

    # to get the spin box values
    def getInputValues(self):
        return [self.RSet.value(), self.GSet.value(), self.BSet.value()]

    def getHexColor(self, c):
        c = [n/255 for n in c]
        _hex = cols.to_hex(c)
        return _hex.upper()

    def extractHexa(self, hex_color):
        c = cols.to_rgb(hex_color)
        c = np.array(np.array(c) * 255, np.int32)
        return c

    def copyHexCode(self):
        hex_code = self.HexDisplay.text()
        cp.copy(hex_code)

    def showWindow(self, title, file):
        with open(file) as info:
            message = info.read().replace("*", '--')
        window = QtWidgets.QMessageBox(PyCOL)

        window.setInformativeText(message)
        window.setWindowTitle(title)
        window.setStyleSheet('background-color: #1e272e;\
            color: white;\
            font-family: Arial;\
            font-weight: bold;')
        self.gitHub = QtWidgets.QPushButton("GitHub", window, clicked=lambda: web.open(PROJECT_REPO))
        self.gitHub.setIcon(QtGui.QIcon(resource_path('assets/icons/github.png')))
        self.gitHub.setCursor(QtCore.Qt.PointingHandCursor)
        self.gitHub.setToolTip("Open Project in GitHub")
        self.gitHub.setGeometry(28, 728, 100, 35)
        window.setStandardButtons(QtWidgets.QMessageBox.Ok)
        window.exec_()

    def setKeySeq(self, seq):
        hwnd = QtWidgets.QShortcut(QtGui.QKeySequence(seq), PyCOL)
        return hwnd

    def applyColor(self):
        try:
            color = self.UserInput.document().toPlainText()

            if not self.UserInput.document().isEmpty():
                # if user enter an hexa-decimal value
                if color.startswith('#'):
                    c = self.extractHexa(color)
                    self.updateSlides(c)
                    self.updateInputs(c)
                    hex_color = color

                else:
                    color = [int(c) for c in str(color).split()]
                    self.updateSlides(color)
                    self.updateInputs(color)
                    hex_color = self.getHexColor(color)
            else:
                color = self.getInputValues()
                hex_color = self.getHexColor(color)
                self.updateSlides(color)

            self.showColor.setStyleSheet(f"background-color: {hex_color}")
            self.HexDisplay.setText(hex_color)

        except Exception as e:
            QtWidgets.QMessageBox.question(PyCOL, "PyCOL",
                "Please give valid color code\nPress Ctrl + I for more info",
                QtWidgets.QMessageBox.Ok)
            hex_color = self.getHexColor(self.getInputValues())
            self.showColor.setStyleSheet(f"background-color: {hex_color}")
            self.HexDisplay.setText(hex_color)

    def generateRandom(self):
        rn = np.random.randint(0, 256, 3)

        self.updateSlides(rn)
        self.updateInputs(rn)
        hex_color = self.getHexColor(self.getInputValues())
        self.HexDisplay.setText(hex_color)
        self.showColor.setStyleSheet(f"background-color: {hex_color}")

    def XPloreColors(self):
        color = QtWidgets.QColorDialog.getColor()

        if color.isValid():
            color = color.name().upper()
            c = self.extractHexa(color)
            self.updateSlides(c)
            self.updateInputs(c)
            self.showColor.setStyleSheet(f'background-color: {color}')
            self.HexDisplay.setText(color)

    def exitPyCOL(self):
        close = QtWidgets.QMessageBox.question(PyCOL,
            "PyCOL", "Do you want to exit PyCOL?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if close == QtWidgets.QMessageBox.Yes:
            PyCOL.close()

    def retranslateUi(self, PyCOL):
        _translate = QtCore.QCoreApplication.translate
        PyCOL.setWindowTitle(_translate("PyCOL", "PyCOL - by Dhanush H V"))
        self.ColorPicker.setText(_translate("PyCOL", "Color Picker"))
        self.RSlide.setToolTip(_translate("PyCOL", "Seek for Red"))
        self.GSlide.setToolTip(_translate("PyCOL", "Seek for Green"))
        self.BSlide.setToolTip(_translate("PyCOL", "Seek for Blue"))
        self.ColorView.setText(_translate("PyCOL", "Color Preview"))
        self.HexDisplay.setToolTip(_translate("PyCOL", "Click to copy Hex Code"))
        self.HexDisplay.setText(_translate("PyCOL", "#FFFFFF"))
        self.Xplore.setToolTip(_translate("PyCOL", "Click here to explore more colors"))
        self.Xplore.setText(_translate("PyCOL", "Explore More Colors"))
        self.UserInput.setToolTip(_translate("PyCOL", "Enter your custom color. . ."))
        self.UserInput.setPlaceholderText(_translate("PyCOL", "Enter your custom color to apply"))
        self.ApplyBtn.setToolTip(_translate("PyCOL", "Click to apply the custom color"))
        self.ApplyBtn.setText(_translate("PyCOL", "Apply"))
        self.InfoBtn.setToolTip(_translate("PyCOL", "More details of PyCOL"))
        self.InfoBtn.setText(_translate("PyCOL", "More Info"))
        self.PyCOL_Menu.setTitle(_translate("PyCOL", "PyCOL"))
        self.flatUI_op.setText(_translate("PyCOL", "FlatUI Color"))
        self.RndColor.setText(_translate("PyCOL", "Random Color"))
        self.PyDoc.setText(_translate("PyCOL", "Application Docs"))
        self.Dev.setText(_translate('PyCOL', "Developer Profile"))
        self.hotKey.setText(_translate('PyCOL', "Keyboard Shortcuts"))
        self.ExitApp.setText(_translate("PyCOL", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    PyCOL = QtWidgets.QMainWindow()
    ui = Ui_PyCOL()
    ui.setupUi(PyCOL)
    PyCOL.show()
    sys.exit(app.exec_())
