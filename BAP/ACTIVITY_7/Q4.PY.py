import sqlite3

def create_table():
    conn = sqlite3.connect('/Volumes/DRIVE/BAP/ACTIVITY_7/Q1.db')
    dog = conn.cursor()
    dog.execute("""CREATE TABLE IF NOT EXISTS students (
                        STUDENT_ID INTEGER PRIMARY KEY,
                        STUDENT_NAME TEXT,
                        STUDENT_GRADE TEXT
                    )""")
    conn.commit()
    conn.close()

def add_student():
    create_table()  # Ensure table exists
    conn = sqlite3.connect('/Volumes/DRIVE/BAP/ACTIVITY_7/Q1.db')
    dog = conn.cursor()
    name = input("Enter the student's name: ")
    grade = input("Enter the student's grade: ")
    dog.execute("INSERT INTO students (STUDENT_NAME, STUDENT_GRADE) VALUES (?, ?)", (name, grade))
    conn.commit()
    conn.close()

def update_grade():
    conn = sqlite3.connect('/Volumes/DRIVE/BAP/ACTIVITY_7/Q1.db')
    dog = conn.cursor()
    student_id = int(input("Enter the student ID to update grade: "))
    new_grade = input("Enter the new grade: ")
    dog.execute("UPDATE students SET STUDENT_GRADE = ? WHERE STUDENT_ID = ?", (new_grade, student_id))
    conn.commit()
    conn.close()

def view_students():
    conn = sqlite3.connect('/Volumes/DRIVE/BAP/ACTIVITY_7/Q1.db')
    dog = conn.cursor()
    dog.execute("SELECT * FROM students")
    students = dog.fetchall()
    for student in students:
        print("ID:", student[0])
        print("Name:", student[1])
        print("Grade:", student[2])
    conn.close()

def main():
    while True:
        print("\n1. Add Student")
        print("2. Update Grade")
        print("3. View Students")
        print("4. Exit")
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            add_student()
        elif choice == 2:
            update_grade()
        elif choice == 3:
            view_students()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
