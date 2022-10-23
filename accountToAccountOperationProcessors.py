from helpers import Helpers
from abc import ABC, abstractmethod
from constants import NOW
from selfOperationProcessors import PassedInvalidAmount, NotEnoughFunds, PassedInvalidAccountId


class AccountToAccountProcessors(ABC, Helpers):

    @abstractmethod
    def operation(self, account_1, account_2, amount):
        pass


class AccountToAccountOperation:
    def __init__(self, date, type, amount, addressee, receiver):
        self.date = date
        self.type = type
        self.amount = amount
        self.addressee = addressee
        self.receiver = receiver


class TransferProcessor(AccountToAccountProcessors):

    def __init__(self, bank):
        self.bank = bank

    def operation(self, from_acc_id, to_acc_id, amount):

        acc_from = self.bank.find_account(from_acc_id)
        acc_to = self.bank.find_account(to_acc_id)

        if acc_from is not None and acc_to is not None:
            if self.is_amount_valid(amount):
                amount = float(amount)
                if self.are_funds_sufficient(acc_from.balance, amount):
                    acc_from.balance -= amount
                    acc_to.balance += amount
                    acc_from.transaction_history.add_operation_to_History(
                        AccountToAccountOperation(NOW, "transfer", amount, acc_from, acc_to))
                    acc_to.transaction_history.add_operation_to_History(
                        AccountToAccountOperation(NOW, "transfer", amount, acc_from, acc_to))
                else:
                    raise NotEnoughFunds()
            else:
                raise PassedInvalidAmount()
        else:
            raise PassedInvalidAccountId()
