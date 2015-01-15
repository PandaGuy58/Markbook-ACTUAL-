from PyQt4.QtSql import *

class SQLConnection:
    """An SQL Connection class"""

    def __init__(self,path):
        self.path = path
        self.db = None

    def open_database(self):
        if self.db:
            self.close_database()
            
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.path)
        
        opened_ok = self.db.open()
        
        return opened_ok

    def close_database(self):
        self.db = None

    def find_ClasUnits(self,values):
        query = QSqlQuery()
        query.prepare("""SELECT * FROM ClasUnits WHERE ClassUnitID = ?""")
        query.addBindValue(values[0])
        query.exec_()
        return query

    def find_Units(self,values):
        query = QSqlQuery()
        query.prepare("""SELECT * FROM Units WHERE UnitID = ?""")
        query.addBindValue(values[0])
        query.exec_()
        return query

    def find_UnitAssignments(self,values):
        query = QSqlQuery()
        query.prepare("""SELECT * FROM UnitAssignments WHERE UnitAssignmentID = ?""")
        query.addBindValue(values[0])
        query.exec_()
        return query

    def find_Assignmets(self,values):
        query = QSqlQuery()
        query.prepare("""SELECT * FROM Assignmets WHERE AssignmentID = ?""")
        query.addBindValue(values[0])
        query.exec_()
        return query

    def find_Teachers(self,values):
        query = QSqlQuery()
        query.prepare("""SELECT * FROM Teachers WHERE TeacherID = ?""")
        query.addBindValue(values[0])
        query.exec_()
        return query

    def find_ClassStudents(self,values):
        query = QSqlQuery()
        query.prepare("""SELECT * FROM ClassStudents WHERE ClassStudentID = ?""")
        query.addBindValue(values[0])
        query.exec_()
        return query

    def find_Students(self,values):
        query = QSqlQuery()
        query.prepare("""SELECT * FROM Students WHERE StudentID = ?""")
        query.addBindValue(values[0])
        query.exec_()
        return query

    def find_Classes(self,values):
        query = QSqlQuery()
        query.prepare("""SELECT * FROM Classes WHERE ClassID = ?""")
        query.addBindValue(values[0])
        query.exec_()
        return query
