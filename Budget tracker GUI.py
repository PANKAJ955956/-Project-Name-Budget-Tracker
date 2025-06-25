import tkinter as tk
from tkinter import messagebox

class BudgetTracker:
    def __init__(self):
        self.total_income = 0
        self.total_expense = 0
        self.transaction_log = []

    def add_income(self, source, amount):
        self.total_income += amount
        self.transaction_log.append(f"[Income] {source}: ₹{amount}")

    def add_expense(self, category, amount):
        self.total_expense += amount
        self.transaction_log.append(f"[Expense] {category}: ₹{amount}")

    def get_balance(self):
        return self.total_income - self.total_expense

    def get_transaction_history(self):
        return "\n".join(self.transaction_log)


class BudgetAppGUI:
    def __init__(self, root):
        self.tracker = BudgetTracker()
        self.root = root
        self.root.title("💰 Budget Tracker GUI")
        self.root.geometry("400x500")
        self.root.config(padx=20, pady=20)

        # --- Income Section ---
        tk.Label(root, text="Add Income", font=("Arial", 14, "bold")).pack()
        self.income_source = tk.Entry(root, width=30)
        self.income_source.pack(pady=5)
        self.income_amount = tk.Entry(root, width=30)
        self.income_amount.pack(pady=5)
        tk.Button(root, text="Add Income", command=self.add_income).pack(pady=5)

        # --- Expense Section ---
        tk.Label(root, text="Add Expense", font=("Arial", 14, "bold")).pack(pady=(15,0))
        self.expense_category = tk.Entry(root, width=30)
        self.expense_category.pack(pady=5)
        self.expense_amount = tk.Entry(root, width=30)
        self.expense_amount.pack(pady=5)
        tk.Button(root, text="Add Expense", command=self.add_expense).pack(pady=5)

        # --- Balance & Transaction Buttons ---
        tk.Button(root, text="View Balance", command=self.view_balance).pack(pady=(20,5))
        tk.Button(root, text="View Transactions", command=self.view_transactions).pack(pady=5)

        # --- Display Output ---
        self.output_area = tk.Text(root, height=10, width=45)
        self.output_area.pack(pady=10)

    def add_income(self):
        source = self.income_source.get()
        try:
            amount = float(self.income_amount.get())
            self.tracker.add_income(source, amount)
            messagebox.showinfo("Success", "Income added!")
            self.income_source.delete(0, tk.END)
            self.income_amount.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def add_expense(self):
        category = self.expense_category.get()
        try:
            amount = float(self.expense_amount.get())
            self.tracker.add_expense(category, amount)
            messagebox.showinfo("Success", "Expense added!")
            self.expense_category.delete(0, tk.END)
            self.expense_amount.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def view_balance(self):
        balance = self.tracker.get_balance()
        self.output_area.delete("1.0", tk.END)
        self.output_area.insert(tk.END, f"💰 Current Balance: ₹{balance}")

    def view_transactions(self):
        transactions = self.tracker.get_transaction_history()
        self.output_area.delete("1.0", tk.END)
        self.output_area.insert(tk.END, "📋 Transactions:\n" + transactions)


if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetAppGUI(root)
    root.mainloop()

