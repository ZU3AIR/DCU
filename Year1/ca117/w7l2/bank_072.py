class BankAccount():

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, value):
        self.balance = self.balance + value

    def withdraw(self, value):
        if self.balance - value >= 0:
            self.balance = self.balance - value
        else:
            print("Insufficient funds available")

    def __str__(self):
        return "Your current balance is: {:.2f} euro".format(self.balance)
