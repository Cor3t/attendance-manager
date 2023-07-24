class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
    
    def format_data(self):
        return f'{self.id},{self.name},{self.age}\n'
    
    @classmethod
    def reformat_data(cls, data : str):
        data = data.strip('\n').split(',')
        id = data[0]
        name = data[1]
        age = data[2]
        return Student(id, name, age)

    def __str__(self):
        return self.format_data()
    
class StudentRecordManager:
    def add_student(self, student: Student):
        with open('student_data.txt', 'a') as f:
            f.write(student.format_data())

    def get_student(self, id):
        with open('student_data.txt', 'r') as f:
            student_data = f.readlines()
            if len(student_data) == 0:
                return 'No student in file'
            for student in student_data:
                if str(id) == student.split(',')[0]:
                    return Student.reformat_data(student)
            else:
                return 'Could not find student'

    def update_student(self, data: Student):

        with open('student_data.txt', 'r') as f:

            student_data = f.readlines()
            if len(student_data) == 0:
                return 'No student in file'
            updates = []

            for student in student_data:
                if str(data.id) == student.split(',')[0]:
                    updates.append(data.format_data())
                else:
                    updates.append(student)
        with open('student_data.txt', 'w') as f: 
            f.writelines(updates)

manager = StudentRecordManager()
student1 = Student(1,'John Mark', 20)
student2 = Student(2,'James Philip', 23)

print(manager.update_student(student2))