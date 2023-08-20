# check balance
# deposit
# withdraw

class ATM:
    def __init__(self,balance=0):
        self.balance = balance
    def __str__(self):
        return f'Your balance is : {self.balance}' 
    
    def deposit(self,amount):
        if amount <=0:
            return 'Your entered ammount is invalid'
        self.balance=self.balance+amount
        return f"{amount} is added in your account successfully"
    def withdraw(self,amount):
        if amount <=0:
            return 'Your entered ammount is invalid'
        if self.balance<amount:
            return 'yout funds are insufficient for this transanction'
        self.balance=self.balance-amount
        return f"{amount} is withdraw from your account successfully"

class ATM2(ATM):
    pass

my_atm2= ATM2(200)
print(my_atm2.balance)

# def display_menu():
#     print('*******ATM MENU*******')
#     print('1. Check Balance')
#     print('2. Deposit')
#     print('3. Withdraw')
#     print('4. Exit')
    
# #    main code
# my_atm = ATM(200)

# while True:
#     display_menu()
#     choice=input('Enter Your choice (1-4): ')
#     print('*******************************')
#     if choice =='1':
#         print(my_atm)
#     elif choice=='2':
#         amount=float(input('Enter the amount for deposit : '))
#         print(my_atm.deposit(amount))
#     elif choice=='3':
#         amount=float(input('Enter the amount for withdraw : '))
#         print(my_atm.withdraw(amount))
#     elif choice=='4':
#         print('Thanks for using ATM, Hava a Nice Day')
#         break
#     else:
#         print('invalid input')
