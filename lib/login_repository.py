from lib.login import Login

class LoginRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_user(self, email):
        result = self._connection.execute('SELECT * FROM users WHERE email = %s', [email])
        if result:
            return result[0]
        else:
            return None
        
    def create_user(self, username, email, password):
        self._connection.execute(
            'INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
            [username, email, password])
        return None
    # def verify_password(self, email, password):
        