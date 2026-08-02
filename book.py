
import sqlite3
import pandas as pd
conn = sqlite3.connect('library.db')
cursor = conn.cursor()
cursor.executescript("""
DROP TABLE IF EXISTS Book;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Book_Loan;
CREATE TABLE Book (
    Book_Id          INTEGER PRIMARY KEY,
    Book_Title       TEXT,
    Author           TEXT,
    Category         TEXT,
    Pages            INTEGER,
    Copies_Available INTEGER
);
CREATE TABLE Member (
    Member_Id   INTEGER PRIMARY KEY,
    Member_Name TEXT
);
CREATE TABLE Book_Loan (
    Loan_Id   INTEGER PRIMARY KEY,
    Book_Id   INTEGER,
    Member_Id INTEGER
);
INSERT INTO Book VALUES
  (1, 'The Secret Garden', 'Frances Hodgson Burnett', 'Fiction', 331, 4),
  (2, 'Science Experiments', 'Riya Shah', 'Science', 120, 6),
  (3, 'Space Adventure', 'Arun Mehta', 'Science', 245, 3),
  (4, 'History of India', 'Neha Rao', 'History', 310, 2),
  (5, 'The Jungle Book', 'Rudyard Kipling', 'Fiction', 277, 5),
  (6, 'Maths Made Easy', 'Anita Das', 'Education', 180, 4),
  (7, 'Stories for Children', 'Meera Singh', 'Fiction', 150, 7),
  (8, 'Amazing Animals', 'Kabir Khan', 'Science', 210, 3);

INSERT INTO Member VALUES
  (1, 'Aarav'), (2, 'Diya'), (3, 'Kabir'), (4, 'Meera');

INSERT INTO Book_Loan VALUES
  (1, 1, 1), (2, 3, 2), (3, 5, 3), (4, 2, 4);
""")
conn.commit()
print('Library database ready!')

tables = pd.read_sql("""SELECT * FROM sqlite_master WHERE type = 'table';""",conn)
print(tables)
book = pd.read_sql("""SELECT * FROM Book;""",conn)
print(book)
print('Rows and columns:',book.shape)
all_books = pd.read_sql("""SELECT * FROM Book;""",conn)
print(all_books)

book_details = pd.read_sql("""SELECT Book_Id, Book_Title,Author FROM Book; """,conn)
print(book_details)

loan_details = pd.read_sql("""SELECT Book_Id, Member_Id FROM Book_Loan;""",conn)
print(loan_details)

science_books = pd.read_sql("""SELECT * FROM Book WHERE Category == 'Science';""",conn)
print(science_books)

available_books = pd.read_sql("""SELECT * FROM Book WHERE Category IN ('Fiction','History') AND Copies_Available > 0;""",conn)
print(available_books)

the_books = pd.read_sql("""SELECT * FROM Book WHERE Book_Title LIKE 'The%';""",conn)
print(the_books)

book_titles = pd.read_sql("""SELECT * FROM Book WHERE Book_Title LIKE '%Book';""",conn)
print(book_titles)

page_range = pd.read_sql("""SELECT MIN(Pages),MAX(Pages) FROM Book;""",conn)
print(page_range)

copy_range = pd.read_sql("""SELECT MIN(Copies_Available),MAX(Copies_Available) FROM Book;""",conn)
print(copy_range)

conn.close()

