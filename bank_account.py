import random

# create Class defining a bank account.
# following attributes: owners name, account number, balance


class BankAccount:
    def __init__(self, full_name):
        self.full_name = full_name
        self.account_number = random.randint(80000000, 89999999)
        self.balance = 0
