from agency.user import User
from agency.account import CheckingAccount, SavingsAccount
from agency.bank import Bank


bank = Bank()
print()

username = str(input('Name: '))
user_age = int(input('Age: '))
user = User(username, user_age)
print('__' * 20)

account_type = int(input('Choose your type account↓\n'
                         '[ 1 ] → Savings Account\n'
                         '[ 2 ] → Checking Account\n'
                         '[ 0 ] → Cancel operation\n'
                         '→ '))

print('__' * 15)
user_agency = int(input('Agency: '))
account_number = int(input('Account: '))

if account_type == 1:
    account = SavingsAccount(user_agency, account_number, 0)
if account_type == 2:
    account = CheckingAccount(user_agency, account_number, 0)

user.add_account(account)
bank.add_account(account)
bank.add_user(user)

while True:

    if bank.authenticate(user):
        print('__' * 15)
        op = int(input('[ 1 ] → Deposit \n'
                        '[ 2 ] → To withdraw \n'
                        '[ 3 ] → Detail \n'
                        '[ 0 ] → Exit \n'
                        '→ '))
        if op == 1:
            value_to_deposit = float(input('US$ '))
            user.account.deposit(value_to_deposit)
        if op == 2:
            value_to_withdraw = float(input('US$ '))
            user.account.to_withdraw(value_to_withdraw)
        if op == 3:
            user.account.details()
        if op == 0:
            pass
            # break
        print('__' * 15)
        cont = int(input('Do would you like a new operation ?\n'
                            '[ 1 ] Yes\n'
                            '[ 2 ] No\n'
                            '→ '))
        if cont == 1:
            continue
        else:
            break
    else:
        print('__' * 15)
        print('No authenticate')
