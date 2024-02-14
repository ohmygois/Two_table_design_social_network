class Post:
    
    def __init__(self, title, content, views, account_id):
        self.title = title
        self.content = content
        self.views = views
        self.account_id = account_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Post({self.title}, {self.content}, {self.views}, {self.account_id})"