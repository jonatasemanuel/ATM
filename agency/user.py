from agency.person import Person


class User(Person):

    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.account = None

    def add_account(self, conta):
        self.account = conta
