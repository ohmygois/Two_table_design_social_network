from lib.accounts import Account


class AccountRepo:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM accounts')
        accounts = []

        for row in rows:
            account = Account(row['email'], row['username'])
            accounts.append(account)
        
        return accounts
    
    def find(self, username):
        rows = self._connection.execute('SELECT * FROM accounts WHERE username=%s', [username])
        row = rows[0]
        return Account(row['email'], row['username'])
    
    def create(self, account):
        rows = self._connection.execute("INSERT INTO accounts (email, username) VALUES (%s,%s)",[account.email, account.username])
        return None

    def delete(self, username):
        rows = self._connection.execute("DELETE FROM accounts WHERE username=%s",[username])
        return None