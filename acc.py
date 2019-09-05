class Account:

    def __init__(self, filepath):
       self.path = filepath # 'self.path' is an instance variable of 'filepath'(argument of 'init'),to use it commit function 
       with open(filepath, 'r') as file:
            self.balance = int(file.read())
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
    
    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.path, 'w') as file:
            file.write(str(self.balance))

account = Account("balance.txt")
print(account.balance)
account.withdraw(100)
print(account.balance)
account.deposit(200)
print(account.balance)
account.commit()