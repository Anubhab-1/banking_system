# main.py
from banking import create_account, login, deposit, withdraw
from file_handler import create_files

def main_menu():
    while True:
        print("\nWelcome to Shadow Banking System!")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            create_account()
        elif choice == '2':
            account_number, name, current_balance = login()
            if account_number:
                while True:
                    print(f"\nWelcome {name}! Your current balance is: {current_balance}")
                    print("1. Deposit Money")
                    print("2. Withdraw Money")
                    print("3. Logout")
                    transaction_choice = input("Enter your choice: ")
                    
                    if transaction_choice == '1':
                        current_balance = deposit(account_number, current_balance)
                    elif transaction_choice == '2':
                        current_balance = withdraw(account_number, current_balance)
                    elif transaction_choice == '3':
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Thank you for using the  Shadow Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Create accounts.txt and transactions.txt if they don't exist
if __name__ == "__main__":
    create_files()  # Ensure the necessary files are created
    main_menu()     # Run the main menu