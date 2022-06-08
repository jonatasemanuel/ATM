from agency.user import User
from agency.account import CheckingAccount, SavingsAccount
from agency.bank import Bank


bank = Bank()
print()

usernarme = str(input('Name: '))
user_age = int(input('Age: '))
user = User(usernarme, user_age)

account_type = int(input('Choose your type account:\n'
                         '[ 1 ] → Savings Account\n'
                         '[ 2 ] → Checking Account\n'
                         '[ 0 ] → Cancel operation\n'))

if account_type == 1:
    user_agency = int(input('Agency: '))
    account_number = int(input('Account: '))
    account = SavingsAccount(user_agency, account_number, 0) # agency, acc, balance

    user.add_account(account)
    bank.add_account(account)
    bank.add_user(user)

    if bank.authenticate(user):
        op = int(input('For deposit press [ 1 ]: \n'
                       'For to withdraw   [ 2 ]: \n'
                       'For detail        [ 3 ]: \n'))
        if op == 1:
            value_to_deposit = float(input('$'))
            user.account.deposit(value_to_deposit)
        if op == 2:
            value_to_withdraw = float(input('$'))
            user.account.to_withdraw(value_to_withdraw)
    else:
        print('No authenticate')

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
