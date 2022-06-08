from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, agency: int, account: int, balance: float):
        self.agency = agency
        self.account = account
        self.balance = balance

    def deposit(self, qtd):
        self.balance += qtd
        print(f'Depositing: US$ {qtd}')
        self.details()

    def details(self):
        print(f'Agency: {self.agency} '
              f'Account: {self.account} '
              f'Balance: US$ {self.balance}')

    @abstractmethod
    def to_withdraw(self, qtd):
        pass


class CheckingAccount(Account):

    def __init__(self, agency, account, balance, limit=500):
        super().__init__(agency, account, balance)
        self.limit = limit

    def to_withdraw(self, qtd):
        print(f'Drawing: US$ {qtd}')
        if self.balance + self.limit < qtd:
            print('No cash')
            return

        self.balance -= qtd
        self.details()


class SavingsAccount(Account):

    def to_withdraw(self, qtd):
        print(f'Drawing: US$ {qtd}')
        if self.balance < qtd:
            print('No cash')
            return

        self.balance -= qtd
        self.details()
