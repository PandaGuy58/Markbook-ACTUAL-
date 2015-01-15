from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
import sqlite3
import sys

from SQLConnection import *
from DisplayTableWidget import *

class MainWindow(QMainWindow):
    """Main Window Layout"""
    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Markbook")
        self.resize(500,500)
        #actions
        #file
        self.new_database = QAction("New Database",self)
        self.open_a_database = QAction("Open a Databse",self)
        self.close_database = QAction("Close Database",self)
        self.exit = QAction("Exit",self)        

        #table
        self.table_Assignments = QAction("Assignments",self)
        self.table_ClassStudents = QAction("Class Students",self)
        self.table_ClassUnits = QAction("Class Units",self)
        self.table_Classes = QAction("Classes",self)
        self.table_Students = QAction("Students",self)
        self.table_Teachers = QAction("Teachers",self)
        self.table_UnitAssignments = QAction("Unit Assignments",self)
        self.table_Units = QAction("Units",self)        

        #add menu the application
        self.menu = QMenuBar()
        self.file_menu = self.menu.addMenu("File")
        self.table_menu = self.menu.addMenu("Tables")

        #add actions to menu
        self.file_menu.addAction(self.new_database)
        self.file_menu.addAction(self.open_a_database)
        self.file_menu.addAction(self.close_database)
        self.file_menu.addAction(self.exit)

        self.table_menu.addAction(self.table_Assignments)
        self.table_menu.addAction(self.table_ClassStudents)
        self.table_menu.addAction(self.table_ClassUnits)
        self.table_menu.addAction(self.table_Classes)
        self.table_menu.addAction(self.table_Students)
        self.table_menu.addAction(self.table_Teachers)
        self.table_menu.addAction(self.table_UnitAssignments)
        self.table_menu.addAction(self.table_Units)

        #initalize menu bar
        self.setMenuBar(self.menu)

        #initialize application
        self.dbNotConnected()

        #triggers
        self.open_a_database.triggered.connect(self.open_connection)
        self.close_database.triggered.connect(self.close_connection)

        #tables
        self.table_Assignments.triggered.connect(self.display_Assignments)
        self.table_ClassStudents.triggered.connect(self.display_ClassStudents)
        self.table_ClassUnits.triggered.connect(self.display_ClassUnits)
        self.table_Classes.triggered.connect(self.display_Classes)
        self.table_Students.triggered.connect(self.display_Students)
        self.table_Teachers.triggered.connect(self.display_Teachers)
        self.table_UnitAssignments.triggered.connect(self.display_UnitAssignments)
        self.table_Units.triggered.connect(self.display_Units)
        
    def open_connection(self):
        path = QFileDialog.getOpenFileName()
        self.connection = SQLConnection(path)
        check = self.connection.open_database()
        self.dbConnected()  #unlocks the toolbar

    def close_connection(self):
        self.connection.close_database()
        self.dbNotConnected()

    def new_connection(self):
        pass
        
    def dbConnected(self):
        self.table_menu.setEnabled(True)
        self.close_database.setEnabled(True)

    def dbNotConnected(self):
        self.table_menu.setEnabled(False)
        self.close_database.setEnabled(False)


    #view table methods:

    def display_ClassUnits(self):
        if not hasattr(self,'DisplayTableWidget'):
            self.display_widget = DisplayTableWidget()
        self.setCentralWidget(self.display_widget)
        query = self.connection.find_ClasUnits()
        self.display_widget.show_results(query)

    def display_Units(self):
        if not hasattr(self,'DisplayTableWidget'):
            self.display_widget = DisplayTableWidget()
        self.setCentralWidget(self.display_widget)
        query = self.connection.find_Units()
        self.display_widget.show_results(query)

    def display_UnitAssignments(self):
        if not hasattr(self,'DisplayTableWidget'):
            self.display_widget = DisplayTableWidget()
        self.setCentralWidget(self.display_widget)
        query = self.connection.find_UnitAssignments()
        self.display_widget.show_results(query)

    def display_Assignments(self):
        if not hasattr(self,'DisplayTableWidget'):
            self.display_widget = DisplayTableWidget()
        self.setCentralWidget(self.display_widget)
        query = self.connection.find_Assignmets()
        self.display_widget.show_results(query)

    def display_Teachers(self):
        if not hasattr(self,'DisplayTableWidget'):
            self.display_widget = DisplayTableWidget()
        self.setCentralWidget(self.display_widget)
        query = self.connection.find_Teachers()
        self.display_widget.show_results(query)

    def display_ClassStudents(self):
        if not hasattr(self,'DisplayTableWidget'):
            self.display_widget = DisplayTableWidget()
        self.setCentralWidget(self.display_widget)
        query = self.connection.find_ClassStudents()
        self.display_widget.show_results(query)

    def display_Students(self):
        if not hasattr(self,'DisplayTableWidget'):
            self.display_widget = DisplayTableWidget()
        self.setCentralWidget(self.display_widget)
        query = self.connection.find_Students()
        self.display_widget.show_results(query)

    def display_Classes(self):
        if not hasattr(self,'DisplayTableWidget'):
            self.display_widget = DisplayTableWidget()
        self.setCentralWidget(self.display_widget)
        query = self.connection.find_Classes()
        self.display_widget.show_results(query)

#-----------------------------------------------------------------
        
class InputDBNameWidget(QWidget):
    """Input widget for new db file"""
    def __init__(self):
        super().__init__()

    def OpenConnectionWidgetLayout(self):
        self.addCreateButton = QPushButton("Create Database")
        
        self.addCancelButton = QPushButton("Cancel")

        #self.addMessageBox = 
    

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()    
