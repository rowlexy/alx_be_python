class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
    def deposit(self, amount):
        if amount < 0:
            print("You can only deposit an amount greater than zero")
        else:
            self.account_balance += amount
            return f"Deposited: ${amount:.2f}"
    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        elif amount <= 0:
            return False
        else:
            self.account_balance -= amount
            return True
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
