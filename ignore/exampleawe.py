# from json xmport *
# PD = {"str1" : ["Раздел 1. Пояснительная записка", "Часть 1", "Книга 1",
#     "Состав проектной документации.", "Здание 1", "SFKQJTQ"],
#       "str2" : ["Раздел 2. Схема участка", "Часть 2", "Книга 2",
#     "Автоматизация и диспетчеризация инженерных систем.", "Здание 2", "SFdasdasTQ"],
#       "str3": ["Раздел 3. пуыощзе069", "Часть 3", "Книга 3",
#                "Исходная и разрешительная документация.", "Здание 3", "SFKQJdsaTQ"]}
# RD = {"str1" : ["Пояснительная записка", "SFKQJTQ"],
#       "str2" : ["Автоматизация и диспетчеризация инженерных систем.", "SFdasdasTQ"]}
# data = {}
# data["PD"] = PD
# data["RD"] = RD
# with open("session.json", "w", encoding="utf-8") as f:
#     dump(data, f)
# for i in range(len(data["PD"].keys())):
#     print(data["PD"][f"str{i + 1}"])
# with open("session.json", "r", encoding="utf-8") as f:
#     data = load(f)
# print(data)
# a = ("Раздел 5. Подраздел 3. «Система водоотведения»."
#      "Сведения об инженерном оборудовании, о сетях и системах инженерно-технического обеспечения")
# a = a.split(". ", maxsplit=3)
# print(a)
# print(a[0][0:9])


# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# import sys
# import time
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#     # method for creating widgets
#     def initUI(self):
#         self.pbar = QProgressBar(self)
#         self.pbar.setGeometry(30, 40, 200, 25)
#         self.btn = QPushButton("Start", self)
#         self.btn.move(40, 80)
#         self.btn.clicked.connect(self.doAction)
#         self.setGeometry(300, 300, 280, 170)
#         self.setWindowTitle("Python")
#         self.show()
#     def doAction(self):
#         for i in range(101):
#             time.sleep(0.05)
#             self.pbar.setValue(i)
#
# # if __name__ == "__main__":
# #     App = QApplication(sys.argv)
# #
# #     window = Example()
# #
# #     sys.exit(App.exec())
# import json
# import datetime
# from datetime import datetime
# from time import time
# str_json = """{"Проектная документация" : {},
#                "Рабочая документация" : {}}"""
# data = json.loads(str_json)
# data["Проектная документация"] = {"Парк в Сутугинской районе в г. Москве" : [{"projectList" : "LIST",
#                                                                            "workerList" : "WORK",
#                                                                            "table" : "TABLE"}]}
# new_json = json.dumps(data, indent=2)
# print(new_json)
# with open("saves.json", "r", encoding="utf-8") as f:
#     data = json.load(f)
# data_save = str(datetime.fromtimestamp(time()))
# data["Рабочая документация"]["project4"] = \
#     {"Сравнить все курсы по цене, рейтингу и отзывам в одном месте":
#     {
#                 "table": "table",
#                 "projectList": "projectList",
#                 "workerList": "workerList",
#                 "data_save" : data_save[0:19]
#     }
# }
# # print(data)
# # # data['Проектная документация'].pop('')
# # print(list(data["Рабочая документация"].keys()))
# print(data["Проектная документация"]["Добрый вечер, поздравляю с 10 летием на рынке ПО"]['workerList'][0])
# with open('config.json', 'r') as f:
#     jobs = json.load(f)
# print(jobs.keys())
# # with open("saves.json", "w", encoding="utf-8") as f:
# #     json.dump(data, f, indent=2)
# # with open("saves.json", "w") as f:
# #     json.dump(data, f, indent=2)
#
# def loadTablePD(self):
#     self.ui.radioButton_PD.setDisabled(True)
#     self.ui.radioButton_RD.setEnabled(True)
#     self.ui.tableWidget.setRowCount(0)
#     self.ui.tableWidget.setColumnCount(6)
#     self.ui.tableWidget.setHorizontalHeaderLabels(("Раздел", "Номер части",
#                                                    "Номер книги",
#                                                    "Название части", "Здание / Секция",
#                                                    "Обозначение"))
#     self.ui.tableWidget.resizeColumnsToContents()
#     self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
#     self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
#     self.ui.tableWidget.setColumnWidth(0, 250)
#     self.ui.tableWidget.setColumnWidth(3, 250)
#
#
# def loadTableRD(self):
#     self.ui.radioButton_RD.setDisabled(True)
#     self.ui.radioButton_PD.setEnabled(True)
#     self.ui.tableWidget.setRowCount(0)
#     self.ui.tableWidget.setColumnCount(2)
#     self.ui.tableWidget.setHorizontalHeaderLabels(("Название раздела", "Обозначение"))
#     self.ui.tableWidget.resizeRowsToContents()
#     self.ui.tableWidget.resizeColumnsToContents()
#     self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
#     self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
#     self.ui.tableWidget.setColumnWidth(0, 700)
# import re
# from docx import Document
#
# document = Document("exam.docx")
# matrix = []
# multi_space_pattern = re.compile(r' ')
# for table in document.tables:
#     for row in table.rows:
#         list_cycle = []
#         string = []
#         for i in row.cells:
#             name = multi_space_pattern.sub(' ', i.text.strip())
#             list_cycle.append(name)
#         if re.match("\d",list_cycle[0]): # 5.1.3
#             nums = re.split("\.", list_cycle[0], maxsplit=3) # ['1', '1']
#             if int(nums[0]) not in [5, 13]:
#                 if len(nums) >= 1:
#                     string.append(f"Раздел {nums[0]}.")
#                 if len(nums) >= 2:
#                     string.append(f"Часть {nums[1]}.")
#                 if len(nums) >= 3:
#                     string.append(f"Книга {nums[2]}.")
#             else:
#                 if len(nums) >= 2:
#                     string.append(f"Раздел {nums[0]}. Подраздел {nums[1]}.")
#                 if len(nums) >= 3:
#                     string.append(f"Часть {nums[2]}.")
#                 if len(nums) >= 4:
#                     string.append(f"Книга {nums[3]}.")
#             kostilb = re.split("\.\s", list_cycle[2], maxsplit=1)
#             string.append(kostilb[-1]) # Наименование части
#             string.append(list_cycle[1]) # Обозначение
#             matrix.append(string)
#
#
# for row in matrix:
#     for cell in row:
#         print(f"||{cell}||", end="\t")
#     print()

