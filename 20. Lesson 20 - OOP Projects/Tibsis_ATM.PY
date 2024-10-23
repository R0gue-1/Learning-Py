from bank_accounts import *

print("Welcome to the royalBank of Tibsis\n 1. Create New Account - Enter 1\n Access Existing Account - Enter 2")

def tibsis_atm():
    account_name = ""
    account_nama = ""
    user_choice = input("\nYour selection : ")

    if int() not in [1,2]:
        print("\nYou must select 1 to create a new account or 2 to access an existing account")
        return tibsis_atm()
    
    def create_new_account(acct_name, acct_num):
        print("\n*** WELCOME TO THE ROYAL BANK OF TIBSIS ACCOUNT CREATION TERMINALD ***\n\nThe following details are requuired to create the account\n1-your account name\n2-your desired account number\nEnter those detials bellow")
        # nonlocal account_name
        # nonlocal account_nama

        account_name = input("Account name: ")
        account_nama = input("Account number")

        if account_name != "" and account_nama != "":
            account_name = BankAccount(account_nama)
        else:
            print("All fields are required")

    def account_actions(accountname):
        print("Welcome to the account management terminal\nSelect an action below to begin\nActions\n1. Deposite\n2. Withdrawal \n3. Transfer")


        if int(user_choice) == 1:            
            create_new_account()
            print(f"Congratulations {account_name} on creating your new RBT with account number {account_nama}\n\n")
            account_actions(account_name)

        elif user_choice == 2:
            print("existing account")


tibsis_atm()
