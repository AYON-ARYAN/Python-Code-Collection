import tkinter as tk


root = tk.Tk()
root.title("Retina Display")

label1 = tk.Label(root, text="Label 1")
label1.pack()

label2 = tk.Label(root, text="Label 2")
label2.pack()

# Create a button
button = tk.Button(root, text="Press It!")
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
