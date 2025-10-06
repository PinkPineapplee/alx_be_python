class BankAccount:
    def __init__(self, initial_balance=0, amount=0):
     self.account_balance = initial_balance
     
    def deposit(self, amount):
       self.account_balance += amount

    def withdraw(self,amount):
      if self.account_balance < self.amount:
          return False
      else:
          self.account_balace -= self.amount
          return True

    def display_balance(self): 
       print(f"Current Balance:${self.account_balance}")     