from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
import sqlite3
import sys

from SQLConnection import *
from main_window import *

class CreateDbWidget(QWidget):
    cancel = pyqtSignal()
    """Layout for a widget to create and initialize a db file"""
    #constructor
    def __init__(self,parent):
        parent = parent
        super().__init__()
        self.createDdWidget_layout()

        #triggers
        self.cancel_button.clicked.connect(self.cancel_trigger)

    def createDdWidget_layout(self):
        self.main_label = QLabel("Create a New Database")
        self.DBname_label = QLabel("Enter file name: ")
        self.DBname_line_edit = QLineEdit()
        self.create_button = QPushButton("Create File")
        self.cancel_button = QPushButton("Cancel")
        
        self.layout = QGridLayout()
        self.layout.addWidget(self.main_label,0,0)
        self.layout.addWidget(self.DBname_label,1,0)
        self.layout.addWidget(self.DBname_line_edit,1,1)
        self.layout.addWidget(self.create_button,2,1)
        self.layout.addWidget(self.cancel_button,2,0)

        self.setLayout(self.layout)

    def cancel_trigger(self):
        self.parent.setLayout(self.stacked_layout.setCurrentIndex[1])
        
        
