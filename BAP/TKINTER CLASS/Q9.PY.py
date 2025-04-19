import tkinter as tk

def button_clicked():
    label.config(text="Button Push!", fg="blue", font=("Arial", 12, "bold"))

root = tk.Tk()
root.title("Labels and Buttons")

label = tk.Label(root, text="Push the button!", fg="green", font=("Helvetica", 14, "italic"))
label.pack(pady=10)

button = tk.Button(root, text="Push Me!", command=button_clicked, bg="yellow", fg="red", font=("Ariel", 100))
button.pack(pady=5)

root.mainloop()
