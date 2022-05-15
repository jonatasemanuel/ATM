from abc import ABC, abstractmethod


class Conta(ABC):

    def __init__(self, agencia:int, num_conta:int, saldo:float):
        self._agencia = agencia
        self._num_conta = num_conta
        self._saldo = saldo

    def depositar(self):
        # FAZER FUNÇÃO DE DEPÓSITO &
        # REVISAR OS REQUISITOS NA AULA.
        pass

    @property
    def saldo(self):
        return f'Saldo atual: {self._saldo}'

    @abstractmethod
    def sacar(self, qtd):
        pass





