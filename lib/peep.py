from datetime import datetime

class Peep:
    def __init__(self, id, username, content, date_time):
        self.id = id
        self.username = username
        self.content = content
        self.date_time = date_time

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Peep({self.id}, {self.username}, {self.content}, {self.date_time})'
    