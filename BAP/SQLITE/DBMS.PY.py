import sqlite3

conn = sqlite3.connect('/Volumes/DRIVE/BAP/SQLITE/ayon.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
  BOOK_ID INTEGER PRIMARY KEY AUTOINCREMENT,
  BOOK_NAME TEXT,
  AUTHOR_NAME TEXT,
  BOOK_PRICE INT
)
""")

def display_menu():
  print("\nMENU")
  print("1. Add Books")
  print("2. Display Books")
  print("3. Delete Book")
  print("4. Purchase Book")
  print("5. Exit")

def add_books():
  num_books = int(input("Enter the number of books to add: "))
  books = []
  for i in range(num_books):
    book_name = input("Enter book name: ")
    author_name = input("Enter author name: ")
    price = int(input("Enter book price: "))
    books.append((book_name, author_name, price))
  cursor.executemany("INSERT INTO books VALUES (?,?,?)", books)
  conn.commit()
  print("Books added successfully!")

def display_books():
  print(f"{'Book ID':<25} {'Book Name':<25} {'Author':>10} {'Price':>10}")
  for row in cursor.execute("SELECT * FROM books").fetchall():
    print(f"{row[0]} {row[1]} {row[2]} {row[3]}")

def delete_book():
  book_id = int(input("Enter the ID of the book to delete: "))
  cursor.execute("DELETE FROM books WHERE BOOK_ID = ?", (book_id,))
  conn.commit()
  print("Book deleted successfully!")

def purchase_book():
  book_id = int(input("Enter the ID of the book to purchase: "))
  cursor.execute("SELECT * FROM books WHERE BOOK_ID = ?", (book_id,))
  book = cursor.fetchone()
  if book:
    print("Book Details:")
    print(f"Book Name: {book[1]}")
    print(f"Author: {book[2]}")
    print(f"Price: {book[3]}")
    confirmation = input("Confirm purchase (y/n): ")
    if confirmation.lower() == 'y':
      print("Generating bill...")
      print(f"Book '{book[1]}' purchased successfully!")
  else:
    print("Book not found!")

while True:
  display_menu()
  choice = input("Enter your choice: ")

  if choice == '1':
    add_books()
  elif choice == '2':
    display_books()
  elif choice == '3':
    delete_book()
  elif choice == '4':
    purchase_book()
  elif choice == '5':
    conn.close()
    print("Exiting program...")
    break
  else:
    print("Invalid choice. Please try again.")
