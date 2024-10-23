from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sarah = BankAccount(2000, "Sarah")

Dave.getBalance()
Sarah.getBalance()

Sarah.deposit(500)
Dave.deposit(600)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(10000, Sarah)

########## ########## ########## ##########

