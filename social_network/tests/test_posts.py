from lib.posts import Post

def test_format():
    post = Post("Ducktales", "quack quack", 20, 1)
    assert post.title == "Ducktales"
    assert post.content == "quack quack"
    assert post.views == 20
    assert post.account_id == 1

def test_equality():
    post1 = Post("Ducktales", "quack quack", 20, 1)
    post2 = Post("Ducktales", "quack quack", 20, 1)
    assert post1 == post2

def test_repr():
    post = Post("Ducktales", "quack quack", 20, 1)
    assert str(post) == "Post(Ducktales, quack quack, 20, 1)"