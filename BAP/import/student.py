class Student:
    count = 0

    def __init__(self, name, age, branch, sem, marks):
        self.name = name
        self.age = age
        self.branch = branch
        self.sem = sem
        self.marks = marks
        self.grade = self.calculate_grade()
        Student.count += 1

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A+'
        elif self.marks in range(80, 90):
            return 'A'
        elif self.marks in range(70, 80):
            return 'B+'
        elif self.marks in range(60, 70):
            return 'B'
        else:
            return 'C'

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)
        print("Semester:", self.sem)
        print("Marks:", self.marks)
        print("Grade:", self.grade)


class StudentGradeSheet:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, branch, sem, marks):
        student = Student(name, age, branch, sem, marks)
        self.students.append(student)
        print("Student information added successfully.")

    def delete_student(self, name):
        for i, student in enumerate(self.students):
            if student.name == name:
                del self.students[i]
                print(f"Student with name {name} deleted successfully.")
                return
        print(f"No student found with name {name}.")

    def print_student_grade(self):
        if not self.students:
            print("No students in the database.")
            return
        print("Student Grade Sheet:")
        for student in self.students:
            student.display_info()

    def update_student(self, name, marks):
        for student in self.students:
            if student.name == name:
                student.marks = marks
                student.grade = student.calculate_grade()
                print(f"Student with name {name} marks updated successfully.")
                return
        print(f"No student found with name {name}.")

    def display_student(self, name):
        for student in self.students:
            if student.name == name:
                print("Student Information:")
                student.display_info()
                return
        print(f"No student found with name {name}.")


grade_sheet_manager = StudentGradeSheet()

while True:
    print("\nStudent Grade Sheet Management Menu:")
    print("1. Add student information")
    print("2. Delete student information")
    print("3. Print student grade sheet")
    print("4. Update student marks")
    print("5. Display student information")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        branch = input("Enter branch: ")
        sem = int(input("Enter semester: "))
        marks = int(input("Enter marks: "))
        grade_sheet_manager.add_student(name, age, branch, sem, marks)
    elif choice == "2":
        name = input("Enter student name to delete: ")
        grade_sheet_manager.delete_student(name)
    elif choice == "3":
        grade_sheet_manager.print_student_grade()
    elif choice == "4":
        name = input("Enter student name to update marks: ")
        marks = int(input("Enter updated marks: "))
        grade_sheet_manager.update_student(name, marks)
    elif choice == "5":
        name = input("Enter student name to display: ")
        grade_sheet_manager.display_student(name)
    elif choice == "6":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

print("\nTotal number of students:", Student.count)
