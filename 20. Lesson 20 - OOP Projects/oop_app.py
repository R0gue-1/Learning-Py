from bank_accounts import *

Anyeyure = BankAccount(1000, "Anyeyure")
Sesa = BankAccount(2000, "Sesa")

Anyeyure.getBalance()
Sesa.getBalance()

Sesa.deposit(500)
Anyeyure.deposit(600)

Anyeyure.withdraw(10000)
Anyeyure.withdraw(10)

Anyeyure.transfer(10000, Sesa)
Anyeyure.transfer(100, Sesa)

########## ########## ########## ##########
Kekeli = InterestRewardsAcct(1000, "Kekeli")
Kekeli.getBalance()
Kekeli.deposit(100)
Kekeli.transfer(100, Anyeyure)

Blaze = SavingsAcct(1000, "Blaze")
Blaze.getBalance()
Blaze.deposit(100)
Blaze.withdraw(2000000)
