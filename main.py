from models.userSource import UserSource
from models.bookSource import BookSource
from models.user import User
from models.book import Book

class Library:

  def lendBook(self, bookid, userid):
    BookSource().updateBookUserid(bookid, userid)
  
  def createBook(self, title, author):
    book = Book(title, author)
    BookSource().addBook(book)

  def indexBooks(self):
    return BookSource().getBooks()

  def indexUsers(self):
    return UserSource().getUsers()

  def menu(self):
    while True:
      print("1. Lend a book")
      print("2. Add a book")
      print("3. Exit")
      choice = input("Choose a number: ")
      if choice == "1":
        users = self.indexUsers()
        books = self.indexBooks()
        print("Users:")
        for index, user in enumerate(users):
          print(index+1, user.name)
        print("Books:")
        for index, book in enumerate(books):
          print(book.id, book.title)
        bookid = int(input("Choose a book: "))
        userid = int(input("Choose a user: "))
        self.lendBook(bookid, userid)
      elif choice == "2":
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        self.createBook(title, author)
      elif choice == "3":
        break

lib = Library()
lib.menu()
