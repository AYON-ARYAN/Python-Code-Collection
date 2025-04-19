import tkinter as tk
from tkinter import messagebox

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    published_year = year_entry.get()

    messagebox.showinfo("Success", "Book added successfully!")

def delete_book():
    book_id = delete_entry.get()
    messagebox.showinfo("Success", "Book deleted successfully!")

def update_book():
    book_id = update_id_entry.get()
    title = update_title_entry.get()
    author = update_author_entry.get()
    published_year = update_year_entry.get()
    messagebox.showinfo("Success", "Book updated successfully!")

def search_books():
    search_term = search_entry.get()
    result_text.config(state=tk.NORMAL)
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, f"Search for: {search_term}")
    result_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Library Management System")

# Add Book Section
add_frame = tk.LabelFrame(root, text="Add Book", padx=10, pady=10)
add_frame.grid(row=0, column=0, padx=10, pady=10)
title_label = tk.Label(add_frame, text="Title:")
title_label.grid(row=0, column=0)
title_entry = tk.Entry(add_frame)
title_entry.grid(row=0, column=1)
author_label = tk.Label(add_frame, text="Author:")
author_label.grid(row=1, column=0)
author_entry = tk.Entry(add_frame)
author_entry.grid(row=1, column=1)
year_label = tk.Label(add_frame, text="Published Year:")
year_label.grid(row=2, column=0)
year_entry = tk.Entry(add_frame)
year_entry.grid(row=2, column=1)
add_button = tk.Button(add_frame, text="Add Book", command=add_book)
add_button.grid(row=3, column=0, columnspan=2)

# Delete Book Section
delete_frame = tk.LabelFrame(root, text="Delete Book", padx=10, pady=10)
delete_frame.grid(row=1, column=0, padx=10, pady=10)
delete_label = tk.Label(delete_frame, text="Book ID:")
delete_label.grid(row=0, column=0)
delete_entry = tk.Entry(delete_frame)
delete_entry.grid(row=0, column=1)
delete_button = tk.Button(delete_frame, text="Delete Book", command=delete_book)
delete_button.grid(row=1, column=0, columnspan=2)

# Update Book Section
update_frame = tk.LabelFrame(root, text="Update Book", padx=10, pady=10)
update_frame.grid(row=0, column=1, padx=10, pady=10)
update_id_label = tk.Label(update_frame, text="Book ID:")
update_id_label.grid(row=0, column=0)
update_id_entry = tk.Entry(update_frame)
update_id_entry.grid(row=0, column=1)
update_title_label = tk.Label(update_frame, text="Title:")
update_title_label.grid(row=1, column=0)
update_title_entry = tk.Entry(update_frame)
update_title_entry.grid(row=1, column=1)
update_author_label = tk.Label(update_frame, text="Author:")
update_author_label.grid(row=2, column=0)
update_author_entry = tk.Entry(update_frame)
update_author_entry.grid(row=2, column=1)
update_year_label = tk.Label(update_frame, text="Published Year:")
update_year_label.grid(row=3, column=0)
update_year_entry = tk.Entry(update_frame)
update_year_entry.grid(row=3, column=1)
update_button = tk.Button(update_frame, text="Update Book", command=update_book)
update_button.grid(row=4, column=0, columnspan=2)

# Search Books Section
search_frame = tk.LabelFrame(root, text="Search Books", padx=10, pady=10)
search_frame.grid(row=1, column=1, padx=10, pady=10)
search_label = tk.Label(search_frame, text="Search:")
search_label.grid(row=0, column=0)
search_entry = tk.Entry(search_frame)
search_entry.grid(row=0, column=1)
search_button = tk.Button(search_frame, text="Search", command=search_books)
search_button.grid(row=1, column=0, columnspan=2)
result_text = tk.Text(search_frame, height=10, width=50, state=tk.DISABLED)
result_text.grid(row=2, column=0, columnspan=2)

root.mainloop()
