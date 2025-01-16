from lib.login import Login
import hashlib

class LoginRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_user(self, email):
        result = self._connection.execute('SELECT * FROM users WHERE email = %s', [email])
        if result:
            return result[0]
        else:
            return None
        
    def get_username(self, id):
        result = self._connection.execute('SELECT username FROM users WHERE id = %s', [id])
        if result:
            return result[0]
        else:
            return None
        
    def create_user(self, username, email, password):
        binary_password = password.encode("utf-8")
        hashed_password = hashlib.sha256(binary_password).hexdigest()
        self._connection.execute(
            'INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
            [username, email, hashed_password])
        return None
    # def verify_password(self, email, password):
    def check_password(self, email, password_attempt):
        # Hash the password attempt
        binary_password_attempt = password_attempt.encode("utf-8")
        hashed_password_attempt = hashlib.sha256(binary_password_attempt).hexdigest()

        # Check whether there is a user in the database with the given email
        # and a matching password hash, using a SELECT statement.
        rows = self._connection.execute(
            'SELECT * FROM users WHERE email = %s AND password = %s',
            [email, hashed_password_attempt])

        # If that SELECT finds any rows, the password is correct.
        return len(rows) > 0