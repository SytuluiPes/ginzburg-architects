# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_saves.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.pushButtonCancel = QtWidgets.QPushButton(Window_Saves)
        self.pushButtonCancel.setMinimumSize(QtCore.QSize(0, 28))
        self.pushButtonCancel.setMaximumSize(QtCore.QSize(138, 28))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout_2.addWidget(self.pushButtonCancel)
        self.pushButtonSave = QtWidgets.QPushButton(Window_Saves)
        self.pushButtonSave.setMinimumSize(QtCore.QSize(0, 28))
        self.pushButtonSave.setMaximumSize(QtCore.QSize(138, 28))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout_2.addWidget(self.pushButtonSave)
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
        self.tableView = QtWidgets.QTableView(Window_Saves)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)

        self.retranslateUi(Window_Saves)
        QtCore.QMetaObject.connectSlotsByName(Window_Saves)

    def retranslateUi(self, Window_Saves):
        _translate = QtCore.QCoreApplication.translate
        Window_Saves.setWindowTitle(_translate("Window_Saves", "Form"))
        self.pushButtonDelete.setText(_translate("Window_Saves", "Удалить"))
        self.pushButtonCancel.setText(_translate("Window_Saves", "Сохранить изменения"))
        self.pushButtonSave.setText(_translate("Window_Saves", "Отменить изменения"))
        self.radioButton_PD.setText(_translate("Window_Saves", "Проектная документация"))
        self.radioButton_RD.setText(_translate("Window_Saves", "Рабочая документация"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window_Saves = QtWidgets.QWidget()
    ui = Ui_Window_Saves()
    ui.setupUi(Window_Saves)
    Window_Saves.show()
    sys.exit(app.exec_())
