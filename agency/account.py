from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, agency: int, account: int, balance: float):
        self.agency = agency
        self.account = account
        self.balance = balance

    def deposit(self, qtd):
        self.balance += qtd
        print(f'Depositing: {qtd}')
        self.details()

    def details(self):
        print(f'Agency: {self.agency} '
              f'Account: {self.account} '
              f'Balance: {self.balance}')

    @abstractmethod
    def to_withdraw(self, qtd):
        pass


class CheckingAccount(Account):

    def __init__(self, agency, conta, balance, limit=100):
        super().__init__(agency, conta, balance)
        self.limit = limit

    def to_withdraw(self, qtd):
        print(f'Sacando: {qtd}')
        if self.balance + self.limit < qtd:
            print('Saldo insuficiente')
            return

        self.balance -= qtd
        self.details()


class SavingsAccount(Account):

    def to_withdraw(self, qtd):
        print(f'Sacando: {qtd}')
        if self.balance < qtd:
            print('Saldo insuficiente')
            return

        self.balance -= qtd
        self.details()
