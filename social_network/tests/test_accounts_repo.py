from lib.accounts_repo import AccountRepo
from lib.accounts import Account

def test_all(db_connection):
    db_connection.seed('seeds/social_network.sql')
    account_repo = AccountRepo(db_connection)

    result = account_repo.all()

    assert result == [
        Account('pato@patomail.com', 'pato2000'),
        Account('cao@dogmail.com', 'doggydog'),
        Account('cat@catmail.com', 'tac')
    ]

def test_find(db_connection):
    db_connection.seed('seeds/social_network.sql')
    account_repo = AccountRepo(db_connection)

    result = account_repo.find('pato2000')

    assert result == Account('pato@patomail.com', 'pato2000')

