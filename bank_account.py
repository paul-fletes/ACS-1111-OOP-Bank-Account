import random

# create Class defining a bank account.
# following attributes: owners name, account number, balance


class BankAccount:
    def __init__(self, full_name):
        self.full_name = full_name
        self.account_number = random.randint(80000000, 99999999)
        self.balance = 0

# methods defined below: deposit, withdraw, get_balance, add_interest, print_statement
    def deposit(self, amount):
        self.balance += amount
        print(f'Amount deposited: ${amount}. New balance: ${self.balance}')

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance -= 10
            print(f'Insufficient funds. You will be charged a $10 overdraft fee.')
        else:
            print(f'Amount withdrawn: ${amount}. New balance: ${self.balance}')

    def get_balance(self):
        print(f'Your balance is: ${self.balance}')
        return self.balance

    def add_interest(self):
        if self.balance > 0:
            interest = (self.balance * 0.00083)
            self.balance += interest
            self.balance = round(self.balance, 2)

    def print_statement(self):
        secure_account = str(self.account_number)
        secure_account = (secure_account[4:8])
        secure_account = f'****{secure_account}'
        print(
            f'{self.full_name}\nAccount Number: {secure_account}\nBalance: {self.balance}')


# 3 instances of BankAccount class below:
mitchell_account = BankAccount('Mitchell')
mitchell_account.deposit(400000)
mitchell_account.print_statement()
mitchell_account.add_interest()
mitchell_account.print_statement()
mitchell_account.withdraw(150)
mitchell_account.print_statement()

intern_account = BankAccount('Paul')
intern_account.deposit(1400)
intern_account.add_interest()
intern_account.print_statement()
intern_account.withdraw(1450)
intern_account.print_statement()

dev_account = BankAccount('Mark')
dev_account.deposit(100000)
dev_account.add_interest()
dev_account.print_statement()
dev_account.withdraw(1000)
dev_account.print_statement()
