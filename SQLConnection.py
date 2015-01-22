from PyQt4.QtSql import *
import sqlite3

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

    def find_ClasUnits(self):
        query = QSqlQuery()
        query.prepare("""SELECT * FROM ClassUnits""")
        query.exec_()
        return query

    def find_Units(self):
        query = QSqlQuery()
        query.prepare("""SELECT * FROM Units""")
        query.exec_()
        return query

    def find_UnitAssignments(self):
        query = QSqlQuery()
        query.prepare("""SELECT * FROM UnitAssignments""")
        query.exec_()
        return query

    def find_Assignmets(self):
        query = QSqlQuery()
        query.prepare("""SELECT * FROM Assignments""")
        query.exec_()
        return query

    def find_Teachers(self):
        query = QSqlQuery()
        query.prepare("""SELECT * FROM Teachers""")
        query.exec_()
        return query

    def find_ClassStudents(self):
        query = QSqlQuery()
        query.prepare("""SELECT * FROM ClassStudents""")
        query.exec_()
        return query

    def find_Students(self):
        query = QSqlQuery()
        query.prepare("""SELECT * FROM Students""")
        query.exec_()
        return query

    def find_Classes(self):
        query = QSqlQuery()
        query.prepare("""SELECT * FROM Classes""")
        query.exec_()
        return query

    def insert_Assignment(self,values):
        query = QSqlQuery()
        query.prepare("""insert into Assignments(AssignmentName,AssignmentMaxMark) values (?,?)""")
        query.addBindValue(values[0])
        query.addBindValue(values[1])
        query.exec_()
       
            
