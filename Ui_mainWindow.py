# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\haoli\eric6\PolicyCloud\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from src.generator import CloudGenerator

class Ui_MainWindow(object):
    def __init__(self):
        sys.stdout = Stream(newText=self.updateText)
        self.sourceDir = ''
        self.background = os.getcwd() + '\\background.jpg'
        self.outputDir = os.getcwd()
        self.maxwords = 100
        global cloud
        cloud = CloudGenerator(self.sourceDir, self.background, self.outputDir, self.maxwords)
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 471)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.inputLabel = QtWidgets.QLabel(self.centralWidget)
        self.inputLabel.setObjectName("inputLabel")
        self.gridLayout.addWidget(self.inputLabel, 0, 0, 1, 1)
        self.inputEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.inputEdit.setObjectName("inputEdit")
        self.inputEdit.textChanged[str].connect(self.onChangedInput)
        
        self.gridLayout.addWidget(self.inputEdit, 0, 1, 1, 4)
        self.maxwordsLabel = QtWidgets.QLabel(self.centralWidget)
        self.maxwordsLabel.setObjectName("maxwordsLabel")
        self.gridLayout.addWidget(self.maxwordsLabel, 3, 0, 1, 1)
        
        self.selectOutputButton = QtWidgets.QPushButton(self.centralWidget)
        self.selectOutputButton.setObjectName("selectOutputButton")
        self.selectOutputButton.clicked.connect(self.setOutputDir)
        self.gridLayout.addWidget(self.selectOutputButton, 2, 5, 1, 1)
        
        self.outputEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.outputEdit.setObjectName("outputEdit")
        self.gridLayout.addWidget(self.outputEdit, 2, 1, 1, 4)
        self.backgroundLabel = QtWidgets.QLabel(self.centralWidget)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.gridLayout.addWidget(self.backgroundLabel, 1, 0, 1, 1)
        self.backgroundEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.backgroundEdit.setObjectName("backgroundEdit")
        self.gridLayout.addWidget(self.backgroundEdit, 1, 1, 1, 4)
        
        self.selectSourceButton = QtWidgets.QPushButton(self.centralWidget)
        self.selectSourceButton.setObjectName("selectSourceButton")
        self.selectSourceButton.clicked.connect(self.setSourceDir)
        self.gridLayout.addWidget(self.selectSourceButton, 0, 5, 1, 1)
        
        self.selectBackgroundButton = QtWidgets.QPushButton(self.centralWidget)
        self.selectBackgroundButton.setObjectName("selectBackgroundButton")
        self.selectBackgroundButton.clicked.connect(self.setBackground)
        self.gridLayout.addWidget(self.selectBackgroundButton, 1, 5, 1, 1)
        
        self.outputLabel = QtWidgets.QLabel(self.centralWidget)
        self.outputLabel.setObjectName("outputLabel")
        self.gridLayout.addWidget(self.outputLabel, 2, 0, 1, 1)
        
        self.spinBox = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.valueChanged[int].connect(self.setMaxwords)
        self.spinBox.setRange(10, 1000)
        self.spinBox.setValue(100)
        self.spinBox.setSingleStep(10)
        self.gridLayout.addWidget(self.spinBox, 3, 1, 1, 2)
        
        self.readFileButton = QtWidgets.QPushButton(self.centralWidget)
        self.readFileButton.setObjectName("readFileButton")
        self.gridLayout.addWidget(self.readFileButton, 4, 2, 1, 1)
        self.readFileButton.clicked.connect(self.readOnly)
        
        self.genPicButton = QtWidgets.QPushButton(self.centralWidget)
        self.genPicButton.setObjectName("genPicButton")
        self.gridLayout.addWidget(self.genPicButton, 4, 3, 1, 1)
        self.genPicButton.clicked.connect(self.generateOnly)
        
        self.generateButton = QtWidgets.QPushButton(self.centralWidget)
        self.generateButton.setObjectName("generateButton")
        self.gridLayout.addWidget(self.generateButton, 4, 0, 1, 2)
        self.generateButton.clicked.connect(self.readAndGenerate)
        
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stdoutLabel = QtWidgets.QLabel(self.centralWidget)
        self.stdoutLabel.setObjectName("stdoutLabel")
        self.gridLayout_2.addWidget(self.stdoutLabel, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser.setObjectName("textBrowser")
        
        self.closeButton = QtWidgets.QPushButton(self.centralWidget)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 4, 4, 1, 2)
        
        self.gridLayout_2.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        MainWindow.setCentralWidget(self.centralWidget)
 
        self.retranslateUi(MainWindow)
        self.closeButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WordCloud"))
        self.inputLabel.setText(_translate("MainWindow", "源文件目录:"))
        self.maxwordsLabel.setText(_translate("MainWindow", "最大词量："))
        self.selectOutputButton.setText(_translate("MainWindow", "选取目录"))
        self.backgroundLabel.setText(_translate("MainWindow", "背景图像："))
        self.selectSourceButton.setText(_translate("MainWindow", "选取目录"))
        self.selectBackgroundButton.setText(_translate("MainWindow", "选取文件"))
        self.outputLabel.setText(_translate("MainWindow", "输出目录："))
        self.readFileButton.setText(_translate("MainWindow", "仅读取文件"))
        self.closeButton.setText(_translate("MainWindow", "关闭"))
        self.genPicButton.setText(_translate("MainWindow", "仅生成图像"))
        self.generateButton.setText(_translate("MainWindow", "读取文件并生成图像"))
        self.stdoutLabel.setText(_translate("MainWindow", "输出信息："))
        
    def setSourceDir(self):
        self.sourceDir = QtWidgets.QFileDialog.getExistingDirectory()
        self.inputEdit.setText(self.sourceDir)
    
    def setBackground(self):
        self.background = QtWidgets.QFileDialog.getOpenFileName()
        self.backgroundEdit.setText(self.background[0])
    
    def setOutputDir(self):
        self.outputDir = QtWidgets.QFileDialog.getExistingDirectory()
        self.outputEdit.setText(self.outputDir)
    
    def setMaxwords(self,  num):
        self.maxwords = num
    
    def onChangedInput(self,  text):
        self.sourceDir = text
        
    def onChangedBackground(self, text):
        self.background = text
    
    def onChangedOutput(self, text):
        self.outputDir = text
    
    def updateText(self,  threadText):
        self.textBrowser.append(threadText)
    
    def readAndGenerate(self):
        self.thread = readAndGenThread()
        self.thread.trigger.connect(self.updateText)
        cloud.update(self.sourceDir,  self.background,  self.outputDir,  self.maxwords)
        self.thread.start()
    
    def readOnly(self):
        self.thread = readThread()
        self.thread.trigger.connect(self.updateText)
        cloud.update(self.sourceDir,  self.background,  self.outputDir,  self.maxwords)
        self.thread.start()
    
    def generateOnly(self):
        self.thread = genThread()
        self.thread.trigger.connect(self.updateText)
        cloud.update(self.sourceDir,  self.background,  self.outputDir,  self.maxwords)
        self.thread.start()
    
    def __del__(self):
    # Restore sys.stdout
        sys.stdout = sys.__stdout__
        
class Stream(QtCore.QObject):
    """Redirects console output to text widget."""
    newText = QtCore.pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))        

class genThread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()
        
    def run(self):
        cloud.generateOnly()
        
class readAndGenThread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()
        
    def run(self):
        cloud.readAndGenerate()
        
class readThread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()
        
    def run(self):
        cloud.readOnly()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

