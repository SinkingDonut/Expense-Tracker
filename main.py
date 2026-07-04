expenses = []
costs = []
while True:
    expense_name = input("Enter expense name (press Q to Quit): ")
    if expense_name.upper() == "Q":
        break
    expenses.append(expense_name)
    expense_cost = input("Enter cost of your expense: ")
    costs.append(expense_cost)

    anotherexp = input("Do you want to add another expense?(y/n): ")
    if anotherexp == "n":
        break
total = 0.00
for item_cost in costs:
    total += float(item_cost)
print("\n--- Summary ---")
print(f"Total spen      t: ${total:.2f}")


