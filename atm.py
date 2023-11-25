class Account:
    def __init__(self, holder_name, pin, balance):
        self.holder_name = holder_name
        self.pin = pin
        self.balance = balance


def validate_pin(card_number, entered_pin):
    return accounts[card_number].pin == entered_pin


def deposit(card_number):
    try:
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            accounts[card_number].balance += amount
            print(f"Deposit successful. New balance: ${accounts[card_number].balance}")
        else:
            print("Invalid amount. Please enter a valid positive number.")
    except ValueError:
        print("Invalid amount. Please enter a valid number.")


def withdraw(card_number):
    try:
        amount = float(input("Enter the amount to withdraw: "))
        if amount > 0:
            if amount <= accounts[card_number].balance:
                accounts[card_number].balance -= amount
                print(f"Withdrawal successful. New balance: ${accounts[card_number].balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid amount. Please enter a valid positive number.")
    except ValueError:
        print("Invalid amount. Please enter a valid number.")


def check_balance(card_number):
    print(f"Your current balance: ${accounts[card_number].balance}")


# Create some sample accounts
accounts = {
    "1234567890": Account("John Doe", "1234", 1000.0),
    "0987654321": Account("Jane Doe", "5678", 1500.0)
}

# ATM loop
while True:
    card_number = input("Enter your card number (or 'exit' to quit): ")

    if card_number.lower() == "exit":
        break

    if card_number in accounts:
        pin = input("Enter your PIN: ")

        if validate_pin(card_number, pin):
            print(f"Welcome, {accounts[card_number].holder_name}!")

            while True:
                print("\nATM Menu:")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    deposit(card_number)
                elif choice == "2":
                    withdraw(card_number)
                elif choice == "3":
                    check_balance(card_number)
                elif choice == "4":
                    print("Thank you for using our ATM. Goodbye!")
                    exit()
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid PIN. Please try again.")
    else:
        print("Invalid card number. Please try again.")
