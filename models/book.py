import sqlite3

class Book:
  def __init__(self, title, author, id = None, user_id = None):
    self.id = id
    self.title = title
    self.author = author
    self.user_id = None

    
