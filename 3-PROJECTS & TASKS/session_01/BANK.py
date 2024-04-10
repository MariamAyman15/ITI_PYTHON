class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, account_number, name, balance=0):
        # Check if the account already exists
        if account_number in self.accounts:
            print(f"Account {account_number} already exists!")
        else:
            # Create a dictionary to store the account details
            self.accounts[account_number] = {'name': name, 'balance': balance}
            print(f"Account {account_number} opened for {name} with balance {balance}")

    def close_account(self, account_number):
        # Check if the account exists
        if account_number not in self.accounts:
            print(f"Account {account_number} does not exist!")
        else:
            # Remove the account from the dictionary
            self.accounts.pop(account_number)
            print(f"Account {account_number} closed")

    def deposit(self, account_number):
        # Check if the account exists
        if account_number not in self.accounts:
            print(f"Account {account_number} does not exist!")
        else:
            # Prompt the user to enter the amount to deposit
            amount = float(input("Enter amount to deposit: "))
            # Add the deposit amount to the account balance
            self.accounts[account_number]['balance'] += amount
            print(f"Deposited {amount} into account {account_number}. New balance is {self.accounts[account_number]['balance']}")

    def withdraw(self, account_number):
        # Check if the account exists
        if account_number not in self.accounts:
            print(f"Account {account_number} does not exist!")
        else:
            # Prompt the user to enter the amount to withdraw
            amount = float(input("Enter amount to withdraw: "))
            # Check if the account has sufficient balance
            if amount > self.accounts[account_number]['balance']:
                print(f"Insufficient balance in account {account_number}")
            else:
                # Subtract the withdrawal amount from the account balance
                self.accounts[account_number]['balance'] -= amount
                print(f"Withdrew {amount} from account {account_number}. New balance is {self.accounts[account_number]['balance']}")

    def get_balance(self, account_number):
        # Check if the account exists
        if account_number not in self.accounts:
            print(f"Account {account_number} does not exist!")
        else:
            # Print the account balance and holder's name
            print(f"Balance of account {account_number} for {self.accounts[account_number]['name']} is {self.accounts[account_number]['balance']}")

    def get_all_accounts(self):
        # Return a set of all account numbers
        return set(self.accounts.keys())

# Create a new instance of the Bank class
bank = Bank()

# Open multiple accounts with user-provided details
while True:
    name = input("Enter your name (or 'quit' to exit): ")
    if name == 'quit':
        break
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance (optional): "))
    bank.open_account(account_number, name, initial_balance)

# Display all accounts in the bank system
print("All accounts in the bank system:")
for account_number in bank.get_all_accounts():
    bank.get_balance(account_number)

# Perform banking operations on one of the accounts
account_number = input("Enter account number to perform banking operations: ")
bank.deposit(account_number)
bank.withdraw(account_number)
bank.get_balance(account_number)

# Close the account
bank.close_account(account_number)