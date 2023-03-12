# https://www.codewars.com/kata/5a03af9606d5b65ff7000009

class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
        
    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError
        else:
            self.balance = self.balance - amount
        return f'{self.name} has {self.balance}.'
    
    def check(self, recipient, amount):
        if recipient.balance <= amount:
            raise ValueError
        if recipient.checking_account == False:
            raise ValueError
        recipient.withdraw(amount)
        self.balance += amount
        return f'{self.name} has {self.balance} and {recipient.name} has {recipient.balance}.'

    
    def add_cash(self, amount):
        self.balance += amount
        return f'{self.name} has {self.balance}.'
