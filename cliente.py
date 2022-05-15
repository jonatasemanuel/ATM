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

    def ver_poupanca(self):
        for conta in self.conta_poupanca:
            print('Poupanca: \n')
            print(f'Agência: {conta._agencia}/  '
                  f'Nº Conta: {conta._num_conta}')


class ContaCorrente(Conta):

    def sacar(self, qtd):
        limite = -500
        print(f'Sacando: {qtd}')
        if not qtd > self._saldo:
            self._saldo -= qtd
            return self._saldo
        else:
            caixa = self._saldo
            self._saldo -= (qtd + limite) - limite
            if self._saldo < limite:
                self._saldo = caixa
                return print(f'Saldo insuficiente')


class ContaPoupanca(Conta):

    def sacar(self, qtd):
        print(f'Sacando: {qtd}')
        if not qtd > self._saldo:
            self._saldo -= qtd
            return self._saldo

        return print('Saldo insuficiente')
