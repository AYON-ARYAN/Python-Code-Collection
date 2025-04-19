import tkinter as tk

root = tk.Tk()
root.title("Label Font")

font_name = "Ariel"
font_size = 28
font_bold = "bold"

custom_font = (font_name, font_size, font_bold)

label = tk.Label(root, text="Hello, Bro!", font=custom_font)
label.pack(pady=20)

root.mainloop()
