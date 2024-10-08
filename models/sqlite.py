import sqlite3

class Sqlite:
  @staticmethod
  def connect():
    conn = sqlite3.connect('database.sqlite')
    return conn
