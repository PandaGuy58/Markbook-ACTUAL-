from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
import sqlite3
import sys

from basic_widgets import *
from SQLConnection import *

class MainWindow(QMainWindow):
    """Main Window Layout"""
    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Markbook")
        self.resize(500,500)

        self.stackedLayout = QStackedLayout()

        self.widget = QWidget()

        self.widget.setLayout(self.stackedLayout)

        self.setCentralWidget(self.widget)

        #menu bar
        self.initialize_bar()
        #status bar

        #initial settings

        #create and add widgets to stackedlayout
        self.startWidget()
        self.createDBWidget()

    def initialize_bar(self):
        self.menu = QMenuBar()
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
        self.table_StudentAssignmentResult = QAction("Student Assignment Results",self)
        
        self.file_menu = self.menu.addMenu("File")
        self.table_menu = self.menu.addMenu("Tables")

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
        self.table_menu.addAction(self.table_StudentAssignmentResult)

        self.setMenuBar(self.menu)       


    def dbOpened(self):
        pass

    def dbClosed(self):
        pass

    #add widgets to stacked layout:

    def startWidget(self):
        self.start_widget = StartWidget(self)
        self.stackedLayout.addWidget(self.start_widget)

    def createDBWidget(self):
        self.createDBWidget = InputDBNameWidget()
        self.stackedLayout.addWidget(self.createDBWidget)
        
    def assignmentsLayout(self):
        pass

    def classesLayout(self):
        pass

    def classStudentsLayout(self):
        pass

    def classUnits(self):
        pass

    def teachersLayout(self):
        pass

    def studentsLayout(self):
        pass

    def studentAssignmentLayout(self):
        pass

    def unitsLayout(self):
        pass

    def unitAssignments(self):
        pass

    #actions

    def open_connection(self):
        path = QFileDialog.getOpenFileName()
        self.connection = SQLConnection(path)
        check = self.connection.open_database()

    def close_connection(self):
        self.connection.close_database()                   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    app.exec_()
