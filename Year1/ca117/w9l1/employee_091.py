
class Employee(object):

    def __init__(self, name, num):
        self.name = name
        self.num = num

    def wages(self):
        return 0.00

    def __str__(self):
        LIST = []
        LIST.append("Name: {:s}".format(self.name))
        LIST.append("Number: {:d}".format(self.num))
        LIST.append("Wages: {:.2f}".format(self.wages()))
        return "\n".join(LIST)

class Manager(Employee):

    def __init__(self, name, num, sal):
        super().__init__(name, num)
        self.sal = sal

    def wages(self):
        return self.sal / 52

class AssemblyWorker(Employee):

    def __init__(self, name, num, pph, hrs):
        super().__init__(name, num)
        self.pph = pph
        self.hrs = hrs

    def wages(self):
        return self.pph * self.hrs
