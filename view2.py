import uuid
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QTableWidget
from PyQt5.QtGui import QFont
from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from player import Player
from team import Team
from consts import TeamType
from model import Model
import datetime

import sqlite3

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('./resources/UI/manager.ui', self)
        # self.show()
        
        self.loadTable()
        self.loadComboBox()
                
        self.pushButton_add_player.clicked.connect(self.add_player)
        self.actionAdd_Player.triggered.connect(self.add_player)
        
        self.pushButton_remove_player.clicked.connect(self.remove_player)
        self.actionRemove_Player.triggered.connect(self.remove_player)
        
        self.actionAdd_Team.triggered.connect(self.add_team)
        
        self.actionRemove_Team.triggered.connect(self.remove_team)
        
        self.pushButton_save.clicked.connect(self.save)
        
        self.pushButton_print.clicked.connect(self.print)
        self.actionPrint.triggered.connect(self.print)
        
        self.actionClose.triggered.connect(self.close)        
        
        testTable = QTableWidget()
        testTable.selectionModel()
        
        self.tableWidget_players.selectionModel().selectionChanged.connect(self.loadForm)
        
    def add_player(self):
        pass
    
    def remove_player(self):
        pass
            
    def add_team(self):
        pass
    
    def remove_team(self):
        pass
    
    def save(self):
        pass
    
    def print(self):
        print(self)
        
    def close(self):
        exit()
        
    def loadForm(self, selectedPlayer):
        
        self.lineEdit_first_name.setText(self.tableWidget_players.item(self.tableWidget_players.currentRow(), 1).text())
        self.lineEdit_last_name.setText(self.tableWidget_players.item(self.tableWidget_players.currentRow(), 2).text())
        self.comboBox_select_team.setCurrentText(self.tableWidget_players.item(self.tableWidget_players.currentRow(), 3).text())
        # self.dateEdit_dob.setDate(self.tableWidget_players.item(self.tableWidget_players.currentRow(), 4).text())
        # self.graphicsView_player_picture.setPixmap(self.tableWidget_players.item(self.tableWidget_players.currentRow(), 5).text())

        for i in range(0, 7):
            print(self.tableWidget_players.item(self.tableWidget_players.currentRow(), i).text())
    
    def loadTable(self):
        tablerow = 0
        model = Model()
        # model.create_team(Team("12345", "team1", TeamType.MEN))
        # model.create_player(Player('1', 'John', 'Doe', "12345", datetime.date.today(), 'picture.png'))
        # model.create_player(Player('2', 'Jane', 'Doe', "12345", datetime.date.today(), 'picture.png'))
        # model.create_player(Player('3', 'Hyoungjin', 'Choi', "12345", datetime.date.today(), 'picture.png'))
        
        players = model.read_players()
        for player in players:
            self.tableWidget_players.setRowCount(len(players))

            self.tableWidget_players.setItem(tablerow, 0, QTableWidgetItem(player.player_id))
            self.tableWidget_players.setItem(tablerow, 1, QTableWidgetItem(player.first_name))
            self.tableWidget_players.setItem(tablerow, 2, QTableWidgetItem(player.last_name))
            self.tableWidget_players.setItem(tablerow, 3, QTableWidgetItem(player.player_team))
            self.tableWidget_players.setItem(tablerow, 4, QTableWidgetItem(player.dob))
            self.tableWidget_players.setItem(tablerow, 5, QTableWidgetItem(player.player_picture))
            self.tableWidget_players.setItem(tablerow, 6, QTableWidgetItem(str(player.player_active)))
            tablerow += 1
    
    def loadComboBox(self):
        pass
            
    def on_clicked(msg):
        message = QMessageBox()
        message.setText(msg)
        message.exec_()
            
def main():
    app = QApplication([])
    
    window = MyGUI()
    # app.exec_()
    # app = QApplication([])
    # window = QWidget()
    # window.setGeometry(100, 100, 200, 300)
    # window.setWindowTitle("My Simple GUI")
    
    # layout = QVBoxLayout()
    
    # table = QTableView()
    # model = QSqlQueryModel()
    # table.setGeometry(0, 0, 200, 300)
    # table.setModel(model)
    
    # layout.addWidget(table)
    
    # label = QLabel("Press The Button Below")
    # textbox = QTextEdit()
    # button = QPushButton("Press Me!")
    
    # button.clicked.connect(lambda: on_clicked(textbox.toPlainText()))
    
    # layout.addWidget(label)
    # layout.addWidget(textbox)
    # layout.addWidget(button)
    
    # window.setLayout(layout)
    
    
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()
    