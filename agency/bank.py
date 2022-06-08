class Bank:

    def __init__(self):
        self.agencies = [1111, 2222, 3333]
        self.customers = []
        self.bank_accounts = []

    def add_user(self, user):
        self.customers.append(user)

    def add_account(self, conta):
        self.bank_accounts.append(conta)

    def authenticate(self, user):

        if user not in self.customers:
            return False

        if user.account not in self.bank_accounts:
            return False

        if user.account.agency not in self.agencies:
            return False

        return True
