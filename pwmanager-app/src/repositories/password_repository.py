from database_connection import get_database_connection
from entities.password import Password

def get_password_by_row(row):
    return Password(row["app"], row["password"], row["username"]) if row else None


class PasswordRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self, username):
        cursor = self._connection.cursor()
        sql = "SELECT * FROM passwords WHERE username=?"
        cursor.execute(sql,(username,))
        rows = cursor.fetchall()
        return list(map(get_password_by_row,rows))

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM passwords")
        self._connection.commit()
        print('Deleted', cursor.rowcount, 'records from the table')

    def find_password(self, app_name, username):
        cursor = self._connection.cursor()
        sql = "SELECT * FROM passwords WHERE username=? AND app=?"
        cursor.execute(sql, (username,app_name))
        rows = cursor.fetchall()
        return get_password_by_row(rows[0])

    def insert_password(self, password):
        cursor = self._connection.cursor()
        sql = "INSERT INTO passwords (username,app,password) VALUES (?,?,?)"
        cursor.execute(sql, (password.username, password.app, password.password))
        self._connection.commit()
        return password

    def delete_password(self, password):
        cursor = self._connection.cursor()
        sql = "DELETE FROM passwords WHERE username=? AND app=?"
        cursor.execute(sql, (password.username, password.app))
        self._connection.commit()
        return password

password_repository = PasswordRepository(get_database_connection())
