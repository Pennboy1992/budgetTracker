def budget_item(arr):
    print("Enter a new item you wish to be added to your budget.")
    item_name = input("Enter the name for your item: ")
    try:
        income_or_debit = int(input("Is this income or a debit:\n1.Income\n2.Expense\nEnter Corresponding Number: "))
    except ValueError:
        print("Please enter a valid choice (1 or 2)")
        income_or_debit = int(input("Is this income or a debit:\n1.Income\n2.Expense\nEnter Corresponding Number: "))

    if income_or_debit == 1:
        pay = float(input("How much will you be making from this source of income this month: "))
    else:
        pay = float(input("How much is this expense costing you per month: "))
    arr.append({"Item": item_name, "Type": "Income" if income_or_debit == 1 else "Expense", "Amount": round(pay, 2)})
    return arr
