class Bank_Account:

    account_balance = 0  
    amount = 0

    name = input("Enter your name: ")

    def __init__(self,starting_amount = 0.00):
         self.account_balance = starting_amount
    
    def deposit_funds(self):
        pass

    def withdraw_funds(self):
        pass

    def transaction_history(self,transaction_string):
        with open('bank_transaction_history','a') as file:
            file.write(f"$ {transaction_string}\t Balance: {self.account_balance} \n")

    print(f"Welcome {name} to Bank app")


class Deposit(Bank_Account): 
    def deposit_funds():
        deposit_amount = float(input("Enter the amount to deposit: "))
        Bank_Account.account_balance = Bank_Account.account_balance + deposit_amount
        Bank_Account.transaction_history(Deposit,f"Deposited {deposit_amount}")
        print("You have deposited: ",deposit_amount)
        print("Your new account balance is: ", Bank_Account.account_balance)

class Withdraw(Bank_Account):
    def withdraw_funds():
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        Bank_Account.account_balance = Bank_Account.account_balance - withdraw_amount
        Bank_Account.transaction_history(Withdraw,f"Withdrew {withdraw_amount}")
        print("You have withdrawn: ",withdraw_amount)
        print("Your new account balance is: ",Bank_Account.account_balance)

is_Exited = False

while(is_Exited == False):
    user_selection = input("Would you like to deposit, withdraw, or exit? ").lower()

    if(user_selection == "deposit"):
        Deposit.deposit_funds()

    elif(user_selection == "withdraw"):
        Withdraw.withdraw_funds()

    elif(user_selection == 'exit'):
        is_Exited = True
        break

    else:
        print("Sorry that is not a valid input... ")