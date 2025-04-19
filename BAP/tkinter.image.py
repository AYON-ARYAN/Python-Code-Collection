import tkinter as tk
from PIL import Image, ImageTk

def display_images():
    # Image 1
    image_path_1 = "/Users/ayon_aryan/Documents/FUCK YOU/2024-Formula1-Ferrari-SF-24-001-2160.jpg"
    image_1 = Image.open(image_path_1)
    tk_image_1 = ImageTk.PhotoImage(image_1)
    image_label_1 = tk.Label(window, image=tk_image_1)
    image_label_1.grid(row=0, column=0, padx=16, pady=9)

    # Image 2
    image_path_2 = "/Users/ayon_aryan/Documents/FUCK YOU/2023-Formula1-Ferrari-SF-23-004-1080.jpg"
    image_2 = Image.open(image_path_2)
    tk_image_2 = ImageTk.PhotoImage(image_2)
    image_label_2 = tk.Label(window, image=tk_image_2)
    image_label_2.grid(row=0, column=1, padx=16, pady=9)

window = tk.Tk()
window.title("Image Display")

# Call function to display images
display_images()

window.mainloop()
