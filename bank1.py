class User:
    def __init__(self, name,age,gender):
        self.name = name
        self.age= age
        self.gender = gender

    def show_details(self):
        print('PersonaL Details!!')
        print('Name:',self.name)
        print('Age:',self.age)
        print('Gender: ',self.gender)

class Bank(User):
    def __init__(self, name,age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self,amount):
        self.amount = int(amount)
        self.balance = self.balance + self.amount
        print(f'Account Successfully deposited: Bank Balance:${self.balance}')

    def withdraw(self,amount):
        self.amount = int(amount)
        if self.amount > self.balance:
            print(f'Insufficient balance in account:Bank Balance:{self.balance}')
        else:
            self.balance = self.balance - self.amount
            print(f'Account withdrawal successful:Amount withdrawn ${self.amount}: Bank Balance: ${self.balance}')

    def view_details(self):
        self.show_details()
        print(f'Account Balance: {self.balance}')

name = input('Enter name: ')
age = input('Enter age: ')
gender = input('Enter gender: ')

bank = Bank(name, age, gender)
while True:
    print('--MENU--')
    print('1. Show details')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Quit')


    choice = input('Enter choice between 1-4: ')
    if choice == '1':
        bank.view_details()
    elif choice == '2':
        amount = input('Please enter amount to deposit: ')
        bank.deposit(amount)
    elif choice == '3':
        amount = input('Please enter amount to withdraw: ')
        bank.withdraw(amount)
    elif choice == '4':
        print('Thank you for banking with us!! <-|->')
        break
    else:
        print('Invalid choice.Please enter valid number between 1-4!!!')
