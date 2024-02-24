class BankAccount: # reused from previous core assignment
    
    bank_name = "Coding Dojo Bank"

    all_accounts = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        print(f"User has deposited ${amount}. New Balance: ${self.balance}")
        return self
    
    
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
            print(f"User has withdrew ${amount}. Remaining balance: ${self.balance}.")
        else:
            self.balance -= 5
            print(f"Insufficient fund: Charging a $5 fee. New balance: {self.balance}")
        return self
    
    @staticmethod
    def can_withdraw(balance, amount):
        if (balance - amount) < 0:
            return False
        else:
            return True
    
    def display_account_info(self):
        print(f"Interest rate: {self.int_rate}")
        print(f"User balance: {self.balance}")
        return self
    
    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self
    
    @classmethod
    def all_bank_account_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.balance = self.account.balance
        print(f"{self.name}'s Balance: {self.balance}")
        return self
    
    def transfer_money(self, amount, other_user):
        if self.account.balance - amount < 0:
            print(f"Insufficient Funds.")
        else:
            self.account.withdraw(amount)
            other_user.account.deposit(amount)
            print(f"{self.name} has transfered {amount} to {other_user.name}'s account.")
            self.display_user_balance()
        return self

user1 = User("Garret", "cuadragarret@gmail.com")
user2 = User("Nathan", "abc@gmail.com")
user1.display_user_balance().make_deposit(5000).make_withdrawal(10000).make_withdrawal(100).display_user_balance().transfer_money(200, user2)

