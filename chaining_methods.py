class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
        else:
            print("Insufficient funds for withdrawal! Current balance is:", self.account_balance)
        return self

    def display_user_balance(self):
        print("Current balance for ", self.name, "is:", self.account_balance)
        return self

    def transfer_money( self, person, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            person.account_balance += amount  
            print("Transfering ", amount, " from ", self.name, " to ", person.name)  
            print("Current balance for ", self.name, "is:", self.account_balance)
            print("Current balance for ", person.name, "is:", person.account_balance)
        else:
            print("Insufficient funds for transfer! Current balance is:", self.account_balance)
        return self
    
nate = User("Nate Langione", "nate@gmail.com")
john = User("John smith", "jsmith@gmail.com")
jane = User("Jane doe", "jdoe@gmail.com")


nate.make_deposit(100).make_deposit(10).make_deposit(45).make_withdrawal(50).display_user_balance().transfer_money(jane, 50)

john.make_deposit(25).make_deposit(75).make_withdrawal(57).make_withdrawal(25).display_user_balance()

jane.make_deposit(500).make_withdrawal(40).make_withdrawal(200).make_withdrawal(85).display_user_balance()
