from agency.user import User
from agency.account import CheckingAccount, SavingsAccount
from agency.bank import Bank
from validation.options_validate import atm_options, new_operation_input, show_account_types, user_account_input, user_age_input, user_agency_input, username_input


bank = Bank()
print('Avaible agencies: 1111 | 2222 | 3333')
print()

username = username_input()
user_age = user_age_input()
user = User(username, user_age)

print('__' * 20)

account_type = show_account_types()

print('__' * 20)
user_agency = user_agency_input()
account_number = user_account_input()

if account_type == 1:
    account = SavingsAccount(user_agency, account_number, 0)
if account_type == 2:
    account = CheckingAccount(user_agency, account_number, 0)

user.add_account(account)
bank.add_account(account)
bank.add_user(user)

while True:

    if bank.authenticate(user):
        print('__' * 20)

        op = atm_options()
        if op == 1:
            value_to_deposit = float(input('US$ '))
            user.account.deposit(value_to_deposit)
        if op == 2:
            value_to_withdraw = float(input('US$ '))
            user.account.to_withdraw(value_to_withdraw)
        if op == 3:
            user.account.details()
        if op == 0:
            break
        else:
            # run the options(op) again
            # make de funciction with the options validation.
            pass

        print('__' * 20)

        cont = new_operation_input()
        if cont == 1:
            continue
        else:
            break
    else:
        print('__' * 20)
        print('No authenticate')
        break
