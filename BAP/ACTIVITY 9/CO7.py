import tkinter as tk
from tkinter import messagebox
import sqlite3

def create_table():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    admission_number TEXT NOT NULL,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    gender TEXT NOT NULL,
                    grade TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def insert_student(admission_number, name, age, gender, grade):
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute('''INSERT INTO students (admission_number, name, age, gender, grade) VALUES (?, ?, ?, ?, ?)''',
              (admission_number, name, age, gender, grade))
    conn.commit()
    conn.close()

def show_students():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM students''')
    rows = c.fetchall()
    conn.close()
    return rows

def submit():
    admission_number = admission_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    grade = grade_entry.get()

    if admission_number == '' or name == '' or age == '' or gender == '' or grade == '':
        messagebox.showerror('Error', 'Please fill in all fields')
    else:
        insert_student(admission_number, name, age, gender, grade)
        messagebox.showinfo('Success', 'Student added successfully')
        admission_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        gender_var.set('')
        grade_entry.delete(0, tk.END)

def display_students():
    students = show_students()
    if students:
        display_window = tk.Toplevel(root)
        display_window.title('All Students')

        for i, student in enumerate(students):
            tk.Label(display_window, text=f'{i+1}. {student[1]}, Name: {student[2]}, Age: {student[3]}, Gender: {student[4]}, Grade: {student[5]}').pack()

    else:
        messagebox.showinfo('Info', 'No students found')

root = tk.Tk()
root.title('Student Management System')

create_table()

tk.Label(root, text='Admission Number:', font=('Arial', 14)).grid(row=0, column=0, padx=10, pady=10)
admission_entry = tk.Entry(root, font=('Arial', 14))
admission_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text='Name:', font=('Arial', 14)).grid(row=1, column=0, padx=10, pady=10)
name_entry = tk.Entry(root, font=('Arial', 14))
name_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text='Age:', font=('Arial', 14)).grid(row=2, column=0, padx=10, pady=10)
age_entry = tk.Entry(root, font=('Arial', 14))
age_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text='Gender:', font=('Arial', 14)).grid(row=3, column=0, padx=10, pady=10)
gender_var = tk.StringVar(root)
gender_var.set('')
gender_option = tk.OptionMenu(root, gender_var, 'Male', 'Female', 'Other')
gender_option.config(font=('Arial', 14))
gender_option.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text='Grade:', font=('Arial', 14)).grid(row=4, column=0, padx=10, pady=10)
grade_entry = tk.Entry(root, font=('Arial', 14))
grade_entry.grid(row=4, column=1, padx=10, pady=10)

submit_button = tk.Button(root, text='Submit', command=submit, font=('Arial', 14))
submit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='WE')

show_button = tk.Button(root, text='Show Students', command=display_students, font=('Arial', 14))
show_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky='WE')

root.mainloop()
