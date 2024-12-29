# banking.py
from file_handler import save_account, log_transaction, read_accounts
from password_manager import hash_password

def create_account():
    name = input("Enter your name: ")
    initial_deposit = float(input("Enter your initial deposit: "))
    account_number = str(100000 + len(read_accounts()))  # Simple account number generation
    password = hash_password(input("Enter a password: "))
    
    account_data = f"{account_number},{name},{initial_deposit},{password}"
    save_account(account_data)
    
    print(f"Your account number: {account_number} (Save this for login)")
    print("Account created successfully! (Account details saved to accounts.txt)")

def login():
    account_number = input("Enter your account number: ")
    password = hash_password(input("Enter your password: "))
    
    accounts = read_accounts()
    
    for account in accounts:
        acc_num, name, balance, pass_hash = account.strip().split(',')
        if acc_num == account_number and pass_hash == password:
            print("Login successful!")
            return acc_num, name, float(balance)
    
    print("Invalid account number or password.")
    return None, None, None

def deposit(account_number, current_balance):
    amount = float(input("Enter amount to deposit: "))
    current_balance += amount
    log_transaction(f"Deposit,{account_number},{amount}")
    print(f"Deposit successful! Current balance: {current_balance}")
    return current_balance

def withdraw(account_number, current_balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > current_balance:
        print("Insufficient balance for this withdrawal.")
        return current_balance
    current_balance -= amount
    log_transaction(f"Withdraw,{account_number},{amount}")
    print(f"Withdrawal successful! Current balance: {current_balance}")
    return current_balance