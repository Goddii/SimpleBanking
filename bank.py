class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print('Personal Details')
        print('Name: ',self.name)
        print('Age: ',self.age)
        print('Gender: ',self.gender)

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self,amount):
        self.amount = int(amount)
        self.balance = self.balance + self.amount
        print(f'Account Deposit Successfull:Bank Balance:${self.balance}')

    def withdraw(self,amount):
        self.amount = int(amount)
        if self.amount > self.balance:
            print(f'Insufficient Balance to withdraw amount:Bank Balance ${self.balance}')
        else:
            self.balance = self.balance - self.amount
            print(f'Account Withdrawal Successful:You have withdrawn ${self.amount}, Bank Balance ${self.balance}')

    def view_details(self):
        self.show_details()
        print(f'Account Balance: ${self.balance}')

name = input('Enter customer name: ')
age = input('Enter customer age: ')
gender = input('Enter customer gender: ')
bank = Bank(name, age, gender)

while True:
    print('--MENU--')
    print('1.DEPOSIT')
    print('2.WITHDRAW')
    print('3.SHOW ACCOUNT INFO: ')
    print('4.QUIT')

    choice = input('Enter choice between 1-4: ')
    if choice == '1':
        amount = input('Please enter amount to deposit: ')
        bank.deposit(amount)
    elif choice == '2':
        amount = input('Please enter amount to withdraw: ')
        bank.withdraw(amount)
    elif choice == '3':
        bank.view_details()
    elif choice == '4':
        print('Thank you for Banking with us')
        break
    else:
        print('Invalid choice.Please enter number between 1-6!!')




