from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
import sqlite3
import sys

from SQLConnection import *
from main_window import *

class AssignmentDeleteWidget(QWidget):
    """delete tool for assignments"""
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.create_layout()

        #triggers
        
    def create_layout(self):

        self.assignmentID_label = QLabel("AssignmentID: ")
        self.delete_button = QPushButton("Delete Assignment")
        self.assignmentID_ComboBox = QComboBox()

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.assignmentID_label)
        self.vertical_layout.addWidget(self.assignmentID_ComboBox)
        self.vertical_layout.addWidget(self.delete_button)

        self.values = self.parent.connection.find_assignmentIDs()
        
    
        
