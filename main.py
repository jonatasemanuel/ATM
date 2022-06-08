from agency.user import User
from agency.account import CheckingAccount, SavingsAccount
from agency.bank import Bank


bank = Bank()
print()

usernarme = str(input('Name: '))
user_age = int(input('Age: '))
user = User(usernarme, user_age)

account_type = int(input('Choose your type account↓\n'
                         '[ 1 ] → Savings Account\n'
                         '[ 2 ] → Checking Account\n'
                         '[ 0 ] → Cancel operation\n'
                         '→'))

if account_type == 1:
    user_agency = int(input('Agency: '))
    account_number = int(input('Account: '))
    account = SavingsAccount(user_agency, account_number, 0) # agency, acc, balance

    user.add_account(account)
    bank.add_account(account)
    bank.add_user(user)

    if bank.authenticate(user):
        op = int(input('[ 1 ]For deposit press \n'
                       '[ 2 ]For to withdraw \n'
                       '[ 3 ]For detail \n'
                       '[ 0 ]For exit \n'
                       '→'))
        if op == 1:
            value_to_deposit = float(input('$'))
            user.account.deposit(value_to_deposit)
        if op == 2:
            value_to_withdraw = float(input('$'))
            user.account.to_withdraw(value_to_withdraw)
        if op == 3:
            user.account.details()
        if op == 0:
            pass
            # break
        cont = int(input('Do would you like a new operation ?\n'
                         '[ 1 ] Yes\n'
                         '[ 2 ] No\n'
                         '→'))
        if cont == 1:
            pass
            # continue
        else:
            pass
            # break
    else:
        print('No authenticate')
