class Student():

    def __init__(self, surname, forename, sid, modlist=[]):
        self.surname = surname
        self.forename = forename
        self.sid = sid
        self.modlist = modlist

    def add_module(self, new_module):
        if new_module not in self.modlist:
            self.modlist.append(new_module)

    def del_module(self, new_module):
        if new_module in self.modlist:
            self.modlist.remove(new_module)

    def print_details(self):
        print("ID: {}".format(self.sid))
        print("Surname: {}".format(self.surname))
        print("Forename: {}".format(self.forename))
        print("Modules: {}".format(" ".join(self.modlist)))
