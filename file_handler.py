# file_handler.py
import os

ACCOUNTS_FILE = 'accounts.txt'
TRANSACTIONS_FILE = 'transactions.txt'

def create_files():
    if not os.path.exists(ACCOUNTS_FILE):
        open(ACCOUNTS_FILE, 'w').close()
    if not os.path.exists(TRANSACTIONS_FILE):
        open(TRANSACTIONS_FILE, 'w').close()

def save_account(account_data):
    with open(ACCOUNTS_FILE, 'a') as f:
        f.write(account_data + '\n')

def log_transaction(transaction_data):
    with open(TRANSACTIONS_FILE, 'a') as f:
        f.write(transaction_data + '\n')

def read_accounts():
    with open(ACCOUNTS_FILE, 'r') as f:
        return f.readlines()