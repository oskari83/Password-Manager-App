from database_connection import get_database_connection
from entities.user import User

def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return list(map(get_user_by_row,rows))

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()
        print('Deleted', cursor.rowcount, 'records from the table')

    def insert_user(self, user):
        cursor = self._connection.cursor()
        sql = "INSERT INTO users (username,password) VALUES (?,?)"
        cursor.execute(sql, (user.username,user.password))
        self._connection.commit()
        return user

    def find_user(self, username):
        cursor = self._connection.cursor()
        sql = "SELECT * FROM users WHERE username=?"
        cursor.execute(sql, (username,))
        rows = cursor.fetchall()
        if len(rows)>=1:
            return get_user_by_row(rows[0])
        else:
            return None

user_repository = UserRepository(get_database_connection())
    