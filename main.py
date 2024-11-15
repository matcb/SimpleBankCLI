import random
from datetime import datetime
print('Welcome to BankCLI!')

choose = input('Choose an option: \n 1- Deposit \n 2- Withdraw  \n 3- balance \n 4- create account --> ')

4
def deposit():
    amount = float(input('Type the amount that you want to deposit! \n --> '))
    account['balance'] += amount
    print(f'You deposited {amount} and now your update balance is: {account["balance"]}')

def show_balance ():
    print(f'Your current balance is: {account["balance"]:.2f}')

def withdraw():
    amount = float(input(f'How much do you want to withddraw?'))
    account['balance'] -= amount
    print(f'Now your balance is:${account["balance"]:.2f}')


def create_account():
    name = input(f'What is your name?')
    account['account_owner'] = name
    account['account_id'] = random.randint(1000,9999)
    print(f'Congrats! See your account informations below:\naccount owner:{account["account_owner"]}\n account id:{account["account_id"]}')
    

account = {'balance': 0,
           'account_id' : '', 
           'account_owner': ''}

transactions = []
def save_transaction(transaction_type, amount, status):
    transaction = {
        'date': datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        'type': transaction_type,
        'amount': amount,
        'balance_after': account['balance'],
        'status': status
    }

    

match choose:
    case '1':
        deposit()
    case '2':
        withdraw()
    case '3':
        show_balance()
    case '4': 
       create_account()
    case '5':
        show_transactions()
    










