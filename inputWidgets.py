from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
import sqlite3
import sys

from SQLConnection import *
from main_window import *

class AssignmentInputWidget(QWidget):
    """Input tool to insert Assignment Records to db"""
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.create_assignment_layout()
        self.assignmentID_line_edit.setEnabled(False)
        self.assignmentMaxMark_line_edit.setEnabled(False)
        self.connection = parent.connection

        #triggers
        self.add_assignment_button.clicked.connect(self.insert_assignment_toDB)
        self.assignmentName_line_edit.returnPressed.connect(self.assignmentName_line_editSignal)

        #status bar       
        self.parent.statusBar.showMessage("Hello Input Widget")
        
    def create_assignment_layout(self):
        #widgets
        self.assignmentID_label = QLabel("AssignmentID:")
        self.assignmentName_label = QLabel("AssignmentName:")
        self.assignmentMaxMark_label = QLabel("AssignmentMaxMark:")

        self.assignmentID_line_edit = QLineEdit("Auto generated")
        self.assignmentName_line_edit = QLineEdit()
        self.assignmentMaxMark_line_edit = QSpinBox()

        self.add_assignment_button = QPushButton("Add Assignment")
        self.cancel_button = QPushButton("Cancel")

        #add widgets to the layout
        self.grid_layout = QGridLayout()
        
        self.grid_layout.addWidget(self.assignmentID_label,0,0)
        self.grid_layout.addWidget(self.assignmentID_line_edit,0,1)
        self.grid_layout.addWidget(self.assignmentName_label,1,0)
        self.grid_layout.addWidget(self.assignmentName_line_edit,1,1)
        self.grid_layout.addWidget(self.assignmentMaxMark_label,2,0)
        self.grid_layout.addWidget(self.assignmentMaxMark_line_edit,2,1)
        self.grid_layout.addWidget(self.add_assignment_button,3,0)
        self.grid_layout.addWidget(self.cancel_button,4,0)

        self.display_widget = QWidget()
        self.display_widget.setLayout(self.grid_layout)
        self.stacked_layout.addWidget(self.display_widget)

    def insert_assignment_toDB(self):
        self.values = (self.assignmentName_line_edit.text(),self.assignmentMaxMark_line_edit.text())       
        self.connection.insert_Assignment(self.values)

    def assignmentName_line_editSignal(self):
        if len(str(self.assignmentID_line_edit)) > 0:
            self.assignmentMaxMark_line_edit.setEnabled(True)

    def assignmentMaxMark_line_editSignal(self):
        try:
            int(self.assignmentMaxMark_label.text())
        except:
            self.parent.statusBar.showMessage("You must enter an integer!")

class ClassInputWidget(QWidget):
    """Input tool to insert Class Records to db"""
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.create_class_layout()

class ClassUnitInputWidget(QWidget):
    """Input tool to insert Assignment Records to db"""
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.create_classUnit_layout()

class UnitInputWidget(QWidget):
    """Input tool to insert Assignment Records to db"""
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.create_unit_layout()

class UnitAssignmentInputWidget(QWidget):
    """Input tool to insert Assignment Records to db"""
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.create_unitAssignment_layout()

class TeacherInputWidget(QWidget):
    """Input tool to insert Assignment Records to db"""
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.create_teacher_layout()

class ClassStudentInputWidget(QWidget):
    """Input tool to insert Assignment Records to db"""
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.create_classStudent_layout()

class StudentInputWidget(QWidget):
    """Input tool to insert Assignment Records to db"""
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.create_student_layout()

class StudentAssignmentResultInputWidget(QWidget):
    """Input tool to insert Assignment Records to db"""
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.create_studentAssignmentResult_layout()


            
            
        
        
        

        
        
    
