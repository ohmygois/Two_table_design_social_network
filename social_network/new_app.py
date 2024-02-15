# file: app.py

from lib.accounts_repo import AccountRepo
from lib.accounts import Account
from lib.database_connection import DatabaseConnection

class Application():
  def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()
    self._connection.seed("seeds/social_network.sql")

  def run(self):
    account_repository = AccountRepo(self._connection)

    while True:
        print("\n1. List all accounts")
        print("2. Find an account by username")
        print("3. Create a new account")
        print("4. Delete an account")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice == "1":
            accounts = account_repository.all()
            for account in accounts:
                print(f"Email: {account.email}, Username: {account.username}")
        elif choice == "2":
            username_to_find = input("Enter the username to find: ")
            try:
                found_account = account_repository.find(username_to_find)
                print(f"Found Account - Email: {found_account.email}, Username: {found_account.username}")
            except IndexError:
                print(f"No account found with the username '{username_to_find}'.")
        elif choice == "3":
            new_email = input("Enter the email for the new account: ")
            new_username = input("Enter the username for the new account: ")
            new_account = Account(new_email, new_username)
            account_repository.create(new_account)
            print(f"New account created - Email: {new_account.email}, Username: {new_account.username}")
        elif choice == "4":
            username_to_delete = input("Enter the username to delete: ")
            account_repository.delete(username_to_delete)
            print(f"Account with username '{username_to_delete}' deleted.")
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

if __name__ == '__main__':
    app = Application()
    app.run()
