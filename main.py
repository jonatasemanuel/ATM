from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca
from banco import Banco

banco = Banco()

c1 = Cliente('Jonatas Emanuel', 23)
conta1 = ContaCorrente(2222, 2343, 5)

banco.add_cliente(c1)
banco.add_conta(conta1)

if banco.autenticar(c1):
    c1.conta.depositar(230)
    c1.conta.sacar(20)
else:
    print('Cliente sem autorização')


c2 = Cliente('Jake Peralta', 39)
conta2 = ContaPoupanca(1111, 2441, 0)
c2.add_conta(conta2)

banco.add_conta(conta2)
banco.add_cliente(c2)

if banco.autenticar(c2):
    c2.conta.depositar(100)
    c2.conta.sacar(10)
else:
    print('Cliente sem autorização')

