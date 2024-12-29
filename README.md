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

Data Files:
accounts.txt: This file stores account details, including account numbers, names, balances, and hashed passwords.
transactions.txt: This file logs all transactions made by users, including deposits and withdrawals.

Usage:
When you run the application, you will be presented with a menu to create an account, log in, or exit.
After logging in, you can deposit or withdraw money and view your current balance.

Contributing:
If you would like to contribute to this project, feel free to fork the repository and submit a pull request with your changes.

License:
This project is open-source and available under the MIT License.

Acknowledgments:
Thank you for using this banking system project. If you have any questions or feedback, please feel free to reach out.

### Instructions for Using the README
1. **Replace `your_username`**: Make sure to replace `your_username` in the clone command with your actual GitHub username.
2. **Save the File**: Save this content in a file named `README.md` in your project directory.
3. **Commit Changes**: If you haven't already, stage and commit the `README.md` file to your GitHub repository:
   ```bash
   git add README.md
   git commit -m "Add README file"
   git push origin main
