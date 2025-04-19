class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.marks = {}

    def add_marks(self, subject, marks):
        self.marks[subject] = marks

    def display_marks(self):
        print("Marks:")
        for subject, marks in self.marks.items():
            print(subject, marks)


class Teacher(Person):
    def __init__(self, name, age, teacher_id):
        super().__init__(name, age)
        self.teacher_id = teacher_id
student1=student("Alice",20,'5001')
student1.add_marks("Bap",85)