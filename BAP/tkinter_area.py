import tkinter as tk


def area():
    selected_shape = shape_listbox.get(shape_listbox.curselection())

    if selected_shape == "Addition":
        addition()
    elif selected_shape == "Subtraction":
        subtraction()
    elif selected_shape == "Multiplication":
        multiplication()
    elif selected_shape == "Division":
        division()


def addition():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 + num2
    result_label.config(text="Result: " + str(result))


def subtraction():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 - num2
    result_label.config(text="Result: " + str(result))


def multiplication():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 * num2
    result_label.config(text="Result: " + str(result))


def division():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    result = num1 / num2
    result_label.config(text="Result: " + str(result))


root = tk.Tk()
root.title("Calculator")

shape_listbox = tk.Listbox(root)
shape_listbox.pack(pady=5)

shape_listbox.insert(1, "Addition")
shape_listbox.insert(2, "Subtraction")
shape_listbox.insert(3, "Multiplication")
shape_listbox.insert(4, "Division")

label1 = tk.Label(root, text="Enter Number:")
label1.pack(pady=5)

entry1 = tk.Entry(root)
entry1.pack(pady=5)

label2 = tk.Label(root, text="Enter Number:")
label2.pack(pady=5)

entry2 = tk.Entry(root)
entry2.pack(pady=5)

calculate_button = tk.Button(root, text="===", command=area)
calculate_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
