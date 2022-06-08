from agency.user import User
from agency.account import CheckingAccount, SavingsAccount
from agency.bank import Bank


bank = Bank()
print()
user1 = User('Jonatas Emanuel', 23)
account1 = SavingsAccount(3333, 7765, 0)

user1.add_account(account1)
bank.add_account(account1)
bank.add_user(user1)

if bank.autenticar(user1):
    user1.account.depositar(100)
    user1.account.sacar(110)
else:
    print('Cliente sem autorização')

# print()
# user2 = Cliente('Jake Peralta', 39)
# account2 = ContaCorrente(2222, 2441, 0)

# user2.add_conta(account2)
# bank.add_conta(account2)
# bank.add_cliente(user2)

# if bank.autenticar(user2):
#     user2.conta.depositar(100)
#     user2.conta.sacar(110)
# else:
#     print('Cliente sem autorização')

# print()
# user3 = Cliente('Michel Scott', 52)
# account3 = ContaCorrente(4354, 4563, 0)

# user3.add_conta(account3)
# bank.add_conta(account3)
# bank.add_cliente(user3)

# if bank.autenticar(user3):
#     user3.conta.sacar(4500)
# else:
#     print('Cliente sem autorização')
