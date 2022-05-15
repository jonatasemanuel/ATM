from abc import ABC, abstractmethod


class Conta(ABC):

    def depositar(self):
        pass

    def saldo(self):
        pass

    @abstractmethod
    def sacar(self, qtd):
        pass





