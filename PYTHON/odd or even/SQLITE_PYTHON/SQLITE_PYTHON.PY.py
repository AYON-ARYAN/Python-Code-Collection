import _sqlite3
conn=_sqlite3.connect('hello.db')

#creating a cursor
dog=conn.cursor()

#creating a table
dog.execute(""" 
    CREATE TABLE customer(
    first_name text ,
    second_name text,
    email text)
    """)
conn.commit()
#filling the table
dog.execute("""INSERT INTO customer VALUES( 'Shark','BABY','aish3@gmail.com')""")
dog.execute("""INSERT INTO customer VALUES('Shama', 'Muddu', 'MUddiKI Fuddi@google.com')""")
dog.execute("""INSERT INTO customer VALUES('Jane', 'Warren', 'jane.conjuring@warren.com')""")
conn.commit()
many_customers = [
('Wes', 'Brown', 'wes@brown.com'), ('Steph', 'Kuewa', 'steph@kuetva.com'),
('Dan', "Pas", 'dan@pas.com'),
    ]
dog. executemany ("INSERT INTO customer VALUES (?,?,?)",many_customers)
conn.commit()
dog.execute ('SELECT * FROM customer')
print(dog.fetchall())
conn.commit()
dog.close()
conn.close()