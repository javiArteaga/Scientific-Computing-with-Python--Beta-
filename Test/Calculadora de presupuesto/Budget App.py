class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance

    def transfer(self, amount, another_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {another_category.name}")
            another_category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][:23]:23}{item['amount']:7.2f}\n"
            total += item['amount']
        output = title + items + f"Total: {total:.2f}"
        return output

def create_spend_chart(categories):
    # Calculate total withdrawals and percentages for each category
    withdrawals = []
    total_withdrawals = 0
    category_names = []

    for category in categories:
        category_names.append(category.name)
        withdrawal = sum(item['amount'] for item in category.ledger if item['amount'] < 0)
        withdrawals.append(withdrawal)
        total_withdrawals += withdrawal

    # Calculate percentages
    percentages = [(w / total_withdrawals) * 100 for w in withdrawals]

    # Build the chart
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:3}| "
        for percent in percentages:
            if percent >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    -" + "---" * len(categories) + "\n"

    # Determine the maximum length of category names
    max_name_length = max(len(name) for name in category_names)

    # Print category names vertically
    for i in range(max_name_length):
        chart += "     "
        for name in category_names:
            if i < len(name):
                chart += name[i] + "  "
            else:
                chart += "   "
        chart += "\n"

    return chart.rstrip("\n")

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
clothing.withdraw(50, "shopping for clothes")

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(50, "fuel")

print(create_spend_chart([food, clothing, auto]))