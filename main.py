from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca
from banco import Banco

bank = Banco()

user1 = Cliente('Jonatas Emanuel', 23)
account1 = ContaPoupanca(3333, 7765, 0)

user1.add_conta(account1)
bank.add_conta(account1)
bank.add_cliente(user1)

if bank.autenticar(user1):
    user1.conta.depositar(100)
    user1.conta.sacar(110)
else:
    print('Cliente sem autorização')


user2 = Cliente('Jake Peralta', 39)
account2 = ContaCorrente(2222, 2441, 0)

user2.add_conta(account2)
bank.add_conta(account2)
bank.add_cliente(user2)

if bank.autenticar(user2):
    user2.conta.depositar(100)
    user2.conta.sacar(110)
else:
    print('Cliente sem autorização')

user3 = Cliente('Michel Scott', 52)
account3 = ContaCorrente(4354, 4563, 0)

user3.add_conta(account3)
bank.add_conta(account3)
bank.add_cliente(user3)

if bank.autenticar(user3):
    user3.conta.sacar(4500)
else:
    print('Cliente sem autorização')
