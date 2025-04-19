import tkinter as tk

root = tk.Tk()
root.geometry("200x200")

label1 = tk.Label(root, text="Ayon", background="purple", fg="grey")
label1.pack()

label2 = tk.Label(root, text="Macbook", background="grey", fg="black")
label2.pack(fill="x")

label3 = tk.Label(root, text="Mam", background="blue", fg="green")
label3.pack(side=tk.LEFT, fill="y")

root.mainloop()
