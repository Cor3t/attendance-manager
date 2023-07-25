import datetime

class StudentNotFound(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Student:
    def __init__(self, id, name, phoneNumber):
        self.id = id
        self.name = name
        self.phoneNumber = phoneNumber
        self.early = True
    
    def __str__(self) -> str:
        return self.name

class AttendanceSystem:
    def __init__(self) -> None:
        self.attendance_record = {}
        self.student_record = []

    def add_student(self, student: Student):
        for _student in self.student_record:
            if _student == student:
                raise Exception
        else:
            self.student_record.append(student)
  
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
        
student1 = Student(1, 'John', '234566')
student2 = Student(1, 'John', '234566')

manager = AttendanceSystem()

manager.add_student(student1)
manager.add_student(student2)

manager.mark_attendance(student1.id)
manager.mark_attendance(student2.id)

print(manager.student_record)
print(manager.attendance_record)