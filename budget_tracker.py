class BudgetTracker:
    def __init__(self):
        self.total_income = 0
        self.total_expense = 0
        self.transaction_log = []

    def add_income(self, source, amount):
        self.total_income += amount
        self.transaction_log.append(f"[Income] {source}: {amount}")

    def add_expense(self, category, amount):
        self.total_expense += amount
        self.transaction_log.append(f"[Expense] {category}: {amount}")

    def get_balance(self):
        return self.total_income - self.total_expense

    def get_transaction_history(self):
        return self.transaction_log


class BudgetApp:
    def __init__(self):
        self.tracker = BudgetTracker()

    def display_menu(self):
        print("\n==== Budget Tracker Menu ====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. View Transaction History")
        print("5. Exit")

    def run(self):
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter your choice (1-5): "))
            except ValueError:
                print(" Please enter a valid number!")
                continue

            if choice == 1:
                source = input("Enter income source: ")
                amount = float(input("Enter amount: ₹"))
                self.tracker.add_income(source, amount)
                print(" Income recorded.")
            elif choice == 2:
                category = input("Enter expense category: ")
                amount = float(input("Enter amount: ₹"))
                self.tracker.add_expense(category, amount)
                print("Expense recorded.")
            elif choice == 3:
                balance = self.tracker.get_balance()
                print(f" Current Balance: {balance}")
            elif choice == 4:
                history = self.tracker.get_transaction_history()
                print(" Transaction History:")
                if not history:
                    print("No transactions yet.")
                else:
                    for item in history:
                        print(item)
            elif choice == 5:
                print(" Exiting Budget Tracker. Goodbye!")
                break
            else:
                print(" Invalid choice. Try again.")


if __name__ == "__main__":
    app = BudgetApp()
    app.run()
