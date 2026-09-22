# ATM Simulator in Python

balance = 10000
pin = "1234"

print("================================")
print("       WELCOME TO ATM")
print("================================")

# PIN Verification
attempts = 3

while attempts > 0:
    entered_pin = input("Enter your PIN: ")

    if entered_pin == pin:
        print("\nLogin Successful!")
        break
    else:
        attempts -= 1
        print("Wrong PIN!")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Your card is blocked.")
else:

    while True:
        print("\n================================")
        print("          ATM MENU")
        print("================================")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        # Check Balance
        if choice == "1":
            print("\nYour balance is ₹", balance)

        # Deposit
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))

            if amount > 0:
                balance = balance + amount
                print("₹", amount, "deposited successfully!")
                print("New balance: ₹", balance)
            else:
                print("Invalid amount!")

        # Withdraw
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Invalid amount!")

            elif amount > balance:
                print("Insufficient balance!")

            else:
                balance = balance - amount
                print("Please collect your cash.")
                print("₹", amount, "withdrawn successfully!")
                print("Remaining balance: ₹", balance)

        # Change PIN
        elif choice == "4":
            old_pin = input("Enter your current PIN: ")

            if old_pin == pin:
                new_pin = input("Enter new PIN: ")

                if len(new_pin) == 4 and new_pin.isdigit():
                    pin = new_pin
                    print("PIN changed successfully!")
                else:
                    print("PIN must contain exactly 4 digits.")
            else:
                print("Incorrect current PIN!")

        # Exit
        elif choice == "5":
            print("\nThank you for using our ATM!")
            print("Please collect your card.")
            break

        else:
            print("Invalid choice! Please try again.")
