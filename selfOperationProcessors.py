from abc import ABC, abstractmethod
from helpers import Helpers
from constants import NOW


class PassedInvalidAmount(Exception):
    pass


class NotEnoughFunds(Exception):
    pass


class PassedInvalidAccountId(Exception):
    pass


class SelfOperation:
    def __init__(self, date, type, amount):
        self.date = date
        self.type = type
        self.amount = amount


class SelfOperationProcessors(ABC, Helpers):

    @abstractmethod
    def operation(self, account_id, amount):
        pass


class DepositProcessor(SelfOperationProcessors):

    def __init__(self, bank):
        self.bank = bank

    def operation(self, account_id, amount):
        account = self.bank.find_account(account_id)
        if account is not None:
            if self.is_amount_valid(amount):
                amount = float(amount)
                account.balance += amount
                account.transaction_history.add_operation_to_History(SelfOperation(NOW, "deposit", str(amount)))
            else:
                raise PassedInvalidAmount()
        else:
            raise PassedInvalidAccountId()


class WithdrawProcessor(SelfOperationProcessors):

    def __init__(self, bank):
        self.bank = bank

    def operation(self, account_id, amount):
        account = self.bank.find_account(account_id)
        if account is not None:
            if self.is_amount_valid(amount):
                amount = float(amount)
                if self.are_funds_sufficient(account.balance, amount):
                    account.balance -= amount
                    account.transaction_history.add_operation_to_History(SelfOperation(NOW, "withdrawal", str(amount)))
                else:
                    raise NotEnoughFunds()
            else:
                raise PassedInvalidAmount()
        else:
            raise PassedInvalidAccountId()
