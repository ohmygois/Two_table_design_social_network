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

def test_create(db_connection):
    db_connection.seed('seeds/social_network.sql')
    account_repo = AccountRepo(db_connection)

    account_repo.create(Account("aslan@jungle.ky", "aslan_theking"))

    assert account_repo.all() == [
        Account('pato@patomail.com', 'pato2000'),
        Account('cao@dogmail.com', 'doggydog'),
        Account('cat@catmail.com', 'tac'),
        Account("aslan@jungle.ky", "aslan_theking")
    ]

def test_delete(db_connection):
    db_connection.seed('seeds/social_network.sql')
    account_repo = AccountRepo(db_connection)

    account_repo.delete("doggydog")
    account_repo.create(Account("aslan@jungle.ky", "aslan_theking"))

    assert account_repo.all() == [
        Account('pato@patomail.com', 'pato2000'),
        Account('cat@catmail.com', 'tac'),
        Account("aslan@jungle.ky", "aslan_theking")
    ]