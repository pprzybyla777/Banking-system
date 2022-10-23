from constants import NOW

class AccountHistory:
    def __init__(self, account):
        self.account = account
        self.history = []

    def add_operation_to_History(self, operation):
        self.history.append(operation)

    @property
    def show_history(self):
        return self.history
