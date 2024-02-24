class BankAccount:
    
    bank_name = "Coding Dojo Bank"

    all_accounts = []

    def __init__(self, name, int_rate, balance): 
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"User has deposited ${amount}. New Balance: ${self.balance}")
        return self
    
    
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance, amount):
            self.balance -= amount
            print(f"User has withdrew ${amount}. Remaining balance: ${self.balance}.")
        else:
            self.balance = self.balance - 5
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
        self.balance = self.balance + (self.balance * self.int_rate)
        return self
    
    @classmethod
    def all_bank_account_info(cls):
        for accounts in cls.all_accounts:
            print(accounts.name)

user1 = BankAccount("User1", .06, 100)
user2 = BankAccount("User2", .03, 500)

user1.deposit(50).deposit(20).deposit(100).withdraw(5000).yield_interest().display_account_info()

user2.deposit(200).deposit(500).withdraw(50).withdraw(100).withdraw(25).withdraw(100).yield_interest().display_account_info()

BankAccount.all_bank_account_info()