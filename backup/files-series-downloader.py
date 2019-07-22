# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FSD.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os, time, re
from urllib.parse import urlparse
from pySmartDL import SmartDL, utils

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(761, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.beginNum = QtWidgets.QSpinBox(self.centralwidget)
        self.beginNum.setObjectName("beginNum")
        self.horizontalLayout.addWidget(self.beginNum)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.endNum = QtWidgets.QSpinBox(self.centralwidget)
        self.endNum.setObjectName("endNum")
        self.horizontalLayout.addWidget(self.endNum)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.downloadBar = QtWidgets.QProgressBar(self.centralwidget)
        self.downloadBar.setProperty("value", 0)
        self.downloadBar.setObjectName("downloadBar")
        self.gridLayout.addWidget(self.downloadBar, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.linkEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.linkEdit.setObjectName("linkEdit")
        self.horizontalLayout_2.addWidget(self.linkEdit)
        self.pathBtn = QtWidgets.QPushButton(self.centralwidget)
        self.pathBtn.setObjectName("pathBtn")
        self.horizontalLayout_2.addWidget(self.pathBtn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.infoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.infoBtn.setObjectName("infoBtn")
        self.verticalLayout.addWidget(self.infoBtn)
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setObjectName("startBtn")
        self.verticalLayout.addWidget(self.startBtn)
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setObjectName("stopBtn")
        self.verticalLayout.addWidget(self.stopBtn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.infoList = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoList.sizePolicy().hasHeightForWidth())
        self.infoList.setSizePolicy(sizePolicy)
        self.infoList.setObjectName("infoList")
        item = QtWidgets.QListWidgetItem()
        self.infoList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.infoList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.infoList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.infoList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.infoList.addItem(item)
        self.horizontalLayout_5.addWidget(self.infoList)
        self.logList = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logList.sizePolicy().hasHeightForWidth())
        self.logList.setSizePolicy(sizePolicy)
        self.logList.setObjectName("logList")
        self.horizontalLayout_5.addWidget(self.logList)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 761, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.file = None
        self.dest = None
        self.totalFinalDownload = 0
        self.totalFile = 0
        self.totalDownloadedSize = 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Serial File Downloader"))
        self.label.setText(_translate("MainWindow", "to"))
        self.label_2.setText(_translate("MainWindow", "Link file :"))
        self.pathBtn.setText(_translate("MainWindow", "..."))
        self.infoBtn.setText(_translate("MainWindow", "Gather Info"))
        self.startBtn.setText(_translate("MainWindow", "Start"))
        self.stopBtn.setText(_translate("MainWindow", "Stop"))
        __sortingEnabled = self.infoList.isSortingEnabled()
        self.infoList.setSortingEnabled(False)
        item = self.infoList.item(0)
        item.setText(_translate("MainWindow", "File at : "))
        item = self.infoList.item(1)
        item.setText(_translate("MainWindow", "Status : "))
        item = self.infoList.item(2)
        item.setText(_translate("MainWindow", "File total : "))
        item = self.infoList.item(3)
        item.setText(_translate("MainWindow", "Total size : "))
        item = self.infoList.item(4)
        item.setText(_translate("MainWindow", "Destination : "))
        self.infoList.setSortingEnabled(__sortingEnabled)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

        self.actionAbout.triggered.connect(self.on_action_menu_about)

        self.pathBtn.clicked.connect(self.on_btn_path_clicked)
        self.infoBtn.clicked.connect(self.on_btn_info_clicked)
        self.startBtn.clicked.connect(self.on_btn_start_clicked)
        self.stopBtn.clicked.connect(self.on_btn_stop_clicked)

    def check_files_info(self, url, dest):
        for i in range(self.beginNum.value(), self.endNum.value() + 1):
            serialUrl = re.sub(r"\{\{(S)\}\}", str(i), url)

            #Get file size
            filesize = utils.get_filesize(serialUrl)

            print('Get filesize of ' + serialUrl + ' : ' + utils.sizeof_human(filesize))

            self.totalFinalDownload += filesize
            self.totalFile += 1
            self.file.stop()

        self.infoList.item(2).setText(self.infoList.item(2).text() + str(self.totalFile))
        self.infoList.item(3).setText(self.infoList.item(3).text() + str(utils.sizeof_human(self.totalFinalDownload)))

    def on_action_menu_about(self):
        print('hello')

    #def on_action_menu_quit(self):


    def on_btn_path_clicked(self):
        self.dest = str(QtWidgets.QFileDialog.getExistingDirectory())
        if not self.dest == None:
            print('Selected path : ' + self.dest)
            self.infoList.item(4).setText('Destination : ' + self.dest)

    def on_btn_info_clicked(self):
        if self.linkEdit.text() == '' and not self.dest == None:
            print('error')
        else:
            url = self.linkEdit.text()
            self.check_files_info(url, self.dest)

    def on_btn_start_clicked(self):
        if self.linkEdit.text() == '' and not self.dest == None:
            print('error')
        else:
            url = self.linkEdit.text()

            self.check_files_info(url, self.dest)

            for i in range(self.beginNum.value(), self.endNum.value() + 1):
                #Serial the url
                serialUrl = re.sub(r"\{\{(S)\}\}", str(i), url)

                #Ping the file
                self.file = SmartDL(serialUrl, self.dest, progress_bar=False)

                #Start the download
                self.file.start(blocking=False)

                self.infoList.item(0).setText('File at : ' + str(i) + ' / ' + str(self.endNum.value()))
                self.infoList.item(1).setText('Status : ' + self.file.get_status())

                tempFileName = ''
                while not self.file.isFinished():
                    #Get file name
                    fileName = urlparse(serialUrl)
                    fileName = os.path.basename(fileName.path)

                    #Log format
                    logText = fileName + ' ' + str(self.file.get_dl_size(human=True)) + ' / ' + str(self.file.get_final_filesize(human=True)) + ' @ ' + str(self.file.get_speed(human=True)) + ' [' + str(self.file.get_eta(human=True)) + ' ]'

                    self.totalDownloadedSize += self.file.get_dl_size()
                    self.infoList.item(3).setText('Total size : ' + str(self.file.get_dl_size(human=True)) + ' / ' + str(utils.sizeof_human(self.totalFinalDownload)))

                    #Check and add to the list log
                    if(fileName == tempFileName):
                        self.logList.item(self.logList.count() - 1).setText(logText)
                    else:
                        self.logList.addItem(logText)
                        tempFileName = fileName

                    self.downloadBar.setValue(self.totalDownloadedSize / self.totalFinalDownload)
                    self.infoList.repaint()
                    self.logList.repaint()
                    QtWidgets.QApplication.processEvents()

                #Download is finished
                if(self.file.isSuccessful()):
                    print('File succesfully downloaded!')
                else:
                    print('There was some error! :')
                    for e in self.file.get_errors():
                        print(str(e))


    def on_btn_stop_clicked(self):
        if not (self.file == None):
            self.file.stop()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
