from lib.posts_repo import PostRepo
from lib.posts import Post

def test_post_all(db_connection):
    db_connection.seed('seeds/social_network.sql')
    post_repo = PostRepo(db_connection)

    result = post_repo.all()

    assert result == [
        Post('Ducktales', 'Story of my life, quack quack quack..', 500, 1),
        Post('Dog Life', 'Say it, bow-wow-wow, Uh, uh, Bow Wow (yeah)', 12, 2),
        Post('Dog Life VOL.2', 'Still waters run deep / Still Snoop Dogg and D.R.E.', 122, 2),
        Post('Meow', 'Meow, meow, meow', 200, 3)
    ]

def test_find(db_connection):
    db_connection.seed('seeds/social_network.sql')
    post_repo = PostRepo(db_connection)

    result = post_repo.find(2)

    assert result == [Post('Dog Life', 'Say it, bow-wow-wow, Uh, uh, Bow Wow (yeah)', 12, 2), Post('Dog Life VOL.2', 'Still waters run deep / Still Snoop Dogg and D.R.E.', 122, 2)]


def test_create(db_connection):
    db_connection.seed('seeds/social_network.sql')
    post_repo = PostRepo(db_connection)

    post_repo.create(Post("MeowMeow", "Meow for life", 100, 3))

    assert post_repo.all() == [
        Post('Ducktales', 'Story of my life, quack quack quack..', 500, 1),
        Post('Dog Life', 'Say it, bow-wow-wow, Uh, uh, Bow Wow (yeah)', 12, 2),
        Post('Dog Life VOL.2', 'Still waters run deep / Still Snoop Dogg and D.R.E.', 122, 2),
        Post('Meow', 'Meow, meow, meow', 200, 3),
        Post("MeowMeow", "Meow for life", 100, 3)
    ]

def test_delete(db_connection):
    db_connection.seed('seeds/social_network.sql')
    post_repo = PostRepo(db_connection)

    post_repo.delete("MeowMeow")

    assert post_repo.all() == [
        Post('Ducktales', 'Story of my life, quack quack quack..', 500, 1),
        Post('Dog Life', 'Say it, bow-wow-wow, Uh, uh, Bow Wow (yeah)', 12, 2),
        Post('Dog Life VOL.2', 'Still waters run deep / Still Snoop Dogg and D.R.E.', 122, 2),
        Post('Meow', 'Meow, meow, meow', 200, 3),
    ]