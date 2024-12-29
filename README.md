# Banking System

## Project Description
This is a simple banking system implemented in Python. The application allows users to create accounts, log in, deposit money, withdraw money, and view their account balance. The system uses file handling to store account and transaction data securely.

## Features Implemented
- **Create Account**: Users can create a new account with a unique account number and password.
- **Secure Password Storage**: Passwords are hashed using SHA-256 to ensure security.
- **Login Functionality**: Users can log in to their accounts using their account number and password.
- **Deposit Money**: Users can deposit money into their accounts.
- **Withdraw Money**: Users can withdraw money from their accounts, with checks for sufficient balance.
- **Transaction Logging**: All transactions (deposits and withdrawals) are logged in a separate file for record-keeping.

## How to Run the Project
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_username/banking_system.git
2. Navigate into the project directory:
    cd banking_system
3. Run the application:
   python main.py
   
Instructions for Installation:
Ensure you have Python installed on your machine. You can download it from python.org.

Data Files:
 1. accounts.txt: This file stores account details, including account numbers, names, balances, and hashed passwords.
 2. transactions.txt: This file logs all transactions made by users, including deposits and withdrawals.

Usage:
When you run the application, you will be presented with a menu to create an account, log in, or exit.
After logging in, you can deposit or withdraw money and view your current balance.

Contributing:
If you would like to contribute to this project, feel free to fork the repository and submit a pull request with your changes.

License:
This project is open-source and available under the MIT License.

Acknowledgments:
Thank you for using this banking system project. If you have any questions or feedback, please feel free to reach out.
