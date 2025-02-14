def deposit(account, amount):
    if amount <= 0:
        print("Deposit amount must be greater than zero.")
    else:
        account['balance'] += amount
        account['transactions'].append(f"Deposited ${amount}")
        print(f"${amount} deposited successfully! Your new balance is: ${account['balance']}")

def withdraw(account, amount):
    if amount <= 0:
        print("Withdrawal amount must be greater than zero.")
    elif amount > account['balance']:
        print("Insufficient balance!")
    else:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrew ${amount}")
        print(f"${amount} withdrawn successfully! Your remaining balance is: ${account['balance']}")

def display_balance(account):
    print(f"\nAccount Type: {account['type']}")
    print(f"Current Balance: ${account['balance']}")
    print(f"Transaction History:")
    if account['transactions']:
        for transaction in account['transactions']:
            print(f" - {transaction}")
    else:
        print("No transactions yet.")

def create_account():
    print("\nCreating a new account...")
    account_type = input("Choose account type (Checking/Savings): ").capitalize()
    if account_type not in ["Checking", "Savings"]:
        print("Invalid account type. Defaulting to Checking.")
        account_type = "Checking"
    
    owner = input("Enter the account owner's name: ")
    balance = float(input("Enter initial deposit amount: "))
    transactions = [f"Account created with initial deposit of ${balance}"]
    
    return {"owner": owner, "type": account_type, "balance": balance, "transactions": transactions}

def transfer(account_from, account_to, amount):
    if amount <= 0:
        print("Transfer amount must be greater than zero.")
    elif amount > account_from['balance']:
        print("Insufficient balance in the sending account!")
    else:
        account_from['balance'] -= amount
        account_to['balance'] += amount
        account_from['transactions'].append(f"Transferred ${amount} to {account_to['owner']}'s account")
        account_to['transactions'].append(f"Received ${amount} from {account_from['owner']}'s account")
        print(f"${amount} transferred successfully!")

def bank_account_simulator():
    print("Welcome to the Complex Bank Account Simulator!")
    
    accounts = {}
    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Account Balance and Transactions")
        print("5. Transfer Money Between Accounts")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            # Create a new account
            account = create_account()
            accounts[account['owner']] = account
            print(accounts)
            print(accountsp)
            print(f"Account created successfully for {account['owner']}!")
        
        elif choice == "2":
            # Deposit money into an account
            owner = input("Enter the account owner's name: ")
            if owner in accounts:
                try:
                    amount = float(input("Enter the amount to deposit: "))
                    deposit(accounts[owner], amount)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            else:
                print("Account not found.")
        
        elif choice == "3":
            # Withdraw money from an account
            owner = input("Enter the account owner's name: ")
            if owner in accounts:
                try:
                    amount = float(input("Enter the amount to withdraw: "))
                    withdraw(accounts[owner], amount)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            else:
                print("Account not found.")
        
        elif choice == "4":
            # Display balance and transaction history
            owner = input("Enter the account owner's name: ")
            if owner in accounts:
                display_balance(accounts[owner])
            else:
                print("Account not found.")
        
        elif choice == "5":
            # Transfer money between accounts
            sender_name = input("Enter your account owner's name: ")
            if sender_name in accounts:
                receiver_name = input("Enter the receiver's account owner's name: ")
                if receiver_name in accounts:
                    try:
                        amount = float(input("Enter the amount to transfer: "))
                        transfer(accounts[sender_name], accounts[receiver_name], amount)
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                else:
                    print("Receiver account not found.")
            else:
                print("Sender account not found.")
        
        elif choice == "6":
            # Exit the program
            print("Thank you for using the Bank Account Simulator! Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Run the simulator
bank_account_simulator()


def authenticate(account):
    attempts = 3
    while attempts > 0:
        password = input("Enter your password: ")
        if password == account['password']:
            return True
        else:
            attempts -= 1
            print(f"Incorrect password. {attempts} attempts remaining.")
    print("Too many failed attempts. Access denied.")
    return False

def view_all_accounts(accounts):
    print("\nAll accounts and their balances:")
    if not accounts:
        print("No accounts available.")
    else:
        for account in accounts.values():
            print(f"Owner: {account['owner']} - Balance: ${account['balance']}")

def bank_account_simulator():
    print("Welcome to the Complex Bank Account Simulator!")
    
    accounts = {}
    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Account Balance and Transactions")
        print("5. Transfer Money Between Accounts")
        print("6. View All Accounts")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            # Create a new account
            account = create_account()
            accounts[account['owner']] = account
            print(f"Account created successfully for {account['owner']}!")
        
        elif choice == "2":
            # Deposit money into an account
            owner = input("Enter the account owner's name: ")
            if owner in accounts:
                if authenticate(accounts[owner]):
                    try:
                        amount = float(input("Enter the amount to deposit: "))
                        deposit(accounts[owner], amount)
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                else:
                    print("Authentication failed.")
            else:
                print("Account not found.")
        
        elif choice == "3":
            # Withdraw money from an account
            owner = input("Enter the account owner's name: ")
            if owner in accounts:
                if authenticate(accounts[owner]):
                    try:
                        amount = float(input("Enter the amount to withdraw: "))
                        withdraw(accounts[owner], amount)
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                else:
                    print("Authentication failed.")
            else:
                print("Account not found.")
        
        elif choice == "4":
            # Display balance and transaction history
            owner = input("Enter the account owner's name: ")
            if owner in accounts:
                if authenticate(accounts[owner]):
                    display_balance(accounts[owner])
                else:
                    print("Authentication failed.")
            else:
                print("Account not found.")
        
        elif choice == "5":
            # Transfer money between accounts
            sender_name = input("Enter your account owner's name: ")
            if sender_name in accounts:
                if authenticate(accounts[sender_name]):
                    receiver_name = input("Enter the receiver's account owner's name: ")
                    if receiver_name in accounts:
                        try:
                            amount = float(input("Enter the amount to transfer: "))
                            transfer(accounts[sender_name], accounts[receiver_name], amount)
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                    else:
                        print("Receiver account not found.")
                else:
                    print("Authentication failed.")
            else:
                print("Sender account not found.")
        
        elif choice == "6":
            # View all accounts and balances
            view_all_accounts(accounts)
        
        elif choice == "7":
            # Exit the program
            print("Thank you for using the Bank Account Simulator! Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


bank_account_simulator()

import time

def deposit(account, amount):
    if amount <= 0:
        print("Deposit amount must be greater than zero.")
    else:
        account['balance'] += amount
        account['transactions'].append(f"Deposited ${amount}")
        print(f"${amount} deposited successfully! Your new balance is: ${account['balance']}")

def withdraw(account, amount):
    if amount <= 0:
        print("Withdrawal amount must be greater than zero.")
    elif amount > account['balance']:
        print("Insufficient balance!")
    else:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrew ${amount}")
        print(f"${amount} withdrawn successfully! Your remaining balance is: ${account['balance']}")

def display_balance(account):
    print(f"\nAccount Type: {account['type']}")
    print(f"Current Balance: ${account['balance']}")
    print(f"Transaction History:")
    if account['transactions']:
        for transaction in account['transactions']:
            print(f" - {transaction}")
    else:
        print("No transactions yet.")

def create_account():
    print("\nCreating a new account...")
    account_type = input("Choose account type (Checking/Savings): ").capitalize()
    if account_type not in ["Checking", "Savings"]:
        print("Invalid account type. Defaulting to Checking.")
        account_type = "Checking"
    
    owner = input("Enter the account owner's name: ")
    password = input("Enter a password for the account: ")
    balance = float(input("Enter initial deposit amount: "))
    transactions = [f"Account created with initial deposit of ${balance}"]
    
    return {
        "owner": owner,
        "password": password,
        "type": account_type,
        "balance": balance,
        "transactions": transactions,
        "withdrawal_count": 0,
        "last_withdrawal_time": None
    }

def transfer(account_from, account_to, amount):
    if amount <= 0:
        print("Transfer amount must be greater than zero.")
    elif amount > account_from['balance']:
        print("Insufficient balance in the sending account!")
    else:
        account_from['balance'] -= amount
        account_to['balance'] += amount
        account_from['transactions'].append(f"Transferred ${amount} to {account_to['owner']}'s account")
        account_to['transactions'].append(f"Received ${amount} from {account_from['owner']}'s account")
        print(f"${amount} transferred successfully!")

def authenticate(account):
    attempts = 3
    while attempts > 0:
        password = input("Enter your password: ")
        if password == account['password']:
            return True
        else:
            attempts -= 1
            print(f"Incorrect password. {attempts} attempts remaining.")
    print("Too many failed attempts. Access denied.")
    return False

def change_password(account):
    if authenticate(account):
        new_password = input("Enter your new password: ")
        account['password'] = new_password
        print("Password changed successfully!")

def view_all_accounts(accounts):
    print("\nAll accounts and their balances:")
    if not accounts:
        print("No accounts available.")
    else:
        for account in accounts.values():
            print(f"Owner: {account['owner']} - Balance: ${account['balance']}")

def track_withdrawals(account):
    """Limit withdrawal attempts per day."""
    current_time = time.time()
    if account['last_withdrawal_time'] is None or current_time - account['last_withdrawal_time'] > 86400:  # 86400 seconds = 1 day
        account['withdrawal_count'] = 0  # Reset count after 24 hours

    if account['withdrawal_count'] >= 3:
        print("You have reached your daily withdrawal limit.")
        return False
    return True

def bank_account_simulator():
    print("Welcome to the Complex Bank Account Simulator!")
    
    accounts = {}
    while True:
        print("\nMenu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Account Balance and Transactions")
        print("5. Transfer Money Between Accounts")
        print("6. View All Accounts")
        print("7. Change Account Password")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == "1":
            # Create a new account
            account = create_account()
            accounts[account['owner']] = account
            print(f"Account created successfully for {account['owner']}!")
        
        elif choice == "2":
            # Deposit money into an account
            owner = input("Enter the account owner's name: ")
            if owner in accounts:
                if authenticate(accounts[owner]):
                    try:
                        amount = float(input("Enter the amount to deposit: "))
                        deposit(accounts[owner], amount)
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                else:
                    print("Authentication failed.")
            else:
                print("Account not found.")
        
        elif choice == "3":
            # Withdraw money from an account
            owner = input("Enter the account owner's name: ")
            if owner in accounts:
                if authenticate(accounts[owner]):
                    if track_withdrawals(accounts[owner]):
                        try:
                            amount = float(input("Enter the amount to withdraw: "))
                            withdraw(accounts[owner], amount)
                            accounts[owner]['withdrawal_count'] += 1
                            accounts[owner]['last_withdrawal_time'] = time.time()
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                else:
                    print("Authentication failed.")
            else:
                print("Account not found.")
        
        elif choice == "4":
            # Display balance and transaction history
            owner = input("Enter the account owner's name: ")
            if owner in accounts:
                if authenticate(accounts[owner]):
                    display_balance(accounts[owner])
                else:
                    print("Authentication failed.")
            else:
                print("Account not found.")
        
        elif choice == "5":
            # Transfer money between accounts
            sender_name = input("Enter your account owner's name: ")
            if sender_name in accounts:
                if authenticate(accounts[sender_name]):
                    receiver_name = input("Enter the receiver's account owner's name: ")
                    if receiver_name in accounts:
                        try:
                            amount = float(input("Enter the amount to transfer: "))
                            transfer(accounts[sender_name], accounts[receiver_name], amount)
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                    else:
                        print("Receiver account not found.")
                else:
                    print("Authentication failed.")
            else:
                print("Sender account not found.")
        
        elif choice == "6":
            # View all accounts and balances
            view_all_accounts(accounts)
        
        elif choice == "7":
            # Change account password
            owner = input("Enter the account owner's name: ")
            if owner in accounts:
                if authenticate(accounts[owner]):
                    change_password(accounts[owner])
                else:
                    print("Authentication failed.")
            else:
                print("Account not found.")
        
        elif choice == "8":
            # Exit the program
            print("Thank you for using the Bank Account Simulator! Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


bank_account_simulator()
import time
import json

def save_data(accounts):
    with open("accounts.json", "w") as file:
        json.dump(accounts, file)

def load_data():
    try:
        with open("accounts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def create_account(accounts):
    print("\nCreating a new account...")
    username = input("Enter a username: ")
    if username in accounts:
        print("Username already exists. Try again.")
        return
    password = input("Enter a password: ")
    security_question = input("Enter a security question (e.g., Your first pet's name?): ")
    security_answer = input("Answer to security question: ")
    account_type = input("Choose account type (Checking/Savings): ").capitalize()
    balance = float(input("Enter initial deposit amount: "))
    accounts[username] = {
        "password": password,
        "security_question": security_question,
        "security_answer": security_answer,
        "type": account_type,
        "balance": balance,
        "transactions": [],
        "is_locked": False,
        "role": "user"
    }
    save_data(accounts)
    print("Account created successfully!")

def login(accounts):
    username = input("Enter your username: ")
    if username not in accounts:
        print("Account not found.")
        return None
    if accounts[username]["is_locked"]:
        print("Account is locked due to multiple failed attempts. Contact admin.")
        return None
    
    attempts = 3
    while attempts > 0:
        password = input("Enter your password: ")
        if password == accounts[username]["password"]:
            print("Login successful!")
            return username
        else:
            attempts -= 1
            print(f"Incorrect password. {attempts} attempts remaining.")
    
    accounts[username]["is_locked"] = True
    save_data(accounts)
    print("Too many failed attempts. Your account has been locked.")
    return None

def reset_password(accounts):
    username = input("Enter your username: ")
    if username not in accounts:
        print("Account not found.")
        return
    print(accounts[username]["security_question"])
    answer = input("Your answer: ")
    if answer == accounts[username]["security_answer"]:
        new_password = input("Enter new password: ")
        accounts[username]["password"] = new_password
        accounts[username]["is_locked"] = False
        save_data(accounts)
        print("Password reset successful!")
    else:
        print("Incorrect answer. Cannot reset password.")

def deposit(accounts, username):
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        accounts[username]["balance"] += amount
        accounts[username]["transactions"].append(f"Deposited ${amount}")
        save_data(accounts)
        print(f"Deposited ${amount}. New balance: ${accounts[username]['balance']}")
    else:
        print("Amount must be greater than zero.")

def withdraw(accounts, username):
    amount = float(input("Enter amount to withdraw: "))
    if amount > accounts[username]["balance"]:
        print("Insufficient balance!")
    else:
        accounts[username]["balance"] -= amount
        accounts[username]["transactions"].append(f"Withdrew ${amount}")
        save_data(accounts)
        print(f"Withdrew ${amount}. New balance: ${accounts[username]['balance']}")

def view_balance(accounts, username):
    print(f"Current balance: ${accounts[username]['balance']}")
    print("Last 5 Transactions:")
    for transaction in accounts[username]["transactions"][-5:]:
        print(transaction)

def admin_menu(accounts):
    while True:
        print("\nAdmin Menu:")
        print("1. View all accounts")
        print("2. Unlock an account")
        print("3. Exit Admin Mode")
        choice = input("Enter your choice: ")
        if choice == "1":
            for user, data in accounts.items():
                print(f"{user}: ${data['balance']} (Locked: {data['is_locked']})")
        elif choice == "2":
            username = input("Enter username to unlock: ")
            if username in accounts:
                accounts[username]["is_locked"] = False
                save_data(accounts)
                print("Account unlocked successfully!")
            else:
                print("User not found.")
        elif choice == "3":
            break

def bank_simulator():
    accounts = load_data()
    while True:
        print("\n1. Create Account")
        print("2. Login")
        print("3. Reset Password")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            username = login(accounts)
            if username:
                if accounts[username]["role"] == "admin":
                    admin_menu(accounts)
                else:
                    while True:
                        print("\n1. Deposit")
                        print("2. Withdraw")
                        print("3. View Balance")
                        print("4. Logout")
                        choice = input("Enter your choice: ")
                        if choice == "1":
                            deposit(accounts, username)
                        elif choice == "2":
                            withdraw(accounts, username)
                        elif choice == "3":
                            view_balance(accounts, username)
                        elif choice == "4":
                            break
        elif choice == "3":
            reset_password(accounts)
        elif choice == "4":
            break

bank_simulator()
