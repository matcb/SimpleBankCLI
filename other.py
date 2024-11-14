print('Welcome to BankCLI!')
balance = 0

def deposit():
    global balance  # Declare balance as global to modify it inside the function
    try:
        amount = float(input('Type the amount to deposit: '))  # Convert input to float
        if amount <= 0:
            print('Amount must be positive')
            return
        balance += amount
        print(f'Now your current balance is: ${balance:.2f}')  # Correct string formatting
    except ValueError:
        print('Please enter a valid number')

# Main program loop
while True:
    choose = input('Choose an option:\n1- Deposit\n2- Withdraw\n3- Balance\n4- Exit\n')
    
    if choose == '1':
        deposit()
    elif choose == '2':
        print('Withdraw feature not implemented yet')
    elif choose == '3':
        print(f'Your current balance is: ${balance:.2f}')
    elif choose == '4':
        print('Thank you for using BankCLI!')
        break
    else:
        print('Invalid option. Please choose 1, 2, 3, or 4')