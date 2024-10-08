from models.sqlite import Sqlite
from models.book import Book

class BookSource:

  def getBooks(self):
    conn = Sqlite.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    result = cursor.fetchall()
    conn.close()
    books = []
    for row in result:
      # print(row[3])
      books.append(Book(row[1], row[2], id=row[0]))
    return books

  def getBook(self, id):
    conn = Sqlite.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE id = ?", (id,))
    result = cursor.fetchone()
    conn.close()
    if result:
      return Book(result[1], result[2])
    return None

  def addBook(self, book):
    conn = Sqlite.connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (book.title, book.author))
    conn.commit()
    conn.close()

  def updateBook(self, book):
    conn = Sqlite.connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title = ?, author = ? WHERE id = ?", 
                   (book.title, book.author, book.id))

  def updateBookUserid(self, bookid, userid):
    conn = Sqlite.connect()
    cursor = conn.cursor()
    print(userid, bookid)
    cursor.execute("UPDATE books SET user_id = ? WHERE id = ?", (userid, bookid))
    conn.commit()
    cursor.close()



