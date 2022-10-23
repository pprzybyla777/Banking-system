from uuid import uuid4
from account import Account


class AlreadyAddedAccount(Exception):
    pass


class NotAnAccount(Exception):
    pass


class Bank:

    def __init__(self):
        self.dict_of_accounts = {}

    def add_account(self, account):
        if isinstance(account, Account):
            if account.get_id is None:
                new_id = str(uuid4())
                account.set_id(new_id)
                self.dict_of_accounts[new_id] = account
            else:
                raise AlreadyAddedAccount()
        else:
            raise NotAnAccount()

    def find_account(self, account_id):
        return self.dict_of_accounts.get(account_id)
