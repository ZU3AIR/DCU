class Customer(object):
    d = 0

    def __init__(self, name, bal, ad1, ad2, ad3):
        self.name = name
        self.bal = bal
        self.ad1 = ad1
        self.ad2 = ad2
        self.ad3 = ad3

    def owes(self):
        return self.bal * (1 - self.d)

    def __str__(self):
        LIST = []
        LIST.append("{:s}".format(self.name))
        LIST.append("{:s}".format(self.ad1))
        LIST.append("{:s}".format(self.ad2))
        LIST.append("{:s}".format(self.ad3))
        LIST.append("Balance: {:.2f}".format(self.bal))
        LIST.append("Discount: {:.0f}%".format(self.d * 100))
        LIST.append("Amount due: {:.2f}".format(self.owes()))
        return "\n".join(LIST)

class ValuedCustomer(Customer):
    d = 0.1
