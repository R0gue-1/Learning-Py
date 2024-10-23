class BallanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName

        print(f"\nAccount '{self.name}' created.\nBallance = GH₵{self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = GH₵{self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit of {amount} made for {self.name}'s Account")
        self.getBalance

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BallanceException(f"\nSorry, account '{self.name} only has a balance of GH₵{self.balance:.2f}")
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
        except BallanceException as error:
            print(f"Withdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer ..')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('Transfer complete \n\n ***********')
        except BallanceException as error:
            print(f"\nTransfer interupted .. {error}")

class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.5)
        print("\nDeposite complete")
        self.getBalance()

class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdrawal completed")
            self.getBalance()
        except BallanceException as error:
            print(f"\nWithdrawal interrupted: {error}")