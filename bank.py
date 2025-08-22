class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_balance):
        if account_number in self.accounts:
            return "Account already exists"
        if initial_balance < 0:
            return "Initial balance must be non-negative"
        self.accounts[account_number] = {
            'account_holder': account_holder,
            'balance': initial_balance
        }
        return "Account created successfully"

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            return "Account does not exist"
        if amount <= 0:
            return "Amount to deposit must be positive"
        self.accounts[account_number]['balance'] += amount
        return f"Deposited ₹{amount} successfully. New balance: ₹{self.accounts[account_number]['balance']}"

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            return "Account does not exist"
        if amount <= 0:
            return "Amount to withdraw must be positive"
        if self.accounts[account_number]['balance'] < amount:
            return "Insufficient balance."
        self.accounts[account_number]['balance'] -= amount
        return f"Withdrew ₹{amount} successfully. New balance: ₹{self.accounts[account_number]['balance']}"

    def check_balance(self, account_number):
        if account_number not in self.accounts:
            return "Account does not exist"
        acc = self.accounts[account_number]
        return f"Account Holder: {acc['account_holder']}\nBalance: ₹{acc['balance']}"


def main():
    bank = Bank()
    print("\n****** Kangal Bank Management System ******")
    while True:
        print("\n1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            acc_no = input("Enter Account Number: ")
            name = input("Enter Account Holder's Name: ")
            try:
                initial_balance = float(input("Enter Initial Balance: "))
            except ValueError:
                print("Invalid amount entered.")
                continue
            print(bank.create_account(acc_no, name, initial_balance))

        elif choice == '2':
            acc_no = input("Enter Account Number: ")
            try:
                amount = float(input("Enter Amount to Deposit: "))
            except ValueError:
                print("Invalid amount entered.")
                continue
            print(bank.deposit(acc_no, amount))

        elif choice == '3':
            acc_no = input("Enter Account Number: ")
            try:
                amount = float(input("Enter Amount to Withdraw: "))
            except ValueError:
                print("Invalid amount entered.")
                continue
            print(bank.withdraw(acc_no, amount))

        elif choice == '4':
            acc_no = input("Enter Account Number: ")
            print(bank.check_balance(acc_no))

        elif choice == '5':
            print("Thank you for banking with us!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
