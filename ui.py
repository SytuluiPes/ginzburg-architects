from PyQt5 import QtCore, QtGui, QtWidgets
generate_progress = 0

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(987, 837)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/320842.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.labelOrganization = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelOrganization.setFont(font)
        self.labelOrganization.setObjectName("labelOrganization")
        self.gridLayout.addWidget(self.labelOrganization, 0, 0, 1, 2)
        self.comboBoxOrg = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxOrg.sizePolicy().hasHeightForWidth())
        self.comboBoxOrg.setSizePolicy(sizePolicy)
        self.comboBoxOrg.setMinimumSize(QtCore.QSize(150, 26))
        self.comboBoxOrg.setMaximumSize(QtCore.QSize(150, 26))
        self.comboBoxOrg.setEditable(False)
        self.comboBoxOrg.setObjectName("comboBoxOrg")
        self.comboBoxOrg.addItem("")
        self.comboBoxOrg.addItem("")
        self.comboBoxOrg.addItem("")
        self.gridLayout.addWidget(self.comboBoxOrg, 0, 2, 1, 1)
        self.labelLetter = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelLetter.setFont(font)
        self.labelLetter.setObjectName("labelLetter")
        self.gridLayout.addWidget(self.labelLetter, 0, 3, 1, 1)
        self.lineEditLetter = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditLetter.setMinimumSize(QtCore.QSize(0, 26))
        self.lineEditLetter.setMaximumSize(QtCore.QSize(16777215, 26))
        self.lineEditLetter.setInputMask("")
        self.lineEditLetter.setText("")
        self.lineEditLetter.setObjectName("lineEditLetter")
        self.gridLayout.addWidget(self.lineEditLetter, 0, 4, 1, 1)
        self.labelDataLetter = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelDataLetter.setFont(font)
        self.labelDataLetter.setObjectName("labelDataLetter")
        self.gridLayout.addWidget(self.labelDataLetter, 0, 5, 1, 1)
        self.lineEditDateLetter = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDateLetter.setMinimumSize(QtCore.QSize(0, 26))
        self.lineEditDateLetter.setMaximumSize(QtCore.QSize(16777215, 26))
        self.lineEditDateLetter.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEditDateLetter.setCursorPosition(0)
        self.lineEditDateLetter.setClearButtonEnabled(False)
        self.lineEditDateLetter.setObjectName("lineEditDateLetter")
        self.gridLayout.addWidget(self.lineEditDateLetter, 0, 6, 1, 1)
        self.SmallTableLayout = QtWidgets.QGridLayout()
        self.SmallTableLayout.setContentsMargins(-1, -1, -1, 0)
        self.SmallTableLayout.setVerticalSpacing(5)
        self.SmallTableLayout.setObjectName("SmallTableLayout")
        self.labelCountWorker = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.labelCountWorker.setFont(font)
        self.labelCountWorker.setObjectName("labelCountWorker")
        self.SmallTableLayout.addWidget(self.labelCountWorker, 0, 0, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setMinimumSize(QtCore.QSize(62, 30))
        self.spinBox.setMaximumSize(QtCore.QSize(62, 30))
        self.spinBox.setMinimum(0)
        self.spinBox.setMaximum(4)
        self.spinBox.setObjectName("spinBox")
        self.SmallTableLayout.addWidget(self.spinBox, 0, 1, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(0, 140))
        self.tableWidget_2.setMaximumSize(QtCore.QSize(16777215, 140))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(26)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.SmallTableLayout.addWidget(self.tableWidget_2, 1, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.SmallTableLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout.addLayout(self.SmallTableLayout, 0, 7, 4, 1)
        self.labelCustomer = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.labelCustomer.setFont(font)
        self.labelCustomer.setObjectName("labelCustomer")
        self.gridLayout.addWidget(self.labelCustomer, 1, 0, 1, 1)
        self.lineEditCustomer = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCustomer.setMinimumSize(QtCore.QSize(0, 24))
        self.lineEditCustomer.setMaximumSize(QtCore.QSize(16777215, 24))
        self.lineEditCustomer.setObjectName("lineEditCustomer")
        self.gridLayout.addWidget(self.lineEditCustomer, 1, 1, 1, 6)
        self.labelContract = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.labelContract.setFont(font)
        self.labelContract.setObjectName("labelContract")
        self.gridLayout.addWidget(self.labelContract, 2, 0, 1, 1)
        self.lineEditContract = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditContract.sizePolicy().hasHeightForWidth())
        self.lineEditContract.setSizePolicy(sizePolicy)
        self.lineEditContract.setMinimumSize(QtCore.QSize(0, 24))
        self.lineEditContract.setMaximumSize(QtCore.QSize(16777215, 24))
        self.lineEditContract.setObjectName("lineEditContract")
        self.lineEditContract.setPlaceholderText('от "01" января 2000 г.')
        self.gridLayout.addWidget(self.lineEditContract, 2, 1, 1, 6)
        self.labelProject = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.labelProject.setFont(font)
        self.labelProject.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelProject.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelProject.setWordWrap(False)
        self.labelProject.setObjectName("labelProject")
        self.gridLayout.addWidget(self.labelProject, 3, 0, 1, 1)
        self.lineEditProject = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.lineEditProject.sizePolicy().hasHeightForWidth())
        self.lineEditProject.setSizePolicy(sizePolicy)
        self.lineEditProject.setMinimumSize(QtCore.QSize(0, 24))
        self.lineEditProject.setMaximumSize(QtCore.QSize(16777215, 24))
        self.lineEditProject.setObjectName("lineEditProject")
        self.gridLayout.addWidget(self.lineEditProject, 3, 1, 1, 6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.LeftBlock = QtWidgets.QHBoxLayout()
        self.LeftBlock.setObjectName("LeftBlock")
        self.buttonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAdd.setMinimumSize(QtCore.QSize(38, 34))
        self.buttonAdd.setMaximumSize(QtCore.QSize(38, 34))
        self.buttonAdd.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/icons8-плюс-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonAdd.setIcon(icon1)
        self.buttonAdd.setIconSize(QtCore.QSize(22, 22))
        self.buttonAdd.setObjectName("buttonAdd")
        self.LeftBlock.addWidget(self.buttonAdd)
        self.buttonDelete = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDelete.setMinimumSize(QtCore.QSize(38, 34))
        self.buttonDelete.setMaximumSize(QtCore.QSize(38, 34))
        self.buttonDelete.setText("")

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/icons8-минус-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonDelete.setIcon(icon2)
        self.buttonDelete.setIconSize(QtCore.QSize(22, 22))
        self.buttonDelete.setObjectName("buttonDelete")
        self.LeftBlock.addWidget(self.buttonDelete)
        self.buttonFolder = QtWidgets.QPushButton(self.centralwidget)
        self.buttonFolder.setEnabled(True)
        self.buttonFolder.setMinimumSize(QtCore.QSize(38, 34))
        self.buttonFolder.setMaximumSize(QtCore.QSize(38, 34))
        self.buttonFolder.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonFolder.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/icons8-папка-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonFolder.setIcon(icon3)
        self.buttonFolder.setIconSize(QtCore.QSize(22, 22))
        self.buttonFolder.setObjectName("buttonFolder")
        self.LeftBlock.addWidget(self.buttonFolder)
        self.buttonSave = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSave.setMinimumSize(QtCore.QSize(38, 34))
        self.buttonSave.setMaximumSize(QtCore.QSize(38, 34))
        self.buttonSave.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/icons8-сохранить-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonSave.setIcon(icon4)
        self.buttonSave.setIconSize(QtCore.QSize(22, 22))
        self.buttonSave.setObjectName("buttonSave")
        self.LeftBlock.addWidget(self.buttonSave)
        self.buttonLoad = QtWidgets.QPushButton(self.centralwidget)
        self.buttonLoad.setMinimumSize(QtCore.QSize(38, 34))
        self.buttonLoad.setMaximumSize(QtCore.QSize(38, 34))
        self.buttonLoad.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/icons8-скачать-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonLoad.setIcon(icon5)
        self.buttonLoad.setIconSize(QtCore.QSize(22, 22))
        self.buttonLoad.setObjectName("buttonLoad")
        self.LeftBlock.addWidget(self.buttonLoad)
        self.buttonDrop = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDrop.setMinimumSize(QtCore.QSize(38, 34))
        self.buttonDrop.setMaximumSize(QtCore.QSize(38, 34))
        self.buttonDrop.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/icons8-корзина-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonDrop.setIcon(icon6)
        self.buttonDrop.setIconSize(QtCore.QSize(22, 22))
        self.buttonDrop.setObjectName("buttonDrop")
        self.LeftBlock.addWidget(self.buttonDrop)
        self.horizontalLayout_4.addLayout(self.LeftBlock)
        self.RightBlock = QtWidgets.QHBoxLayout()
        self.RightBlock.setObjectName("RightBlock")
        self.RadioButtons = QtWidgets.QHBoxLayout()
        self.RadioButtons.setObjectName("RadioButtons")
        self.radioButton_PD = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_PD.setMinimumSize(QtCore.QSize(15, 40))
        self.radioButton_PD.setMaximumSize(QtCore.QSize(16777215, 40))
        self.radioButton_PD.setSizeIncrement(QtCore.QSize(0, 0))
        self.radioButton_PD.setBaseSize(QtCore.QSize(0, 0))
        self.radioButton_PD.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_PD.setAutoFillBackground(False)
        self.radioButton_PD.setIconSize(QtCore.QSize(25, 25))
        self.radioButton_PD.setChecked(True)
        self.radioButton_PD.setObjectName("radioButton_PD")
        self.RadioButtons.addWidget(self.radioButton_PD)
        self.radioButton_RD = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_RD.setMinimumSize(QtCore.QSize(0, 40))
        self.radioButton_RD.setMaximumSize(QtCore.QSize(16777215, 40))
        self.radioButton_RD.setObjectName("radioButton_RD")
        self.RadioButtons.addWidget(self.radioButton_RD)
        self.RightBlock.addLayout(self.RadioButtons)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.RightBlock.addItem(spacerItem1)
        self.buttonGenerate = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonGenerate.sizePolicy().hasHeightForWidth())
        self.buttonGenerate.setSizePolicy(sizePolicy)
        self.buttonGenerate.setMinimumSize(QtCore.QSize(0, 40))
        self.buttonGenerate.setMaximumSize(QtCore.QSize(16777215, 40))
        self.buttonGenerate.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.buttonGenerate.setObjectName("buttonGenerate")
        self.RightBlock.addWidget(self.buttonGenerate)
        self.buttonEdit = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.buttonEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.buttonEdit.setObjectName("buttonEdit")
        self.RightBlock.addWidget(self.buttonEdit)
        self.horizontalLayout_4.addLayout(self.RightBlock)
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 8)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 5, 0, 1, 8)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Генератор документов"))
        self.labelOrganization.setText(_translate("MainWindow", "Организация:"))
        self.comboBoxOrg.setItemText(0, _translate("MainWindow", "ООО ГА"))
        self.comboBoxOrg.setItemText(1, _translate("MainWindow", "ООО ГиА"))
        self.comboBoxOrg.setItemText(2, _translate("MainWindow", "ООО АРБ ГА"))
        self.labelLetter.setText(_translate("MainWindow", "Выписка №:"))
        self.labelDataLetter.setText(_translate("MainWindow", "Дата выписки:"))
        self.lineEditDateLetter.setPlaceholderText(_translate("MainWindow", "01.01.2000"))
        self.labelCountWorker.setText(_translate("MainWindow", "Количество исполнителей:"))
        self.labelCustomer.setText(_translate("MainWindow", "Заказчик:"))
        self.labelContract.setText(_translate("MainWindow", "Договор:"))
        self.labelProject.setText(_translate("MainWindow", "Название \n"
"проекта:"))
        self.radioButton_PD.setText(_translate("MainWindow", "Проектная \n"
"документация"))
        self.radioButton_RD.setText(_translate("MainWindow", "Рабочая \n"
"документация"))
        self.buttonGenerate.setText(_translate("MainWindow", "Сгенерировать \n"
"файлы"))
        self.buttonEdit.setText(_translate("MainWindow", "Редактировать \n"
"справочник"))

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(537, 394)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBack = QtWidgets.QPushButton(Form)
        self.buttonBack.setMinimumSize(QtCore.QSize(71, 28))
        self.buttonBack.setMaximumSize(QtCore.QSize(71, 28))
        self.buttonBack.setObjectName("Back")
        self.gridLayout.addWidget(self.buttonBack, 0, 0, 1, 1)
        self.buttonAdd = QtWidgets.QPushButton(Form)
        self.buttonAdd.setMinimumSize(QtCore.QSize(71, 28))
        self.buttonAdd.setMaximumSize(QtCore.QSize(71, 28))
        self.buttonAdd.setObjectName("Add")
        self.gridLayout.addWidget(self.buttonAdd, 0, 1, 1, 1)
        self.buttonDelete = QtWidgets.QPushButton(Form)
        self.buttonDelete.setMinimumSize(QtCore.QSize(71, 28))
        self.buttonDelete.setMaximumSize(QtCore.QSize(71, 28))
        self.buttonDelete.setObjectName("Delete")
        self.gridLayout.addWidget(self.buttonDelete, 0, 2, 1, 1)
        self.buttonSave = QtWidgets.QPushButton(Form)
        self.buttonSave.setMinimumSize(QtCore.QSize(0, 28))
        self.buttonSave.setMaximumSize(QtCore.QSize(16777215, 28))
        self.buttonSave.setObjectName("Save")
        self.gridLayout.addWidget(self.buttonSave, 0, 3, 1, 1)
        self.buttonCancel = QtWidgets.QPushButton(Form)
        self.buttonCancel.setMinimumSize(QtCore.QSize(0, 28))
        self.buttonCancel.setMaximumSize(QtCore.QSize(16777215, 28))
        self.buttonCancel.setObjectName("Cancel")
        self.gridLayout.addWidget(self.buttonCancel, 0, 4, 1, 1)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Редактор справочника"))
        self.buttonBack.setText(_translate("Form", "Назад"))
        self.buttonAdd.setText(_translate("Form", "Добавить"))
        self.buttonDelete.setText(_translate("Form", "Удалить"))
        self.buttonSave.setText(_translate("Form", "Сохранить изменения"))
        self.buttonCancel.setText(_translate("Form", "Отменить изменения"))

class Ui_Window_Saves(object):
    def setupUi(self, Window_Saves):
        Window_Saves.setObjectName("Window_Saves")
        Window_Saves.resize(807, 620)
        self.gridLayout = QtWidgets.QGridLayout(Window_Saves)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonDelete = QtWidgets.QPushButton(Window_Saves)
        self.pushButtonDelete.setMinimumSize(QtCore.QSize(71, 28))
        self.pushButtonDelete.setMaximumSize(QtCore.QSize(71, 28))
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.horizontalLayout_2.addWidget(self.pushButtonDelete)
        self.pushButtonSave = QtWidgets.QPushButton(Window_Saves)
        self.pushButtonSave.setMinimumSize(QtCore.QSize(0, 28))
        self.pushButtonSave.setMaximumSize(QtCore.QSize(138, 28))
        self.pushButtonSave.setObjectName("pushButtonCancel")
        self.horizontalLayout_2.addWidget(self.pushButtonSave)
        self.pushButtonCancel = QtWidgets.QPushButton(Window_Saves)
        self.pushButtonCancel.setMinimumSize(QtCore.QSize(0, 28))
        self.pushButtonCancel.setMaximumSize(QtCore.QSize(138, 28))
        self.pushButtonCancel.setObjectName("pushButtonSave")
        self.horizontalLayout_2.addWidget(self.pushButtonCancel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_PD = QtWidgets.QRadioButton(Window_Saves)
        self.radioButton_PD.setObjectName("radioButton_PD")
        self.horizontalLayout.addWidget(self.radioButton_PD)
        self.radioButton_RD = QtWidgets.QRadioButton(Window_Saves)
        self.radioButton_RD.setObjectName("radioButton_RD")
        self.horizontalLayout.addWidget(self.radioButton_RD)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Window_Saves)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.retranslateUi(Window_Saves)
        QtCore.QMetaObject.connectSlotsByName(Window_Saves)

    def retranslateUi(self, Window_Saves):
        _translate = QtCore.QCoreApplication.translate
        Window_Saves.setWindowTitle(_translate("Window_Saves", "Form"))
        self.pushButtonDelete.setText(_translate("Window_Saves", "Удалить"))
        self.pushButtonSave.setText(_translate("Window_Saves", "Сохранить изменения"))
        self.pushButtonCancel.setText(_translate("Window_Saves", "Отменить изменения"))
        self.radioButton_PD.setText(_translate("Window_Saves", "Проектная документация"))
        self.radioButton_RD.setText(_translate("Window_Saves", "Рабочая документация"))