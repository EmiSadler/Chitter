from lib.peep import Peep

class PeepRepository:
    def __init__(self, connection):
        self._connection = connection
    
    
    def create(self, username, content, users_id):
        self._connection.execute(
            'INSERT INTO peeps (username, content, users_id) VALUES (%s, %s, %s)',
            [username, content, users_id])
        return None

    
    def delete(self, peep_id):
        self._connection.execute(
            'DELETE FROM peeps WHERE id = %s', [peep_id])
        return None


    def all(self):
        rows = self._connection.execute('SELECT * from peeps')
        peeps = []
        for row in rows:
            picture_id = self.find_picture_id_by_user_id(row["users_id"])
            item = Peep(row["id"], row["username"], picture_id, row["content"], row["date_only"], row["time_only"], row["users_id"])
            peeps.append(item)
        return peeps
    
    def find_picture_id_by_user_id(self, user_id):
        rows = self._connection.execute('SELECT picture_id FROM users WHERE id = %s', [user_id])
        return rows[0]["picture_id"]
    
