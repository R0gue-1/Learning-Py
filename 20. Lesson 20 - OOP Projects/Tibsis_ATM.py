from bank_accounts import *

print("Welcome to the royalBank of Tibsis\n 1. Create New Account - Enter 1\n Access Existing Account - Enter 2")

def tibsis_atm():
    account_name = ""
    account_nama = ""
    initiald_amt = ""

    user_choice = input("\nYour selection : ")

    if user_choice not in ["1","2"]:
        print("\n\n\nYou must select 1 to create a new account or 2 to access an existing account")
        return tibsis_atm()
    
    def create_new_account(acct_name, acct_num):
        print("\n*** WELCOME TO THE ROYAL BANK OF TIBSIS ACCOUNT CREATION TERMINALD ***\n\nThe following details are requuired to create the account\n1-your account name\n2-your desired account number\n3-your first deposit\nEnter those detials bellow\n")
        # nonlocal account_name
        # nonlocal account_nama

        account_name = input("Account name : ")
        account_nama = input("Account number : ")
        initiald_amt = input("Initial Deposit : ")

        if account_name != "" and account_nama != "":
            new_account = BankAccount(initiald_amt, account_nama, account_name)
        else:
            print("All fields are required\n\n")

    def account_actions(account_name):
        action_list = {
            "1" : "Deposite Screen",
            "2" : "Withdrawal Screen",
            "3" : "Transfer Screen",
        }
        print("Welcome to the account management terminal\nSelect an action below to begin\nActions\n1. Deposite\n2. Withdrawal \n3. Transfer")
        acct_action = input("\nSelect your desired action ...")

        if acct_action in action_list.keys():
            action_title = action_list[acct_action]

            print(f"********** ********** **********\n       {action_title}\n********** ********** **********")

            if action_title == "Withdrawal Screen":
                print("withdraw")
                
            elif action_title == "Deposite Screenn":
                print("withdraw")
            elif action_title == "Transfer Screenn":
                print("withdraw")
        else:
            print("\n\n    *** Invalid Entry !!! ***\n********** ********** **********")
            return account_actions(account_name)





    if user_choice == "1":            
        create_new_account(account_nama, initiald_amt)
        # print(f"\nCongratulations {str(account_name)} on creating your new RBT with account number {account_nama}.\n\n")
        account_actions(account_name)
    elif int(user_choice) == 2:
        print("existing account")

tibsis_atm()