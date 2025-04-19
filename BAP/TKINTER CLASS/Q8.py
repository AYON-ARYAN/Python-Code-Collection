import tkinter as tk

root = tk.Tk()
root.title("Image Demo")

image = tk.PhotoImage(file="/Users/ayon_aryan/Documents/FUCK YOU/2024-Formula1-Ferrari-SF-24-001-2160.jpg")

label = tk.Label(root, image=image)
label.pack()

root.mainloop()
