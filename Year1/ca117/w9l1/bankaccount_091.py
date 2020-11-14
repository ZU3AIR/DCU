class BankAccount(object):

    nan = 16555232
    at = "General"

    def __init__(self, fn, sn, bal):
        self.fn = fn
        self.sn = sn
        self.bal = bal
        self.an = BankAccount.nan
        BankAccount.nan += 1

    def lodge(self, b):
        self.bal += b

    def withdraw(self, b):
        if self.bal > b:
            self.bal -= b
        else:
            print("Insufficient funds available")

    def __str__(self):
        LIST = []
        LIST.append("Name: {} {}".format(self.fn, self.sn))
        LIST.append("Account number: {}".format(self.an))
        LIST.append("Account type: {}".format(self.at))
        LIST.append("Balance: {:.2f}".format(self.bal))
        return "\n".join(LIST)

class CurrentAccount(BankAccount):

    overD = -1000
    at = "Current"

    def withdraw(self, num):
        if self.bal - num >= -1000:
            self.bal -= num
        else:
            print("Insufficient funds available")

    def __str__(self):
        LIST = []
        LIST.append(super().__str__())
        LIST.append("Overdraft: {:.2f}".format(self.overD))
        return "\n".join(LIST)

class SavingsAccount(BankAccount):

    inR = 0.01
    at = "Savings"

    def apply_interest(self):
        self.bal *= (1 + self.inR)

    def __str__(self):
        LIST = []
        LIST.append(super().__str__())
        LIST.append("Interest rate: {}".format(self.inR))
        return "\n".join(LIST)
