from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.book_repository import BookRepository

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
# connection.seed("seeds/music_library.sql")

# Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# List them out
# for artist in artists:
#     print(artist)

# Retrieve all albums
# album_repository = AlbumRepository(connection)
# albums = album_repository.all()

# # List them out
# print("Here's a list of all albums:\n")
# for album in albums:
#     print(album)
"""
BookStore example.
"""
# Seed with some seed data
connection.seed("seeds/book_store.sql")

# Retrieve all books
book_repository = BookRepository(connection)
books = book_repository.all()

# List them out
print("Here's a list of all books:\n")
for book in books:
    print(book)

