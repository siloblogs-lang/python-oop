# Bad exapmle
class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance

account = BadBankAccount(0)
account.balance = -1
print(account.balance)

# better solution
class BankAccount:
    def __init__(self):
        self._balance = 0.0

    # getter property to get balance
    @property
    def balance(self):
        return self._balance
    
    def _invalid_amount(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must me greater than 0")
    
    def deposit(self, amount):
        self._invalid_amount(amount)
        self._balance += amount

    def withdraw(self, amount):
        self._invalid_amount(amount)
        if amount > self._balance:
            raise ValueError("You have insuffient fund")
        self._balance -= amount

account1 = BankAccount()
account1.deposit(10)
print(account1.balance)
account1.withdraw(15)
print(account1.balance)