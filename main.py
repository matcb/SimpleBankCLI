
print('Welcome to BankCLI!')
choose = input('Choose an option: \n 1- Deposit \n 2- Withdraw  \n 3- balance \n --> ')

balance = 0

def deposit():
    
    global balance
    amount = float(input('Type the amount that you want to deposit! \n --> '))
    balance += amount
    print(f'Now your current balance is: ${balance:.2f}')


if choose == '1':
    deposit()












