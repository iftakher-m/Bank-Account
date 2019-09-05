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

class Checking(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath) # 'init' method from class 'Account' is called .
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - (self.fee + amount )

checking = Checking("balance.txt",5)
# checking.deposit(1200)
# print(checking.balance)
# checking.transfer(100)
# print(checking.balance)
checking.commit()
print(checking.balance)