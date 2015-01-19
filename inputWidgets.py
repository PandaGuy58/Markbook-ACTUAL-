from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

class AssignmentInputWidget(QWidget):
    """Input tool to insert Assignment Records to db"""
    def __init__(self):
        super().__init__()
        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.create_assignment_layout()
        
    def create_assignment_layout(self):
        #widgets
        self.assignmentID_label = QLabel("AssignmentID:")
        self.assignmentName_label = QLabel("AssignmentName:")
        self.assignmentMark_label = QLabel("AssignmentMark:")
        self.assignmentMaxMark_label = QLabel("AssignmentMaxMark:")

        self.assignmentID_line_edit = QLineEdit()
        self.assignmentName_line_edit = QLineEdit()
        self.assignmentMark_line_edit = QLineEdit()
        self.assignmentMaxMark_line_edit = QLineEdit()

        self.add_assignment_button = QPushButton("Add Assignment")
        self.cancel_button = QPushButton("Cancel")

        #add widgets to the layout
        self.grid_layout = QGridLayout()
        
        self.grid_layout.addWidget(self.assignmentID_label,0,0)
        self.grid_layout.addWidget(self.assignmentID_line_edit,0,1)
        self.grid_layout.addWidget(self.assignmentName_label,1,0)
        self.grid_layout.addWidget(self.assignmentName_line_edit,1,1)
        self.grid_layout.addWidget(self.assignmentMark_label,2,0)
        self.grid_layout.addWidget(self.assignmentMark_line_edit,2,1)
        self.grid_layout.addWidget(self.assignmentMaxMark_label,3,0)
        self.grid_layout.addWidget(self.assignmentMaxMark_line_edit,3,1)
        self.grid_layout.addWidget(self.add_assignment_button,4,0)
        self.grid_layout.addWidget(self.cancel_button,5,0)

        self.display_widget = QWidget()
        self.display_widget.setLayout(self.grid_layout)
        self.stacked_layout.addWidget(self.display_widget)    

        
        
    
