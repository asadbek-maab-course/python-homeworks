from random import randint
import json as js
class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.__balance = balance
    
    def show_balance(self):
        return self.__balance
    
    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        else:
            print("amount 0 dan katta bo'lishi kerak")
        return False
    def withdraw(self, amount):
        if amount > 0 and amount < self.__balance:
            self.__balance -= amount
            return True
        elif amount > self.__balance:
            print("Mablag' yetarli emas")
        else:
            print("amount 0 dan katta bo'lishi kerak")
        return False
    
    def to_json(self):
        json_string = '{"account_number": "{}", "name" : "{}", "balance" : "{}"}'.format(self.account_number, self.name, self.__balance)
        return json_string
    
    def __str__(self):
        return f"Account({self.name}, {self.account_number}, {self.__balance})"
    
    def details(self):
        return f"Owner          | {self.name}\nAccount number | {self.account_number}\nBalance        | {self.__balance}"

class Bank:    
    def __init__(self):
        self.file = "/media/asadbek/D/maab/new/python-homeworks/lesson-8/homework/bank.json"
        self.accounts = self.load_from_file()

    def view_all(self):
        for i in self.accounts:
            print(i)

    def create_account(self):
        name = input("Enter name: ")
        initial_deposit = int(input("Enter first deposite amount: "))
        account_number = str(randint(1,9))
        for i in range(15):
            account_number += str(randint(0,9))
        acc = Account(account_number, name, initial_deposit)
        self.accounts.append(acc)
        self.save_to_file()
        print("Account created successfully!")
        print(acc.details())

    def save_to_file(self):
        f = open(self.file, 'w')
        f.write(self.accounts_to_line())
        f.close()
    
    def load_from_file(self):
        lst = []
        with open(self.file, 'r') as f:
            for acc in js.loads(f.read() or "[]"):
                lst.append(Account(acc['account_number'], acc['name'], acc['_Account__balance']))
        return lst

    def accounts_to_line(self):
        return js.dumps(self.accounts, default = lambda a:a.__dict__, sort_keys=1)
    
    def search(self, number = None, get = False):
        if number is None:
            number = input("Enter account number(16 digit):")
        number = str(number)
        for a in self.accounts:
            if a.account_number == number:
                if get:
                    return a
                print(a.details())
                break
        else:
            print("Account not found")
    
    def deposite(self):
        number = input("Enter account number(16 digit): ")
        a = self.search(number, get=True)
        if a is None:
            return
        amount = int(input("Enter amount of money: "))
        if a.deposite(amount):
            print("Deposite successfull")
            print(f"{a.name}'s balance:", a.show_balance())
    def withdraw(self):
        number = input("Enter account number(16 digit): ")
        a = self.search(number, get=True)
        if a is None:
            return
        amount = int(input("Enter amount of money: "))
        if a.withdraw(amount):
            print("Withdraw successfull")
            print(f"{a.name}'s balance:", a.show_balance())


b = Bank()
def hl():
    print("""h - help
a - view all
c - create new account
s - show account details
d - deposite to account
w - withdraw
q - quit""")

hl()
while True:
    c = input(">> ")
    if c == 'h':
        hl()
    elif c == 'a':
        b.view_all()
    elif c == 'c':
        b.create_account()
    elif c == 's':
        b.search()
    elif c == 'd':
        b.deposite()
        b.save_to_file()
    elif c == 'w':
        b.withdraw()
        b.save_to_file()
    elif c == 'q':
        break
