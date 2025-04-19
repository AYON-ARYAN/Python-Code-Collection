import tkinter as tk

root = tk.Tk()
root.title("Text Box Demo")

root.geometry("400x300")

text_box = tk.Text(root, width=40, height=10)
text_box.pack(pady=20)

root.mainloop()
