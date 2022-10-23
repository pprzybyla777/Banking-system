from bank import Bank
from account import Account
from selfOperationProcessors import DepositProcessor, WithdrawProcessor

B = Bank()

a1 = Account("Joe", 1)
a2 = Account("Ann", 2222)

B.add_account(a1)
B.add_account(a2)

print(a1.__dict__)
print(a2.__dict__)

d = DepositProcessor(B)
w = WithdrawProcessor(B)

d.operation(a1.get_id, 10)

print(a1.__dict__)

print("H")
print(a1.transaction_history.show_history[0].__dict__["date"])
