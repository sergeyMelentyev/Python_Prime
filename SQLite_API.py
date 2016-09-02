import sqlite3

connect_db = sqlite3.connect("MyDatabase.sql3")

# could be created several cursors for parallel processing
cursor = connect_db.cursor()

# drop table if it exists
cursor.execute("DROP TABLE IF EXISTS publisher")

# create a new table
cursor.execute("""CREATE TABLE publisher(
                    pubid INT PRIMARY KEY,
                    pubname VARCHAR(25),
                    puburl VARCHAR(125))""")

#drop table if it exists
cursor.execute("DROP TABLE IF EXISTS book")

# create a new table
cursor.execute("""\
                CREATE TABLE book (
                bkisbn CHAR(10) PRIMARY KEY,
                bktitle VARCHAR(60),
                bkyear INT,
                bkpubid INT,
                FOREIGN KEY(bkpubid) REFERENCES publisher(pubid))
                """)

# create a simple list of publishers
book_tuple = (
        ("Holden Web", "http://holdenweb.com"),
        ("Apress", "http://apress.com"),
        ("O`Reilly Media", "http://oreilly.com"),
        ("Packt Publisher", "http:///www.packtpub.com")
)
book_dict = {
    "1565926218": ("Python Programming on Win32", 1999, 2),
    "1590597257": ("The Definitive Guide to Django", 2011, 1),
    "1234567890": ("No book You ever heard of", 2015, 0),
    "0569007973": ("The Python Cookbook", 2009, 2),
    "7818471947": ("Expert Python Programming", 2012, 3)
}

ISBN = "1234567890"
book = book_dict[ISBN]
publisher = book_tuple[book[2]]
print("""\
ISBN        {}
Title:      {}
Year:       {}
Publisher:  {}
URL:        {}""".format(ISBN, book[0], book[1], publisher[0], publisher[1]))

# insert data to the database
for i, publisher in enumerate(book_tuple):
    cursor.execute("""
        INSERT INTO publisher (pubid, pubname, puburl)
        VALUES(?, ?, ?)""", (i, publisher[0], publisher[1]))

# select all columns from te publisher table
cursor.execute("SELECT * FROM publisher")
cursor.fetchall()

for ISBN, (title, year, pubid) in book_dict.items():
    cursor.execute("""
        INSERT INTO book
        (bkisbn, bktitle, bkyear, bkpubid)
        VALUES (?, ?, ?, ?)""", (ISBN, title, year, pubid))

cursor.execute("SELECT * FROM book")
cursor.fetchall()

# retrieve a join of two tables
cursor.execute("""SELECT * FROM book JOIN publisher ON pubid=bkpubid""")
cursor.fetchall()

connect_db.commit()
connect_db.close()
