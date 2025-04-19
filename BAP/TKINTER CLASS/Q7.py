import tkinter as tk

def button_clicked():
    label.config(text="Button was Push!")

root = tk.Tk()
root.title("Button Press")

label = tk.Label(root, text="Pressed the button!")
label.pack(pady=10)

button = tk.Button(root, text="Push Me!", command=button_clicked)
button.pack(pady=5)

root.mainloop()
