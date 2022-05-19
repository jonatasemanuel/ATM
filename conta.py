from abc import ABC, abstractmethod


class Conta(ABC):

    def __init__(self, agencia: int, conta: int, saldo: float):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, qtd):
        self.saldo += qtd
        print(f'Depositando: {qtd}')
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self.agencia} '
              f'Conta: {self.conta} '
              f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, qtd):
        pass


class ContaCorrente(Conta):

    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, qtd):
        print(f'Sacando: {qtd}')
        if self.saldo + self.limite < qtd:
            print('Saldo insuficiente')
            return

        self.saldo -= qtd
        self.detalhes()


class ContaPoupanca(Conta):

    def sacar(self, qtd):
        print(f'Sacando: {qtd}')
        if self.saldo < qtd:
            print('Saldo insuficiente')
            return

        self.saldo -= qtd
        self.detalhes()
