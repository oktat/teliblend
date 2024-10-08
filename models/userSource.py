from models.sqlite import Sqlite
from models.user import User

class UserSource:

  def getUsers(self):
    conn = Sqlite.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    conn.close()
    users = []
    for row in result:
      users.append(User(row[1]))
    return users

  def getUser(self, id):
    conn = Sqlite.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
    result = cursor.fetchone()
    conn.close()
    if result:
      return User(result[1])
    return None

  def addUser(self, user):
    conn = Sqlite.connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (?)", (user.name,))
    conn.commit()
    conn.close()

  def updateUser(self, user):
    conn = Sqlite.connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ? WHERE id = ?", (user.name, user.id))
    conn.commit()
    conn.close()

  def deleteUser(self, id):
    conn = Sqlite.connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    conn.close()
