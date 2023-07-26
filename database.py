import mysql.connector as sql
from attendance_system import Student

class DB:
    def __init__(self) -> None:
        self.__db = sql.connect(
            host='localhost',
            user='root',
            password='ROSEline123',
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

