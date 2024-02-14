class Account:
    
    def __init__(self, email, username):
        self.email = email
        self.username = username

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Account({self.email}, {self.username})"