from agency.person import Person


class User(Person):

    def __init__(self, name, age):
        super().__init__(name, age)
        self.account = None

    def add_account(self, account):
        self.account = account
