import csv
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def add_expense(self, amount, category, description=""):
        expense = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "amount": float(amount),
            "category": category,
            "description": description
        }
        self.expenses.append(expense)
        self.save_expenses()
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        for exp in self.expenses:
            print(f"{exp['date']} | {exp['category']} | ₹{exp['amount']} | {exp['description']}")

    def total_by_category(self, category):
        total = sum(exp["amount"] for exp in self.expenses if exp["category"].lower() == category.lower())
        print(f"Total spent on {category}: ₹{total}")

    def total_expenses(self):
        total = sum(exp["amount"] for exp in self.expenses)
        print(f"Total expenses: ₹{total}")

    def save_expenses(self):
        with open(self.filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["date", "amount", "category", "description"])
            writer.writeheader()
            writer.writerows(self.expenses)

    def load_expenses(self):
        try:
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                self.expenses = list(reader)
                for exp in self.expenses:
                    exp["amount"] = float(exp["amount"])
        except FileNotFoundError:
            self.expenses = []

# Example usage
if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total by Category")
        print("4. Total Expenses")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            description = input("Enter description (optional): ")
            tracker.add_expense(amount, category, description)
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            category = input("Enter category: ")
            tracker.total_by_category(category)
        elif choice == "4":
            tracker.total_expenses()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
