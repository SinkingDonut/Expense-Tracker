expenses = []
cost = []
choice = []
while True:
    expense_name = input("Enter expense name (press Q to Quit): ")
    if expense_name.upper() == "Q":
        break
    expenses.append(expense_name)
    expense_cost = input("Enter cost of your expense: ")
    cost.append(expense_cost)

    anotherexp = input("Do you want to add another expense?(y/n): ")
    if anotherexp == "y":
        choice.append(anotherexp)
    elif anotherexp == "n":
        break
total = 0.00
for item_cost in cost:
    total += float(item_cost)
print("\n--- Summary ---")
print(f"Total spent: ${total:.2f}")


