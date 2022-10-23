from accountHistory import AccountHistory

class Account:

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = float(balance)
        self.id = None
        self.transaction_history = AccountHistory(self)

    def set_id(self, id):
        self.id = id

    @property
    def get_id(self):
        return self.id
