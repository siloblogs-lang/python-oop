class BankAccount:
    MIN_BALANCE = 100
    
    @property
    def _print_balance(self):
        print("1st balance: $", self._balance)

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance
        self._print_balance


    def _is_valid_amount(self, amount):
        return amount > 0

    def __log_transaction(self, transaction_type, amount):
        print(f"You've made ${amount} {transaction_type}. New balance: ${self._balance}")

    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            # print("Your new balance: $",self._balance )
            self.__log_transaction("deposit", amount)

    def withdrawal(self, amount):
        if amount > 0:
            self._balance -= amount
            self.__log_transaction("withdrawal", amount)

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5
    
account = BankAccount("Alice", 500)
account.deposit(200)
account.withdrawal(300)
# Access static method on the class
print(BankAccount.is_valid_interest_rate(3.5))
print(BankAccount.is_valid_interest_rate(12))