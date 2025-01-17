from datetime import datetime

class Peep:
    def __init__(self, id, username, picture_id, content, date_only, time_only, users_id):
        self.id = id
        self.username = username
        self.picture_id = picture_id
        self.content = content
        self.date_only = date_only
        self.time_only = time_only
        self.users_id = users_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Peep({self.id}, {self.username}, {self.picture_id}, {self.content}, {self.date_only}, {self.time_only})'
    
