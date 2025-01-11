from lib.peep import Peep

class PeepRepository:
    def __init__(self):
        self.peeps = []

    def all(self):
        return self.peeps
    
    def create(self, content, date_time):
        peep = Peep(len(self.peeps) + 1, content, date_time)
        self.peeps.append(peep)
        return peep
    
