
class Login:
    def __init__(self, id, username, email, password, picture_id):
        self.id = id
        self.username = username
        self.email = email
        self.password =  password
        self.picture_id = picture_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Login({self.id}, {self.username}, {self.email})'
    
    def is_valid(self):
        if self.username == None or self.username == "":
            return False
        if self.email == None or self.email == "":
            return False
        if self.password == None or self.password == "":
            return False    
        return True

    def generate_errors(self):
        errors = []
        if self.username == None or self.username == "":
            errors.append("Username is required")
        if self.email == None or self.email == "":
            errors.append("Email is required")
        if self.password == None or self.password == "":
            errors.append("Password is required")
        return errors