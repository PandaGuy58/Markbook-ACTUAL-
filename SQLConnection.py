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

    def find_ClassUnits(self):
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

    def find_StudentAssignmentResult(self):
        query = QSqlQuery()
        query.prepare("""Select * FROM StudentAssignmentResults""")
        query.exec_()
        return query


    def insert_Assignment(self,values):
        query = QSqlQuery()
        query.prepare("""INSERT into Assignments(AssignmentName,AssignmentMaxMark) values (?,?)""")
        query.addBindValue(values[0])
        query.addBindValue(values[1])
        query.exec_()

    def insert_ClassStudent(self,values):
        query = QSqlQuery()
        query.prepare("""INSERT into ClassStudents(StudentID,ClassID) values (?,?)""")
        query.addBindValue(values[0])
        query.addBindValue(values[1])
        query.exec_()

    def insert_ClassUnit(self,values):
        query = QSqlQuery()
        query.prepare("""INSERT into ClassUnits(ClassID,UnitID) values (?,?)""")
        query.addBindValue(values[0])
        query.addBindValue(values[1])
        query.exec_()

    def insert_Class(self,values):
        query = QSqlQuery()
        query.prepare("""INSERT into Classes(ClassName,TeacherID) values (?,?)""")
        query.addBindValue(values[0])
        query.addBindValue(values[1])
        query.exec_()

    def insert_Student(self,values):
        query = QSqlQuery()
        query.prepare("""INSERT into Students(StudentName,StudentSurname) values (?,?)""")
        query.addBindValue(values[0])
        query.addBindValue(values[1])
        query.exec_()

    def insert_Teacher(self,values):
        query = QSqlQuery()
        query.prepare("""INSERT into Teachers(TeacherName,TeacherSurname) values (?,?)""")
        query.addBindValue(values[0])
        query.addBindValue(values[1])
        query.exec_()

    def insert_UnitAssignment(self,values):
        query = QSqlQuery()
        query.prepare("""INSERT into UnitAssignments(UnitID,AssignmentID) values (?,?)""")
        query.addBindValue(values[0])
        query.addBindValue(values[1])
        query.exec_()
    
    def insert_Unit(self,values):
        query = QSqlQuery()
        query.prepare("""INSERT into Units(UnitName) values (?,)""")
        query.addBindValue(values[0])
        query.exec_()

    def insert_StudentAssignmentResult(self,values):
        query = QSqlQuery()
        query.prepare("""INSERT into StudentAssignmentResults(StudentID,AssignmentID,AssignmentMark) values (?,?,?)""")
        query.addBindValue(values[0])
        query.addBindValue(values[1])
        query.addBindValue(values[2])
        query.exec_()
            
