from datetime import datetime

print('Welcome to BankCLI!')

# Initialize account and transaction storage
account = {
    'balance': 0,
    'account_number': '12345',
    'holder_name': 'Default User'
}

# List to store transaction history
transactions = []

def save_transaction(transaction_type, amount, status):
    transaction = {
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'type': transaction_type,
        'amount': amount,
        'balance_after': account['balance'],
        'status': status
    }
    transactions.append(transaction)

def deposit():
    try:
        amount = float(input('Type the amount to deposit: '))
        if amount <= 0:
            print('Amount must be positive')
            save_transaction('deposit', amount, 'failed')
            return
            
        account['balance'] += amount
        save_transaction('deposit', amount, 'success')
        print(f"Now your current balance is: ${account['balance']:.2f}")
    except ValueError:
        print('Please enter a valid number')
        save_transaction('deposit', 0, 'failed')

def withdraw():
    try:
        amount = float(input('Type the amount to withdraw: '))
        if amount <= 0:
            print('Amount must be positive')
            save_transaction('withdraw', amount, 'failed')
            return
            
        if amount > account['balance']:
            print('Insufficient funds')
            print(f"Your current balance is: ${account['balance']:.2f}")
            save_transaction('withdraw', amount, 'failed')
            return
            
        account['balance'] -= amount
        save_transaction('withdraw', amount, 'success')
        print(f'Successfully withdrew ${amount:.2f}')
        print(f"Now your current balance is: ${account['balance']:.2f}")
    except ValueError:
        print('Please enter a valid number')
        save_transaction('withdraw', 0, 'failed')

def show_balance():
    print(f"Your current balance is: ${account['balance']:.2f}")

def show_transactions():
    if not transactions:
        print("\nNo transactions yet.")
        return
        
    print("\nTransaction History:")
    print("-" * 80)
    print(f"{'Date':<20} {'Type':<10} {'Amount':<10} {'Balance':<10} {'Status':<10}")
    print("-" * 80)
    
    for t in transactions:
        print(f"{t['date']:<20} {t['type']:<10} ${t['amount']:<9.2f} ${t['balance_after']:<9.2f} {t['status']:<10}")

# Main program loop
while True:
    choose = input('\nChoose an option:\n1- Deposit\n2- Withdraw\n3- Balance\n4- Transaction History\n5- Exit\n')
    
    match choose:
        case '1':
            deposit()
        case '2':
            withdraw()
        case '3':
            show_balance()
        case '4':
            show_transactions()
        case '5':
            print('Thank you for using BankCLI!')
            break
        case _:
            print('Invalid option. Please choose 1, 2, 3, 4, or 5')