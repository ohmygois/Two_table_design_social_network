from lib.posts import Post

class PostRepo:
    
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM posts")
        posts = []

        for row in rows:
            post = Post(row['title'], row['content'],row['views'],row['account_id'])
            posts.append(post)
        return posts
    
    def find(self, account_id):
        rows = self._connection.execute("SELECT * FROM posts WHERE account_id =%s", [account_id])
        posts = []

        for row in rows:
            post = Post(row['title'], row['content'],row['views'],row['account_id'])
            posts.append(post)
        return posts
        
    def create(self, post):
        rows = self._connection.execute("INSERT INTO posts (title, content, views, account_id) VALUES (%s,%s,%s,%s)",[post.title, post.content, post.views, post.account_id])
        return None

    def delete(self, title):
        rows = self._connection.execute("DELETE FROM posts WHERE title=%s",[title])
        return None