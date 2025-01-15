from lib.peep import Peep

class PeepRepository:
    def __init__(self, connection):
        self._connection = connection
    
    
    def create(self, content):
        self._connection.execute(
            'INSERT INTO peeps (content) VALUES (%s)',
            [content])
        return None
    # def create(self, content, date_time):
    #     peep = Peep(len(self.peeps) + 1, content, date_time)
    #     self.peeps.append(peep)
    #     return peep
    
    def delete(self, peep_id):
        self._connection.execute(
            'DELETE FROM peeps WHERE id = %s', [peep_id])
        return None


    def all(self):
        rows = self._connection.execute('SELECT * from peeps')
        peeps = []
        for row in rows:
            item = Peep(row["id"], row["username"], row["content"], row["date_time"])
            peeps.append(item)
        return peeps