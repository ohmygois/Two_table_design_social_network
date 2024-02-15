from lib.database_connection import DatabaseConnection
from lib.posts_repo import PostRepo
from lib.accounts_repo import AccountRepo
from lib.accounts import Account
from lib.posts import Post

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/social_network.sql")

# Retrieve all accounts
account_repo = AccountRepo(connection)
accounts = account_repo.all()

# Retrieve all posts
post_repo = PostRepo(connection)
posts = post_repo.all()

# List them out
print("Here's a list of all accounts:\n")
for account in accounts:
    print(account)

print("\nHere's a list of all posts:\n")
for post in posts:
    print(post)

# Delete user and list new user list out
print("\nDeleting tac user:\n")
account_repo.delete('tac')
accounts = account_repo.all()
for account in accounts:
    print(account)
posts = post_repo.all()
print("\nHere's a list of updated posts:\n")
for post in posts:
    print(post)

# Add user and list new user list out
print("\nAdding aslan user:\n")
account = Account("aslan@jungle.ky", "aslan_theking")
account_repo.create(account)
accounts = account_repo.all()
post = Post('Lion King', "I'm surrounded by idiots", 1500, 4)
post_repo.create(post)
posts = post_repo.all()
for account in accounts:
    print(account)
posts = post_repo.all()
print("\nHere's a list of updated posts:\n")
for post in posts:
    print(post)