from lib.accounts import Account

def test_format():
    account = Account("cat@gatmail.com", "catcat")
    assert account.email == "cat@gatmail.com"
    assert account.username == "catcat"


def test_equality():
    account1 = Account("cat@gatmail.com", "catcat")
    account2 = Account("cat@gatmail.com", "catcat")
    assert account1 == account2

def test_repr():
    account = Account("cat@gatmail.com", "catcat")
    assert str(account) == "Account(cat@gatmail.com, catcat)"