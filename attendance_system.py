import datetime
import mysql.connector as sql
from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ.get('user')
password = os.environ.get('password')
host = os.environ.get('host')


class StudentNotFound(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Student:
    def __init__(self, id, first_name, last_name, phoneNumber):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phoneNumber = phoneNumber
    
    def __str__(self) -> str:
        return self.name

class DB:
    def __init__(self) -> None:
        self.__db = sql.connect(
            host=host,
            user=user,
            password=password,
            database='attendancemanager'
        )
        self.studentT = 'student'
        self.presentT = 'present'
        self.__cursor = self.__db.cursor()

    def add_new_student(self, student: Student):
        self.__cursor.execute(f'INSERT INTO {self.studentT} (first_name, last_name, phone_number) VALUES (%s, %s, %s)', (student.first_name, student.last_name, student.phoneNumber))      
        self.__db.commit()
    
    def all_student(self):
        self.__cursor.execute(f'SELECT * FROM {self.studentT}')
        return self.__cursor.fetchall()


class AttendanceSystem:
    def __init__(self) -> None:
        self.db = DB()
        self.attendance_record = {}
        self.student_record = []

    def add_student(self, student: Student):
        for _student in self.db.all_student():
            if _student[1] == student.first_name and _student[2] == student.last_name:
                raise Exception
        else:
            self.db.add_new_student(student)
  
    def mark_attendance(self, id):
        date = datetime.datetime.now().date()
        for student in self.student_record:
            if student.id == id:
                if date in self.attendance_record.keys():
                    self.attendance_record[date].append(student)
                else:
                    self.attendance_record[date] = [student]
                break
        else:
            raise StudentNotFound
        
    
        
student1 = Student(1, 'John', 'James', '234566')
student2 = Student(2, 'James', 'John', '234566')

manager = AttendanceSystem()
manager.add_student(student1)

