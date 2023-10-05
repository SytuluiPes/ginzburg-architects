from sys import argv, exit
from PyQt5.QtCore import Qt
from ui import *
from docxtpl import DocxTemplate
import os
from re import sub, split
from PyQt5.QtWidgets import QMessageBox, QComboBox, QHeaderView
from webbrowser import open as op
from json import dump, load
from datetime import datetime
from time import time

class custom_combo_box(QComboBox):
    def init(self, parent=None):
        super(custom_combo_box, self).init(parent)

    def wheelEvent(self, event):
        event.ignore()


class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadTablePD()
        self.loadTableWorker()
        self.ui.radioButton_PD.clicked.connect(self.confirm_change_tableWidget)
        self.ui.radioButton_RD.clicked.connect(self.confirm_change_tableWidget)
        self.ui.buttonDelete.clicked.connect(self.del_row)
        self.ui.buttonGenerate.clicked.connect(self.generate)
        self.ui.buttonFolder.clicked.connect(self.go_to_folder)
        self.ui.buttonSave.clicked.connect(self.save)
        self.ui.buttonLoad.clicked.connect(self.load)
        self.ui.buttonDrop.clicked.connect(lambda: self.drop(True))
        self.ui.buttonEdit.clicked.connect(self.show_window_edit)
        self.ui.buttonAdd.clicked.connect(self.add_row)
        self.ui.buttonAdd.setToolTip("Добавить строку")
        self.ui.buttonDelete.setToolTip("Удалить строку")
        self.ui.buttonFolder.setToolTip("Перейти к расположению")
        self.ui.buttonSave.setToolTip("Сохранить")
        self.ui.buttonLoad.setToolTip("Загрузить")
        self.ui.buttonDrop.setToolTip("Сбросить")
    def loadTableWorker(self):
        with open("same_config.json", "r") as f:
            data = load(f)
        self.ui.tableWidget_2.setColumnCount(2)
        self.ui.tableWidget_2.setHorizontalHeaderLabels(("Должность", "Фамилия И.О."))
        self.ui.tableWidget_2.resizeColumnsToContents()
        self.ui.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_2.setRowCount(self.ui.spinBox.value())
        combo_box5 = custom_combo_box()
        combo_box5.addItems(data["Должность"])
        self.ui.tableWidget_2.setCellWidget(0, 0, combo_box5)
        self.ui.spinBox.valueChanged.connect(self.spinbox)

    def confirm_change_tableWidget(self):
        if self.ui.tableWidget.rowCount() > 0:
            info = QMessageBox()
            info.setWindowTitle("Подтверждение")
            info.setText("Текущие поля таблицы будут очищены!\nВы уверены, что хотите продолжить?")
            info.setWindowIcon(QtGui.QIcon("img/err.png"))
            info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            answer = info.exec_()
            if answer == QMessageBox.Ok:
                if self.ui.tableWidget.columnCount() == 6:
                    self.loadTableRD()
                else:
                    self.loadTablePD()
            else:
                if self.sender().objectName() == "radioButton_PD":
                    self.ui.radioButton_RD.setChecked(True)
                else:
                    self.ui.radioButton_PD.setChecked(True)
        else:
            if self.ui.tableWidget.columnCount() == 6:
                self.loadTableRD()
            else:
                self.loadTablePD()
    def loadTablePD(self):
        self.ui.radioButton_PD.setChecked(True)
        self.ui.radioButton_PD.setDisabled(True)
        self.ui.radioButton_RD.setEnabled(True)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(6)
        self.ui.tableWidget.setHorizontalHeaderLabels(("Раздел", "Номер части",
                                                       "Номер книги",
                                                       "Название части", "Здание / Секция",
                                                       "Обозначение"))
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.setColumnWidth(0, 250)
        self.ui.tableWidget.setColumnWidth(3, 250)

    def loadTableRD(self):
        self.ui.radioButton_RD.setChecked(True)
        self.ui.radioButton_RD.setDisabled(True)
        self.ui.radioButton_PD.setEnabled(True)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(("Название раздела", "Обозначение"))
        self.ui.tableWidget.resizeRowsToContents()
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.setColumnWidth(0, 700)

    def generate(self):
        rowCount = self.ui.tableWidget.rowCount()
        rowCount2 = self.ui.tableWidget_2.rowCount()
        if rowCount == 0:
            error("Разделы не выбраны!")
        elif rowCount2 == 0:
            error("Исполнители не указаны!")
        else:
            columnCount = self.ui.tableWidget.columnCount()
            path = os.path.join(os.path.join(os.path.expanduser("~")), "Desktop")
            os.makedirs(os.path.join(path, "Титульники"), exist_ok=True)
            path += "/Титульники"
            flag_folder = True
            table, projectList, workerList, doc, split1 = [], [], [], False, []
            projectList.append(self.ui.lineEditCustomer.text())  # Добавляем заказчика projectList[0]
            projectList.append(self.ui.lineEditContract.text())  # Добавляем номер договора projectList[1]
            projectList.append(self.ui.lineEditProject.text())  # Добавляем название объекта projectList[2]
            projectList.append(self.ui.lineEditLetter.text())  # Добавляем номер выписки projectList[3]
            projectList.append(self.ui.lineEditDateLetter.text())  # Добавляем дату выписки projectList[4]
            data_save = str(datetime.fromtimestamp(time()))
            for o in range(rowCount2):
                for j in range(self.ui.tableWidget_2.columnCount()):
                    if j == 0:
                        try:
                            workerList.append(self.ui.tableWidget_2.cellWidget(o, j).currentText())
                        except AttributeError:
                            workerList.append("")
                    else:
                        try:
                            workerList.append(self.ui.tableWidget_2.item(o, j).text())
                        except AttributeError:
                            workerList.append("")
            for o in range(8 - len(workerList)):
                workerList.append("")
            for o in range(len(projectList) - 2):  # для всех полей меняем кавычки
                projectList[o] = sub(r'"', "«", projectList[o], count=1)
                projectList[o] = sub(r'"', "»", projectList[o], count=1)
            ################################################################################################## КАВЫЧКИ
            for ii in range(rowCount):
                for j in range(columnCount):
                    if columnCount == 6:
                        if j == 0:  # Разбиваем раздел на номер, название, подраздел и название подраздела
                            try:
                                split1.append(split(r"\.\s",
                                                    self.ui.tableWidget.cellWidget(ii, j).currentText(), maxsplit=2))
                                table.append(self.ui.tableWidget.cellWidget(ii, j).currentText())
                            except AttributeError:
                                table.append("")
                        elif 1 <= j <= 3:  # считывание для комбобоксов
                            try:
                                table.append(self.ui.tableWidget.cellWidget(ii, j).currentText())
                            except AttributeError:
                                table.append("")
                        else:
                            try:  # считывание для текстовых полей
                                table.append(self.ui.tableWidget.item(ii, j).text())
                            except AttributeError:  # обработка пустых полей
                                table.append("")
                    else:
                        try:
                            table.append(self.ui.tableWidget.item(ii, j).text())
                        except AttributeError:  # обработка пустых полей
                            table.append("")
                if flag_folder:
                    if projectList[2] == "":
                        error('Название объекта не указано!')
                        return
                    else:
                        if columnCount == 6:
                            if len(projectList[2]) > 80:
                                os.makedirs(os.path.join(path, f"ПД_{projectList[2][0:80]}"), exist_ok=True)
                                path += f"/ПД_{projectList[2][0:80]}"
                            else:
                                os.makedirs(os.path.join(path, f"ПД_{projectList[2]}"), exist_ok=True)
                                path += f"/ПД_{projectList[2]}"
                        else:
                            if len(projectList[2]) > 80:
                                os.makedirs(os.path.join(path, f"РД_{projectList[2][0:80]}"), exist_ok=True)
                                path += f"/РД_{projectList[2][0:80]}"
                            else:
                                os.makedirs(os.path.join(path, f"РД_{projectList[2]}"), exist_ok=True)
                                path += f"/РД_{projectList[2]}"
                print(table)
                print(split1)
                if columnCount == 6 and table[ii * 6][0:8] == "Раздел 5":
                    doc = DocxTemplate("templates/PD_5.docx")
                elif columnCount == 6:
                    doc = DocxTemplate("templates/PD.docx")
                else:
                    doc = DocxTemplate("templates/RD.docx")
                org = "«Гинзбург Архитектс»"
                if self.ui.comboBoxOrg.currentText() == "ООО АРБ ГА":
                    doc.replace_pic("GA.png", "templates/ARB.png")
                    org = "Архитектурно-Реставрационное Бюро «Гинзбург Архитектс»"
                elif self.ui.comboBoxOrg.currentText() == "ООО ГиА":
                    doc.replace_pic("GA.png", "templates/GIA.png")
                    org = "«Гинзбург и Архитекторы»"
                projectList.append(org)              # Добавляем название организации projectList[5]
                projectList.append(data_save[0:19])  # Добавляем дату сохранения файла projectList[6]
                if columnCount == 6:
                    print(table[ii * 6][0:8])
                    if table[ii * 6][0:8] == "Раздел 5":
                        context = {"organization": projectList[5], "letter": projectList[3], "dateLetter": projectList[4],
                                   "customer": projectList[0], "contract": projectList[1],
                                   "projectName": projectList[2],
                                   "chapterNum": split1[ii][0], "subsectionNum": split1[ii][1],
                                   "subsectionName": split1[ii][2], "partNum": table[ii * 6 + 1],
                                   "bookNum": table[ii * 6 + 2], "partName": table[ii * 6 + 3],
                                   "building": table[ii * 6 + 4], "mark": table[ii * 6 + 5], "role1": workerList[0],
                                   "name1": workerList[1], "role2": workerList[2], "name2": workerList[3],
                                   "role3": workerList[4], "name3": workerList[5], "role4": workerList[6],
                                   "name4": workerList[7]}
                    else:
                        context = {"organization": projectList[5], "letter": projectList[3], "dateLetter": projectList[4],
                                   "customer": projectList[0], "contract": projectList[1],
                                   "projectName": projectList[2],
                                   "chapterNum": split1[ii][0], "chapterName": split1[ii][1],
                                   "partNum": table[ii * 6 + 1],
                                   "bookNum": table[ii * 6 + 2], "partName": table[ii * 6 + 3],
                                   "building": table[ii * 6 + 4], "mark": table[ii * 6 + 5], "role1": workerList[0],
                                   "name1": workerList[1], "role2": workerList[2], "name2": workerList[3],
                                   "role3": workerList[4], "name3": workerList[5], "role4": workerList[6],
                                   "name4": workerList[7]}
                else:
                    context = {"organization": projectList[5], "letter": projectList[3], "dateLetter": projectList[4],
                               "customer": projectList[0], "contract": projectList[1],
                               "projectName": projectList[2],
                               "chapterName": table[ii * 2], "mark": table[ii * 2 + 1],
                               "role1": workerList[0], "name1": workerList[1], "role2": workerList[2],
                               "name2": workerList[3], "role3": workerList[4], "name3": workerList[5],
                               "role4": workerList[6], "name4": workerList[7]}
                doc.render(context)
                if columnCount == 6:
                    if table[ii * 6][0:8] == "Раздел 5":
                        doc.save(f"{path}/{split1[ii][0]} {split1[ii][1]} {split1[ii][2]} ({ii + 1}).docx")
                    else:
                        doc.save(f"{path}/{split1[ii][0]} {split1[ii][1]} ({ii + 1}).docx")
                else:
                    doc.save(f"{path}/{table[ii * 2]} ({ii + 1}).docx")
                flag_folder = False
                self.setWindowTitle(f"Генератор документов - Генерация {100 / rowCount * (ii + 1)} %")
            self.setWindowTitle("Генератор документов - Генерация завершена")
            self.save(False)
            info("Файлы успешно сгенерированы!")
            self.setWindowTitle("Генератор документов")
    def add_row(self):
        with open("same_config.json", "r") as f:
            data = load(f)
        print(self.ui.tableWidget.columnCount())
        for i in range(10):
            if self.ui.tableWidget.columnCount() == 6:
                rowCount = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(rowCount)
                combo_box1 = custom_combo_box()
                combo_box1.addItems(data["Раздел"])
                self.ui.tableWidget.setCellWidget(rowCount, 0, combo_box1)

                combo_box2 = custom_combo_box()
                combo_box2.setEditable(True)
                combo_box2.addItems(data["Номер части"])
                self.ui.tableWidget.setCellWidget(rowCount, 1, combo_box2)

                combo_box3 = custom_combo_box()
                combo_box3.setEditable(True)
                combo_box3.addItems(data["Номер книги"])
                self.ui.tableWidget.setCellWidget(rowCount, 2, combo_box3)

                combo_box4 = custom_combo_box()
                combo_box4.setEditable(True)
                combo_box4.addItems(data["Название части"])
                self.ui.tableWidget.setCellWidget(rowCount, 3, combo_box4)
            else:
                rowCount = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(rowCount)
    def del_row(self):
        rowCount = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.removeRow(rowCount - 1)

    def load(self):
        global flag
        removePD, removeRD = [], []
        flag = True
        with open("saves.json", "r") as f:
            data = load(f)
        widget = QtWidgets.QDialog()
        widget.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)  # убирает значок вопроса с верхней панели
        ui = Ui_Window_Saves()
        ui.setupUi(widget)
        with open("styles.qss", "r") as styles:
            widget.setStyleSheet(styles.read())
        widget.setWindowTitle("Загрузить")
        widget.setWindowIcon(QtGui.QIcon("img/320842.png"))
        ui.tableWidget.setColumnCount(2)
        ui.tableWidget.setHorizontalHeaderLabels(("Наименование объекта", "Дата сохранения"))
        ui.tableWidget.resizeColumnsToContents()
        ui.tableWidget.resizeRowsToContents()
        ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        ui.tableWidget.setColumnWidth(0, 600)
        ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        if self.ui.radioButton_PD.isChecked() == True:
            keys = list(data["Проектная документация"].keys())
            for i in range(len(keys)):
                ui.tableWidget.insertRow(ui.tableWidget.rowCount())
                ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(keys[i]))
                ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(
                    data["Проектная документация"][f"{keys[i]}"].get("save_time")))
                ui.tableWidget.item(i, 1).setFlags(Qt.ItemIsEnabled)
            ui.radioButton_PD.setChecked(True)
            ui.radioButton_PD.setDisabled(True)
        else:
            keys = list(data["Рабочая документация"].keys())
            for i in range(len(keys)):
                ui.tableWidget.insertRow(ui.tableWidget.rowCount())
                ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(keys[i]))
                ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(
                    data["Рабочая документация"][f"{keys[i]}"].get("save_time")))
                ui.tableWidget.item(i, 1).setFlags(Qt.ItemIsEnabled)
            ui.radioButton_RD.setChecked(True)
            ui.radioButton_RD.setDisabled(True)
        if ui.tableWidget.rowCount() == 0:
            ui.pushButtonDelete.setDisabled(True)
        else:
            ui.pushButtonDelete.setEnabled(True)
        def update_table():
            if flag:
                with open('saves.json', 'r') as f:
                    data = load(f)
            else:
                with open('saves.json', 'r') as f:
                    data = load(f)
                for i in removePD:
                    try:
                        data['Проектная документация'].pop(i)
                    except KeyError:
                        pass
                for i in removeRD:
                    try:
                        data['Рабочая документация'].pop(i)
                    except KeyError:
                        pass
            ui.tableWidget.setRowCount(0)
            if ui.radioButton_PD.isChecked() == True:
                keys = list(data["Проектная документация"].keys())
                for i in range(len(keys)):
                    ui.tableWidget.insertRow(ui.tableWidget.rowCount())
                    ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(keys[i]))
                    ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(
                        data["Проектная документация"][f"{keys[i]}"].get("save_time")))
                    ui.tableWidget.item(i, 1).setFlags(Qt.ItemIsEnabled)
                ui.radioButton_PD.setDisabled(True)
                ui.radioButton_RD.setEnabled(True)
            else: # iu.radioButton_RD.isChecked() == False:
                keys = list(data["Рабочая документация"].keys())
                for i in range(len(keys)):
                    ui.tableWidget.insertRow(ui.tableWidget.rowCount())
                    ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(keys[i]))
                    ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(
                        data["Рабочая документация"][f"{keys[i]}"].get("save_time")))
                    ui.tableWidget.item(i, 1).setFlags(Qt.ItemIsEnabled)
                ui.radioButton_RD.setDisabled(True)
                ui.radioButton_PD.setEnabled(True)
            if ui.tableWidget.rowCount() == 0:
                ui.pushButtonDelete.setDisabled(True)
            else:
                ui.pushButtonDelete.setEnabled(True)
        def delete():
            global flag
            flag = False
            answer = confirm(f"\"{ui.tableWidget.currentItem().data(0)}\" будет удален!\n"
                             f"Вы уверены, что хотите продолжить?")
            if answer == QMessageBox.Ok and ui.radioButton_PD.isChecked():
                with open('same_saves.json', 'r') as f:
                    data = load(f)
                try:
                    data['Проектная документация'].pop(ui.tableWidget.currentItem().data(0))
                except KeyError:
                    pass
                with open('same_saves.json', 'w') as f:
                    dump(data, f, indent=2)
                removePD.append(ui.tableWidget.currentItem().data(0))
                ui.tableWidget.removeRow(ui.tableWidget.currentRow())
                if ui.tableWidget.rowCount() == 0:
                    ui.pushButtonDelete.setDisabled(True)
                else:
                    ui.pushButtonDelete.setEnabled(True)
            elif answer == QMessageBox.Ok and ui.radioButton_RD.isChecked():
                with open('same_saves.json', 'r') as f:
                    data = load(f)
                try:
                    data['Рабочая документация'].pop(ui.tableWidget.currentItem().data(0))
                except KeyError:
                    pass
                with open('same_saves.json', 'w') as f:
                    dump(data, f, indent=2)
                removeRD.append(ui.tableWidget.currentItem().data(0))
                ui.tableWidget.removeRow(ui.tableWidget.currentRow())
                if ui.tableWidget.rowCount() == 0:
                    ui.pushButtonDelete.setDisabled(True)
                else:
                    ui.pushButtonDelete.setEnabled(True)
            else:
                pass
        def save_finnaly():
            with open('saves.json', 'r') as f:
                data = load(f)
            for item in removePD:
                try:
                    data['Проектная документация'].pop(item)
                except KeyError:
                    pass
            for item in removeRD:
                try:
                    data['Рабочая документация'].pop(item)
                except KeyError:
                    pass
            with open('saves.json', 'w') as f:
                dump(data, f, indent=2)
            info('Изменения применены!')
        def save_cancel():
            global flag
            flag = True
            with open('saves.json', 'r') as f:
                data = load(f)
            with open('same_saves.json', 'w') as f:
                dump(data, f, indent=2)
            info('Изменения отменены!')
            update_table()
        def load_save():
            if ui.tableWidget.currentColumn() == 1:
                pass
            else:
                save_name = ui.tableWidget.currentItem().text()
                pd = ui.radioButton_PD.isChecked()
                widget.close()
                if pd:
                    table = 'Проектная документация'
                    self.ui.radioButton_PD.setChecked(True)
                    self.ui.radioButton_PD.setDisabled(True)
                    self.ui.radioButton_RD.setEnabled(True)
                else:
                    table = 'Рабочая документация'
                    self.ui.radioButton_RD.setChecked(True)
                    self.ui.radioButton_RD.setDisabled(True)
                    self.ui.radioButton_PD.setEnabled(True)
                with open('saves.json', 'r') as f:
                    data = load(f)
                self.drop(False)
                self.ui.comboBoxOrg.setCurrentText(data[f'{table}'][f'{save_name}']['projectList'][5])
                self.ui.lineEditLetter.setText(data[f'{table}'][f'{save_name}']['projectList'][3])
                self.ui.lineEditDateLetter.setText(data[f'{table}'][f'{save_name}']['projectList'][4])
                self.ui.lineEditCustomer.setText(data[f'{table}'][f'{save_name}']['projectList'][0])
                self.ui.lineEditProject.setText(data[f'{table}'][f'{save_name}']['projectList'][2])
                self.ui.lineEditContract.setText(data[f'{table}'][f'{save_name}']['projectList'][1])
                with open('config.json','r') as f:
                    data_save = load(f)
                for item in range(len(data[f'{table}'][f'{save_name}']['workerList'])):
                    if data[f'{table}'][f'{save_name}']['workerList'][item] != '':
                        if item % 2 == 0:
                            self.ui.tableWidget_2.insertRow(self.ui.tableWidget_2.rowCount())
                            combo_box5 = custom_combo_box()
                            combo_box5.addItems(data_save["Должность"])
                            self.ui.tableWidget_2.setCellWidget(item // 2, 0, combo_box5)
                            if data[f'{table}'][f'{save_name}']['workerList'][item] not in data_save["Должность"]:
                                combo_box5.addItem(data[f'{table}'][f'{save_name}']['workerList'][item])
                            combo_box5.setCurrentText(data[f'{table}'][f'{save_name}']['workerList'][item])
                        else:
                            self.ui.tableWidget_2.setItem(item // 2, 1, QtWidgets.QTableWidgetItem(
                                data[f'{table}'][f'{save_name}']['workerList'][item]))
                    else:
                        pass
                self.ui.spinBox.setValue(self.ui.tableWidget_2.rowCount())
                if pd:
                    self.loadTablePD()
                    for item in range(len(data[f'{table}'][f'{save_name}']['table'])):
                        if item % 6 == 0:
                            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
                            combo_box5 = custom_combo_box()
                            combo_box5.addItems(data_save["Раздел"])
                            self.ui.tableWidget.setCellWidget(item // 6, 0, combo_box5)
                            if data[f'{table}'][f'{save_name}']['table'][item] not in data_save["Раздел"]:
                                combo_box5.addItem(data[f'{table}'][f'{save_name}']['table'][item])
                            combo_box5.setCurrentText(data[f'{table}'][f'{save_name}']['table'][item])
                        elif item % 6 == 1:
                            combo_box5 = custom_combo_box()
                            combo_box5.addItems(data_save["Номер части"])
                            self.ui.tableWidget.setCellWidget(item // 6, 1, combo_box5)
                            if data[f'{table}'][f'{save_name}']['table'][item] not in data_save["Номер части"]:
                                combo_box5.addItem(data[f'{table}'][f'{save_name}']['table'][item])
                            combo_box5.setCurrentText(data[f'{table}'][f'{save_name}']['table'][item])
                        elif item % 6 == 2:
                            combo_box5 = custom_combo_box()
                            combo_box5.addItems(data_save["Номер книги"])
                            self.ui.tableWidget.setCellWidget(item // 6, 2, combo_box5)
                            if data[f'{table}'][f'{save_name}']['table'][item] not in data_save["Номер книги"]:
                                combo_box5.addItem(data[f'{table}'][f'{save_name}']['table'][item])
                            combo_box5.setCurrentText(data[f'{table}'][f'{save_name}']['table'][item])
                        elif item % 6 == 3:
                            combo_box5 = custom_combo_box()
                            combo_box5.addItems(data_save["Название части"])
                            self.ui.tableWidget.setCellWidget(item // 6, 3, combo_box5)
                            if data[f'{table}'][f'{save_name}']['table'][item] not in data_save["Название части"]:
                                combo_box5.addItem(data[f'{table}'][f'{save_name}']['table'][item])
                            combo_box5.setCurrentText(data[f'{table}'][f'{save_name}']['table'][item])
                        elif item % 6 == 4:
                            self.ui.tableWidget.setItem(item // 6, 4, QtWidgets.QTableWidgetItem(
                                data[f'{table}'][f'{save_name}']['table'][item]))
                        else:
                            self.ui.tableWidget.setItem(item // 6, 5, QtWidgets.QTableWidgetItem(
                                data[f'{table}'][f'{save_name}']['table'][item]))
                else:
                    self.loadTableRD()
                    for item in range(len(data[f'{table}'][f'{save_name}']['table'])):
                        if item % 2 == 0:
                            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
                            self.ui.tableWidget.setItem(item // 2, 0, QtWidgets.QTableWidgetItem(
                                data[f'{table}'][f'{save_name}']['table'][item]))
                        elif item % 2 == 1:
                            self.ui.tableWidget.setItem(item // 2, 1, QtWidgets.QTableWidgetItem(
                                data[f'{table}'][f'{save_name}']['table'][item]))
        ui.radioButton_PD.clicked.connect(update_table)
        ui.radioButton_RD.clicked.connect(update_table)
        ui.pushButtonDelete.clicked.connect(delete)
        ui.pushButtonSave.clicked.connect(save_finnaly)
        ui.pushButtonCancel.clicked.connect(save_cancel)
        ui.tableWidget.itemDoubleClicked.connect(load_save)
        widget.exec_()
    def save(self, flag=True):
        rowCount = self.ui.tableWidget.rowCount()
        rowCount2 = self.ui.tableWidget_2.rowCount()
        if self.ui.lineEditProject.text() == '':
            error('Название объекта не указано!')
        elif rowCount == 0:
            error("Разделы не выбраны!")
        elif rowCount2 == 0:
            error("Исполнители не указаны!")
        else:
            projectList, workerList, table = [], [], []
            projectList.append(self.ui.lineEditCustomer.text())  # Добавляем заказчика
            projectList.append(self.ui.lineEditContract.text())  # Добавляем номер договора
            projectList.append(self.ui.lineEditProject.text())  # Добавляем название объекта
            projectList.append(self.ui.lineEditLetter.text())  # Добавляем номер выписки
            projectList.append(self.ui.lineEditDateLetter.text())  # Добавляем дату выписки
            projectList.append(self.ui.comboBoxOrg.currentText())
            for o in range(self.ui.tableWidget_2.rowCount()):
                for j in range(self.ui.tableWidget_2.columnCount()):
                    if j == 0:
                        try:
                            workerList.append(self.ui.tableWidget_2.cellWidget(o, j).currentText())
                        except AttributeError:
                            workerList.append("")
                    else:
                        try:
                            workerList.append(self.ui.tableWidget_2.item(o, j).text())
                        except AttributeError:
                            workerList.append("")
            for o in range(8 - len(workerList)):
                workerList.append("")
            for ii in range(self.ui.tableWidget.rowCount()):
                for j in range(self.ui.tableWidget.columnCount()):
                    if self.ui.tableWidget.columnCount() == 6:
                        if j < 4:  # Разбиваем раздел на номер, название, подраздел и название подраздела
                            try:
                                table.append(self.ui.tableWidget.cellWidget(ii, j).currentText())
                            except AttributeError:
                                table.append("")
                        else:
                            try:  # считывание для текстовых полей
                                table.append(self.ui.tableWidget.item(ii, j).text())
                            except AttributeError:  # обработка пустых полей
                                table.append("")
                    else:
                        try:
                            table.append(self.ui.tableWidget.item(ii, j).text())
                        except AttributeError:  # обработка пустых полей
                            table.append("")
            with open("saves.json", "r") as f:
                data = load(f)
            data_save = str(datetime.fromtimestamp(time()))
            if self.ui.radioButton_PD.isChecked():
                data["Проектная документация"][f'{projectList[2]}'] = \
                {
                    "table": table,
                    "projectList": projectList,
                    "workerList": workerList,
                    "save_time": data_save[0:19]
                }
            else:
                data["Рабочая документация"][f'{projectList[2]}'] = \
                    {
                        "table": table,
                        "projectList": projectList,
                        "workerList": workerList,
                        "save_time": data_save[0:19]
                    }
            with open("saves.json", "w", encoding="utf-8") as f:
                dump(data, f, indent=2)
            if flag:
                info("Файлы успешно сохранены!")
            else:
                pass

    def go_to_folder(self):
        path = os.path.join(os.path.join(os.path.expanduser("~")), "Desktop")
        os.makedirs(os.path.join(path, "Титульники"), exist_ok=True)
        path += "\Титульники"
        path = sub(r"\\", "/", path)
        op(path)
    def spinbox(self):
        rowCount = self.ui.tableWidget_2.rowCount()
        spinValue = self.ui.spinBox.value()
        difference = spinValue - rowCount
        if difference > 0:
            for i in range(difference):
                rowCount = self.ui.tableWidget_2.rowCount()
                self.ui.tableWidget_2.insertRow(rowCount)
                with open("same_config.json", "r") as f:
                    data = load(f)
                combo_box5 = custom_combo_box()
                combo_box5.addItems(data["Должность"])
                self.ui.tableWidget_2.setCellWidget(rowCount, 0, combo_box5)
        else:
            for i in range(difference * -1):
                rowCount = self.ui.tableWidget_2.rowCount()
                self.ui.tableWidget_2.removeRow(rowCount - 1)

    def drop(self, conf=True):
        if conf:
            returnValue = confirm("Все поля будут очищены!\nВы уверены, что хотите продолжить?")
            if returnValue == QMessageBox.Ok:
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget_2.setRowCount(0)
                self.ui.lineEditCustomer.clear()
                self.ui.lineEditDateLetter.clear()
                self.ui.lineEditLetter.clear()
                self.ui.lineEditProject.clear()
                self.ui.lineEditContract.clear()
                self.ui.comboBoxOrg.setCurrentText("ООО ГА")
                self.ui.spinBox.setValue(0)
            else:
                pass
        else:
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget_2.setRowCount(0)

    def show_window_edit(self):
        with open("same_config.json", "r") as f:
            data = load(f)

        def setList():
            with open("same_config.json", "r") as f:
                data = load(f)
            global setList
            if ui.buttonAdd.isEnabled() == False:
                setList = ui.listWidget.currentIndex().data()
                ui.buttonAdd.setEnabled(True)
                ui.buttonDelete.setEnabled(True)
                ui.listWidget.clear()
                for value in data[setList]:
                    item = QtWidgets.QListWidgetItem(value)
                    item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)
                    ui.listWidget.addItem(item)

        def back():
            ui.buttonAdd.setEnabled(False)
            ui.buttonDelete.setEnabled(False)
            ui.listWidget.clear()
            ui.listWidget.addItems(list(data.keys()))

        def add():
            item = QtWidgets.QListWidgetItem("Введите значение")
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable)
            str = ui.listWidget.currentRow()
            ui.listWidget.insertItem(ui.listWidget.currentRow() + 1, item)
            save_list()
            ui.listWidget.setCurrentRow(str + 1)

        def delete():
            str = ui.listWidget.currentRow()
            ui.listWidget.takeItem(ui.listWidget.currentRow())
            save_list()
            ui.listWidget.setCurrentRow(str)

        def save_list():
            global setList
            with open("same_config.json", "r", encoding="utf-8") as f:
                data = load(f)
            data[setList].clear()
            list_items = []
            for i in range(ui.listWidget.count()):
                ui.listWidget.setCurrentRow(i)
                list_items.append(ui.listWidget.currentIndex().data())
            data[setList] = list_items
            print(data[setList])
            print(list_items)
            with open("same_config.json", "w", encoding="utf-8") as f:
                dump(data, f)

        def save_finnaly():
            with open("same_config.json", "r", encoding="utf-8") as f:
                data = load(f)
            with open("config.json", "w", encoding="utf-8") as f:
                dump(data, f)
            info("Изменения успешно применены!")
            widget.close()

        def save_cancel():
            with open("config.json", "r", encoding="utf-8") as f:
                data = load(f)
            with open("same_config.json", "w", encoding="utf-8") as f:
                dump(data, f)
            widget.close()
        widget = QtWidgets.QDialog()
        widget.setWindowFlags(QtCore.Qt.WindowCloseButtonHint) # убирает значок вопроса с верхней панели
        ui = Ui_Form()
        with open("styles.qss", "r") as styles:
            widget.setStyleSheet(styles.read())
        ui.setupUi(widget)
        widget.setWindowTitle("Радактор справочника")
        widget.setWindowIcon(QtGui.QIcon("img/320842.png"))
        ui.listWidget.addItems(list(data.keys()))
        ui.buttonAdd.setEnabled(False)
        ui.buttonDelete.setEnabled(False)

        ui.listWidget.itemDoubleClicked.connect(setList)
        ui.buttonAdd.clicked.connect(add)
        ui.buttonBack.clicked.connect(back)
        ui.buttonDelete.clicked.connect(delete)
        ui.listWidget.itemChanged.connect(save_list)
        ui.buttonSave.clicked.connect(save_finnaly)
        ui.buttonCancel.clicked.connect(save_cancel)

        widget.exec_()

def error(text_error):
    error = QMessageBox()
    error.setWindowTitle("Ошибка")
    error.setText(text_error)
    error.setWindowIcon(QtGui.QIcon("img/err.png"))
    error.setStandardButtons(QMessageBox.Ok)
    error.exec_()


def info(text_info):

    info = QMessageBox()
    info.setWindowTitle("Уведомление")
    info.setText(text_info)
    info.setWindowIcon(QtGui.QIcon("img/icons8-галочка-96.png"))
    info.setStandardButtons(QMessageBox.Ok)
    info.exec_()

def confirm(text_info):
    info = QMessageBox()
    info.setWindowTitle("Подтверждение")
    info.setText(text_info)
    info.setWindowIcon(QtGui.QIcon("img/err.png"))
    info.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    answer = info.exec_()
    return answer
def create_app():
    app = QtWidgets.QApplication(argv)
    win = window()
    with open("styles.qss", "r") as styles:
        win.setStyleSheet(styles.read())
    win.show()
    exit(app.exec_())


create_app()
