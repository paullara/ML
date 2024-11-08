balance = 0.0

def show_menu():
    print("\nWelcome to the Simple Banking System")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def check_balance():
    print(f"Your current balance is: ${balance:.2f}")

def deposit():
    global balance
    try:
        amount = float(input("Enter amount to deposit: $"))
        if amount > 0:
            balance += amount
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Amount must be greater than zero.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def withdraw():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: $"))
        if amount > 0:
            if amount <= balance:
                balance -= amount
                print(f"${amount:.2f} withdrawn successfully.")
            else:
                print("Insufficient funds.")
        else:
            print("Amount must be greater than zero.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def banking_system():
    while True:
        show_menu()
        try:
            choice = int(input("Select an option: "))
            if choice == 1:
                check_balance()
            elif choice == 2:
                deposit()
            elif choice == 3:
                withdraw()
            elif choice == 4:
                print("Exiting the banking system. Thank you!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

banking_system()
