import argparse

class BankAccount:
    INTEREST_RATE = 0.01  # 1% interest rate for simplicity

    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
            return None
        else:
            self.balance -= amount
            return self.balance

    def get_balance(self):
        return self.balance

    def get_interest(self):
        return self.balance * self.INTEREST_RATE

    def apply_interest(self):
        self.balance += self.get_interest()
        return self.balance

def main():
    account = BankAccount()
    while True:
        print("\nOptions:")
        print("1: Deposit")
        print("2: Withdraw")
        print("3: View balance")
        print("4: Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
            interest_received = account.get_interest()
            account.apply_interest()
            print(f"Deposited ${amount}. New balance after interest: ${account.get_balance():.2f}")
            print(f"Interest Received: ${interest_received:.2f}")

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            if account.withdraw(amount) is not None:
                interest_received = account.get_interest()
                account.apply_interest()
                print(f"Withdrew ${amount}. New balance after interest: ${account.get_balance():.2f}")
                print(f"Interest Received: ${interest_received:.2f}")

        elif choice == "3":
            interest_received = account.get_interest()
            account.apply_interest()
            print(f"Current balance after interest: ${account.get_balance():.2f}")
            print(f"Interest Received: ${interest_received:.2f}")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()


def main():
    parser = argparse.ArgumentParser(description="CLI Bank Account tool")
    parser.add_argument('command', choices=['deposit', 'withdraw', 'get_balance'], help='The action to perform')
    parser.add_argument('amount', type=float, nargs='?', default=0, help='The amount for deposit/withdraw')

    args = parser.parse_args()

    account = BankAccount()  # For this example, we're using a new account every time. Persistent storage would be a future enhancement.

    if args.command == "deposit":
        account.deposit(args.amount)
        interest_received = account.get_interest()
        account.apply_interest()
        print(f"Deposited ${args.amount}. New balance after interest: ${account.get_balance():.2f}")
        print(f"Interest Received: ${interest_received:.2f}")

    elif args.command == "withdraw":
        if account.withdraw(args.amount) is not None:
            interest_received = account.get_interest()
            account.apply_interest()
            print(f"Withdrew ${args.amount}. New balance after interest: ${account.get_balance():.2f}")
            print(f"Interest Received: ${interest_received:.2f}")

    elif args.command == "get_balance":
        interest_received = account.get_interest()
        account.apply_interest()
        print(f"Current balance after interest: ${account.get_balance():.2f}")
        print(f"Interest Received: ${interest_received:.2f}")

if __name__ == "__main__":
    main()
