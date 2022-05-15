from pessoa import Pessoa
from Banco.conta import Conta


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super(Cliente, self).__init__(nome, idade)
        self.conta_corrente = []
        self.conta_poupanca = []

    def add_corrente(self, conta):
        self.conta_corrente.append(conta)

    def add_poupanca(self, conta):
        self.conta_poupanca.append(conta)

    def ver_corrente(self):
        for conta in self.conta_corrente:
            print('Conta Corrente: \n')
            print(f'Agência: {conta._agencia}/  '
                  f'Nº Conta: {conta._num_conta}')


class ContaCorrente(Conta):

    def __init__(self, agencia, num_conta, saldo):
        super().__init__()
        self._agencia = agencia
        self._num_conta = num_conta
        self._saldo = saldo

    @property
    def saldo(self):

        return f'Saldo atual: {self._saldo}'

    def sacar(self, qtd):
        print(f'Sacando: {qtd}')
        self._saldo -= qtd
        return self._saldo


class ContaPoupanca(Conta):

    def sacar(self, qtd):
        pass
