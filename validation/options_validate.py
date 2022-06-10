
def username_input():
    username = str(input('Name: '))
    return username

def user_age_input():
    user_age = int(input('Age: '))
    return user_age

def show_account_types():
    account_type = int(input(
                         'Choose your type account↓\n'
                         '[ 1 ] → Savings Account\n'
                         '[ 2 ] → Checking Account\n'
                         '[ 0 ] → Cancel operation\n'
                         '→ '))
    return account_type

def user_agency_input():
    user_agency = int(input('Agency: '))
    return user_agency

def user_account_input():
    account_number = int(input('Account: '))
    return account_number

def atm_options():
    op = int(input(
        '[ 1 ] → Deposit \n'
        '[ 2 ] → To withdraw \n'
        '[ 3 ] → Detail \n'
        '[ 0 ] → Exit \n'
        '→ '))
    return op

def new_operation_input():
    cont = int(input('Do would you like a new operation ?\n'
                     '[ 1 ] Yes\n'
                     '[ 2 ] No\n'
                     '→ '))
    return cont
    # return account_options